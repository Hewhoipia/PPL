grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : declare EOF ;

declare: vardecl declare_tail | funcdecl declare_tail;
declare_tail: declare | ;

vardecl: list_ID ';';
num_type: 'int' | 'float';
list_ID: num_type ID list_ID_tail;
list_ID_tail: ',' ID list_ID_tail | ;

funcdecl: num_type ID param body ;
param: '(' list_param ')';
list_param: each_param list_param_tail | ;
list_param_tail: ';' each_param list_param_tail | ;
each_param: list_ID | list_expr;
list_expr: expr list_expr_tail;
list_expr_tail: ',' expr list_expr_tail | ;

body: '{' list_stmt '}';
list_stmt: stmt list_stmt | ;
stmt: vardecl | stmt_assi | stmt_call | stmt_return;
stmt_assi: ID '=' expr ';';
stmt_call: ID param ';';
stmt_return: 'return' expr ';';

expr: expr_ADD;
expr_ADD: expr_SUB '+' expr_ADD| expr_SUB;
expr_SUB: expr_SUB '-' expr_SUB| expr_MULDIV;
expr_MULDIV: expr_MULDIV '*' expr_other| expr_MULDIV '/' expr_other| expr_other;
expr_other: ID | NUMBER | ID param;

ID: [a-zA-Z][0-9a-zA-Z]*;
NUMBER	: Num+ ('.'Num+)? Expo?;
//STRING	: DoubleQuote ((SINGLEQUOTE DoubleQuote)|BACKSPACE|FORMFEED|CR|NEWLINE|TAB|BACKSLASH|~["])* DoubleQuote {text.self=text.self[1:-1]};
fragment Num: [0-9];
fragment Expo: [eE][-+]?Num+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
