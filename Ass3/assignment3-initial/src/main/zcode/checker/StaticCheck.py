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
        self.kind=kind
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
        typ=None
        if ctx.varType is not None and ctx.varInit is not None:
            typDecl=ctx.varType
            typInit=self.visit(ctx.varInit,o)
            if isinstance(typInit, Symbol):
                if typInit.typ is None: typInit.typ = typDecl
                if isinstance(typInit.typ, ArrayType):
                    if type(typInit.typ.eleType) != type(typDecl): raise TypeMismatchInStatement(ctx)
                else:
                    if type(typInit.typ) != type(typDecl): raise TypeMismatchInStatement(ctx)
            else:
                if type(typDecl) != type(typInit): raise TypeMismatchInStatement(ctx)
            typ=typDecl
        elif ctx.varType is not None:
            typ = ctx.varType
        elif ctx.varInit is not None:
            typInit = self.visit(ctx.varInit,o)
            if isinstance(typInit, Symbol):
                if typInit.typ is None: raise TypeCannotBeInferred(ctx)
                typ=typInit.typ
            else: typ=typInit
        for symbol in o[0]:
            if ctx.name.name == symbol.name:
                raise Redeclared(Variable, ctx.name.name)
        o[0].append(Symbol(DeclKind('var'), ctx.name.name, typ))
            
    def visitFuncDecl(self, ctx:FuncDecl, o:object):
        param=[[]]
        for vardecl in ctx.param:
            typ=None
            if vardecl.varInit is not None:
                typDecl=vardecl.varType
                typInit=self.visit(vardecl.varInit,param+o)
                if isinstance(typInit, Symbol):
                    if typInit.typ is None: typInit.typ = typDecl
                    if isinstance(typInit.typ, ArrayType):
                        if type(typInit.typ.eleType) != type(typDecl): raise TypeMismatchInStatement(vardecl)
                    else:
                        if type(typInit.typ) != type(typDecl): raise TypeMismatchInStatement(vardecl)
                else:
                    if type(typDecl) != type(typInit): raise TypeMismatchInStatement(vardecl)
                typ=typDecl
            else:
                typ=vardecl.varType
            for symbol in param[0]:
                if vardecl.name.name == symbol.name:
                    raise Redeclared(Parameter, vardecl.name.name)
            param[0].append(Symbol(DeclKind('param'), vardecl.name.name, typ))
        o[0].append(Symbol(DeclKind('funcDecl' if ctx.body is None else 'funcDefi', param[0]), ctx.name.name))
        if ctx.body is not None: self.visit(ctx.body,param+o)

    def visitBinaryOp(self, ctx:BinaryOp, o:object):
        if ctx.op in ['+', '-', '*', '/', '%']: # input Number
            left=self.visit(ctx.left)
            right=self.visit(ctx.right)
            if isinstance(left, Symbol):
                if left.typ is not None:
                    if not isinstance(left.typ, NumberType()): raise TypeMismatchInExpression(ctx)
                elif left.typ is None: left.typ = NumberType()
            if isinstance(right, Symbol):
                if right.typ is not None:
                    if not isinstance(right.typ, NumberType()): raise TypeMismatchInExpression(ctx)
                elif right.typ is None: right.typ = NumberType()
            return NumberType()
        if ctx.op in ['=', '!=', '<', '>', '<=', '>=']: # input Number
            return BoolType()
        if ctx.op in ['and', 'or']: # input Bool
            return BoolType()
        if ctx.op == '...': # input String
            return StringType()
        if ctx.op == '==': # input String
            return BoolType()

    def visitUnaryOp(self, ctx:UnaryOp, o:object):
        if ctx.op == '-': # input Number
            return NumberType()
        if ctx.op == 'not': # input Bool
            return BoolType()           

    def visitCallExpr(self, ctx:CallExpr, o:object):
        pass

    def visitId(self, ctx:Id, o:object):
        pass

    def visitArrayCell(self, ctx:ArrayCell, o:object):
        pass

    def visitBlock(self, ctx:Block, o:object):
        pass

    def visitIf(self, ctx:If, o:object):
        pass

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
        self.visit(ctx.value)