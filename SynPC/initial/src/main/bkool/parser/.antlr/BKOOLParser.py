# Generated from d:/Code/HK232/PPL/SynPC/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
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
        4,1,4,30,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,3,1,20,8,1,1,2,1,2,3,2,24,8,2,1,3,1,3,1,4,1,
        4,1,4,0,0,5,0,2,4,6,8,0,0,26,0,10,1,0,0,0,2,19,1,0,0,0,4,23,1,0,
        0,0,6,25,1,0,0,0,8,27,1,0,0,0,10,11,3,2,1,0,11,12,5,0,0,1,12,1,1,
        0,0,0,13,14,3,6,3,0,14,15,3,4,2,0,15,20,1,0,0,0,16,17,3,8,4,0,17,
        18,3,4,2,0,18,20,1,0,0,0,19,13,1,0,0,0,19,16,1,0,0,0,20,3,1,0,0,
        0,21,24,3,2,1,0,22,24,1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,5,1,
        0,0,0,25,26,5,1,0,0,26,7,1,0,0,0,27,28,5,2,0,0,28,9,1,0,0,0,2,19,
        23
    ]

class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'vardecl'", "'funcdecl'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declare = 1
    RULE_declare_tail = 2
    RULE_vardecl = 3
    RULE_funcdecl = 4

    ruleNames =  [ "program", "declare", "declare_tail", "vardecl", "funcdecl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    ERROR_CHAR=4

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

        def declare(self):
            return self.getTypedRuleContext(BKOOLParser.DeclareContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.declare()
            self.state = 11
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def declare_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Declare_tailContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_declare




    def declare(self):

        localctx = BKOOLParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declare)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.vardecl()
                self.state = 14
                self.declare_tail()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.funcdecl()
                self.state = 17
                self.declare_tail()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(BKOOLParser.DeclareContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_declare_tail




    def declare_tail(self):

        localctx = BKOOLParser.Declare_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare_tail)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.declare()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(BKOOLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





