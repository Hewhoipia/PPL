from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

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
    def monoInfer(o, obj:Symbol, typ:Type):
        pass

class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.root=ast

    def check(self):
        return self.visit(self.root, None)
    
    def visitProgram(self, ctx:Program, o:object):
        o=[[]]
        for x in ctx.decl:
            self.visit(x,o)
        for symbol in o[0]:
            if symbol.name == 'main': return
        raise NoEntryPoint()

    def visitVarDecl(self, ctx:VarDecl, o:object):
        for symbol in o[0]:
            if ctx.name.name == symbol.name and symbol.declKind.kind == 'var':
                raise Redeclared(Variable(), ctx.name.name)
        typ=None
        if ctx.varType is not None and ctx.varInit is not None:
            typDecl=ctx.varType
            typInit=self.visit(ctx.varInit,o)
            if isinstance(typInit, Symbol):
                if typInit.typ is None: typInit.typ = typDecl
                typInit=typInit.typ
            if type(typDecl) != type(typInit): raise TypeMismatchInStatement(ctx)
            if isinstance(typDecl, ArrayType):
                if type(typDecl.eleType) != type(typInit.eleType): raise TypeMismatchInStatement(ctx)
                #if typDecl.size != typInit.size: raise TypeMismatchInStatement(ctx)
            typ=typDecl
        elif ctx.varType is not None:
            typ = ctx.varType
        elif ctx.varInit is not None:
            typInit = self.visit(ctx.varInit,o)
            if isinstance(typInit, Symbol):
                if typInit.typ is None: raise TypeCannotBeInferred(ctx)
                typInit=typInit.typ
            typ=typInit
        o[0].append(Symbol(DeclKind('var'), ctx.name.name, typ))
            
    def visitFuncDecl(self, ctx:FuncDecl, o:object):
        for symbol in o[0]:
            if ctx.name.name == symbol.name and symbol.declKind.kind != 'var':
                if symbol.declKind.kind == 'funcDefi' or (symbol.declKind.kind == 'funcDecl' and ctx.body is None):
                    raise Redeclared(Variable(), ctx.name.name)
        param=[[]]
        for vardecl in ctx.param:
            typ=None
            if vardecl.varInit is not None:
                typDecl=vardecl.varType
                typInit=self.visit(vardecl.varInit,param+o)
                if isinstance(typInit, Symbol):
                    if typInit.typ is None: typInit.typ = typDecl
                    typInit=typInit.typ
                if type(typDecl) != type(typInit): raise TypeMismatchInStatement(vardecl)
                if isinstance(typDecl, ArrayType):
                    if type(typDecl.eleType) != type(typInit.eleType): raise TypeMismatchInStatement(vardecl)
                    #if typDecl.size!= typInit.size: raise TypeMismatchInStatement(vardecl)
                typ=typDecl
            else:
                typ=vardecl.varType
            for symbol in param[0]:
                if vardecl.name.name == symbol.name:
                    raise Redeclared(Parameter(), vardecl.name.name)
            param[0].append(Symbol(DeclKind('param'), vardecl.name.name, typ))
        o[0].append(Symbol(DeclKind('funcDecl' if ctx.body is None else 'funcDefi', param[0]), ctx.name.name))
        if ctx.body is not None: self.visit(ctx.body,[[]]+param+o)

    def visitBinaryOp(self, ctx:BinaryOp, o:object):
        if ctx.op in ['+', '-', '*', '/', '%']: # input Number
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, NumberType()): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = NumberType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, NumberType()): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = NumberType()
                right=right.typ
            if not isinstance(left, NumberType) or not isinstance(right, NumberType):
                raise TypeMismatchInExpression(ctx)
            return NumberType()
        if ctx.op in ['=', '!=', '<', '>', '<=', '>=']: # input Number
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, NumberType()): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = NumberType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, NumberType()): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = NumberType()
                right=right.typ
            if not isinstance(left, NumberType) or not isinstance(right, NumberType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op in ['and', 'or']: # input Bool
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, BoolType()): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = BoolType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, BoolType()): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = BoolType()
                right=right.typ
            if not isinstance(left, BoolType) or not isinstance(right, BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()
        if ctx.op == '...': # input String
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, StringType()): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = StringType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, StringType()): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = StringType()
                right=right.typ
            if not isinstance(left, StringType) or not isinstance(right, StringType):
                raise TypeMismatchInExpression(ctx)
            return StringType()
        if ctx.op == '==': # input String
            left=self.visit(ctx.left, o)
            right=self.visit(ctx.right, o)
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, StringType()): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = StringType()
                left=left.typ
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, StringType()): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = StringType()
                right=right.typ
            if not isinstance(left, StringType) or not isinstance(right, StringType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnaryOp(self, ctx:UnaryOp, o:object):
        if ctx.op == '-': # input Number
            operand=self.visit(ctx.operand, o)
            if isinstance(operand, Symbol):
                if operand.typ is not None:
                    if not isinstance(operand.typ, NumberType()): raise TypeMismatchInExpression(ctx)
                elif operand.typ is None: operand.typ = NumberType()
                operand=operand.typ
            if not isinstance(operand, NumberType):
                raise TypeMismatchInExpression(ctx)
            return NumberType()
        if ctx.op == 'not': # input Bool
            operand=self.visit(ctx.operand, o)
            if isinstance(operand, Symbol):
                if operand.typ is not None:
                    if not isinstance(operand.typ, BoolType()): raise TypeMismatchInExpression(ctx)
                elif operand.typ is None: operand.typ = BoolType()
                operand=operand.typ
            if not isinstance(operand, BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()           

    def visitCallExpr(self, ctx:CallExpr, o:object):
        # func call
        id=None
        for x in o:
            for symbol in x:
                if ctx.name.name == symbol.name and symbol.declKind.kind != 'var':
                    id=symbol
        if id is None: raise Undeclared(Function(), ctx.name.name)
        if id.declKind.kind == 'funcDecl': raise NoDefinition(id.name)
        if isinstance(id.typ, VoidType): raise TypeMismatchInExpression(ctx)
        if len(ctx.args) != len(id.declKind.param): raise TypeMismatchInExpression(ctx)
        for i in range(len(ctx.args)):
            typ = self.visit(ctx.args[i], o)
            if isinstance(typ, Symbol):
                if typ.typ is None:typ.typ=id.declKind.param[i].typ
                if type(typ.typ) != type(id.declKind.param[i].typ): raise TypeMismatchInExpression(ctx)
                continue
            if type(typ) != type(id.declKind.param[i].typ): raise TypeMismatchInExpression(ctx)
            if isinstance(typ, ArrayType):
                if typ.size != id.declKind.param[i].typ.size: raise TypeMismatchInExpression(ctx)
                if type(typ.eleType) != type(id.declKind.param[i].typ.eleType): raise TypeMismatchInExpression(ctx)
        return id

    def visitId(self, ctx:Id, o:object):
        for x in o:
            for symbol in x:
                if ctx.name == symbol.name and symbol.declKind.kind == 'var':
                    return symbol
        raise Undeclared(Identifier(), ctx.name)

    def visitArrayCell(self, ctx:ArrayCell, o:object):
        typ=self.visit(ctx.arr, o)
        if isinstance(typ, Symbol):
            if not isinstance(typ.typ, ArrayType): raise TypeMismatchInExpression(ctx)
            for i in ctx.idx:
                if isinstance(i, Symbol):
                    if i.typ is None:
                        i.typ = NumberType()
                        break
                    if i.typ is not None: i=i.typ
                if type(self.visit(i)) is not NumberType: raise TypeMismatchInExpression(ctx)
        return typ

    def visitBlock(self, ctx:Block, o:object):
        for stmt in ctx.stmt:
            self.visit(stmt, o)

    def visitIf(self, ctx:If, o:object):
        # if expr
        typeIf=self.visit(ctx.expr)
        if isinstance(typeIf, Symbol):
            if typeIf.typ is None: typeIf.typ = BoolType()
            elif typeIf.typ is not None:
                if not isinstance(typeIf.typ, BoolType): raise TypeMismatchInStatement(ctx)
            typeIf=typeIf.typ
        if not isinstance(typeIf, BoolType): raise TypeMismatchInStatement(ctx)
        self.visit(ctx.thenStmt)
        # elif expr
        for tup in ctx.elifStmt:
            typeElif=self.visit(tup[0])
            if isinstance(typeElif, Symbol):
                if typeElif.typ is None: typeElif.typ = BoolType()
                elif typeElif.typ is not None:
                    if not isinstance(typeElif.typ, BoolType): raise TypeMismatchInStatement(ctx)
                typeElif=typeElif.typ
            if not isinstance(typeElif, BoolType): raise TypeMismatchInStatement(ctx)
            self.visit(tup[1])
        if ctx.elseStmt is not None: self.visit(ctx.elseStmt)

    def visitFor(self, ctx:For, o:object):
        pass

    def visitContinue(self, ctx:Continue, o:object):
        pass

    def visitBreak(self, ctx:Break, o:object):
        pass

    def visitReturn(self, ctx:VarDecl, o:object):
        pass

    def visitAssign(self, ctx:Assign, o:object):
        pass

    def visitCallStmt(self, ctx:CallStmt, o:object):
        pass

    def visitNumberLiteral(self, ctx:NumberLiteral, o:object):
        return NumberType()

    def visitBooleanLiteral(self, ctx:BooleanLiteral, o:object):
        return BoolType()

    def visitStringLiteral(self, ctx:StringLiteral, o:object):
        return BoolType()

    def visitArrayLiteral(self, ctx:ArrayLiteral, o:object):
        size=None # size: List[float]
        eleType=None # eleType: Type
        value=[]
        for expr in ctx.value:
            value.append(self.visit(expr, o))
        for typ in value:
            if isinstance(typ, Symbol):
                if typ.typ is not None:
                    eleType=typ.typ
                    break
                continue
            if isinstance(typ, ArrayType):
                eleType=typ.eleType
                break
            eleType=typ
            break
        if eleType is not None: # infer in expr
            for typ in value:
                if isinstance(typ, Symbol):
                    if typ.typ is not None:
                        if type(typ.typ) != type(eleType): raise TypeMismatchInExpression(ctx)
                    if typ.typ is None:
                        typ.typ=eleType()
        elif eleType is None: raise TypeCannotBeInferred(ctx)
        return ArrayType(size, eleType)