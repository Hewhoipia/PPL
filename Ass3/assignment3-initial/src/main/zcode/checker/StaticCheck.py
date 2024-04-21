from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

# Phan Thanh Thong - 2153846

class DeclKind:
    def __init__(self, kind:str, param:list=None):
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
        self.visit(self.root, None)
    
    def visitProgram(self, ctx:Program, o:object):
        o=[[]]
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
            if symbol.name == 'main' and symbol.declKind.kind == 'funcDefi' and not symbol.declKind.param:
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
        elif ctx.varInit is not None:
            symbol=Symbol(DeclKind('var'), ctx.name.name, typ)
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
            elif is_func_decl is None:
                o[0].insert(0,Symbol(DeclKind('funcDefi', param[0]), ctx.name.name))
            self.visit(ctx.body,[[]]+param+o)
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
        if isinstance(id.typ, VoidType): raise TypeMismatchInExpression(ctx)
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
            for i in range(len(ctx.idx)):
                size.append(typ.typ.size[i])
        if not size: return typ.typ.eleType
        elif size: return ArrayType(size, typ.typ.eleType)

    def visitBlock(self, ctx:Block, o:object):
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
        # raise PrintTest(lhs.name + "|" + str(type(lhs.typ)))
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
                    eleType=typ.eleType
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
                    if isinstance(value[i].eleType, Type):
                        if type(value[i].eleType) != type(eleType): raise TypeMismatchInExpression(ctx)
                        continue
                    elif not isinstance(value[i].eleType, Type):
                        Utils.infer(value[i].eleType, eleType)
                        continue
                if type(value[i]) != type(eleType): raise TypeMismatchInExpression(ctx)
        elif eleType is None:
            eleType=[]
            for typ in value:
                if isinstance(typ, ArrayType):
                    eleType+=typ.eleType
                elif isinstance(typ, Symbol):
                    eleType+=[typ]
        if isinstance(value[0], ArrayType):
            for typ in value:
                if typ.size != value[0].size: raise TypeMismatchInExpression(ctx)
            size+=value[0].size
        return ArrayType(size, eleType)