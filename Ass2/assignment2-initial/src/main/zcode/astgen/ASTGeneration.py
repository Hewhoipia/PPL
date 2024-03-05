from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
#program: decls_list EOF;
#def __init__(self, decl)
# decl: List[Decl]  # empty list if there is no statement in block
        return Program(self.visit(ctx.decls_list()))
    
    def visitDecls_list(self, ctx: ZCodeParser.Decls_listContext):
#decls_list: decls NEWLINE decls_list | ;
        return [self.visit(ctx.decls)] + self.visit(ctx.decls_list()) if ctx.decls() else []
    
    def visitDecls(self, ctx: ZCodeParser.DeclsContext):
#decls: vari_decls | func_decls | ;
#class FuncDecl(Decl): def __init__(self, name, param, body=None):
        if ctx.vari_decls():
            return self.visit(ctx.vari_decls())
        elif ctx.func_decls():
            return self.visit(ctx.func_decls())
        else:
            return None
    
    def visitVari_decls(self, ctx: ZCodeParser.Vari_declsContext):
#vari_decls: vari_decls_type vari_decls_id | DYNAMIC IDENTIFIER | vari_decls_type vari_decls_id ASSIGN expr | vari_decls_impli IDENTIFIER ASSIGN expr;
#class VarDecl(Decl, Stmt): def __init__(self, name, varType=None, modifier=None, varInit=None):
        self.name=None
        self.varType=None
        self.modifier=None
        self.varInit=None
        return VarDecl(self.name, self.varType, self.modifier, self.varInit)
    
    def visitVari_decls_type(self, ctx: ZCodeParser.Vari_decls_typeContext):
#vari_decls_type: KWNUMBER | KWBOOL | KWSTRING;
        return
    
    def visitVari_decls_impli(self, ctx: ZCodeParser.Vari_decls_impliContext):
#vari_decls_impli: DYNAMIC | VAR;
        return
    
    def visitArray(self, ctx: ZCodeParser.ArrayContext):
#array: IDENTIFIER OPENSQBRACKET list_expr CLOSESQBRACKET;
        return
    
    def visitArray_tail(self, ctx: ZCodeParser.Array_tailContext):
#array_tail: OPENSQBRACKET list_expr CLOSESQBRACKET;
        return
    
    def visitArray_decls(self, ctx: ZCodeParser.Array_declsContext):
#array_decls: IDENTIFIER OPENSQBRACKET list_num CLOSESQBRACKET;
        return
    
    def visitList_num(self, ctx: ZCodeParser.List_numContext):
#list_num: NUMBER | NUMBER COMMA list_num;
        return
    
    def visitList_expr(self, ctx: ZCodeParser.List_exprContext):
#list_expr: expr | expr COMMA list_expr;
        return
    
    def visitVari_decls_id(self, ctx: ZCodeParser.Vari_decls_idContext):
#vari_decls_id: IDENTIFIER | array_decls;
        return
    
    def visitVari_id(self, ctx: ZCodeParser.Vari_idContext):
#vari_id: IDENTIFIER | array;
        return
    
    def visitFunc_decls(self, ctx: ZCodeParser.Func_declsContext):
#func_decls: FUNC IDENTIFIER OPENPAREN list_param CLOSEPAREN func_sepa func_body;
        return
    
    def visitFunc_param(self, ctx: ZCodeParser.Func_paramContext):
#func_param: OPENPAREN list_param CLOSEPAREN;
        return
    
    def visitList_param(self, ctx: ZCodeParser.List_paramContext):
#list_param: params list_param_tail | ;
        return
    
    def visitList_param_tail(self, ctx: ZCodeParser.List_param_tailContext):
#list_param_tail: COMMA params list_param_tail | ;
        return
    
    def visitParams(self, ctx: ZCodeParser.ParamsContext):
#params: vari_decls_type vari_decls_id;
        return
    
    def visitFunc_sepaContext(self, ctx: ZCodeParser.Func_sepaContext):
#func_sepa: NEWLINE func_sepa | ;
        return
    
    def visitFunc_body(self, ctx: ZCodeParser.Func_bodyContext):
#func_body : stmt_return | stmt_block | ;
        return
    
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
#stmt: stmt_vari_decl | stmt_assi | stmt_cond | stmt_for | stmt_break
#    | stmt_continue | stmt_return | stmt_func_call | stmt_block;
        return
    
    def visitList_stmt(self, ctx: ZCodeParser.List_stmtContext):
#list_stmt: stmt stmt_sepa_nonnull list_stmt | ;
        return
    
    def visitStmt_vari_decl(self, ctx: ZCodeParser.Stmt_vari_declContext):
#stmt_vari_decl: vari_decls;
        return
    
    def visitStmt_assi(self, ctx: ZCodeParser.Stmt_assiContext):
#stmt_assi: vari_id ASSIGN expr;
        return
    
    def visitStmt_cond(self, ctx: ZCodeParser.Stmt_condContext):
