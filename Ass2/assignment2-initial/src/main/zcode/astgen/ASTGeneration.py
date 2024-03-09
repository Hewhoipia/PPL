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
        return [self.visit(ctx.decls())] + self.visit(ctx.decls_list()) if ctx.decls() else []
    
    def visitDecls(self, ctx: ZCodeParser.DeclsContext):
#decls: vari_decls | func_decls | ;
        if ctx.vari_decls():
            return self.visit(ctx.vari_decls())
        elif ctx.func_decls():
            return self.visit(ctx.func_decls())
        else:
            return None



#VARI DECLS

    def visitVari_decls(self, ctx: ZCodeParser.Vari_declsContext):
#vari_decls: vari_decls_type vari_decls_id | DYNAMIC IDENTIFIER | vari_decls_type vari_decls_id ASSIGN expr | vari_decls_impli IDENTIFIER ASSIGN expr;
#class VarDecl(Decl, Stmt): def __init__(self, name, varType=None, modifier=None, varInit=None):
# class ArrayType(Type):
#     # size: List[float]
#     # eleType: Type

#     def __init__(self, size, eleType):
        self.name=None
        self.varType=None
        self.modifier=None
        self.varInit=None
        if (ctx.vari_decls_impli()):
            self.name=Id(ctx.IDENTIFIER().getText())
            self.varType=None
            self.modifier=self.visit(ctx.vari_decls_impli())
            self.varInit=self.visit(ctx.expr())
        elif (ctx.DYNAMIC()):
            self.name=Id(ctx.IDENTIFIER().getText())
            self.varType=None
            self.modifier=ctx.DYNAMIC().getText()
            self.varInit=None
        elif(ctx.ASSIGN()):
            vari=self.visit(ctx.vari_decls_id())
            if (isinstance(vari,Id)):
                self.name=vari
                self.varType=self.visit(ctx.vari_decls_type())
            else:
                self.name=vari[0]
                self.varType=ArrayType(vari[1],self.visit(ctx.vari_decls_type()))
            self.modifier=None
            self.varInit=self.visit(ctx.expr())
        else:
            vari=self.visit(ctx.vari_decls_id())
            if (isinstance(vari,Id)):
                self.name=vari
                self.varType=self.visit(ctx.vari_decls_type())
            else:
                self.name=vari[0]
                self.varType=ArrayType(vari[1],self.visit(ctx.vari_decls_type()))
            self.modifier=None
            self.varInit=None
        return VarDecl(self.name, self.varType, self.modifier, self.varInit)
    
    def visitVari_decls_type(self, ctx: ZCodeParser.Vari_decls_typeContext):
#vari_decls_type: KWNUMBER | KWBOOL | KWSTRING;
        if (ctx.KWNUMBER()):
            return NumberType()
        elif (ctx.KWBOOL()):
            return BoolType()
        else:
            return StringType()
    
    def visitVari_decls_impli(self, ctx: ZCodeParser.Vari_decls_impliContext):
#vari_decls_impli: DYNAMIC | VAR;
        return ctx.DYNAMIC().getText() if ctx.DYNAMIC() else ctx.VAR().getText()
    
    def visitArray(self, ctx: ZCodeParser.ArrayContext):
#array: (IDENTIFIER|expr_func_call) OPENSQBRACKET list_expr CLOSESQBRACKET;
        return ArrayCell(Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.expr_func_call()) ,self.visit(ctx.list_expr()))
    
    def visitArray_tail(self, ctx: ZCodeParser.Array_tailContext):
#array_tail: OPENSQBRACKET list_expr CLOSESQBRACKET;
        return ArrayLiteral(self.visit(ctx.list_expr()))
    
    def visitArray_decls(self, ctx: ZCodeParser.Array_declsContext):
#array_decls: IDENTIFIER OPENSQBRACKET list_num CLOSESQBRACKET;
        return (Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_num()))
    
    def visitList_num(self, ctx: ZCodeParser.List_numContext):
#list_num: NUMBER | NUMBER COMMA list_num;
        return [float(ctx.NUMBER().getText())] + self.visit(ctx.list_num()) if ctx.list_num() else [float(ctx.NUMBER().getText())]
    
    def visitList_expr(self, ctx: ZCodeParser.List_exprContext):
#list_expr: expr | expr COMMA list_expr;
        return [self.visit(ctx.expr())] + self.visit(ctx.list_expr()) if ctx.list_expr() else [self.visit(ctx.expr())]
    
    def visitVari_decls_id(self, ctx: ZCodeParser.Vari_decls_idContext):
