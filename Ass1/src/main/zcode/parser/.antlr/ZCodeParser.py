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
        4,1,46,190,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,75,8,1,1,2,1,2,1,2,3,2,80,8,2,1,3,1,3,
        1,3,1,3,3,3,86,8,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,
        11,1,11,3,11,116,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,
        13,1,13,1,14,1,14,1,14,1,14,3,14,132,8,14,1,15,1,15,1,15,1,15,1,
        15,3,15,139,8,15,1,16,1,16,3,16,143,8,16,1,17,1,17,1,17,3,17,148,
        8,17,1,18,1,18,3,18,152,8,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,
        1,21,1,21,1,22,1,22,3,22,165,8,22,1,23,1,23,3,23,169,8,23,1,24,1,
        24,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,3,27,184,
        8,27,1,28,1,28,1,29,1,29,1,29,0,0,30,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,1,1,0,
        5,7,176,0,60,1,0,0,0,2,74,1,0,0,0,4,79,1,0,0,0,6,85,1,0,0,0,8,87,
        1,0,0,0,10,90,1,0,0,0,12,95,1,0,0,0,14,98,1,0,0,0,16,101,1,0,0,0,
        18,103,1,0,0,0,20,108,1,0,0,0,22,115,1,0,0,0,24,117,1,0,0,0,26,123,
        1,0,0,0,28,131,1,0,0,0,30,138,1,0,0,0,32,142,1,0,0,0,34,147,1,0,
        0,0,36,151,1,0,0,0,38,153,1,0,0,0,40,155,1,0,0,0,42,157,1,0,0,0,
        44,164,1,0,0,0,46,168,1,0,0,0,48,170,1,0,0,0,50,172,1,0,0,0,52,174,
        1,0,0,0,54,183,1,0,0,0,56,185,1,0,0,0,58,187,1,0,0,0,60,61,3,2,1,
        0,61,62,5,0,0,1,62,1,1,0,0,0,63,64,3,38,19,0,64,65,3,4,2,0,65,75,
        1,0,0,0,66,67,3,6,3,0,67,68,3,4,2,0,68,75,1,0,0,0,69,70,3,24,12,
        0,70,71,3,4,2,0,71,75,1,0,0,0,72,75,5,39,0,0,73,75,1,0,0,0,74,63,
        1,0,0,0,74,66,1,0,0,0,74,69,1,0,0,0,74,72,1,0,0,0,74,73,1,0,0,0,
        75,3,1,0,0,0,76,77,5,39,0,0,77,80,3,2,1,0,78,80,1,0,0,0,79,76,1,
        0,0,0,79,78,1,0,0,0,80,5,1,0,0,0,81,86,3,8,4,0,82,86,3,10,5,0,83,
        86,3,12,6,0,84,86,3,14,7,0,85,81,1,0,0,0,85,82,1,0,0,0,85,83,1,0,
        0,0,85,84,1,0,0,0,86,7,1,0,0,0,87,88,3,16,8,0,88,89,5,1,0,0,89,9,
        1,0,0,0,90,91,5,9,0,0,91,92,5,1,0,0,92,93,5,32,0,0,93,94,3,58,29,
        0,94,11,1,0,0,0,95,96,5,10,0,0,96,97,5,1,0,0,97,13,1,0,0,0,98,99,
        3,16,8,0,99,100,3,18,9,0,100,15,1,0,0,0,101,102,7,0,0,0,102,17,1,
        0,0,0,103,104,5,1,0,0,104,105,5,36,0,0,105,106,3,20,10,0,106,107,
        5,37,0,0,107,19,1,0,0,0,108,109,5,40,0,0,109,110,3,22,11,0,110,21,
        1,0,0,0,111,112,5,38,0,0,112,113,5,40,0,0,113,116,3,22,11,0,114,
        116,1,0,0,0,115,111,1,0,0,0,115,114,1,0,0,0,116,23,1,0,0,0,117,118,
        5,11,0,0,118,119,5,1,0,0,119,120,3,26,13,0,120,121,3,34,17,0,121,
        122,3,36,18,0,122,25,1,0,0,0,123,124,5,34,0,0,124,125,3,28,14,0,
        125,126,5,35,0,0,126,27,1,0,0,0,127,128,3,32,16,0,128,129,3,30,15,
        0,129,132,1,0,0,0,130,132,1,0,0,0,131,127,1,0,0,0,131,130,1,0,0,
        0,132,29,1,0,0,0,133,134,5,38,0,0,134,135,3,32,16,0,135,136,3,30,
        15,0,136,139,1,0,0,0,137,139,1,0,0,0,138,133,1,0,0,0,138,137,1,0,
        0,0,139,31,1,0,0,0,140,143,3,8,4,0,141,143,3,14,7,0,142,140,1,0,
        0,0,142,141,1,0,0,0,143,33,1,0,0,0,144,145,5,39,0,0,145,148,3,34,
        17,0,146,148,1,0,0,0,147,144,1,0,0,0,147,146,1,0,0,0,148,35,1,0,
        0,0,149,152,3,50,25,0,150,152,3,52,26,0,151,149,1,0,0,0,151,150,
        1,0,0,0,152,37,1,0,0,0,153,154,1,0,0,0,154,39,1,0,0,0,155,156,3,
        6,3,0,156,41,1,0,0,0,157,158,3,44,22,0,158,159,3,46,23,0,159,160,
        5,32,0,0,160,161,3,58,29,0,161,43,1,0,0,0,162,165,3,16,8,0,163,165,
        1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,45,1,0,0,0,166,169,5,
        1,0,0,167,169,3,18,9,0,168,166,1,0,0,0,168,167,1,0,0,0,169,47,1,
        0,0,0,170,171,1,0,0,0,171,49,1,0,0,0,172,173,1,0,0,0,173,51,1,0,
        0,0,174,175,5,20,0,0,175,176,3,54,27,0,176,177,3,56,28,0,177,178,
        3,54,27,0,178,179,5,21,0,0,179,53,1,0,0,0,180,181,5,39,0,0,181,184,
        3,54,27,0,182,184,5,39,0,0,183,180,1,0,0,0,183,182,1,0,0,0,184,55,
        1,0,0,0,185,186,1,0,0,0,186,57,1,0,0,0,187,188,1,0,0,0,188,59,1,
        0,0,0,12,74,79,85,115,131,138,142,147,151,164,168,183
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
                     "'begin'", "'end'", "'not'", "'and'", "'or'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "<INVALID>", "'=='", "'<-'", 
                     "'...'", "'('", "')'", "'['", "']'", "','", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "MAIN", "TRUE", "FALSE", 
                      "KWNUMBER", "KWBOOL", "KWSTRING", "RETURN", "VAR", 
                      "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "COMPARENUM", "COMPARESTR", "ASSIGN", "CONCAT", "OPENPAREN", 
                      "CLOSEPAREN", "OPENSQBRACKET", "CLOSESQBRACKET", "COMMA", 
                      "NEWLINE", "NUMBER", "STRING", "CMT", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decls_stmt = 1
    RULE_decls_stmt_tail = 2
    RULE_vari_decls = 3
    RULE_vari_decls_type1 = 4
    RULE_vari_decls_type2 = 5
    RULE_vari_decls_type3 = 6
    RULE_vari_decls_type4 = 7
    RULE_vari_type = 8
    RULE_array = 9
    RULE_list_num = 10
    RULE_list_num_tail = 11
    RULE_func_decls = 12
    RULE_func_param = 13
    RULE_list_param = 14
    RULE_list_param_tail = 15
    RULE_params = 16
    RULE_func_sepa = 17
    RULE_func_body = 18
    RULE_stmt = 19
    RULE_stmt_vari_decl = 20
    RULE_stmt_assi = 21
    RULE_assi_type = 22
    RULE_assi_id = 23
    RULE_stmt_if = 24
    RULE_stmt_return = 25
    RULE_stmt_block = 26
    RULE_stmt_block_sepa = 27
    RULE_list_stmt = 28
    RULE_expr = 29

    ruleNames =  [ "program", "decls_stmt", "decls_stmt_tail", "vari_decls", 
                   "vari_decls_type1", "vari_decls_type2", "vari_decls_type3", 
                   "vari_decls_type4", "vari_type", "array", "list_num", 
                   "list_num_tail", "func_decls", "func_param", "list_param", 
                   "list_param_tail", "params", "func_sepa", "func_body", 
                   "stmt", "stmt_vari_decl", "stmt_assi", "assi_type", "assi_id", 
                   "stmt_if", "stmt_return", "stmt_block", "stmt_block_sepa", 
                   "list_stmt", "expr" ]

    EOF = Token.EOF
    IDENTIFIER=1
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
    NOT=22
    AND=23
    OR=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    COMPARENUM=30
    COMPARESTR=31
    ASSIGN=32
    CONCAT=33
    OPENPAREN=34
    CLOSEPAREN=35
    OPENSQBRACKET=36
    CLOSESQBRACKET=37
    COMMA=38
    NEWLINE=39
    NUMBER=40
    STRING=41
    CMT=42
    WS=43
    ERROR_CHAR=44
    UNCLOSE_STRING=45
    ILLEGAL_ESCAPE=46

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

        def decls_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_stmtContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.decls_stmt()
            self.state = 61
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decls_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def decls_stmt_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_stmt_tailContext,0)


        def vari_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_declsContext,0)


        def func_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declsContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_decls_stmt




    def decls_stmt(self):

        localctx = ZCodeParser.Decls_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls_stmt)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.stmt()
                self.state = 64
                self.decls_stmt_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.vari_decls()
                self.state = 67
                self.decls_stmt_tail()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.func_decls()
                self.state = 70
                self.decls_stmt_tail()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decls_stmt_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def decls_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decls_stmt_tail




    def decls_stmt_tail(self):

        localctx = ZCodeParser.Decls_stmt_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decls_stmt_tail)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(ZCodeParser.NEWLINE)
                self.state = 77
                self.decls_stmt()
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


    class Vari_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_decls_type1(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type1Context,0)


        def vari_decls_type2(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type2Context,0)


        def vari_decls_type3(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type3Context,0)


        def vari_decls_type4(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type4Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls




    def vari_decls(self):

        localctx = ZCodeParser.Vari_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vari_decls)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.vari_decls_type1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.vari_decls_type2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 83
                self.vari_decls_type3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.vari_decls_type4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_type1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type1




    def vari_decls_type1(self):

        localctx = ZCodeParser.Vari_decls_type1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vari_decls_type1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.vari_type()
            self.state = 88
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_type2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type2




    def vari_decls_type2(self):

        localctx = ZCodeParser.Vari_decls_type2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vari_decls_type2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(ZCodeParser.VAR)
            self.state = 91
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 92
            self.match(ZCodeParser.ASSIGN)
            self.state = 93
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_type3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type3




    def vari_decls_type3(self):

        localctx = ZCodeParser.Vari_decls_type3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vari_decls_type3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(ZCodeParser.DYNAMIC)
            self.state = 96
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_type4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_typeContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type4




    def vari_decls_type4(self):

        localctx = ZCodeParser.Vari_decls_type4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vari_decls_type4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.vari_type()
            self.state = 99
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KWNUMBER(self):
            return self.getToken(ZCodeParser.KWNUMBER, 0)

        def KWBOOL(self):
            return self.getToken(ZCodeParser.KWBOOL, 0)

        def KWSTRING(self):
            return self.getToken(ZCodeParser.KWSTRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_type




    def vari_type(self):

        localctx = ZCodeParser.Vari_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vari_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPENSQBRACKET(self):
            return self.getToken(ZCodeParser.OPENSQBRACKET, 0)

        def list_num(self):
            return self.getTypedRuleContext(ZCodeParser.List_numContext,0)


        def CLOSESQBRACKET(self):
            return self.getToken(ZCodeParser.CLOSESQBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 104
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 105
            self.list_num()
            self.state = 106
            self.match(ZCodeParser.CLOSESQBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def list_num_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_num_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_num




    def list_num(self):

        localctx = ZCodeParser.List_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(ZCodeParser.NUMBER)
            self.state = 109
            self.list_num_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_num_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def list_num_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_num_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_num_tail




    def list_num_tail(self):

        localctx = ZCodeParser.List_num_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_num_tail)
        try:
            self.state = 115
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(ZCodeParser.COMMA)
                self.state = 112
                self.match(ZCodeParser.NUMBER)
                self.state = 113
                self.list_num_tail()
                pass
            elif token in [37]:
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


    class Func_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def func_param(self):
            return self.getTypedRuleContext(ZCodeParser.Func_paramContext,0)


        def func_sepa(self):
            return self.getTypedRuleContext(ZCodeParser.Func_sepaContext,0)


        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decls




    def func_decls(self):

        localctx = ZCodeParser.Func_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(ZCodeParser.FUNC)
            self.state = 118
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 119
            self.func_param()
            self.state = 120
            self.func_sepa()
            self.state = 121
            self.func_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def list_param(self):
            return self.getTypedRuleContext(ZCodeParser.List_paramContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_func_param




    def func_param(self):

        localctx = ZCodeParser.Func_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ZCodeParser.OPENPAREN)
            self.state = 124
            self.list_param()
            self.state = 125
            self.match(ZCodeParser.CLOSEPAREN)
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

        def params(self):
            return self.getTypedRuleContext(ZCodeParser.ParamsContext,0)


        def list_param_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_param_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_param




    def list_param(self):

        localctx = ZCodeParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_param)
        try:
            self.state = 131
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.params()
                self.state = 128
                self.list_param_tail()
                pass
            elif token in [35]:
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

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def params(self):
            return self.getTypedRuleContext(ZCodeParser.ParamsContext,0)


        def list_param_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_param_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_param_tail




    def list_param_tail(self):

        localctx = ZCodeParser.List_param_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_param_tail)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(ZCodeParser.COMMA)
                self.state = 134
                self.params()
                self.state = 135
                self.list_param_tail()
                pass
            elif token in [35]:
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


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_decls_type1(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type1Context,0)


        def vari_decls_type4(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type4Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_params




    def params(self):

        localctx = ZCodeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_params)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.vari_decls_type1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.vari_decls_type4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_sepaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def func_sepa(self):
            return self.getTypedRuleContext(ZCodeParser.Func_sepaContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_sepa




    def func_sepa(self):

        localctx = ZCodeParser.Func_sepaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_sepa)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 144
                self.match(ZCodeParser.NEWLINE)
                self.state = 145
                self.func_sepa()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_return(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_returnContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_body




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_func_body)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.stmt_return()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.stmt_block()
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


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_vari_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_declsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_vari_decl




    def stmt_vari_decl(self):

        localctx = ZCodeParser.Stmt_vari_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt_vari_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.vari_decls()
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

        def assi_type(self):
            return self.getTypedRuleContext(ZCodeParser.Assi_typeContext,0)


        def assi_id(self):
            return self.getTypedRuleContext(ZCodeParser.Assi_idContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_assi




    def stmt_assi(self):

        localctx = ZCodeParser.Stmt_assiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt_assi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.assi_type()
            self.state = 158
            self.assi_id()
            self.state = 159
            self.match(ZCodeParser.ASSIGN)
            self.state = 160
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assi_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assi_type




    def assi_type(self):

        localctx = ZCodeParser.Assi_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_assi_type)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.vari_type()
                pass
            elif token in [1]:
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


    class Assi_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assi_id




    def assi_id(self):

        localctx = ZCodeParser.Assi_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_assi_id)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_if




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)

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


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_return




    def stmt_return(self):

        localctx = ZCodeParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt_return)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def stmt_block_sepa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Stmt_block_sepaContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Stmt_block_sepaContext,i)


        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(ZCodeParser.BEGIN)
            self.state = 175
            self.stmt_block_sepa()
            self.state = 176
            self.list_stmt()
            self.state = 177
            self.stmt_block_sepa()
            self.state = 178
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_block_sepaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def stmt_block_sepa(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_block_sepaContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block_sepa




    def stmt_block_sepa(self):

        localctx = ZCodeParser.Stmt_block_sepaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_block_sepa)
        try:
            self.state = 183
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(ZCodeParser.NEWLINE)
                self.state = 181
                self.stmt_block_sepa()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(ZCodeParser.NEWLINE)
                pass


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


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_stmt




    def list_stmt(self):

        localctx = ZCodeParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_list_stmt)
        try:
            self.enterOuterAlt(localctx, 1)

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


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





