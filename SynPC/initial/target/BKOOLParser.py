# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write(" \4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3\26\n\3\3\4\3\4\5\4\32\n\4")
        buf.write("\3\5\3\5\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2\34\2\f\3\2")
        buf.write("\2\2\4\25\3\2\2\2\6\31\3\2\2\2\b\33\3\2\2\2\n\35\3\2\2")
        buf.write("\2\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2\17\20\5\b\5\2")
        buf.write("\20\21\5\6\4\2\21\26\3\2\2\2\22\23\5\n\6\2\23\24\5\6\4")
        buf.write("\2\24\26\3\2\2\2\25\17\3\2\2\2\25\22\3\2\2\2\26\5\3\2")
        buf.write("\2\2\27\32\5\4\3\2\30\32\3\2\2\2\31\27\3\2\2\2\31\30\3")
        buf.write("\2\2\2\32\7\3\2\2\2\33\34\7\3\2\2\34\t\3\2\2\2\35\36\7")
        buf.write("\4\2\2\36\13\3\2\2\2\4\25\31")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = BKOOLParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declare)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.vardecl()
                self.state = 14
                self.declare_tail()
                pass
            elif token in [BKOOLParser.T__1]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_tail" ):
                return visitor.visitDeclare_tail(self)
            else:
                return visitor.visitChildren(self)




    def declare_tail(self):

        localctx = BKOOLParser.Declare_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare_tail)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__0, BKOOLParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.declare()
                pass
            elif token in [BKOOLParser.EOF]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




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





