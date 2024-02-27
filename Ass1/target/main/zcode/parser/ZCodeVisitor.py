# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decls_list.
    def visitDecls_list(self, ctx:ZCodeParser.Decls_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decls_list_tail.
    def visitDecls_list_tail(self, ctx:ZCodeParser.Decls_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decls.
    def visitDecls(self, ctx:ZCodeParser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vari_decls.
    def visitVari_decls(self, ctx:ZCodeParser.Vari_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vari_decls_1.
    def visitVari_decls_1(self, ctx:ZCodeParser.Vari_decls_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vari_decls_2.
    def visitVari_decls_2(self, ctx:ZCodeParser.Vari_decls_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vari_decls_type.
    def visitVari_decls_type(self, ctx:ZCodeParser.Vari_decls_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vari_decls_impli.
    def visitVari_decls_impli(self, ctx:ZCodeParser.Vari_decls_impliContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array.
    def visitArray(self, ctx:ZCodeParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_tail.
    def visitArray_tail(self, ctx:ZCodeParser.Array_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_expr.
    def visitList_expr(self, ctx:ZCodeParser.List_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vari_id.
    def visitVari_id(self, ctx:ZCodeParser.Vari_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decls.
    def visitFunc_decls(self, ctx:ZCodeParser.Func_declsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_param.
    def visitFunc_param(self, ctx:ZCodeParser.Func_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_param.
    def visitList_param(self, ctx:ZCodeParser.List_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_param_tail.
    def visitList_param_tail(self, ctx:ZCodeParser.List_param_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#params.
    def visitParams(self, ctx:ZCodeParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vd_for_func.
    def visitVd_for_func(self, ctx:ZCodeParser.Vd_for_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#vd_type_ff.
    def visitVd_type_ff(self, ctx:ZCodeParser.Vd_type_ffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_sepa.
    def visitFunc_sepa(self, ctx:ZCodeParser.Func_sepaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_body.
    def visitFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#list_stmt.
    def visitList_stmt(self, ctx:ZCodeParser.List_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_vari_decl.
    def visitStmt_vari_decl(self, ctx:ZCodeParser.Stmt_vari_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_assi.
    def visitStmt_assi(self, ctx:ZCodeParser.Stmt_assiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_assi_1.
    def visitStmt_assi_1(self, ctx:ZCodeParser.Stmt_assi_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_assi_2.
    def visitStmt_assi_2(self, ctx:ZCodeParser.Stmt_assi_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_cond.
    def visitStmt_cond(self, ctx:ZCodeParser.Stmt_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_if.
    def visitStmt_if(self, ctx:ZCodeParser.Stmt_ifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_elif.
    def visitStmt_elif(self, ctx:ZCodeParser.Stmt_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_else.
    def visitStmt_else(self, ctx:ZCodeParser.Stmt_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_for.
    def visitStmt_for(self, ctx:ZCodeParser.Stmt_forContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_break.
    def visitStmt_break(self, ctx:ZCodeParser.Stmt_breakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_continue.
    def visitStmt_continue(self, ctx:ZCodeParser.Stmt_continueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_return.
    def visitStmt_return(self, ctx:ZCodeParser.Stmt_returnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_func_call.
    def visitStmt_func_call(self, ctx:ZCodeParser.Stmt_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sfc_param.
    def visitSfc_param(self, ctx:ZCodeParser.Sfc_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sfc_list_args.
    def visitSfc_list_args(self, ctx:ZCodeParser.Sfc_list_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sfc_list_args_tail.
    def visitSfc_list_args_tail(self, ctx:ZCodeParser.Sfc_list_args_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sfc_args.
    def visitSfc_args(self, ctx:ZCodeParser.Sfc_argsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sfc_body.
    def visitSfc_body(self, ctx:ZCodeParser.Sfc_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_block.
    def visitStmt_block(self, ctx:ZCodeParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_sepa_nonnull.
    def visitStmt_sepa_nonnull(self, ctx:ZCodeParser.Stmt_sepa_nonnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_sepa_null.
    def visitStmt_sepa_null(self, ctx:ZCodeParser.Stmt_sepa_nullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_string.
    def visitExpr_string(self, ctx:ZCodeParser.Expr_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_string_concat.
    def visitExpr_string_concat(self, ctx:ZCodeParser.Expr_string_concatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_cond.
    def visitExpr_cond(self, ctx:ZCodeParser.Expr_condContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_compare.
    def visitExpr_compare(self, ctx:ZCodeParser.Expr_compareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_cond_andor.
    def visitExpr_cond_andor(self, ctx:ZCodeParser.Expr_cond_andorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_cond_not.
    def visitExpr_cond_not(self, ctx:ZCodeParser.Expr_cond_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_num.
    def visitExpr_num(self, ctx:ZCodeParser.Expr_numContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#e_n_addsub.
    def visitE_n_addsub(self, ctx:ZCodeParser.E_n_addsubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#e_n_muldivmod.
    def visitE_n_muldivmod(self, ctx:ZCodeParser.E_n_muldivmodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#e_n_nega.
    def visitE_n_nega(self, ctx:ZCodeParser.E_n_negaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_other.
    def visitExpr_other(self, ctx:ZCodeParser.Expr_otherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolval.
    def visitBoolval(self, ctx:ZCodeParser.BoolvalContext):
        return self.visitChildren(ctx)



del ZCodeParser