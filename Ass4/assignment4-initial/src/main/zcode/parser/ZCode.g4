grammar ZCode;

@lexer::header {
# 2153043
from lexererr import *
}

options {
	language=Python3;
}

// 2153043
program: newline_list? declaration_list EOF;
//------------------------------STATEMENTS
statement_list: statement+;
statement: variable_declaration
			| assignment_statement
			| if_statement
			| for_statement
			| break_statement
			| continue_statement
			| return_statement
			| function_call_statement
			| block_statement
			;

assignment_statement: IDENTIFIER (OPEN_SQUARE_BRACKET expression_list CLOSE_SQUARE_BRACKET)? ASSIGN expression newline_list;

if_statement: if_part 
				elif_list//?
				else_part?
				;
if_part: IF OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET newline_list? statement ;
// elif_list: elif_part elif_list | elif_part ;
elif_list: elif_part*;
elif_part: ELIF OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET newline_list? statement;
else_part: ELSE newline_list? statement;

for_statement: FOR IDENTIFIER UNTIL expression BY expression newline_list? statement;

break_statement: BREAK newline_list;

continue_statement: CONTINUE newline_list;

return_statement: RETURN expression? newline_list;

function_call_statement: function_call newline_list;
function_call: IDENTIFIER OPEN_ROUND_BRACKET expression_list? CLOSE_ROUND_BRACKET;

block_statement: BEGIN newline_list statement_list? END newline_list; 
// declaration
declaration_list: declaration+;

declaration: variable_declaration
			| function_declaration
			;
variable_declaration: parameter (ASSIGN expression)? newline_list
					| VAR IDENTIFIER ASSIGN expression newline_list
					| DYNAMIC IDENTIFIER (ASSIGN expression)? newline_list
					;
// type_declaration: type_modifier explicit_variable (ASSIGN expression)? newline_list;
// var_declaration: VAR IDENTIFIER ASSIGN expression newline_list;
// dynamic_declaration: DYNAMIC IDENTIFIER (ASSIGN expression)? newline_list;

function_declaration: FUNC IDENTIFIER OPEN_ROUND_BRACKET parameter_list CLOSE_ROUND_BRACKET ((newline_list? (block_statement | return_statement)) | newline_list) ;
parameter_list: parameter parameter_listtail | ;
parameter_listtail: COMMA parameter parameter_listtail | ;
parameter: (NUMBER | BOOLEAN | STRING) IDENTIFIER (OPEN_SQUARE_BRACKET number_list CLOSE_SQUARE_BRACKET)? ;
// type_modifier: NUMBER | BOOLEAN | STRING;
// explicit_variable: IDENTIFIER OPEN_SQUARE_BRACKET number_list CLOSE_SQUARE_BRACKET
// 					| IDENTIFIER;
// implicit_variable: IDENTIFIER;
number_list: NUMBER_LITERAL number_listtail;
number_listtail: COMMA NUMBER_LITERAL number_listtail | ;

newline_list: NEWLINE+;

//------------------------------EXPRESSSIONS
// written in BNFs as lecturer suggested from old videos (for later assignments)
expression_list: expression expression_listtail;
expression_listtail: COMMA expression expression_listtail | ;

expression: string_operation;

string_operation: relational_operation CONCAT relational_operation
				| relational_operation;

relational_operation: logical_operation (EQUAL_NUMBER | EQUAL_STRING | NOT_EQUAL | LESS_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN | GREATER_THAN_OR_EQUAL) logical_operation
					// | logical_operation EQUAL_STRING logical_operation
					// | logical_operation NOT_EQUAL logical_operation
					// | logical_operation LESS_THAN logical_operation
					// | logical_operation LESS_THAN_OR_EQUAL logical_operation
					// | logical_operation GREATER_THAN logical_operation
					// | logical_operation GREATER_THAN_OR_EQUAL logical_operation
					| logical_operation;

logical_operation: logical_operation (AND | OR) adding_operation
				| adding_operation;

