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

decls_list: decls decls_list_tail | ;
    decls_list_tail: NEWLINE decls decls_list_tail | ;
    decls: vari_decls | func_decls | ;

// Vari
vari_decls: vari_decls_type1 | vari_decls_type2 | vari_decls_type3 | vari_decls_type4;
    vari_decls_type1: vari_type IDENTIFIER; // number, bool, string
    vari_decls_type2: VAR IDENTIFIER ASSIGN expr; // var
    vari_decls_type3: DYNAMIC IDENTIFIER; // dynamic
    vari_decls_type4: vari_type array; // array
    vari_type: KWNUMBER | KWBOOL | KWSTRING;
    array: IDENTIFIER array_tail;
        array_tail: OPENSQBRACKET list_expr_num CLOSESQBRACKET;
        list_expr_num: expr_num list_expr_num_tail | expr_num;
            list_expr_num_tail: COMMA expr_num list_expr_num_tail | ;
    array_val: OPENSQBRACKET list_expr CLOSESQBRACKET;
        list_expr: expr list_expr_tail | ;
            list_expr_tail: COMMA expr list_expr_tail | ;

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
    list_stmt: stmt_sepa_nonnull stmt list_stmt | ; // list of stmts
    stmt_vari_decl: vari_decls;
    stmt_assi: assi_type assi_id ASSIGN expr;
        assi_type: vari_type | ;
        assi_id: IDENTIFIER | array;
    stmt_cond: stmt_if stmt_elif stmt_sepa_nonnull stmt_else;
        stmt_if: IF OPENPAREN expr_cond CLOSEPAREN stmt_sepa_null stmt;
        stmt_elif: stmt_sepa_nonnull ELIF OPENPAREN expr_cond CLOSEPAREN stmt_sepa_null stmt stmt_elif | ;
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
    stmt_block: BEGIN list_stmt stmt_sepa_nonnull END;

        stmt_sepa_nonnull: NEWLINE stmt_sepa_nonnull | NEWLINE;
        stmt_sepa_null: NEWLINE stmt_sepa_null | ;

// Expr
expr: expr_cond | expr_string | expr_num;
expr_cond: expr_cond_andor; // boolean
    expr_cond_andor : expr_cond_andor AND expr_cond_andor
                    | expr_cond_andor OR expr_cond_andor
                    | expr_cond_not;
    expr_cond_not: NOT expr_cond_not | expr_cond_other;
    expr_cond_other: OPENPAREN expr_cond CLOSEPAREN | IDENTIFIER | boolval | array | array_val | stmt_func_call;
    boolval: TRUE | FALSE;
expr_string: expr_string_compare | expr_string_concat; // string
    expr_string_concat: stringval CONCAT stringval e_s_c_tail;
        e_s_c_tail: CONCAT stringval e_s_c_tail | ;
    expr_string_compare: stringval COMPARESTR stringval;
    stringval: OPENPAREN expr_string CLOSEPAREN | IDENTIFIER | STRING | array | array_val | stmt_func_call;
expr_num: e_n_addsub; // number
    e_n_addsub      : e_n_addsub ADD e_n_addsub
                    | e_n_addsub SUB e_n_addsub
                    | e_n_muldivmod;
    e_n_muldivmod   : e_n_muldivmod MUL e_n_muldivmod
                    | e_n_muldivmod DIV e_n_muldivmod
                    | e_n_muldivmod MOD e_n_muldivmod
                    | e_n_nega;
    e_n_nega        : SUB e_n_nega | e_n_other;
    e_n_other: OPENPAREN expr_num CLOSEPAREN | IDENTIFIER | NUMBER | array | array_val | stmt_func_call;



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