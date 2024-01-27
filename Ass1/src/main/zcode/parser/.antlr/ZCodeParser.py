# Generated from /Users/thong/WorkSpace/PPL/Ass1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,1,49,9,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,0,0,2,0,2,0,0,6,0,4,
        1,0,0,0,2,6,1,0,0,0,4,5,1,0,0,0,5,1,1,0,0,0,6,7,1,0,0,0,7,3,1,0,
        0,0,0
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'##'", "'main'", "'true'", "'false'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'not'", "'and'", "'or'", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "<INVALID>", "'=='", "'<-'", "'...'", 
                     "'('", "')'", "'['", "']'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "CMT", "MAIN", "TRUE", "FALSE", "KWNUMBER", 
                      "KWBOOL", "KWSTRING", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "IDENTIFIER", 
                      "ARRAYDIMEN", "LOGIC", "NOT", "AND", "OR", "ARIOPER", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "COMPARENUM", "COMPARESTR", 
                      "ASSIGN", "CONCAT", "OPENPAREN", "CLOSEPAREN", "OPENSQBRACKET", 
                      "CLOSESQBRACKET", "NUMBER", "BOOLVAL", "STRING", "NEWLINE", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_array = 1

    ruleNames =  [ "program", "array" ]

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
    ARRAYDIMEN=23
    LOGIC=24
    NOT=25
    AND=26
    OR=27
    ARIOPER=28
    ADD=29
    SUB=30
    MUL=31
    DIV=32
    MOD=33
    COMPARENUM=34
    COMPARESTR=35
    ASSIGN=36
    CONCAT=37
    OPENPAREN=38
    CLOSEPAREN=39
    OPENSQBRACKET=40
    CLOSESQBRACKET=41
    NUMBER=42
    BOOLVAL=43
    STRING=44
    NEWLINE=45
    WS=46
    ERROR_CHAR=47
    UNCLOSE_STRING=48
    ILLEGAL_ESCAPE=49

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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_array




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





