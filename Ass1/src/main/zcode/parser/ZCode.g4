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

program: ;

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

// Literals
NUMBER	: Num+ ('.'Num+)? Expo?;
BOOLVAL	: TRUE|FALSE;
STRING	: DoubleQuote ((SINGLEQUOTE DoubleQuote)|BACKSPACE|FORMFEED|CR|NEWLINE|TAB|BACKSLASH|~["])* DoubleQuote {text.self=text.self[1:-1]};
// Array in Parser

// Fragments
fragment Char: [a-zA-Z];
fragment LowChar: [a-z];
fragment Num: [0-9];
fragment Expo: [eE][-+]?Num+;
fragment DoubleQuote: '"';
// Supported escape sequences
fragment BACKSPACE	: '\b';
fragment FORMFEED	: '\f';
fragment CR			: '\r'; // Carriage return
NEWLINE				: '\n';
fragment TAB		: '\t';
fragment SINGLEQUOTE: '\'';
fragment BACKSLASH	: '\\';

// Comment
CMT: '##' (.)*? -> skip;

WS : [ \t\r]+ -> skip; // skip spaces, tabs
ERROR_CHAR: . ;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;