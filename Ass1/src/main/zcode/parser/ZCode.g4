grammar ZCode;
// Student ID: 2153846

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

// PARSER
program: decls_list EOF;

decls_list: decls NEWLINE decls_list | ;
    decls: vari_decls | func_decls | ;

// Vari
vari_decls: vari_decls_type vari_decls_id | DYNAMIC IDENTIFIER | vari_decls_type vari_decls_id ASSIGN expr | vari_decls_impli IDENTIFIER ASSIGN expr;
    vari_decls_type: KWNUMBER | KWBOOL | KWSTRING;
    vari_decls_impli: DYNAMIC | VAR;
    array: (IDENTIFIER|expr_func_call) OPENSQBRACKET list_expr CLOSESQBRACKET;
    array_tail: OPENSQBRACKET list_expr CLOSESQBRACKET;
    array_decls: IDENTIFIER OPENSQBRACKET list_num CLOSESQBRACKET;
        list_num: NUMBER | NUMBER COMMA list_num;
        list_expr: expr | expr COMMA list_expr;
    vari_decls_id: IDENTIFIER | array_decls;
    vari_id: IDENTIFIER | array;

// Func
func_decls: FUNC IDENTIFIER OPENPAREN list_param CLOSEPAREN func_sepa func_body;
    list_param: params list_param_tail | ;
    list_param_tail: COMMA params list_param_tail | ;
    params: vari_decls_type vari_decls_id;
    func_sepa: NEWLINE func_sepa | ;
    func_body : stmt_return | stmt_block | ;

// stmt
stmt: stmt_vari_decl | stmt_assi | stmt_cond | stmt_for | stmt_break
    | stmt_continue | stmt_return | stmt_func_call | stmt_block; // each stmt
    list_stmt: stmt stmt_sepa_nonnull list_stmt | ; // list of stmts
    stmt_vari_decl: vari_decls;
    stmt_assi: vari_id ASSIGN expr;
    stmt_cond: stmt_if stmt_elif* stmt_else?;
        stmt_if: IF OPENPAREN expr CLOSEPAREN stmt_sepa_null stmt;
        stmt_elif: stmt_sepa_nonnull ELIF OPENPAREN expr CLOSEPAREN stmt_sepa_null stmt;
        stmt_else: stmt_sepa_nonnull ELSE stmt_sepa_null stmt;
    stmt_for: FOR IDENTIFIER UNTIL expr BY expr stmt_sepa_null stmt;
        stmt_break: BREAK;
        stmt_continue: CONTINUE;
    stmt_return: RETURN expr | RETURN;
    stmt_func_call: IDENTIFIER OPENPAREN sfc_list_args CLOSEPAREN;
        sfc_list_args: expr sfc_list_args_tail | ;
        sfc_list_args_tail: COMMA expr sfc_list_args_tail | ;
    stmt_block: BEGIN stmt_sepa_nonnull list_stmt END;
    stmt_sepa_nonnull: NEWLINE | NEWLINE stmt_sepa_nonnull;
    stmt_sepa_null: NEWLINE stmt_sepa_null | ;

// Expr
expr: expr_string_concat;
    // string
    expr_string_concat: expr_compare CONCAT expr_compare | expr_compare;
    // boolean
    expr_compare: expr_cond_andor COMPARENUM expr_cond_andor
                | expr_cond_andor COMPARESTR expr_cond_andor
                | expr_cond_andor;
    expr_cond_andor : expr_cond_andor AND e_n_addsub
                    | expr_cond_andor OR e_n_addsub
                    | e_n_addsub;
    expr_cond_not: NOT expr_cond_not | e_n_nega;
    // number
    e_n_addsub      : e_n_addsub ADD e_n_muldivmod
                    | e_n_addsub SUB e_n_muldivmod
                    | e_n_muldivmod;
    e_n_muldivmod   : e_n_muldivmod MUL expr_cond_not
                    | e_n_muldivmod DIV expr_cond_not
                    | e_n_muldivmod MOD expr_cond_not
                    | expr_cond_not;
    e_n_nega        : SUB e_n_nega | expr_other;
    expr_other  : OPENPAREN expr CLOSEPAREN
                | IDENTIFIER
                | NUMBER
                | STRING
                | boolval | array | array_tail | expr_func_call;
    expr_func_call: IDENTIFIER OPENPAREN sfc_list_args CLOSEPAREN;
    boolval: TRUE | FALSE;



// LEXER

// Key words
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
ELIF		: 'elif';
ELSE		: 'else';
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
NUMBER	: Num+ ('.'Num+)? Expo?;
// ES: escape sequence
fragment ES: ES_BACKSLASH | ES_SINGLEQUOTE ;
fragment ES_BACKSLASH: '\\' [bfrnt'\\] | BACKSPACE | FORMFEED | CR | TAB;
fragment ES_SINGLEQUOTE: SINGLEQUOTE DoubleQuote | SINGLEQUOTE;
fragment POSTFIX_ES_BACKSLASH: [bftnr'\\] ;
fragment POSTFIX_ES_SINGLEQUOTE: ["] ;
fragment NOT_POSTFIX_ES_BACKSLASH: ~[bftnr'\\] ;
fragment NOT_POSTFIX_ES_SINGLEQUOTE: ~["] ;
fragment STRING_CHAR: ~["'\b\f\t\r\n\\] | ES ;
STRING: DoubleQuote STRING_CHAR* DoubleQuote {self.text = self.text[1:-1]};
// Array in Parser

// ID
IDENTIFIER: (Char|'_') (Char|Num|'_')*;

// Fragments
fragment Char: [a-zA-Z];
fragment LowChar: [a-z];
fragment Num: [0-9];
fragment Expo: [eE][-+]?Num+;
fragment DoubleQuote: '"';
// Supported escape sequences
fragment BACKSPACE	:'\b';
fragment FORMFEED	:'\f';
fragment CR			:'\r'; // Carriage return
fragment TAB		:'\t';
fragment SINGLEQUOTE:'\\' ['] | ['];
fragment BACKSLASH	:'\\''\\';

// Comment
CMT: '##' ~[\n\r\f]* -> skip;

WS : [ \t\r]+ -> skip; // skip spaces, tabs

UNCLOSE_STRING: DoubleQuote STRING_CHAR* ('\r\n' | '\n' | EOF) 
{
	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
		raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: DoubleQuote STRING_CHAR* (([\\] NOT_POSTFIX_ES_BACKSLASH?) | (['] NOT_POSTFIX_ES_SINGLEQUOTE?))
{
    raise IllegalEscape(self.text[1:])
} ;
ERROR_CHAR: . {raise ErrorToken(self.text)};