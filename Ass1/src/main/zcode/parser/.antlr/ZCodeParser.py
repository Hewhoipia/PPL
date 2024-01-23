# Generated from d:/Code/HK232/PPL/Ass1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,1,0,0,
        0,3,1,1,0,0,0,0
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'main'", "'true'", "'false'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "<INVALID>", "<INVALID>", "'not'", 
                     "'and'", "'or'", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "CMT", "MAIN", "TRUE", "FALSE", "KWNUMBER", 
                      "KWBOOL", "KWSTRING", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "IDENTIFIER", 
                      "LOGIC", "NOT", "AND", "OR", "ARIOPER", "COMPARE", 
                      "OPENPAREN", "CLOSEPAREN", "OPENSQBRACKET", "CLOSESQBRACKET", 
                      "NUMBER", "BOOLVAL", "STRING", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    CMT=1
    MAIN=2
    TRUE=3
    FALSE=4
    KWNUMBER=5
    KWBOOL=6
    KWSTRING=7
    RETURN=8
    VAR=9
    DYNAMIC=10
    FUNC=11
    FOR=12
    UNTIL=13
    BY=14
    BREAK=15
    CONTINUE=16
    IF=17
    ELSE=18
    ELIF=19
    BEGIN=20
    END=21
    IDENTIFIER=22
    LOGIC=23
    NOT=24
    AND=25
    OR=26
    ARIOPER=27
    COMPARE=28
    OPENPAREN=29
    CLOSEPAREN=30
    OPENSQBRACKET=31
    CLOSESQBRACKET=32
    NUMBER=33
    BOOLVAL=34
    STRING=35
    WS=36
    ERROR_CHAR=37
    UNCLOSE_STRING=38
    ILLEGAL_ESCAPE=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





