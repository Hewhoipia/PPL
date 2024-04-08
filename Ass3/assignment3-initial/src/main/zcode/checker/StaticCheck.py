from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast):
        self.root=ast

    def check(self):
        return self.visit(self.root,None)
    
    def visitProgram(self, ctx:Program, o:object):
        raise NoEntryPoint()
        o=[[]]
        for x in ctx.decl:
            self.visit(x,o)

    def visitVarDecl(self, ctx:VarDecl, o:object):
        pass

    def visitFuncDecl(self, ctx:FuncDecl, o:object):
        pass

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