grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : INT+ EOF;

INT: '0' | [1-9][0-9_]*{self.text=self.text.replace('_','')};

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: .  {raise ErrorToken(self.text)};
