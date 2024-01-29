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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("\u00bc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3>\n\3\3\4\3\4\5\4B\n\4\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\5\bQ\n\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13`\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\5\fg\n\f\3\r\3\r\5\rk\n\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17u\n\17\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\5\21\177\n\21\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u0085\n\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u009b\n\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\7\30\u00a3\n\30\f\30\16\30\u00a6\13\30\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u00b1\n\31\f\31")
        buf.write("\16\31\u00b4\13\31\3\32\3\32\3\32\3\32\5\32\u00ba\n\32")
        buf.write("\3\32\2\4.\60\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\2\3\3\2\4\5\2\u00b3\2\64\3\2\2\2\4=\3")
        buf.write("\2\2\2\6A\3\2\2\2\bC\3\2\2\2\nF\3\2\2\2\fH\3\2\2\2\16")
        buf.write("P\3\2\2\2\20R\3\2\2\2\22W\3\2\2\2\24_\3\2\2\2\26f\3\2")
        buf.write("\2\2\30j\3\2\2\2\32l\3\2\2\2\34t\3\2\2\2\36v\3\2\2\2 ")
        buf.write("~\3\2\2\2\"\u0084\3\2\2\2$\u0086\3\2\2\2&\u008b\3\2\2")
        buf.write("\2(\u008f\3\2\2\2*\u0093\3\2\2\2,\u009a\3\2\2\2.\u009c")
        buf.write("\3\2\2\2\60\u00a7\3\2\2\2\62\u00b9\3\2\2\2\64\65\5\4\3")
        buf.write("\2\65\66\7\2\2\3\66\3\3\2\2\2\678\5\b\5\289\5\6\4\29>")
        buf.write("\3\2\2\2:;\5\20\t\2;<\5\6\4\2<>\3\2\2\2=\67\3\2\2\2=:")
        buf.write("\3\2\2\2>\5\3\2\2\2?B\5\4\3\2@B\3\2\2\2A?\3\2\2\2A@\3")
        buf.write("\2\2\2B\7\3\2\2\2CD\5\f\7\2DE\7\3\2\2E\t\3\2\2\2FG\t\2")
        buf.write("\2\2G\13\3\2\2\2HI\5\n\6\2IJ\7\21\2\2JK\5\16\b\2K\r\3")
        buf.write("\2\2\2LM\7\6\2\2MN\7\21\2\2NQ\5\16\b\2OQ\3\2\2\2PL\3\2")
        buf.write("\2\2PO\3\2\2\2Q\17\3\2\2\2RS\5\n\6\2ST\7\21\2\2TU\5\22")
        buf.write("\n\2UV\5\36\20\2V\21\3\2\2\2WX\7\7\2\2XY\5\24\13\2YZ\7")
        buf.write("\b\2\2Z\23\3\2\2\2[\\\5\30\r\2\\]\5\26\f\2]`\3\2\2\2^")
        buf.write("`\3\2\2\2_[\3\2\2\2_^\3\2\2\2`\25\3\2\2\2ab\7\3\2\2bc")
        buf.write("\5\30\r\2cd\5\26\f\2dg\3\2\2\2eg\3\2\2\2fa\3\2\2\2fe\3")
        buf.write("\2\2\2g\27\3\2\2\2hk\5\f\7\2ik\5\32\16\2jh\3\2\2\2ji\3")
        buf.write("\2\2\2k\31\3\2\2\2lm\5*\26\2mn\5\34\17\2n\33\3\2\2\2o")
        buf.write("p\7\6\2\2pq\5*\26\2qr\5\34\17\2ru\3\2\2\2su\3\2\2\2to")
        buf.write("\3\2\2\2ts\3\2\2\2u\35\3\2\2\2vw\7\t\2\2wx\5 \21\2xy\7")
        buf.write("\n\2\2y\37\3\2\2\2z{\5\"\22\2{|\5 \21\2|\177\3\2\2\2}")
        buf.write("\177\3\2\2\2~z\3\2\2\2~}\3\2\2\2\177!\3\2\2\2\u0080\u0085")
        buf.write("\5\b\5\2\u0081\u0085\5$\23\2\u0082\u0085\5&\24\2\u0083")
        buf.write("\u0085\5(\25\2\u0084\u0080\3\2\2\2\u0084\u0081\3\2\2\2")
        buf.write("\u0084\u0082\3\2\2\2\u0084\u0083\3\2\2\2\u0085#\3\2\2")
        buf.write("\2\u0086\u0087\7\21\2\2\u0087\u0088\7\13\2\2\u0088\u0089")
        buf.write("\5*\26\2\u0089\u008a\7\3\2\2\u008a%\3\2\2\2\u008b\u008c")
        buf.write("\7\21\2\2\u008c\u008d\5\22\n\2\u008d\u008e\7\3\2\2\u008e")
        buf.write("\'\3\2\2\2\u008f\u0090\7\f\2\2\u0090\u0091\5*\26\2\u0091")
        buf.write("\u0092\7\3\2\2\u0092)\3\2\2\2\u0093\u0094\5,\27\2\u0094")
        buf.write("+\3\2\2\2\u0095\u0096\5.\30\2\u0096\u0097\7\r\2\2\u0097")
        buf.write("\u0098\5,\27\2\u0098\u009b\3\2\2\2\u0099\u009b\5.\30\2")
        buf.write("\u009a\u0095\3\2\2\2\u009a\u0099\3\2\2\2\u009b-\3\2\2")
        buf.write("\2\u009c\u009d\b\30\1\2\u009d\u009e\5\60\31\2\u009e\u00a4")
        buf.write("\3\2\2\2\u009f\u00a0\f\4\2\2\u00a0\u00a1\7\16\2\2\u00a1")
        buf.write("\u00a3\5.\30\5\u00a2\u009f\3\2\2\2\u00a3\u00a6\3\2\2\2")
        buf.write("\u00a4\u00a2\3\2\2\2\u00a4\u00a5\3\2\2\2\u00a5/\3\2\2")
        buf.write("\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8\b\31\1\2\u00a8\u00a9")
        buf.write("\5\62\32\2\u00a9\u00b2\3\2\2\2\u00aa\u00ab\f\5\2\2\u00ab")
        buf.write("\u00ac\7\17\2\2\u00ac\u00b1\5\62\32\2\u00ad\u00ae\f\4")
        buf.write("\2\2\u00ae\u00af\7\20\2\2\u00af\u00b1\5\62\32\2\u00b0")
        buf.write("\u00aa\3\2\2\2\u00b0\u00ad\3\2\2\2\u00b1\u00b4\3\2\2\2")
        buf.write("\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\61\3\2")
        buf.write("\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00ba\7\21\2\2\u00b6\u00ba")
        buf.write("\7\22\2\2\u00b7\u00b8\7\21\2\2\u00b8\u00ba\5\22\n\2\u00b9")
        buf.write("\u00b5\3\2\2\2\u00b9\u00b6\3\2\2\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00ba\63\3\2\2\2\20=AP_fjt~\u0084\u009a\u00a4\u00b0\u00b2")
        buf.write("\u00b9")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'int'", "'float'", "','", "'('", 
                     "')'", "'{'", "'}'", "'='", "'return'", "'+'", "'-'", 
                     "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUMBER", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declare = 1
    RULE_declare_tail = 2
    RULE_vardecl = 3
    RULE_num_type = 4
    RULE_list_ID = 5
    RULE_list_ID_tail = 6
    RULE_funcdecl = 7
    RULE_param = 8
    RULE_list_param = 9
    RULE_list_param_tail = 10
    RULE_each_param = 11
    RULE_list_expr = 12
    RULE_list_expr_tail = 13
    RULE_body = 14
    RULE_list_stmt = 15
    RULE_stmt = 16
    RULE_stmt_assi = 17
    RULE_stmt_call = 18
    RULE_stmt_return = 19
    RULE_expr = 20
    RULE_expr_ADD = 21
    RULE_expr_SUB = 22
    RULE_expr_MULDIV = 23
    RULE_expr_other = 24

    ruleNames =  [ "program", "declare", "declare_tail", "vardecl", "num_type", 
                   "list_ID", "list_ID_tail", "funcdecl", "param", "list_param", 
                   "list_param_tail", "each_param", "list_expr", "list_expr_tail", 
                   "body", "list_stmt", "stmt", "stmt_assi", "stmt_call", 
                   "stmt_return", "expr", "expr_ADD", "expr_SUB", "expr_MULDIV", 
                   "expr_other" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    ID=15
    NUMBER=16
    WS=17
    ERROR_CHAR=18

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
            self.state = 50
            self.declare()
            self.state = 51
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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.vardecl()
                self.state = 54
                self.declare_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.funcdecl()
                self.state = 57
                self.declare_tail()
                pass


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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__1, BKOOLParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
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

        def list_ID(self):
            return self.getTypedRuleContext(BKOOLParser.List_IDContext,0)


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
            self.state = 65
            self.list_ID()
            self.state = 66
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Num_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_num_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum_type" ):
                return visitor.visitNum_type(self)
            else:
                return visitor.visitChildren(self)




    def num_type(self):

        localctx = BKOOLParser.Num_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_num_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.T__1 or _la==BKOOLParser.T__2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_IDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num_type(self):
            return self.getTypedRuleContext(BKOOLParser.Num_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_ID_tail(self):
            return self.getTypedRuleContext(BKOOLParser.List_ID_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID" ):
                return visitor.visitList_ID(self)
            else:
                return visitor.visitChildren(self)




    def list_ID(self):

        localctx = BKOOLParser.List_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_list_ID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.num_type()
            self.state = 71
            self.match(BKOOLParser.ID)
            self.state = 72
            self.list_ID_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ID_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def list_ID_tail(self):
            return self.getTypedRuleContext(BKOOLParser.List_ID_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_ID_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_ID_tail" ):
                return visitor.visitList_ID_tail(self)
            else:
                return visitor.visitChildren(self)




    def list_ID_tail(self):

        localctx = BKOOLParser.List_ID_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_ID_tail)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(BKOOLParser.T__3)
                self.state = 75
                self.match(BKOOLParser.ID)
                self.state = 76
                self.list_ID_tail()
                pass
            elif token in [BKOOLParser.T__0, BKOOLParser.T__5]:
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


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num_type(self):
            return self.getTypedRuleContext(BKOOLParser.Num_typeContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.num_type()
            self.state = 81
            self.match(BKOOLParser.ID)
            self.state = 82
            self.param()
            self.state = 83
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_param(self):
            return self.getTypedRuleContext(BKOOLParser.List_paramContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(BKOOLParser.T__4)
            self.state = 86
            self.list_param()
            self.state = 87
            self.match(BKOOLParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def each_param(self):
            return self.getTypedRuleContext(BKOOLParser.Each_paramContext,0)


        def list_param_tail(self):
            return self.getTypedRuleContext(BKOOLParser.List_param_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param" ):
                return visitor.visitList_param(self)
            else:
                return visitor.visitChildren(self)




    def list_param(self):

        localctx = BKOOLParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_param)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__1, BKOOLParser.T__2, BKOOLParser.ID, BKOOLParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.each_param()
                self.state = 90
                self.list_param_tail()
                pass
            elif token in [BKOOLParser.T__5]:
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


    class List_param_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def each_param(self):
            return self.getTypedRuleContext(BKOOLParser.Each_paramContext,0)


        def list_param_tail(self):
            return self.getTypedRuleContext(BKOOLParser.List_param_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_param_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param_tail" ):
                return visitor.visitList_param_tail(self)
            else:
                return visitor.visitChildren(self)




    def list_param_tail(self):

        localctx = BKOOLParser.List_param_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_param_tail)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(BKOOLParser.T__0)
                self.state = 96
                self.each_param()
                self.state = 97
                self.list_param_tail()
                pass
            elif token in [BKOOLParser.T__5]:
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


    class Each_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_ID(self):
            return self.getTypedRuleContext(BKOOLParser.List_IDContext,0)


        def list_expr(self):
            return self.getTypedRuleContext(BKOOLParser.List_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_each_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEach_param" ):
                return visitor.visitEach_param(self)
            else:
                return visitor.visitChildren(self)




    def each_param(self):

        localctx = BKOOLParser.Each_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_each_param)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__1, BKOOLParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.list_ID()
                pass
            elif token in [BKOOLParser.ID, BKOOLParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.list_expr()
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


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def list_expr_tail(self):
            return self.getTypedRuleContext(BKOOLParser.List_expr_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = BKOOLParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.expr()
            self.state = 107
            self.list_expr_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expr_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def list_expr_tail(self):
            return self.getTypedRuleContext(BKOOLParser.List_expr_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_expr_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr_tail" ):
                return visitor.visitList_expr_tail(self)
            else:
                return visitor.visitChildren(self)




    def list_expr_tail(self):

        localctx = BKOOLParser.List_expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_expr_tail)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(BKOOLParser.T__3)
                self.state = 110
                self.expr()
                self.state = 111
                self.list_expr_tail()
                pass
            elif token in [BKOOLParser.T__0, BKOOLParser.T__5]:
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.List_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(BKOOLParser.T__6)
            self.state = 117
            self.list_stmt()
            self.state = 118
            self.match(BKOOLParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(BKOOLParser.StmtContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.List_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_list_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmt" ):
                return visitor.visitList_stmt(self)
            else:
                return visitor.visitChildren(self)




    def list_stmt(self):

        localctx = BKOOLParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_stmt)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.T__1, BKOOLParser.T__2, BKOOLParser.T__9, BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.stmt()
                self.state = 121
                self.list_stmt()
                pass
            elif token in [BKOOLParser.T__7]:
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


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def stmt_assi(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_assiContext,0)


        def stmt_call(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_callContext,0)


        def stmt_return(self):
            return self.getTypedRuleContext(BKOOLParser.Stmt_returnContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKOOLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 126
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.stmt_assi()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.stmt_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 129
                self.stmt_return()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_assiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_assi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assi" ):
                return visitor.visitStmt_assi(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assi(self):

        localctx = BKOOLParser.Stmt_assiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmt_assi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BKOOLParser.ID)
            self.state = 133
            self.match(BKOOLParser.T__8)
            self.state = 134
            self.expr()
            self.state = 135
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_call" ):
                return visitor.visitStmt_call(self)
            else:
                return visitor.visitChildren(self)




    def stmt_call(self):

        localctx = BKOOLParser.Stmt_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmt_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(BKOOLParser.ID)
            self.state = 138
            self.param()
            self.state = 139
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stmt_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_return" ):
                return visitor.visitStmt_return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_return(self):

        localctx = BKOOLParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(BKOOLParser.T__9)
            self.state = 142
            self.expr()
            self.state = 143
            self.match(BKOOLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_ADD(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_ADDContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.expr_ADD()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_ADDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_SUB(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_SUBContext,0)


        def expr_ADD(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_ADDContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_ADD

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_ADD" ):
                return visitor.visitExpr_ADD(self)
            else:
                return visitor.visitChildren(self)




    def expr_ADD(self):

        localctx = BKOOLParser.Expr_ADDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr_ADD)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.expr_SUB(0)
                self.state = 148
                self.match(BKOOLParser.T__10)
                self.state = 149
                self.expr_ADD()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.expr_SUB(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_SUBContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_MULDIV(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_MULDIVContext,0)


        def expr_SUB(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Expr_SUBContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Expr_SUBContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_SUB

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_SUB" ):
                return visitor.visitExpr_SUB(self)
            else:
                return visitor.visitChildren(self)



    def expr_SUB(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr_SUBContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr_SUB, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.expr_MULDIV(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKOOLParser.Expr_SUBContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_SUB)
                    self.state = 157
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 158
                    self.match(BKOOLParser.T__11)
                    self.state = 159
                    self.expr_SUB(3) 
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_MULDIVContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_other(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_otherContext,0)


        def expr_MULDIV(self):
            return self.getTypedRuleContext(BKOOLParser.Expr_MULDIVContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_MULDIV

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_MULDIV" ):
                return visitor.visitExpr_MULDIV(self)
            else:
                return visitor.visitChildren(self)



    def expr_MULDIV(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKOOLParser.Expr_MULDIVContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expr_MULDIV, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.expr_other()
            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 174
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = BKOOLParser.Expr_MULDIVContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_MULDIV)
                        self.state = 168
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 169
                        self.match(BKOOLParser.T__12)
                        self.state = 170
                        self.expr_other()
                        pass

                    elif la_ == 2:
                        localctx = BKOOLParser.Expr_MULDIVContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_MULDIV)
                        self.state = 171
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 172
                        self.match(BKOOLParser.T__13)
                        self.state = 173
                        self.expr_other()
                        pass

             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_otherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def NUMBER(self):
            return self.getToken(BKOOLParser.NUMBER, 0)

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr_other

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_other" ):
                return visitor.visitExpr_other(self)
            else:
                return visitor.visitChildren(self)




    def expr_other(self):

        localctx = BKOOLParser.Expr_otherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expr_other)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(BKOOLParser.NUMBER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.match(BKOOLParser.ID)
                self.state = 182
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.expr_SUB_sempred
        self._predicates[23] = self.expr_MULDIV_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_SUB_sempred(self, localctx:Expr_SUBContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_MULDIV_sempred(self, localctx:Expr_MULDIVContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