#stmt_cond: stmt_if stmt_elif* stmt_else?;
        return
    
    def visitStmt_if(self, ctx: ZCodeParser.Stmt_ifContext):
#stmt_if: IF OPENPAREN expr CLOSEPAREN stmt_sepa_null stmt;
        return
    
    def visitStmt_elif(self, ctx: ZCodeParser.Stmt_elifContext):
#stmt_elif: stmt_sepa_nonnull ELIF OPENPAREN expr CLOSEPAREN stmt_sepa_null stmt;
        return
    
    def visitStmt_else(self, ctx: ZCodeParser.Stmt_elseContext):
#stmt_else: stmt_sepa_nonnull ELSE stmt_sepa_null stmt;
        return
    
    def visitStmt_for(self, ctx: ZCodeParser.Stmt_forContext):
#stmt_for: FOR IDENTIFIER UNTIL expr BY expr stmt_sepa_null stmt;
        return
    
    def visitStmt_break(self, ctx: ZCodeParser.Stmt_breakContext):
#stmt_break: BREAK;
        return
    
    def visitStmt_continue(self, ctx: ZCodeParser.Stmt_continueContext):
#stmt_continue: CONTINUE;
        return
    
    def visitStmt_return(self, ctx: ZCodeParser.Stmt_returnContext):
#stmt_return: RETURN expr | RETURN;
        return
    
    def visitStmt_func_call(self, ctx: ZCodeParser.Stmt_func_callContext):
#stmt_func_call: IDENTIFIER OPENPAREN sfc_list_args CLOSEPAREN sfc_body;
        return
    
    def visitSfc_list_args(self, ctx: ZCodeParser.Sfc_list_argsContext):
#sfc_list_args: expr sfc_list_args_tail | ;
        return
    
    def visitSfc_list_args_tail(self, ctx: ZCodeParser.Sfc_list_args_tailContext):
#sfc_list_args_tail: COMMA expr sfc_list_args_tail | ;
        return
    
    def visitSfc_body(self, ctx: ZCodeParser.Sfc_bodyContext):
#sfc_body: array_tail | ;
        return
    
    def visitStmt_block(self, ctx: ZCodeParser.Stmt_blockContext):
#stmt_block: BEGIN stmt_sepa_nonnull list_stmt END;
        return
    
    def visitStmt_sepa_nonnull(self, ctx: ZCodeParser.Stmt_sepa_nonnullContext):
#stmt_sepa_nonnull: NEWLINE | NEWLINE stmt_sepa_nonnull;
        return
    
    def visitStmt_sepa_null(self, ctx: ZCodeParser.Stmt_sepa_nullContext):
#stmt_sepa_null: NEWLINE stmt_sepa_null | ;
        return
    
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
#expr: expr_string_concat;
        return
    
    def visitExpr_string_concat(self, ctx: ZCodeParser.Expr_string_concatContext):
#expr_string_concat: expr_compare CONCAT expr_compare | expr_compare;
        return
    
    def visitExpr_compare(self, ctx: ZCodeParser.Expr_compareContext):
# expr_compare: expr_cond_andor COMPARENUM expr_cond_andor
#                 | expr_cond_andor COMPARESTR expr_cond_andor
#                 | expr_cond_andor;
        return
    
    def visitExpr_cond_andor(self, ctx: ZCodeParser.Expr_cond_andorContext):
# expr_cond_andor : expr_cond_andor AND e_n_addsub
#                 | expr_cond_andor OR e_n_addsub
#                 | e_n_addsub;
        return
    
    def visitExpr_cond_not(self, ctx: ZCodeParser.Expr_cond_notContext):
#expr_cond_not: NOT expr_cond_not | e_n_nega;
        return
    
    def visitE_n_addsub(self, ctx: ZCodeParser.E_n_addsubContext):
# e_n_addsub      : e_n_addsub ADD e_n_muldivmod
#                 | e_n_addsub SUB e_n_muldivmod
#                 | e_n_muldivmod;
        return
    
    def visitE_n_muldivmod(self, ctx: ZCodeParser.E_n_muldivmodContext):
# e_n_muldivmod   : e_n_muldivmod MUL expr_cond_not
#                 | e_n_muldivmod DIV expr_cond_not
#                 | e_n_muldivmod MOD expr_cond_not
#                 | expr_cond_not;
        return
    
    def visitE_n_nega(self, ctx: ZCodeParser.E_n_negaContext):
#e_n_nega        : SUB e_n_nega | expr_other;
        return
    
    def visitExpr_other(self, ctx: ZCodeParser.Expr_otherContext):
# expr_other  : OPENPAREN expr CLOSEPAREN
#                 | IDENTIFIER
#                 | NUMBER
#                 | STRING
#                 | boolval | array | array_tail | stmt_func_call;
        return
    
    def visitBoolval(self, ctx: ZCodeParser.BoolvalContext):
#boolval: TRUE | FALSE;
        return