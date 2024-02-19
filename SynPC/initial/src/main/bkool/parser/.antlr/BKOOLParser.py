# Generated from /Users/thong/WorkSpace/PPL/SynPC/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
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
        4,1,18,186,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,3,2,64,8,2,1,3,1,3,1,3,1,4,1,
        4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,79,8,6,1,7,1,7,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,94,8,9,1,10,1,10,1,10,1,10,1,
        10,3,10,101,8,10,1,11,1,11,3,11,105,8,11,1,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,13,3,13,115,8,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,
        1,15,3,15,125,8,15,1,16,1,16,1,16,1,16,3,16,131,8,16,1,17,1,17,1,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,
        21,1,21,1,21,1,21,1,21,3,21,153,8,21,1,22,1,22,1,22,1,22,1,22,1,
        22,5,22,161,8,22,10,22,12,22,164,9,22,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,5,23,175,8,23,10,23,12,23,178,9,23,1,24,1,24,1,
        24,1,24,3,24,184,8,24,1,24,0,2,44,46,25,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,0,1,1,0,2,3,177,0,50,
        1,0,0,0,2,59,1,0,0,0,4,63,1,0,0,0,6,65,1,0,0,0,8,68,1,0,0,0,10,70,
        1,0,0,0,12,78,1,0,0,0,14,80,1,0,0,0,16,85,1,0,0,0,18,93,1,0,0,0,
        20,100,1,0,0,0,22,104,1,0,0,0,24,106,1,0,0,0,26,114,1,0,0,0,28,116,
        1,0,0,0,30,124,1,0,0,0,32,130,1,0,0,0,34,132,1,0,0,0,36,137,1,0,
        0,0,38,141,1,0,0,0,40,145,1,0,0,0,42,152,1,0,0,0,44,154,1,0,0,0,
        46,165,1,0,0,0,48,183,1,0,0,0,50,51,3,2,1,0,51,52,5,0,0,1,52,1,1,
        0,0,0,53,54,3,6,3,0,54,55,3,4,2,0,55,60,1,0,0,0,56,57,3,14,7,0,57,
        58,3,4,2,0,58,60,1,0,0,0,59,53,1,0,0,0,59,56,1,0,0,0,60,3,1,0,0,
        0,61,64,3,2,1,0,62,64,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,5,1,
        0,0,0,65,66,3,10,5,0,66,67,5,1,0,0,67,7,1,0,0,0,68,69,7,0,0,0,69,
        9,1,0,0,0,70,71,3,8,4,0,71,72,5,15,0,0,72,73,3,12,6,0,73,11,1,0,
        0,0,74,75,5,4,0,0,75,76,5,15,0,0,76,79,3,12,6,0,77,79,1,0,0,0,78,
        74,1,0,0,0,78,77,1,0,0,0,79,13,1,0,0,0,80,81,3,8,4,0,81,82,5,15,
        0,0,82,83,3,16,8,0,83,84,3,28,14,0,84,15,1,0,0,0,85,86,5,5,0,0,86,
        87,3,18,9,0,87,88,5,6,0,0,88,17,1,0,0,0,89,90,3,22,11,0,90,91,3,
        20,10,0,91,94,1,0,0,0,92,94,1,0,0,0,93,89,1,0,0,0,93,92,1,0,0,0,
        94,19,1,0,0,0,95,96,5,1,0,0,96,97,3,22,11,0,97,98,3,20,10,0,98,101,
        1,0,0,0,99,101,1,0,0,0,100,95,1,0,0,0,100,99,1,0,0,0,101,21,1,0,
        0,0,102,105,3,10,5,0,103,105,3,24,12,0,104,102,1,0,0,0,104,103,1,
        0,0,0,105,23,1,0,0,0,106,107,3,40,20,0,107,108,3,26,13,0,108,25,
        1,0,0,0,109,110,5,4,0,0,110,111,3,40,20,0,111,112,3,26,13,0,112,
        115,1,0,0,0,113,115,1,0,0,0,114,109,1,0,0,0,114,113,1,0,0,0,115,
        27,1,0,0,0,116,117,5,7,0,0,117,118,3,30,15,0,118,119,5,8,0,0,119,
        29,1,0,0,0,120,121,3,32,16,0,121,122,3,30,15,0,122,125,1,0,0,0,123,
        125,1,0,0,0,124,120,1,0,0,0,124,123,1,0,0,0,125,31,1,0,0,0,126,131,
        3,6,3,0,127,131,3,34,17,0,128,131,3,36,18,0,129,131,3,38,19,0,130,
        126,1,0,0,0,130,127,1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,131,
        33,1,0,0,0,132,133,5,15,0,0,133,134,5,9,0,0,134,135,3,40,20,0,135,
        136,5,1,0,0,136,35,1,0,0,0,137,138,5,15,0,0,138,139,3,16,8,0,139,
        140,5,1,0,0,140,37,1,0,0,0,141,142,5,10,0,0,142,143,3,40,20,0,143,
        144,5,1,0,0,144,39,1,0,0,0,145,146,3,42,21,0,146,41,1,0,0,0,147,
        148,3,44,22,0,148,149,5,11,0,0,149,150,3,42,21,0,150,153,1,0,0,0,
        151,153,3,44,22,0,152,147,1,0,0,0,152,151,1,0,0,0,153,43,1,0,0,0,
        154,155,6,22,-1,0,155,156,3,46,23,0,156,162,1,0,0,0,157,158,10,2,
        0,0,158,159,5,12,0,0,159,161,3,44,22,3,160,157,1,0,0,0,161,164,1,
        0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,45,1,0,0,0,164,162,1,0,
        0,0,165,166,6,23,-1,0,166,167,3,48,24,0,167,176,1,0,0,0,168,169,
        10,3,0,0,169,170,5,13,0,0,170,175,3,48,24,0,171,172,10,2,0,0,172,
        173,5,14,0,0,173,175,3,48,24,0,174,168,1,0,0,0,174,171,1,0,0,0,175,
        178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,47,1,0,0,0,178,176,
        1,0,0,0,179,184,5,15,0,0,180,184,5,16,0,0,181,182,5,15,0,0,182,184,
        3,16,8,0,183,179,1,0,0,0,183,180,1,0,0,0,183,181,1,0,0,0,184,49,
        1,0,0,0,14,59,63,78,93,100,104,114,124,130,152,162,174,176,183
    ]

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




    def declare_tail(self):

        localctx = BKOOLParser.Declare_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare_tail)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
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

        def list_ID(self):
            return self.getTypedRuleContext(BKOOLParser.List_IDContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




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




    def num_type(self):

        localctx = BKOOLParser.Num_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_num_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
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




    def list_ID_tail(self):

        localctx = BKOOLParser.List_ID_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_list_ID_tail)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(BKOOLParser.T__3)
                self.state = 75
                self.match(BKOOLParser.ID)
                self.state = 76
                self.list_ID_tail()
                pass
            elif token in [1, 6]:
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




    def list_param(self):

        localctx = BKOOLParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_param)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 15, 16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.each_param()
                self.state = 90
                self.list_param_tail()
                pass
            elif token in [6]:
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




    def list_param_tail(self):

        localctx = BKOOLParser.List_param_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_param_tail)
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(BKOOLParser.T__0)
                self.state = 96
                self.each_param()
                self.state = 97
                self.list_param_tail()
                pass
            elif token in [6]:
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




    def each_param(self):

        localctx = BKOOLParser.Each_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_each_param)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.list_ID()
                pass
            elif token in [15, 16]:
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




    def list_expr_tail(self):

        localctx = BKOOLParser.List_expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_expr_tail)
        try:
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(BKOOLParser.T__3)
                self.state = 110
                self.expr()
                self.state = 111
                self.list_expr_tail()
                pass
            elif token in [1, 6]:
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




    def list_stmt(self):

        localctx = BKOOLParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_stmt)
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 10, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.stmt()
                self.state = 121
                self.list_stmt()
                pass
            elif token in [8]:
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
         




