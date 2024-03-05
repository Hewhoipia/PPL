# Generated from d:/Code/HK232/PPL/Ass2/assignment2-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decls_list.
    def enterDecls_list(self, ctx:ZCodeParser.Decls_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decls_list.
    def exitDecls_list(self, ctx:ZCodeParser.Decls_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decls.
    def enterDecls(self, ctx:ZCodeParser.DeclsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decls.
    def exitDecls(self, ctx:ZCodeParser.DeclsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vari_decls.
    def enterVari_decls(self, ctx:ZCodeParser.Vari_declsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vari_decls.
    def exitVari_decls(self, ctx:ZCodeParser.Vari_declsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vari_decls_type.
    def enterVari_decls_type(self, ctx:ZCodeParser.Vari_decls_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vari_decls_type.
    def exitVari_decls_type(self, ctx:ZCodeParser.Vari_decls_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vari_decls_impli.
    def enterVari_decls_impli(self, ctx:ZCodeParser.Vari_decls_impliContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vari_decls_impli.
    def exitVari_decls_impli(self, ctx:ZCodeParser.Vari_decls_impliContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array.
    def enterArray(self, ctx:ZCodeParser.ArrayContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array.
    def exitArray(self, ctx:ZCodeParser.ArrayContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_tail.
    def enterArray_tail(self, ctx:ZCodeParser.Array_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_tail.
    def exitArray_tail(self, ctx:ZCodeParser.Array_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_decls.
    def enterArray_decls(self, ctx:ZCodeParser.Array_declsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_decls.
    def exitArray_decls(self, ctx:ZCodeParser.Array_declsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#list_num.
    def enterList_num(self, ctx:ZCodeParser.List_numContext):
        pass

    # Exit a parse tree produced by ZCodeParser#list_num.
    def exitList_num(self, ctx:ZCodeParser.List_numContext):
        pass


    # Enter a parse tree produced by ZCodeParser#list_expr.
    def enterList_expr(self, ctx:ZCodeParser.List_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#list_expr.
    def exitList_expr(self, ctx:ZCodeParser.List_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vari_decls_id.
    def enterVari_decls_id(self, ctx:ZCodeParser.Vari_decls_idContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vari_decls_id.
    def exitVari_decls_id(self, ctx:ZCodeParser.Vari_decls_idContext):
        pass


    # Enter a parse tree produced by ZCodeParser#vari_id.
    def enterVari_id(self, ctx:ZCodeParser.Vari_idContext):
        pass

    # Exit a parse tree produced by ZCodeParser#vari_id.
    def exitVari_id(self, ctx:ZCodeParser.Vari_idContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_decls.
    def enterFunc_decls(self, ctx:ZCodeParser.Func_declsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_decls.
    def exitFunc_decls(self, ctx:ZCodeParser.Func_declsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_param.
    def enterFunc_param(self, ctx:ZCodeParser.Func_paramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_param.
    def exitFunc_param(self, ctx:ZCodeParser.Func_paramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#list_param.
    def enterList_param(self, ctx:ZCodeParser.List_paramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#list_param.
    def exitList_param(self, ctx:ZCodeParser.List_paramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#list_param_tail.
    def enterList_param_tail(self, ctx:ZCodeParser.List_param_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#list_param_tail.
    def exitList_param_tail(self, ctx:ZCodeParser.List_param_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#params.
    def enterParams(self, ctx:ZCodeParser.ParamsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#params.
    def exitParams(self, ctx:ZCodeParser.ParamsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_sepa.
    def enterFunc_sepa(self, ctx:ZCodeParser.Func_sepaContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_sepa.
    def exitFunc_sepa(self, ctx:ZCodeParser.Func_sepaContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_body.
    def enterFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_body.
    def exitFunc_body(self, ctx:ZCodeParser.Func_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#list_stmt.
    def enterList_stmt(self, ctx:ZCodeParser.List_stmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#list_stmt.
    def exitList_stmt(self, ctx:ZCodeParser.List_stmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_vari_decl.
    def enterStmt_vari_decl(self, ctx:ZCodeParser.Stmt_vari_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_vari_decl.
    def exitStmt_vari_decl(self, ctx:ZCodeParser.Stmt_vari_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_assi.
    def enterStmt_assi(self, ctx:ZCodeParser.Stmt_assiContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_assi.
    def exitStmt_assi(self, ctx:ZCodeParser.Stmt_assiContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_cond.
    def enterStmt_cond(self, ctx:ZCodeParser.Stmt_condContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_cond.
    def exitStmt_cond(self, ctx:ZCodeParser.Stmt_condContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_if.
    def enterStmt_if(self, ctx:ZCodeParser.Stmt_ifContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_if.
    def exitStmt_if(self, ctx:ZCodeParser.Stmt_ifContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_elif.
    def enterStmt_elif(self, ctx:ZCodeParser.Stmt_elifContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_elif.
    def exitStmt_elif(self, ctx:ZCodeParser.Stmt_elifContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_else.
    def enterStmt_else(self, ctx:ZCodeParser.Stmt_elseContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_else.
    def exitStmt_else(self, ctx:ZCodeParser.Stmt_elseContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_for.
    def enterStmt_for(self, ctx:ZCodeParser.Stmt_forContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_for.
    def exitStmt_for(self, ctx:ZCodeParser.Stmt_forContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_break.
    def enterStmt_break(self, ctx:ZCodeParser.Stmt_breakContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_break.
    def exitStmt_break(self, ctx:ZCodeParser.Stmt_breakContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_continue.
    def enterStmt_continue(self, ctx:ZCodeParser.Stmt_continueContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_continue.
    def exitStmt_continue(self, ctx:ZCodeParser.Stmt_continueContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_return.
    def enterStmt_return(self, ctx:ZCodeParser.Stmt_returnContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_return.
    def exitStmt_return(self, ctx:ZCodeParser.Stmt_returnContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_func_call.
    def enterStmt_func_call(self, ctx:ZCodeParser.Stmt_func_callContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_func_call.
    def exitStmt_func_call(self, ctx:ZCodeParser.Stmt_func_callContext):
        pass


    # Enter a parse tree produced by ZCodeParser#sfc_list_args.
    def enterSfc_list_args(self, ctx:ZCodeParser.Sfc_list_argsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#sfc_list_args.
    def exitSfc_list_args(self, ctx:ZCodeParser.Sfc_list_argsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#sfc_list_args_tail.
    def enterSfc_list_args_tail(self, ctx:ZCodeParser.Sfc_list_args_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#sfc_list_args_tail.
    def exitSfc_list_args_tail(self, ctx:ZCodeParser.Sfc_list_args_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#sfc_body.
    def enterSfc_body(self, ctx:ZCodeParser.Sfc_bodyContext):
        pass

    # Exit a parse tree produced by ZCodeParser#sfc_body.
    def exitSfc_body(self, ctx:ZCodeParser.Sfc_bodyContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_block.
    def enterStmt_block(self, ctx:ZCodeParser.Stmt_blockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_block.
    def exitStmt_block(self, ctx:ZCodeParser.Stmt_blockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_sepa_nonnull.
    def enterStmt_sepa_nonnull(self, ctx:ZCodeParser.Stmt_sepa_nonnullContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_sepa_nonnull.
    def exitStmt_sepa_nonnull(self, ctx:ZCodeParser.Stmt_sepa_nonnullContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_sepa_null.
    def enterStmt_sepa_null(self, ctx:ZCodeParser.Stmt_sepa_nullContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_sepa_null.
    def exitStmt_sepa_null(self, ctx:ZCodeParser.Stmt_sepa_nullContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_string_concat.
    def enterExpr_string_concat(self, ctx:ZCodeParser.Expr_string_concatContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_string_concat.
    def exitExpr_string_concat(self, ctx:ZCodeParser.Expr_string_concatContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_compare.
    def enterExpr_compare(self, ctx:ZCodeParser.Expr_compareContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_compare.
    def exitExpr_compare(self, ctx:ZCodeParser.Expr_compareContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_cond_andor.
    def enterExpr_cond_andor(self, ctx:ZCodeParser.Expr_cond_andorContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_cond_andor.
    def exitExpr_cond_andor(self, ctx:ZCodeParser.Expr_cond_andorContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_cond_not.
    def enterExpr_cond_not(self, ctx:ZCodeParser.Expr_cond_notContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_cond_not.
    def exitExpr_cond_not(self, ctx:ZCodeParser.Expr_cond_notContext):
        pass


    # Enter a parse tree produced by ZCodeParser#e_n_addsub.
    def enterE_n_addsub(self, ctx:ZCodeParser.E_n_addsubContext):
        pass

    # Exit a parse tree produced by ZCodeParser#e_n_addsub.
    def exitE_n_addsub(self, ctx:ZCodeParser.E_n_addsubContext):
        pass


    # Enter a parse tree produced by ZCodeParser#e_n_muldivmod.
    def enterE_n_muldivmod(self, ctx:ZCodeParser.E_n_muldivmodContext):
        pass

    # Exit a parse tree produced by ZCodeParser#e_n_muldivmod.
    def exitE_n_muldivmod(self, ctx:ZCodeParser.E_n_muldivmodContext):
        pass


    # Enter a parse tree produced by ZCodeParser#e_n_nega.
    def enterE_n_nega(self, ctx:ZCodeParser.E_n_negaContext):
        pass

    # Exit a parse tree produced by ZCodeParser#e_n_nega.
    def exitE_n_nega(self, ctx:ZCodeParser.E_n_negaContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr_other.
    def enterExpr_other(self, ctx:ZCodeParser.Expr_otherContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr_other.
    def exitExpr_other(self, ctx:ZCodeParser.Expr_otherContext):
        pass


    # Enter a parse tree produced by ZCodeParser#boolval.
    def enterBoolval(self, ctx:ZCodeParser.BoolvalContext):
        pass

    # Exit a parse tree produced by ZCodeParser#boolval.
    def exitBoolval(self, ctx:ZCodeParser.BoolvalContext):
        pass



del ZCodeParser