#vari_decls_id: IDENTIFIER | array_decls;
        return Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.array_decls())
    
    def visitVari_id(self, ctx: ZCodeParser.Vari_idContext):
#vari_id: IDENTIFIER | array;
        return Id(ctx.IDENTIFIER().getText()) if ctx.IDENTIFIER() else self.visit(ctx.array())
    
    
    
#FUNC DECLS
    
    def visitFunc_decls(self, ctx: ZCodeParser.Func_declsContext):
#func_decls: FUNC IDENTIFIER OPENPAREN list_param CLOSEPAREN func_sepa;
#class FuncDecl(Decl):
    # name: Id
    # param: List[VarDecl]  # empty list if there is no parameter
    # body: Stmt = None  # None if this is just a declaration-part
#def __init__(self, name, param, body=None):
        return FuncDecl(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.list_param()), self.visit(ctx.func_body()))
    
    def visitList_param(self, ctx: ZCodeParser.List_paramContext):
#list_param: params list_param_tail | ;
        return [self.visit(ctx.params())] + self.visit(ctx.list_param_tail()) if ctx.params() else []
    
    def visitList_param_tail(self, ctx: ZCodeParser.List_param_tailContext):
#list_param_tail: COMMA params list_param_tail | ;
        return [self.visit(ctx.params())] + self.visit(ctx.list_param_tail()) if ctx.params() else []
    
    def visitParams(self, ctx: ZCodeParser.ParamsContext):
#params: vari_decls_type vari_decls_id;
        self.name=None
        self.varType=None
        self.modifier=None
        self.varInit=None
        vari=self.visit(ctx.vari_decls_id())
        if (isinstance(vari,Id)):
            self.name=vari
            self.varType=self.visit(ctx.vari_decls_type())
        else:
            self.name=vari[0]
            self.varType=ArrayType(vari[1],self.visit(ctx.vari_decls_type()))
        return VarDecl(self.name, self.varType, self.modifier, self.varInit)
    
    def visitFunc_sepaContext(self, ctx: ZCodeParser.Func_sepaContext):
#func_sepa: NEWLINE func_sepa | ;
        return None
    
    def visitFunc_body(self, ctx: ZCodeParser.Func_bodyContext):
#func_body : stmt_return | stmt_block | ;
        if ctx.stmt_return():
            return self.visit(ctx.stmt_return())
        elif ctx.stmt_block():
            return self.visit(ctx.stmt_block())
        else: return None
    
    
#STMT
    
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
#stmt: stmt_vari_decl | stmt_assi | stmt_cond | stmt_for | stmt_break
#    | stmt_continue | stmt_return | stmt_func_call | stmt_block;
        if (ctx.stmt_vari_decl()):
            return self.visit(ctx.stmt_vari_decl())
        if (ctx.stmt_assi()):
            return self.visit(ctx.stmt_assi())
        if (ctx.stmt_cond()):
            return self.visit(ctx.stmt_cond())
        if (ctx.stmt_for()):
            return self.visit(ctx.stmt_for())
        if (ctx.stmt_break()):
            return self.visit(ctx.stmt_break())
        if (ctx.stmt_continue()):
            return self.visit(ctx.stmt_continue())
        if (ctx.stmt_return()):
            return self.visit(ctx.stmt_return())
        if (ctx.stmt_func_call()):
            return self.visit(ctx.stmt_func_call())
        return self.visit(ctx.stmt_block())
    
    def visitList_stmt(self, ctx: ZCodeParser.List_stmtContext):
#list_stmt: stmt stmt_sepa_nonnull list_stmt | ;
        return [self.visit(ctx.stmt())] + self.visit(ctx.list_stmt()) if ctx.stmt() else []
    
    def visitStmt_vari_decl(self, ctx: ZCodeParser.Stmt_vari_declContext):
#stmt_vari_decl: vari_decls;
        return self.visit(ctx.vari_decls())
    
    def visitStmt_assi(self, ctx: ZCodeParser.Stmt_assiContext):
#stmt_assi: vari_id ASSIGN expr;
        return Assign(self.visit(ctx.vari_id()), self.visit(ctx.expr()))
    
    def visitStmt_cond(self, ctx: ZCodeParser.Stmt_condContext):
