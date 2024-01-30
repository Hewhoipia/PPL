grammar ZCode;

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
array: IDENTIFIER OPENSQBRACKET list_num CLOSESQBRACKET;
list_num: NUMBER list_num_tail;
list_num_tail: COMMA NUMBER list_num_tail | ;

// Func
func_decls: FUNC IDENTIFIER func_param func_sepa func_body;
func_param: OPENPAREN list_param CLOSEPAREN;
list_param: params list_param_tail | ;
list_param_tail: ',' params list_param_tail | ;
params: vari_decls_type1 | vari_decls_type4;
func_sepa: NEWLINE func_sepa | ;
func_body : stmt_return | stmt_block;

// stmt
stmt: ;
stmt_vari_decl: vari_decls;
stmt_assi: assi_type assi_id ASSIGN expr;
assi_type: vari_type | ;
assi_id: IDENTIFIER | array;
stmt_if: IF exp THEN list_stmt
        (ELSEIF exp THEN list_stmt)*
        (ELSE list_stmt)?
        ENDIF DOT ;

stmt_return: ;
stmt_block: BEGIN stmt_block_sepa list_stmt stmt_block_sepa END;
stmt_block_sepa: NEWLINE stmt_block_sepa | NEWLINE;
list_stmt: ;

// Expr
expr: ;



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
ERROR_CHAR: . ;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;