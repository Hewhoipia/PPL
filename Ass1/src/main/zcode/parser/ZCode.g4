grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: ;

// Comment
CMT: '##';

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


IDENTIFIER: (Char|'_') (Char|Num|'_')*;
ARRAYDIMEN: OPENSQBRACKET NUMBER (','NUMBER)* CLOSESQBRACKET;

// Operators
LOGIC	: (NOT|AND|OR);
NOT		: 'not';
AND		: 'and';
OR		: 'or';
ARIOPER	: ADD|SUB|MUL|DIV|MOD;
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
STRING	: DoubleQuote (~["]|(SINGLEQUOTE DoubleQuote)|BACKSPACE|FORMFEED|CR|NEWLINE|TAB|BACKSLASH)* DoubleQuote {text.self=text.self[1:-1]};
array:; // Parser

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


WS : [ \t\r]+ -> skip ; // skip spaces, tabs, newlines
ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;