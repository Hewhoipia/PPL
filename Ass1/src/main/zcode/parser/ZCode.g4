grammar ZCode;
// Student ID: 2153846

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language=Python3;
}

// PARSER
program: decls_stmt EOF;

decls_stmt: stmt decls_stmt_tail | vari_decls decls_stmt_tail | func_decls decls_stmt_tail | NEWLINE | ;
    decls_stmt_tail: NEWLINE decls_stmt | ;

// Vari
vari_decls: vari_decls_type1 | vari_decls_type2 | vari_decls_type3 | vari_decls_type4;
    vari_decls_type1: vari_type IDENTIFIER; // number, bool, string
    vari_decls_type2: VAR IDENTIFIER ASSIGN expr; // var
    vari_decls_type3: DYNAMIC IDENTIFIER; // dynamic
    vari_decls_type4: vari_type array; // array
    vari_type: KWNUMBER | KWBOOL | KWSTRING;
    array: IDENTIFIER array_tail;
        array_tail: OPENSQBRACKET list_expr_num CLOSESQBRACKET;
        list_expr_num: ;
    array_val: OPENSQBRACKET list_expr CLOSESQBRACKET;
        list_expr: ;

// Func
func_decls: FUNC IDENTIFIER func_param func_sepa func_body;
    func_param: OPENPAREN list_param CLOSEPAREN;
    list_param: params list_param_tail | ;
    list_param_tail: COMMA params list_param_tail | ;
    params: vari_decls_type1 | vari_decls_type4;
    func_sepa: NEWLINE func_sepa | ;
    func_body : stmt_return | stmt_block;

// stmt
stmt: stmt_vari_decl | stmt_assi | stmt_cond | stmt_for | stmt_break
    | stmt_continue | stmt_return | stmt_func_call | stmt_block; // each stmt
    list_stmt: stmt list_stmt_tail | ; // list of stmts
        list_stmt_tail: stmt_sepa_nonnull stmt list_stmt_tail | ;
    stmt_vari_decl: vari_decls;
    stmt_assi: assi_type assi_id ASSIGN expr;
        assi_type: vari_type | ;
        assi_id: IDENTIFIER | array;
    stmt_cond: stmt_if stmt_sepa_nonnull stmt_elif stmt_sepa_nonnull stmt_else;
        stmt_if: IF OPENPAREN expr_cond CLOSEPAREN stmt_sepa_null stmt;
        stmt_elif: ELIF OPENPAREN expr_cond CLOSEPAREN stmt_sepa_null stmt stmt_sepa_nonnull stmt_elif | ;
        stmt_else: ELSE stmt_sepa_null stmt | ;
    stmt_for: FOR IDENTIFIER UNTIL expr_cond BY expr stmt_sepa_null stmt;
        stmt_break: BREAK;
        stmt_continue: CONTINUE;
    stmt_return: RETURN expr;
    stmt_func_call: IDENTIFIER sfc_param;
        sfc_param: OPENPAREN sfc_list_args CLOSEPAREN;
        sfc_list_args: sfc_args sfc_list_args_tail | ;
        sfc_list_args_tail: COMMA sfc_args sfc_list_args_tail | ;
        sfc_args: expr;
    stmt_block: BEGIN stmt_sepa_nonnull list_stmt stmt_sepa_nonnull END;

        stmt_sepa_nonnull: NEWLINE stmt_sepa_nonnull | NEWLINE;
        stmt_sepa_null: NEWLINE stmt_sepa_null | ;

// Expr
expr: ;
expr_cond: ; // boolean
    expr_cond_andor : expr_cond_andor AND expr_cond_andor
                    | expr_cond_andor OR expr_cond_andor
                    | expr_cond_not;
    expr_cond_not: NOT expr_cond_not | expr_cond_other;
    expr_cond_other: IDENTIFIER | boolval;
    boolval: TRUE | FALSE ;
expr_string: ; // string
expr_num: ; // number



// LEXER
// ID
IDENTIFIER: (Char|'_') (Char|Num|'_')*;

// Key words
MAIN		: 'main';
TRUE		: 'true';
FALSE		: 'false';
KWNUMBER	: 'number';
KWBOOL		: 'bool';
KWSTRING	: 'string';
RETURN		: 'return';
VAR			: 'var';
DYNAMIC		: 'dynamic';
FUNC		: 'func';
FOR			: 'for';
UNTIL		: 'until';
BY			: 'by';
BREAK		: 'break';
CONTINUE	: 'continue';
IF			: 'if';
ELSE		: 'else';
ELIF		: 'elif';
BEGIN		: 'begin';
END			: 'end';

// Operators
NOT		: 'not';
AND		: 'and';
OR		: 'or';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
COMPARENUM	: ('!'?'=')|([<>]'='?);
COMPARESTR	: '==';
ASSIGN	: '<-';
CONCAT	: '...';

// Separators
OPENPAREN	: '(';
CLOSEPAREN	: ')';
OPENSQBRACKET	: '[';
CLOSESQBRACKET	: ']';
COMMA       : ',';
NEWLINE		: '\n';

// Literals
NUMBER	: Num ('.'Num)? Expo?;
STRING	: DoubleQuote ((SINGLEQUOTE DoubleQuote)|BACKSPACE|FORMFEED|CR|NEWLINE|TAB|BACKSLASH|~["])* DoubleQuote {text.self=text.self[1:-1]};
// Array in Parser

// Fragments
fragment Char: [a-zA-Z];
fragment LowChar: [a-z];
fragment Num: [0-9]+;
fragment Expo: [eE][-+]?Num;
fragment DoubleQuote: '"';
// Supported escape sequences
fragment BACKSPACE	: '\b';
fragment FORMFEED	: '\f';
fragment CR			: '\r'; // Carriage return
fragment TAB		: '\t';
fragment SINGLEQUOTE: '\'';
fragment BACKSLASH	: '\\';

// Comment
CMT: '##' (.)*? -> skip;

WS : [ \t\r]+ -> skip; // skip spaces, tabs

UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
ERROR_CHAR: . ;