#stmt_cond: stmt_if stmt_elif* stmt_else?;
        stmtIf=self.visit(ctx.stmt_if())
        self.ifExpr=stmtIf[0]
        self.thenStmt=stmtIf[1]
        self.elifStmt=[self.visit(x) for x in ctx.stmt_elif()]
        self.elseStmt=self.visit(ctx.stmt_else()) if ctx.stmt_else() else None
        return If(self.ifExpr, self.thenStmt, self.elifStmt, self.elseStmt)
    
    def visitStmt_if(self, ctx: ZCodeParser.Stmt_ifContext):
#stmt_if: IF OPENPAREN expr CLOSEPAREN stmt_sepa_null stmt;
        return (self.visit(ctx.expr()), self.visit(ctx.stmt()))
    
    def visitStmt_elif(self, ctx: ZCodeParser.Stmt_elifContext):
#stmt_elif: stmt_sepa_nonnull ELIF OPENPAREN expr CLOSEPAREN stmt_sepa_null stmt;
        return (self.visit(ctx.expr()), self.visit(ctx.stmt()))
    
    def visitStmt_else(self, ctx: ZCodeParser.Stmt_elseContext):
#stmt_else: stmt_sepa_nonnull ELSE stmt_sepa_null stmt;
        return self.visit(ctx.stmt())
    
    def visitStmt_for(self, ctx: ZCodeParser.Stmt_forContext):
#stmt_for: FOR IDENTIFIER UNTIL expr BY expr stmt_sepa_null stmt;
        return For(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.stmt()))
    
    def visitStmt_break(self, ctx: ZCodeParser.Stmt_breakContext):
#stmt_break: BREAK;
        return Break()
    
    def visitStmt_continue(self, ctx: ZCodeParser.Stmt_continueContext):
#stmt_continue: CONTINUE;
        return Continue()
    
    def visitStmt_return(self, ctx: ZCodeParser.Stmt_returnContext):
#stmt_return: RETURN expr | RETURN;
        self.expr=self.visit(ctx.expr()) if ctx.expr() else None
        return Return(self.expr)
    
    def visitStmt_func_call(self, ctx: ZCodeParser.Stmt_func_callContext):
#stmt_func_call: IDENTIFIER OPENPAREN sfc_list_args CLOSEPAREN;
#class CallStmt(Stmt):
#     # name: Id
#     # args: List[Expr]  # empty list if there is no argument
#     def __init__(self, name, args):
        return CallStmt(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.sfc_list_args()))
    
    def visitSfc_list_args(self, ctx: ZCodeParser.Sfc_list_argsContext):
#sfc_list_args: expr sfc_list_args_tail | ;
        return [self.visit(ctx.expr())] + self.visit(ctx.sfc_list_args_tail()) if ctx.expr() else []
    
    def visitSfc_list_args_tail(self, ctx: ZCodeParser.Sfc_list_args_tailContext):
#sfc_list_args_tail: COMMA expr sfc_list_args_tail | ;
        return [self.visit(ctx.expr())] + self.visit(ctx.sfc_list_args_tail()) if ctx.expr() else []
    
    def visitStmt_block(self, ctx: ZCodeParser.Stmt_blockContext):
#stmt_block: BEGIN stmt_sepa_nonnull list_stmt END;
        return Block(self.visit(ctx.list_stmt()))
    
    def visitStmt_sepa_nonnull(self, ctx: ZCodeParser.Stmt_sepa_nonnullContext):
#stmt_sepa_nonnull: NEWLINE | NEWLINE stmt_sepa_nonnull;
        return None
    
    def visitStmt_sepa_null(self, ctx: ZCodeParser.Stmt_sepa_nullContext):
#stmt_sepa_null: NEWLINE stmt_sepa_null | ;
        return None



#EXPR

    def visitExpr(self, ctx: ZCodeParser.ExprContext):
#expr: expr_string_concat;
        return self.visit(ctx.expr_string_concat())
    
    def visitExpr_string_concat(self, ctx: ZCodeParser.Expr_string_concatContext):
#expr_string_concat: expr_compare CONCAT expr_compare | expr_compare;
        return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.expr_compare(0)), self.visit(ctx.expr_compare(1))) if ctx.CONCAT() else self.visit(ctx.expr_compare(0))
    
    def visitExpr_compare(self, ctx: ZCodeParser.Expr_compareContext):
