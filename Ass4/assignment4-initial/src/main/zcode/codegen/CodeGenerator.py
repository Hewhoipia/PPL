from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *
from Utils import *

# Phan Thanh Thong - 2153846

###### Static Check #####

from StaticError import *

class DeclKind:
    def __init__(self, kind:str, param:list=[]):
        # kind must be 'var', 'funcDecl' or 'funcDefi'
        self.kind=kind
        self.param=param
        
class Symbol:
    def __init__(self, kind:DeclKind, name:str, typ:Type=None):
        self.declKind=kind
        self.name=name
        self.typ=typ

class Utils:
    def infer(o:object, typ:Type):
        for symbol in o:
            if symbol.typ is None: symbol.typ=typ
            elif symbol.typ is not None: continue

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.root=ast

    def check(self):
        o=[[]]
        self.visit(self.root, o)
        return o
    
    def visitProgram(self, ctx:Program, o:object):
        # build-in func
        o[0].append(Symbol(DeclKind('funcDefi'), 'readNumber', NumberType()))
        o[0].append(Symbol(DeclKind('funcDefi',[Symbol(DeclKind('var'), 'anArg', NumberType())]), 'writeNumber', VoidType()))
        o[0].append(Symbol(DeclKind('funcDefi'), 'readBool', BoolType()))
        o[0].append(Symbol(DeclKind('funcDefi',[Symbol(DeclKind('var'), 'anArg', BoolType())]), 'writeBool', VoidType()))
        o[0].append(Symbol(DeclKind('funcDefi'), 'readString', StringType()))
        o[0].append(Symbol(DeclKind('funcDefi',[Symbol(DeclKind('var'), 'anArg', StringType())]), 'writeString', VoidType()))
        # declarations
        for x in ctx.decl:
            self.visit(x,o)
        isMain=False
        for symbol in o[0]:
            if symbol.name == 'main' and symbol.declKind.kind == 'funcDefi' and not symbol.declKind.param and isinstance(symbol.typ, VoidType):
                isMain=True
            if symbol.declKind.kind == 'funcDecl': raise NoDefinition(symbol.name)
        if isMain is False: raise NoEntryPoint()

    def visitVarDecl(self, ctx:VarDecl, o:object):
        for symbol in o[0]:
            if ctx.name.name == symbol.name and symbol.declKind.kind == 'var':
                raise Redeclared(Variable(), ctx.name.name)
        typ=None
        if ctx.varType is not None and ctx.varInit is not None:
            typDecl=ctx.varType
            typ=typDecl
            o[0].append(Symbol(DeclKind('var'), ctx.name.name, typ))
            typInit=self.visit(ctx.varInit,o)
            if typInit is None:
                raise TypeCannotBeInferred(ctx)
            if isinstance(typInit, Symbol):
                if typInit.typ is None: typInit.typ = typDecl
                typInit=typInit.typ
            if type(typDecl) != type(typInit): raise TypeMismatchInStatement(ctx)
            if isinstance(typDecl, ArrayType):
                if not isinstance(typInit.eleType, Type):
                    if typDecl.size < typInit.size: raise TypeCannotBeInferred(ctx)
                    resi=typDecl.size[:]
                    for i in range(len(typInit.size)):
                        if typDecl.size[i] != typInit.size[i]: raise TypeCannotBeInferred(ctx)
                        resi.pop(0)
                    if resi:
                        Utils.infer(typInit.eleType, ArrayType(resi, typDecl.eleType))
                        typInit=typDecl
                    elif not resi:
                        Utils.infer(typInit.eleType, typDecl.eleType)
                        typInit=typDecl
                if (type(typDecl.eleType) != type(typInit.eleType)) or (typDecl.size != typInit.size):
                    raise TypeMismatchInStatement(ctx)
            
        elif ctx.varType is not None:
            typ = ctx.varType
            o[0].append(Symbol(DeclKind('var'), ctx.name.name, typ))
        elif ctx.varInit is not None and ctx.modifier == "var":
            symbol=Symbol(DeclKind('var'), ctx.name.name, VoidType())
            o[0].append(symbol)
            typInit = self.visit(ctx.varInit,o)
            if typInit is None:
                raise TypeCannotBeInferred(ctx)
            if isinstance(typInit, Symbol):
                if typInit.typ is None: raise TypeCannotBeInferred(ctx)
                typInit=typInit.typ
            if isinstance(typInit, ArrayType):
                if not isinstance(typInit.eleType, Type): raise TypeCannotBeInferred(ctx)
            symbol.typ=typInit
        elif ctx.varInit is not None and ctx.modifier == "dynamic":
            symbol=Symbol(DeclKind('var'), ctx.name.name)
            o[0].append(symbol)
            typInit = self.visit(ctx.varInit,o)
            if symbol.typ is None:
                if typInit is None:
                    raise TypeCannotBeInferred(ctx)
                if isinstance(typInit, Symbol):
                    if typInit.typ is None: raise TypeCannotBeInferred(ctx)
                    typInit=typInit.typ
                if isinstance(typInit, ArrayType):
                    if not isinstance(typInit.eleType, Type): raise TypeCannotBeInferred(ctx)
                symbol.typ=typInit
            elif symbol.typ is not None:
                if isinstance(typInit, Symbol):
                    if typInit.typ is None: typInit.typ = symbol.typ
                    typInit=typInit.typ
                if type(symbol.typ) != type(typInit): raise TypeMismatchInStatement(ctx)
                if isinstance(symbol.typ, ArrayType):
                    if not isinstance(typInit.eleType, Type):
                        if symbol.typ.size < typInit.size: raise TypeCannotBeInferred(ctx)
                        resi=symbol.typ.size[:]
                        for i in range(len(typInit.size)):
                            if symbol.typ.size[i] != typInit.size[i]: raise TypeCannotBeInferred(ctx)
                            resi.pop(0)
                        if resi:
                            Utils.infer(typInit.eleType, ArrayType(resi, symbol.typ.eleType))
                            typInit=symbol.typ
                        elif not resi:
                            Utils.infer(typInit.eleType, symbol.typ.eleType)
                            typInit=symbol.typ
                    if (type(symbol.typ.eleType) != type(typInit.eleType)) or (symbol.typ.size != typInit.size):
                        raise TypeMismatchInStatement(ctx)
        else: o[0].append(Symbol(DeclKind('var'), ctx.name.name, typ))
            
    def visitFuncDecl(self, ctx:FuncDecl, o:object):
        is_func_decl=None #store a function if it is "funcDecl"
        for symbol in o[0]:
            if ctx.name.name == symbol.name and symbol.declKind.kind != 'var':
                if symbol.declKind.kind == 'funcDefi':
                    raise Redeclared(Function(), ctx.name.name)
                elif symbol.declKind.kind == 'funcDecl':
                    is_func_decl=symbol
                    break
        param=[[]]
        for vardecl in ctx.param:
            typ=None
            # if vardecl.varInit is not None:
            #     typDecl=vardecl.varType
            #     typInit=self.visit(vardecl.varInit,param+o)
            #     if isinstance(typInit, Symbol):
            #         if typInit.typ is None: typInit.typ = typDecl
            #         typInit=typInit.typ
            #     if type(typDecl) != type(typInit): raise TypeMismatchInStatement(vardecl)
            #     if isinstance(typDecl, ArrayType):
            #         if (type(typDecl.eleType) != type(typInit.eleType)) or (typDecl.size != typInit.size):
            #             raise TypeMismatchInStatement(ctx)
            #     typ=typDecl
            # else:
            typ=vardecl.varType
            for symbol in param[0]:
                if vardecl.name.name == symbol.name:
                    raise Redeclared(Parameter(), vardecl.name.name)
            param[0].append(Symbol(DeclKind('var'), vardecl.name.name, typ))
        if ctx.body is not None:
            check_return=None
            if is_func_decl is not None:
                if len(param[0]) != len(is_func_decl.declKind.param):
                    raise Redeclared(Function(), ctx.name.name)
                for i in range(len(param[0])):
                    if type(is_func_decl.declKind.param[i].typ) != type(param[0][i].typ):
                        raise Redeclared(Function(), ctx.name.name)
                is_func_decl.declKind.kind = "funcDefi"
                is_func_decl.declKind.param = param[0]
                o[0].remove(is_func_decl)
                o[0].insert(0,is_func_decl)
                check_return=is_func_decl
            elif is_func_decl is None:
                check_return=Symbol(DeclKind('funcDefi', param[0]), ctx.name.name)
                o[0].insert(0,check_return)
            self.visit(ctx.body,param+o)
            if check_return.typ is None: check_return.typ=VoidType()
        elif ctx.body is None:
            if is_func_decl is not None: raise Redeclared(Function(), ctx.name.name)
            o[0].insert(0,Symbol(DeclKind('funcDecl', param[0]), ctx.name.name))

    def visitBinaryOp(self, ctx:BinaryOp, o:object):
        if ctx.op in ['+', '-', '*', '/', '%']: # input Number
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if left is None or right is None:
                return None
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, NumberType): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = NumberType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, NumberType): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = NumberType()
                right=right.typ
            if not isinstance(left, NumberType) or not isinstance(right, NumberType):
                raise TypeMismatchInExpression(ctx)
            return NumberType()
        if ctx.op in ['=', '!=', '<', '>', '<=', '>=']: # input Number
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if left is None or right is None:
                return None
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, NumberType): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = NumberType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, NumberType): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = NumberType()
                right=right.typ
            if not isinstance(left, NumberType) or not isinstance(right, NumberType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op in ['and', 'or']: # input Bool
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if left is None or right is None:
                return None
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, BoolType): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = BoolType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, BoolType): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = BoolType()
                right=right.typ
            if not isinstance(left, BoolType) or not isinstance(right, BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op == '...': # input String
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if left is None or right is None:
                return None
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, StringType): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = StringType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, StringType): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = StringType()
                right=right.typ
            if not isinstance(left, StringType) or not isinstance(right, StringType):
                raise TypeMismatchInExpression(ctx)
            return StringType()
        if ctx.op == '==': # input String
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if left is None or right is None:
                return None
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, StringType): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = StringType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, StringType): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = StringType()
                right=right.typ
            if not isinstance(left, StringType) or not isinstance(right, StringType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnaryOp(self, ctx:UnaryOp, o:object):
        if ctx.op == '-': # input Number
            operand=self.visit(ctx.operand, o)
            if operand is None:
                return None
            if isinstance(operand, Symbol):
                if operand.typ is not None:
                    if not isinstance(operand.typ, NumberType): raise TypeMismatchInExpression(ctx)
                elif operand.typ is None: operand.typ = NumberType()
                operand=operand.typ
            if not isinstance(operand, NumberType):
                raise TypeMismatchInExpression(ctx)
            return NumberType()
        if ctx.op == 'not': # input Bool
            operand=self.visit(ctx.operand, o)
            if operand is None:
                return None
            if isinstance(operand, Symbol):
                if operand.typ is not None:
                    if not isinstance(operand.typ, BoolType): raise TypeMismatchInExpression(ctx)
                elif operand.typ is None: operand.typ = BoolType()
                operand=operand.typ
            if not isinstance(operand, BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()           

    def visitCallExpr(self, ctx:CallExpr, o:object):
        # func call expr
        id=None
        for x in o:
            for symbol in x:
                if ctx.name.name == symbol.name and symbol.declKind.kind != 'var':
                    id=symbol
                    break
            if id is not None: break
        if id is None: raise Undeclared(Function(), ctx.name.name)
        # if id.declKind.kind == 'funcDecl': raise NoDefinition(id.name)
        if len(ctx.args) != len(id.declKind.param): raise TypeMismatchInExpression(ctx)
        for i in range(len(ctx.args)):
            typ = self.visit(ctx.args[i], o)
            if typ is None:
                return None
            if isinstance(typ, Symbol):
                if typ.typ is None:typ.typ=id.declKind.param[i].typ
                if type(typ.typ) != type(id.declKind.param[i].typ): raise TypeMismatchInExpression(ctx)
                continue
            if type(typ) != type(id.declKind.param[i].typ): raise TypeMismatchInExpression(ctx)
            if isinstance(typ, ArrayType):
                if not isinstance(typ.eleType, Type):
                    if id.declKind.param[i].typ.size < typ.size: raise TypeCannotBeInferred(ctx)
                    resi=id.declKind.param[i].typ.size[:]
                    for i in range(len(typ.size)):
                        if id.declKind.param[i].typ.size[i] != typ.size[i]: raise TypeCannotBeInferred(ctx)
                        resi.pop(0)
                    if resi:
                        Utils.infer(typ.eleType, ArrayType(resi, id.declKind.param[i].typ.eleType))
                        typ=id.declKind.param[i].typ
                    elif not resi:
                        Utils.infer(typ.eleType, id.declKind.param[i].typ.eleType)
                        typ=id.declKind.param[i].typ
                if type(typ.eleType) != type(id.declKind.param[i].typ.eleType) or typ.size != id.declKind.param[i].typ.size: raise TypeMismatchInExpression(ctx)
        if isinstance(id.typ, VoidType): raise TypeMismatchInExpression(ctx)
        return id

    def visitId(self, ctx:Id, o:object):
        for x in o:
            for symbol in x:
                if ctx.name == symbol.name and symbol.declKind.kind == 'var':
                    return symbol
        raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx:ArrayCell, o:object):
        size=[]
        typ=self.visit(ctx.arr, o)
        if isinstance(typ, Symbol):
            if not isinstance(typ.typ, ArrayType): raise TypeMismatchInExpression(ctx)
            if len(ctx.idx) > len(typ.typ.size): raise TypeMismatchInExpression(ctx)
            for i in ctx.idx:
                idx=self.visit(i, o)
                if idx is None:
                    return None
                if isinstance(idx, Symbol):
                    if idx.typ is None:
                        idx.typ = NumberType()
                        continue
                    if idx.typ is not None: idx=idx.typ
                if type(idx) is not NumberType: raise TypeMismatchInExpression(ctx)
        if len(ctx.idx) < len(typ.typ.size):
            resi=typ.typ.size[:]
            for i in range(len(ctx.idx)):
                resi.pop(0)
            size=resi
        if not size: return typ.typ.eleType
        elif size: return ArrayType(size, typ.typ.eleType)

    def visitBlock(self, ctx:Block, o:object):
        o=[[]]+o
        for stmt in ctx.stmt:
            self.visit(stmt, o)

    def visitIf(self, ctx:If, o:object):
        # if expr
        typeIf=self.visit(ctx.expr,o)
        if typeIf is None:
            return None
        if isinstance(typeIf, Symbol):
            if typeIf.typ is None: typeIf.typ = BoolType()
            elif typeIf.typ is not None:
                if not isinstance(typeIf.typ, BoolType): raise TypeMismatchInStatement(ctx)
            typeIf=typeIf.typ
        if not isinstance(typeIf, BoolType): raise TypeMismatchInStatement(ctx)
        self.visit(ctx.thenStmt, [[]]+o)
        # elif expr
        for tup in ctx.elifStmt:
            typeElif=self.visit(tup[0],o)
            if typeElif is None:
                return None
            if isinstance(typeElif, Symbol):
                if typeElif.typ is None: typeElif.typ = BoolType()
                elif typeElif.typ is not None:
                    if not isinstance(typeElif.typ, BoolType): raise TypeMismatchInStatement(ctx)
                typeElif=typeElif.typ
            if not isinstance(typeElif, BoolType): raise TypeMismatchInStatement(ctx)
            self.visit(tup[1],[[]]+o)
        if ctx.elseStmt is not None: self.visit(ctx.elseStmt,[[]]+o)
        return

    def visitFor(self, ctx:For, o:object):
        typ=self.visit(ctx.name,o)
        if typ.typ is None: typ.typ = NumberType()
        elif not isinstance(typ, NumberType): raise TypeMismatchInStatement(ctx)
        typ=self.visit(ctx.condExpr,o)
        if typ is None:
            return None
        if isinstance(typ, Symbol):
            if typ.typ is None: typ.typ = BoolType()
            elif not isinstance(typ, BoolType): raise TypeMismatchInStatement(ctx)
        typ=self.visit(ctx.updExpr,o)
        if typ is None:
            return None
        if isinstance(typ, Symbol):
            if typ.typ is None: typ.typ = NumberType()
            elif not isinstance(typ, NumberType): raise TypeMismatchInStatement(ctx)
        self.visit(ctx.body, [[Symbol(DeclKind("var"),"inloop")]]+o)
        return

    def visitContinue(self, ctx:Continue, o:object):
        for scope in o:
            for symbol in scope:
                if symbol.name == "inloop": return
        raise MustInLoop(ctx)

    def visitBreak(self, ctx:Break, o:object):
        for scope in o:
            for symbol in scope:
                if symbol.name == "inloop": return
        raise MustInLoop(ctx)

    def visitReturn(self, ctx:Return, o:object):
        typ=None
        if ctx.expr is None: typ=VoidType()
        elif ctx.expr is not None:
            typ = self.visit(ctx.expr, o)
            if typ is None:
                return None
            if isinstance(typ, Symbol):
                if typ.typ is None: raise TypeCannotBeInferred(ctx)
                elif typ.typ is not None: typ=typ.typ
            
        for scope in o:
            for symbol in scope:
                if symbol.declKind.kind == "funcDefi":
                    if symbol.typ is None:
                        if isinstance(typ, ArrayType):
                            if not isinstance(typ.eleType, Type): raise TypeCannotBeInferred(ctx)
                        symbol.typ=typ
                        return
                    elif type(symbol.typ) == type(typ):
                        if isinstance(symbol.typ, ArrayType):
                            if not isinstance(typ.eleType, Type):
                                if symbol.typ.size < typ.size: raise TypeCannotBeInferred(ctx)
                                resi=symbol.typ.size[:]
                                for i in range(len(typ.size)):
                                    if symbol.typ.size[i] != typ.size[i]: raise TypeCannotBeInferred(ctx)
                                    resi.pop(0)
                                if resi:
                                    Utils.infer(typ.eleType, ArrayType(resi, symbol.typ.eleType))
                                    typ=symbol.typ
                                elif not resi:
                                    Utils.infer(typ.eleType, symbol.typ.eleType)
                                    typ=symbol.typ
                            #     Utils.infer(typ.eleType, symbol.typ.eleType)
                            #     typ.eleType=symbol.typ.eleType
                            if (type(typ.eleType) != type(symbol.typ.eleType)) or (typ.size != symbol.typ.size):
                                raise TypeMismatchInStatement(ctx)
                        return
                    elif type(symbol.typ) != type(typ):
                        raise TypeMismatchInStatement(ctx)
                # elif symbol.declKind.kind == "funcDecl": raise NoDefinition(symbol.name)

    def visitAssign(self, ctx:Assign, o:object):
        lhs=self.visit(ctx.lhs, o)
        rhs=self.visit(ctx.rhs, o)
        if lhs is None or rhs is None:
            raise TypeCannotBeInferred(ctx)
        if isinstance(lhs, Symbol) and isinstance(rhs, Symbol):
            if lhs.typ is None:
                if rhs.typ is None: raise TypeCannotBeInferred(ctx)
                elif rhs.typ is not None:
                    lhs.typ=rhs.typ
                    return
            if rhs.typ is None:
                if lhs.typ is None: raise TypeCannotBeInferred(ctx)
                elif lhs.typ is not None:
                    rhs.typ = lhs.typ
                    return
            elif lhs.typ is not None and rhs.typ is not None:
                if type(lhs.typ) != type(rhs.typ): raise TypeMismatchInStatement(ctx)
                if isinstance(lhs.typ, ArrayType):
                    if (type(lhs.typ.eleType) != type(rhs.typ.eleType)) or (lhs.typ.size != rhs.typ.size):
                        raise TypeMismatchInStatement(ctx)
        elif isinstance(lhs, Symbol):
            if lhs.typ is None:
                if rhs is None: raise TypeCannotBeInferred(ctx)
                elif rhs is not None:
                    if isinstance(rhs, ArrayType) and not isinstance(rhs.eleType, Type): raise TypeCannotBeInferred(ctx)
                    lhs.typ=rhs
                    return
            elif lhs.typ is not None:
                if type(lhs.typ) != type(rhs): raise TypeMismatchInStatement(ctx)
                if isinstance(lhs.typ, ArrayType):
                    if not isinstance(rhs.eleType, Type):
                        if lhs.typ.size < rhs.size: raise TypeCannotBeInferred(ctx)
                        resi=lhs.typ.size[:]
                        for i in range(len(rhs.size)):
                            if lhs.typ.size[i] != rhs.size[i]: raise TypeCannotBeInferred(ctx)
                            resi.pop(0)
                        if resi:
                            Utils.infer(rhs.eleType, ArrayType(resi, lhs.typ.eleType))
                            rhs=lhs.typ
                        elif not resi:
                            Utils.infer(rhs.eleType, lhs.typ.eleType)
                            rhs=lhs.typ
                    #     Utils.infer(rhs.eleType, lhs.typ.eleType)
                    #     rhs.eleType=lhs.typ.eleType
                    if (type(lhs.typ.eleType) != type(rhs.eleType)) or (lhs.typ.size != rhs.size):
                        raise TypeMismatchInStatement(ctx)
        elif not isinstance(lhs, Symbol) and not isinstance(rhs, Symbol):
            if type(lhs) != type(rhs): raise TypeMismatchInStatement(ctx)
            if isinstance(lhs, ArrayType):
                if type(lhs.eleType) != type(rhs.eleType): raise TypeMismatchInStatement(ctx)
                if lhs.size != rhs.size: raise TypeMismatchInStatement(ctx)
        elif not isinstance(lhs, Symbol):
            if rhs.typ is None:
                if lhs is None: raise TypeCannotBeInferred(ctx)
                elif lhs is not None:
                    rhs.typ = lhs
                    return
            elif lhs is not None and rhs.typ is not None:
                if type(lhs) != type(rhs.typ): raise TypeMismatchInStatement(ctx)
                if isinstance(rhs.typ, ArrayType):
                    if (type(lhs.eleType) != type(rhs.typ.eleType)) or (lhs.size != rhs.typ.size):
                        raise TypeMismatchInStatement(ctx)
            

    def visitCallStmt(self, ctx:CallStmt, o:object):
        # func call stmt
        id=None
        for x in o:
            for symbol in x:
                if ctx.name.name == symbol.name and symbol.declKind.kind != 'var':
                    id=symbol
                    break
            if id is not None: break
        if id is None: raise Undeclared(Function(), ctx.name.name)
        # if id.declKind.kind == 'funcDecl': raise NoDefinition(id.name)
        
        if id.typ is None: id.typ=VoidType
        elif not isinstance(id.typ, VoidType): raise TypeMismatchInStatement(ctx)
        
        if len(ctx.args) != len(id.declKind.param): raise TypeMismatchInStatement(ctx)
        for i in range(len(ctx.args)):
            typ = self.visit(ctx.args[i], o)
            if typ is None:
                raise TypeCannotBeInferred(ctx)
            if isinstance(typ, Symbol):
                if typ.typ is None:typ.typ=id.declKind.param[i].typ
                if type(typ.typ) != type(id.declKind.param[i].typ): raise TypeMismatchInStatement(ctx)
                continue
            if type(typ) != type(id.declKind.param[i].typ): raise TypeMismatchInStatement(ctx)
            if isinstance(typ, ArrayType):
                if not isinstance(typ.eleType, Type):
                    if id.declKind.param[i].typ.size < typ.size: raise TypeCannotBeInferred(ctx)
                    resi=id.declKind.param[i].typ.size[:]
                    for i in range(len(typ.size)):
                        if id.declKind.param[i].typ.size[i] != typ.size[i]: raise TypeCannotBeInferred(ctx)
                        resi.pop(0)
                    if resi:
                        Utils.infer(typ.eleType, ArrayType(resi, id.declKind.param[i].typ.eleType))
                        typ=id.declKind.param[i].typ
                    elif not resi:
                        Utils.infer(typ.eleType, id.declKind.param[i].typ.eleType)
                        typ=id.declKind.param[i].typ
                #     Utils.infer(typ.eleType, id.declKind.param[i].typ.eleType)
                #     typ.eleType=id.declKind.param[i].typ.eleType
                if type(typ.eleType) != type(id.declKind.param[i].typ.eleType) or typ.size != id.declKind.param[i].typ.size: raise TypeMismatchInStatement(ctx)
        

    def visitNumberLiteral(self, ctx:NumberLiteral, o:object):
        return NumberType()

    def visitBooleanLiteral(self, ctx:BooleanLiteral, o:object):
        return BoolType()

    def visitStringLiteral(self, ctx:StringLiteral, o:object):
        return StringType()

    def visitArrayLiteral(self, ctx:ArrayLiteral, o:object):
        size=None # size: List[float]
        eleType=None # eleType: Type
        value=[]
        for expr in ctx.value:
            typ=self.visit(expr, o)
            if typ is None:
                return None
            value.append(typ)
        size=[float(len(ctx.value))]
        for typ in value:
            if isinstance(typ, Symbol):
                if typ.typ is not None:
                    eleType=typ.typ
                    break
                continue
            if isinstance(typ, ArrayType):
                if isinstance(typ.eleType, Type):
                    eleType=typ
                    break
                continue
            eleType=typ
            break
        if eleType is not None: # infer in expr
            for i in range(len(ctx.value)):
                if isinstance(value[i], Symbol):
                    if value[i].typ is not None:
                        if type(value[i].typ) != type(eleType): raise TypeMismatchInExpression(ctx)
                        continue
                    elif value[i].typ is None:
                        value[i].typ=eleType
                        continue
                if isinstance(value[i], ArrayType):
                    if isinstance(eleType, ArrayType):
                        if isinstance(value[i].eleType, Type):
                            if type(value[i].eleType) != type(eleType.eleType): raise TypeMismatchInExpression(ctx)
                            continue
                        elif not isinstance(value[i].eleType, Type):
                            Utils.infer(value[i].eleType, eleType.eleType)
                            continue
                    elif not isinstance(eleType, ArrayType):
                        if isinstance(value[i].eleType, Type):
                            if type(value[i].eleType) != type(eleType): raise TypeMismatchInExpression(ctx)
                            continue
                        elif not isinstance(value[i].eleType, Type):
                            Utils.infer(value[i].eleType, eleType)
                            continue
                if type(value[i]) != type(eleType): raise TypeMismatchInExpression(ctx)
            if isinstance(eleType, ArrayType): eleType=eleType.eleType
        elif eleType is None:
            eleType=[]
            for typ in value:
                if isinstance(typ, ArrayType):
                    eleType+=typ.eleType
                elif isinstance(typ, Symbol):
                    eleType+=[typ]
        check_size=None
        for typ in value:
            if isinstance(typ, ArrayType):
                check_size=typ.size
            elif isinstance(typ, Symbol):
                if isinstance(typ.typ, ArrayType):
                    check_size=typ.typ.size
                else: check_size=1
            else: check_size=1
            break
        for typ in value:
            if isinstance(typ, ArrayType):
                if check_size != typ.size: raise TypeMismatchInExpression(ctx)
            elif isinstance(typ, Symbol):
                if isinstance(typ.typ, ArrayType):
                    if check_size != typ.typ.size: raise TypeMismatchInExpression(ctx)
                else:
                    if check_size != 1: raise TypeMismatchInExpression(ctx)
            else:
                if check_size != 1: raise TypeMismatchInExpression(ctx)
        if isinstance(value[0], ArrayType):
            size+=value[0].size
        return ArrayType(size, eleType)

######## Code gen ########

class ClassData:
    def __init__(self, cname, pname, mem):
        self.cname = cname # class name
        self.pname = pname # parent name
        self.mem = mem

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class SymbolLove:
    def __init__(self, name:str, mtype:MType, value=None, kind=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind # var or func

    def __str__(self):
        return "Symbol("+self.name+","+str(self.mtype)+")"

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [SymbolLove("readNumber", MType(list(), NumberType()), CName(self.libName), 'func'),
                SymbolLove("writeNumber", MType([NumberType()],
                       VoidType()), CName(self.libName), 'func'),
                SymbolLove("readBool", MType(list(), BoolType()), CName(self.libName), 'func'),
                SymbolLove("writeBool", MType([BoolType()],
                       VoidType()), CName(self.libName), 'func'),
                SymbolLove("readString", MType(list(), StringType()), CName(self.libName), 'func'),
                SymbolLove("writeString", MType([StringType()],
                       VoidType()), CName(self.libName), 'func')
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        glob = StaticChecker(ast).check()        
        glob_env = []
        for sym in glob[0][:(len(glob[0])-6)]:
            glob_env.append(SymbolLove(sym.name,
                MType([i.typ for i in sym.declKind.param] if sym.declKind.kind!='var' else None,sym.typ),
                CName("ZCodeClass"), 'func' if sym.declKind.kind != 'var' else 'var'))
        gl = self.init()
        gc = CodeGenVisitor(ast, gl+glob_env, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value

class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.globInit=list() #list of Assign stmt

    def visitProgram(self, ast:Program, c):
        ctx = ClassType("ZCodeClass")
        self.className = ctx.classname
        self.emit = Emitter(self.path+"/" + self.className + ".j")
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for ele in ast.decl:
            if type(ele) is VarDecl:
                self.visit(ele, SubBody(None, self.env))
        self.genMETHOD(FuncDecl(Id("<clinit>"), list(), Block(self.globInit)), self.env, Frame("<clinit>", None))
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None), self.env, Frame("<init>", None))
        for ele in ast.decl:
            if type(ele) is FuncDecl:
                self.visit(ele, self.env)
        self.emit.emitEPILOG()

    def visitClassDecl(self, ast, c):
        pass

    def genMETHOD(self, ast, o, frame):
        isInit = ast.name.name == "<init>"
        isClinit = ast.name.name == "<clinit>"
        isMain = ast.name.name == "main" and len(
            ast.param) == 0 and type(frame.returnType) is VoidType
        returnType = frame.returnType if isMain else VoidType()
        methodName = ast.name.name
        intype = None
        isStatic = None
        if isMain:
            intype=[ArrayType(0, StringType())]
            isStatic=True
        elif isInit or isClinit:
            intype=[]
            isStatic=False
        else:
            symbol=None
            for sym in o:
                if sym.name == ast.name.name and type(sym.value) is CName:
                    symbol=sym
                    break
            intype=symbol.mtype.partype
            isStatic=True
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(
            methodName, mtype, isStatic, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(
                Id(self.className)), frame.getStartLabel(), frame.getEndLabel(), frame))
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(
                Id(self.className)), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                0, StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(
                frame, [self.visit(ele, env)]+env.sym), ast.param, SubBody(frame, []))
            glenv = local.sym+glenv

        body = ast.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if body is not None: self.visit(body, SubBody(frame, glenv))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        noReturn = True
        if type(body) is Block:
            for stmt in body.stmt:
                if type(stmt) is Return: noReturn = False
        if noReturn:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast:FuncDecl, o):
        symbol=None
        for sym in o:
            if sym.name == ast.name.name and sym.kind == 'func':
                symbol=sym
                break
        frame = Frame(ast.name.name, symbol.mtype.rettype)
        self.genMETHOD(ast, o, frame)

    def visitVarDecl(self, ast:VarDecl, o):
        if o.frame is not None:
            idx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.name.name, ast.varType,
                o.frame.getStartLabel(), o.frame.getEndLabel()))
            return SymbolLove(ast.name.name, MType(None,ast.varType), Index(idx), 'var')
        if o.frame is None:
            symbol=None
            for sym in o:
                if sym.name == ast.name.name and sym.kind == 'var':
                    symbol=sym
                    break
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name.name, symbol.mtype.rettype, False, ""))
            if ast.varInit is not None:
                self.globInit+=[Assign(Id(ast.name), ast.varInit)]
            

    def visitNumberType(self, ast:NumberType, o):
        pass

    def visitBoolType(self, ast:BoolType, o):
        pass

    def visitStringType(self, ast:StringType, o):
        pass

    def visitArrayType(self, ast:ArrayType, o):
        pass

    def visitBinaryOp(self, ast:BinaryOp, o):
        e1code, e1type = self.visit(ast.left,o)
        e2code, e2type = self.visit(ast.right,o)
        op = ast.op
        
        right = e1type
        if op in ['>','<','>=','<=','!=','=']:
            #if op == '=': op = '==' # ZCode make = be the compare of number
            opCode = fast[op](op, right, o.frame)
            right = BoolType()
        elif op in ['+', '-', '', '/']: #['+', '-', '', '/', '%']:
            opCode = fast[op](op, right, o.frame)
            right = NumberType()
        elif op == '%':
            opCode = self.emit.emitMOD(o.frame)
            right = NumberType()
        elif op == 'and':
            opCode = self.emit.emitANDOP(o.frame)
            right = BoolType()
        elif op == 'or':
            opCode = self.emit.emitOROP(o.frame)
            right = BoolType()
        elif op == "...":
            obj = "\tnew java/lang/StringBuilder\n"
            duplicate = "\tdup\n"
            initialize = "\tinvokespecial java/lang/StringBuilder/<init>()V\n"
            apd = "\tinvokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;\n"
            sth2Str = "\tinvokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;\n"
            return obj+duplicate+initialize+ e1code+apd+ e2code+apd +sth2Str, StringType()
        elif op == "==":
            opcode = "\tinvokevirtual java/lang/String/equals(Ljava/lang/Object;)Z\n"
            right = BoolType()
        return e1code + e2code + opcode, right
    
    def visitUnaryOp(self, ast, o):
        op = ast.op
        ec, typ = self.visit(ast.operand, o)
        if op == '-':
            return ec + self.emit.emitNEGOP(typ, o.frame), typ
        return ec + self.emit.emitNOT(typ, o.frame), typ

    def visitCallExpr(self, ast:CallExpr, o):
        pass

    def visitId(self, ast:Id, o):
        pass

    def visitArrayCell(self, ast:ArrayCell, o):
        pass

    def visitBlock(self, ast:Block, o):
        list(map(lambda x: self.visit(x, o), ast.stmt))

    def visitIf(self, ast:If, o):
        pass

    def visitFor(self, ast:For, o):
        pass

    def visitContinue(self, ast:Continue, o):
        pass

    def visitBreak(self, ast:Break, o):
        pass

    def visitReturn(self, ast:Return, o):
        pass

    def visitAssign(self, ast:Assign, o):
        pass

    def visitCallStmt(self, ast:CallStmt, o):
        frame = o.frame
        nenv = o.sym
        sym = next(filter(lambda x: ast.name.name == x.name and x.kind == 'func', nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", list())
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1))
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
            cname + "/" + ast.name.name, ctype, frame))

    def visitNumberLiteral(self, ast:NumberLiteral, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), NumberType()

    def visitBooleanLiteral(self, ast:BooleanLiteral, o):
        pass

    def visitStringLiteral(self, ast:StringLiteral, o):
        pass

    def visitArrayLiteral(self, ast:ArrayLiteral, o):
        pass
