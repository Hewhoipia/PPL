from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class DeclKind:
    def __init__(self, kind:str, param:list=None):
        # kind must be 'var', 'param', 'funcDecl' or 'funcDefi'
        self.kind=kind
        self.param=param
        
class Symbol:
    def __init__(self, kind:DeclKind, name:str, typ:Type=None):
        self.kind=kind
        self.name=name
        self.typ=typ

class Utils:
    def Infer(o, name:object, typ:Type):
        for scope in o:
            for symbol in scope:
                if symbol.name == name:
                    symbol.typ=typ
                    return typ
        

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
        if ctx.varType is not None or ctx.modifier is not None:
            typ=None
            if ctx.varType is not None and ctx.varInit is not None:
                typDecl=self.visit(ctx.varType)
                typInit=self.visit(ctx.varInit)
                if 
            elif ctx.varType is not None:
                typ = self.visit(ctx.varType)
            elif ctx.varInit is not None:
                typ = self.visit(ctx.varInit)
            for symbol in o[0]:
                if ctx.name.name == symbol.name:
                    raise Redeclared(Variable, ctx.name.name)
            o[0].append(Symbol(DeclKind('var'), ctx.name.name, typ))
        else:
            pass

    def visitFuncDecl(self, ctx:FuncDecl, o:object):
        param=[]
        for x in ctx.param:
            typ=self.visit(x.varType)
            for symbol in param:
                if x.name.name == symbol.name:
                    raise Redeclared(Parameter, x.name.name)
            param.append(Symbol(DeclKind('param'), x.name.name, typ))
        o[0].append(Symbol(DeclKind('funcDecl' if ctx.body is None else 'funcDefi', param), ctx.name.name))

    def visitNumberType(self, ctx:NumberType, o:object):
        pass

    def visitBoolType(self, ctx:BoolType, o:object):
        pass

    def visitStringType(self, ctx:StringType, o:object):
        pass

    def visitArrayType(self, ctx:ArrayType, o:object):
        pass

    def visitBinaryOp(self, ctx:BinaryOp, o:object):
        pass

    def visitUnaryOp(self, ctx:UnaryOp, o:object):
        pass

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
        pass

    def visitBooleanLiteral(self, ctx:BooleanLiteral, o:object):
        pass

    def visitStringLiteral(self, ctx:StringLiteral, o:object):
        pass

    def visitArrayLiteral(self, ctx:ArrayLiteral, o:object):
        pass