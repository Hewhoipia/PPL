from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *


class ASTGeneration(ZCodeVisitor):

    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
#program: decls_list EOF;
#def __init__(self, decl)
# decl: List[Decl]  # empty list if there is no statement in block
        return Program([Decl])
    
    def visitDecls_list(self, ctx: ZCodeParser.Decls_listContext):
#decls_list: decls NEWLINE decls_list | ;
#class VarDecl(Decl, Stmt): def __init__(self, name, varType=None, modifier=None, varInit=None):
#class FuncDecl(Decl): def __init__(self, name, param, body=None):
        return
    
    def visitDecls(self, ctx: ZCodeParser.DeclsContext):
#decls: vari_decls | func_decls | ;
        return
    
    def visitVari_decls(self, ctx: ZCodeParser.Vari_declsContext):
#vari_decls: vari_decls_type vari_decls_id | DYNAMIC IDENTIFIER | vari_decls_type vari_decls_id ASSIGN expr | vari_decls_impli IDENTIFIER ASSIGN expr;
        return
    
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