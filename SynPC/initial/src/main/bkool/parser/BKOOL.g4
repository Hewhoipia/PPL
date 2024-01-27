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
vardecl: 'vardecl' ;
funcdecl: 'funcdecl' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
