# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declare.
    def visitDeclare(self, ctx:BKOOLParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declare_tail.
    def visitDeclare_tail(self, ctx:BKOOLParser.Declare_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardecl.
    def visitVardecl(self, ctx:BKOOLParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#num_type.
    def visitNum_type(self, ctx:BKOOLParser.Num_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_ID.
    def visitList_ID(self, ctx:BKOOLParser.List_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_ID_tail.
    def visitList_ID_tail(self, ctx:BKOOLParser.List_ID_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#funcdecl.
    def visitFuncdecl(self, ctx:BKOOLParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_param.
    def visitList_param(self, ctx:BKOOLParser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_param_tail.
    def visitList_param_tail(self, ctx:BKOOLParser.List_param_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#each_param.
    def visitEach_param(self, ctx:BKOOLParser.Each_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_expr.
    def visitList_expr(self, ctx:BKOOLParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_expr_tail.
    def visitList_expr_tail(self, ctx:BKOOLParser.List_expr_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#list_stmt.
    def visitList_stmt(self, ctx:BKOOLParser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt.
    def visitStmt(self, ctx:BKOOLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_assi.
    def visitStmt_assi(self, ctx:BKOOLParser.Stmt_assiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_call.
    def visitStmt_call(self, ctx:BKOOLParser.Stmt_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stmt_return.
    def visitStmt_return(self, ctx:BKOOLParser.Stmt_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_ADD.
    def visitExpr_ADD(self, ctx:BKOOLParser.Expr_ADDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_SUB.
    def visitExpr_SUB(self, ctx:BKOOLParser.Expr_SUBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_MULDIV.
    def visitExpr_MULDIV(self, ctx:BKOOLParser.Expr_MULDIVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr_other.
    def visitExpr_other(self, ctx:BKOOLParser.Expr_otherContext):
        return self.visitChildren(ctx)



del BKOOLParser