# expr_compare: expr_cond_andor COMPARENUM expr_cond_andor
#                 | expr_cond_andor COMPARESTR expr_cond_andor
#                 | expr_cond_andor;
        if ctx.COMPARENUM():
            return BinaryOp(ctx.COMPARENUM().getText(), self.visit(ctx.expr_cond_andor(0)), self.visit(ctx.expr_cond_andor(1)))
        if ctx.COMPARESTR():
            return BinaryOp(ctx.COMPARESTR().getText(),self.visit(ctx.expr_cond_andor(0)),self.visit(ctx.expr_cond_andor(1)))
        return self.visit(ctx.expr_cond_andor(0))
    
    def visitExpr_cond_andor(self, ctx: ZCodeParser.Expr_cond_andorContext):
# expr_cond_andor : expr_cond_andor AND e_n_addsub
#                 | expr_cond_andor OR e_n_addsub
#                 | e_n_addsub;
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.expr_cond_andor()), self.visit(ctx.e_n_addsub()))
        if ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.expr_cond_andor()), self.visit(ctx.e_n_addsub()))
        return self.visit(ctx.e_n_addsub())
    
    def visitExpr_cond_not(self, ctx: ZCodeParser.Expr_cond_notContext):
#expr_cond_not: NOT expr_cond_not | e_n_nega;
        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr_cond_not())) if ctx.NOT() else self.visit(ctx.e_n_nega())
    
    def visitE_n_addsub(self, ctx: ZCodeParser.E_n_addsubContext):
# e_n_addsub      : e_n_addsub ADD e_n_muldivmod
#                 | e_n_addsub SUB e_n_muldivmod
#                 | e_n_muldivmod;
        if ctx.ADD():
            return BinaryOp(ctx.ADD().getText(), self.visit(ctx.e_n_addsub()), self.visit(ctx.e_n_muldivmod()))
        if ctx.SUB():
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.e_n_addsub()), self.visit(ctx.e_n_muldivmod()))
        return self.visit(ctx.e_n_muldivmod())
    
    def visitE_n_muldivmod(self, ctx: ZCodeParser.E_n_muldivmodContext):
# e_n_muldivmod   : e_n_muldivmod MUL expr_cond_not
#                 | e_n_muldivmod DIV expr_cond_not
#                 | e_n_muldivmod MOD expr_cond_not
#                 | expr_cond_not;
        if ctx.MUL():
            return BinaryOp(ctx.MUL().getText(), self.visit(ctx.e_n_muldivmod()), self.visit(ctx.expr_cond_not()))
        if ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.e_n_muldivmod()), self.visit(ctx.expr_cond_not()))
        if ctx.MOD():
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.e_n_muldivmod()), self.visit(ctx.expr_cond_not()))
        return self.visit(ctx.expr_cond_not())
    
    def visitE_n_nega(self, ctx: ZCodeParser.E_n_negaContext):
#e_n_nega        : SUB e_n_nega | expr_other;
        return UnaryOp(ctx.SUB().getText() ,self.visit(ctx.e_n_nega())) if ctx.SUB() else self.visit(ctx.expr_other())
    
    def visitExpr_other(self, ctx: ZCodeParser.Expr_otherContext):
# expr_other  : OPENPAREN expr CLOSEPAREN
#                 | IDENTIFIER
#                 | NUMBER
#                 | STRING
#                 | boolval | array | array_tail | expr_func_call;
        if ctx.expr():
            return self.visit(ctx.expr())
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.NUMBER():
            return NumberLiteral(float(ctx.NUMBER().getText()))
        if ctx.STRING():
            return StringLiteral(ctx.STRING().getText())
        if ctx.boolval():
            return self.visit(ctx.boolval())
        if ctx.array():
            return self.visit(ctx.array())
        if ctx.array_tail():
            return self.visit(ctx.array_tail())
        return self.visit(ctx.expr_func_call())
    
    def visitExpr_func_call(self, ctx: ZCodeParser.Expr_func_callContext):
# expr_func_call: IDENTIFIER OPENPAREN sfc_list_args CLOSEPAREN sfc_body;
# class CallExpr(Expr):
#     # name: Id
#     # args: List[Expr]

#     def __init__(self, name, args):
        return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.sfc_list_args()))
    
    def visitBoolval(self, ctx: ZCodeParser.BoolvalContext):
#boolval: TRUE | FALSE;
        text_value = ctx.TRUE().getText() if ctx.TRUE() else ctx.FALSE().getText()
        bool_value = text_value.lower() == 'true'
        return BooleanLiteral(bool_value)