adding_operation: adding_operation (PLUS | MINUS) multiplying_operation
				| multiplying_operation;

multiplying_operation: multiplying_operation (MULTIPLY | DIVIDE | MODULO) not_operation
					| not_operation;

not_operation: NOT not_operation
				| sign_operation;

sign_operation: (MINUS | PLUS) sign_operation
				//| PLUS sign_operation
				| element
				;

// index_operation: //index_operation OPEN_SQUARE_BRACKET expression_list CLOSE_SQUARE_BRACKET
// 				element;

element: IDENTIFIER
		| literal
		| function_call
		| (IDENTIFIER | function_call) OPEN_SQUARE_BRACKET expression_list CLOSE_SQUARE_BRACKET
		| OPEN_ROUND_BRACKET expression CLOSE_ROUND_BRACKET
		;


//------------------------------LITERALS
literal: NUMBER_LITERAL 
		| STRING_LITERAL 
		| BOOLEAN_LITERAL 
		| UNCLOSE_STRING 
		| ILLEGAL_ESCAPE 
		| array_literal;

NUMBER_LITERAL: INTERGER_PART DECIMAL_PART? EXPONENT_PART?;
fragment INTERGER_PART: [0-9]+;
fragment DECIMAL_PART: '.' [0-9]*;
fragment EXPONENT_PART: ('e' | 'E') ('+' | '-')? [0-9]+;

STRING_LITERAL: '"' CHARACTERS_IN_STRING*? '"' {
	self.text = self.text[1:-1];
};

UNCLOSE_STRING: '"' CHARACTERS_IN_STRING*? (NEWLINE | EOF) {
	raise UncloseString(self.text[1:].replace('\r\n', '\n'));
};

ILLEGAL_ESCAPE: '"' CHARACTERS_IN_STRING*? ILLEGAL_ESCAPE_CHARS {
	raise IllegalEscape(self.text[1:]);
};

BOOLEAN_LITERAL: TRUE | FALSE;

array_literal: OPEN_SQUARE_BRACKET expression_list CLOSE_SQUARE_BRACKET;

//ARRAY_LITERAL: OPEN_SQUARE_BRACKET (literal (COMMA literal)*)? CLOSE_SQUARE_BRACKET;

//------------------------------KEYWORDS

TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOLEAN: 'bool';
STRING: 'string';

RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';

FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';

IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';

NOT: 'not';
AND: 'and';
OR: 'or';

//OPERATORS

PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';
MODULO: '%';

EQUAL_NUMBER: '=';
EQUAL_STRING: '==';
NOT_EQUAL: '!=';
ASSIGN: '<-';

LESS_THAN: '<';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN: '>';
GREATER_THAN_OR_EQUAL: '>=';

CONCAT: '...';

// SEPARATORS

OPEN_ROUND_BRACKET: '(';
CLOSE_ROUND_BRACKET: ')';

OPEN_SQUARE_BRACKET: '[';
CLOSE_SQUARE_BRACKET: ']';

COMMA: ',';

//------------------------------IDENTIFIER & COMMENTS AND SPECIAL CHARACTERS

IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;
COMMENT: '##' (~[\n])* -> skip; // single-line comment

//WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
NEWLINE: '\n' ;
CARRIAGE_RETURN: '\r' -> skip;
WHITESPACE: [ \t\b\f]+ -> skip ; // skip spaces, tabs

//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;
fragment CHARACTERS_IN_STRING: (LEGAL_ESCAPE_CHARS | ~('"' | '\\' | '\n'));
fragment LEGAL_ESCAPE_CHARS: '\\' ('b' | 'f' | 'n' | 'r' | 't' | '\'' | '\\' | ' ') | '\'' '"';
fragment ILLEGAL_ESCAPE_CHARS: '\\' ~('b' | 'f' | 'n' | 'r' | 't' | '\'' | '\\' | ' ') | '\'' ~["];
ERROR_CHAR: . {raise ErrorToken(self.text)};