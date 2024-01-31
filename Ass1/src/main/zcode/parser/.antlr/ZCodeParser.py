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
        4,1,46,232,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,3,1,85,8,1,1,2,1,2,1,2,3,2,90,8,2,1,3,1,3,1,3,1,3,3,3,96,8,
        3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,
        8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,126,
        8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,
        1,14,1,14,3,14,142,8,14,1,15,1,15,1,15,1,15,1,15,3,15,149,8,15,1,
        16,1,16,3,16,153,8,16,1,17,1,17,1,17,3,17,158,8,17,1,18,1,18,3,18,
        162,8,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,
        1,23,1,23,3,23,177,8,23,1,24,1,24,3,24,181,8,24,1,25,1,25,1,25,1,
        25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,3,27,206,8,27,1,28,1,28,1,29,1,
        29,1,29,3,29,213,8,29,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,
        32,1,32,1,32,3,32,226,8,32,1,33,1,33,1,34,1,34,1,34,0,0,35,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,0,1,1,0,5,7,215,0,70,1,0,0,0,2,84,
        1,0,0,0,4,89,1,0,0,0,6,95,1,0,0,0,8,97,1,0,0,0,10,100,1,0,0,0,12,
        105,1,0,0,0,14,108,1,0,0,0,16,111,1,0,0,0,18,113,1,0,0,0,20,118,
        1,0,0,0,22,125,1,0,0,0,24,127,1,0,0,0,26,133,1,0,0,0,28,141,1,0,
        0,0,30,148,1,0,0,0,32,152,1,0,0,0,34,157,1,0,0,0,36,161,1,0,0,0,
        38,163,1,0,0,0,40,165,1,0,0,0,42,167,1,0,0,0,44,169,1,0,0,0,46,176,
        1,0,0,0,48,180,1,0,0,0,50,182,1,0,0,0,52,188,1,0,0,0,54,205,1,0,
        0,0,56,207,1,0,0,0,58,212,1,0,0,0,60,214,1,0,0,0,62,216,1,0,0,0,
        64,225,1,0,0,0,66,227,1,0,0,0,68,229,1,0,0,0,70,71,3,2,1,0,71,72,
        5,0,0,1,72,1,1,0,0,0,73,74,3,38,19,0,74,75,3,4,2,0,75,85,1,0,0,0,
        76,77,3,6,3,0,77,78,3,4,2,0,78,85,1,0,0,0,79,80,3,24,12,0,80,81,
        3,4,2,0,81,85,1,0,0,0,82,85,5,39,0,0,83,85,1,0,0,0,84,73,1,0,0,0,
        84,76,1,0,0,0,84,79,1,0,0,0,84,82,1,0,0,0,84,83,1,0,0,0,85,3,1,0,
        0,0,86,87,5,39,0,0,87,90,3,2,1,0,88,90,1,0,0,0,89,86,1,0,0,0,89,
        88,1,0,0,0,90,5,1,0,0,0,91,96,3,8,4,0,92,96,3,10,5,0,93,96,3,12,
        6,0,94,96,3,14,7,0,95,91,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,
        94,1,0,0,0,96,7,1,0,0,0,97,98,3,16,8,0,98,99,5,1,0,0,99,9,1,0,0,
        0,100,101,5,9,0,0,101,102,5,1,0,0,102,103,5,32,0,0,103,104,3,66,
        33,0,104,11,1,0,0,0,105,106,5,10,0,0,106,107,5,1,0,0,107,13,1,0,
        0,0,108,109,3,16,8,0,109,110,3,18,9,0,110,15,1,0,0,0,111,112,7,0,
        0,0,112,17,1,0,0,0,113,114,5,1,0,0,114,115,5,36,0,0,115,116,3,20,
        10,0,116,117,5,37,0,0,117,19,1,0,0,0,118,119,5,40,0,0,119,120,3,
        22,11,0,120,21,1,0,0,0,121,122,5,38,0,0,122,123,5,40,0,0,123,126,
        3,22,11,0,124,126,1,0,0,0,125,121,1,0,0,0,125,124,1,0,0,0,126,23,
        1,0,0,0,127,128,5,11,0,0,128,129,5,1,0,0,129,130,3,26,13,0,130,131,
        3,34,17,0,131,132,3,36,18,0,132,25,1,0,0,0,133,134,5,34,0,0,134,
        135,3,28,14,0,135,136,5,35,0,0,136,27,1,0,0,0,137,138,3,32,16,0,
        138,139,3,30,15,0,139,142,1,0,0,0,140,142,1,0,0,0,141,137,1,0,0,
        0,141,140,1,0,0,0,142,29,1,0,0,0,143,144,5,38,0,0,144,145,3,32,16,
        0,145,146,3,30,15,0,146,149,1,0,0,0,147,149,1,0,0,0,148,143,1,0,
        0,0,148,147,1,0,0,0,149,31,1,0,0,0,150,153,3,8,4,0,151,153,3,14,
        7,0,152,150,1,0,0,0,152,151,1,0,0,0,153,33,1,0,0,0,154,155,5,39,
        0,0,155,158,3,34,17,0,156,158,1,0,0,0,157,154,1,0,0,0,157,156,1,
        0,0,0,158,35,1,0,0,0,159,162,3,60,30,0,160,162,3,62,31,0,161,159,
        1,0,0,0,161,160,1,0,0,0,162,37,1,0,0,0,163,164,1,0,0,0,164,39,1,
        0,0,0,165,166,1,0,0,0,166,41,1,0,0,0,167,168,3,6,3,0,168,43,1,0,
        0,0,169,170,3,46,23,0,170,171,3,48,24,0,171,172,5,32,0,0,172,173,
        3,66,33,0,173,45,1,0,0,0,174,177,3,16,8,0,175,177,1,0,0,0,176,174,
        1,0,0,0,176,175,1,0,0,0,177,47,1,0,0,0,178,181,5,1,0,0,179,181,3,
        18,9,0,180,178,1,0,0,0,180,179,1,0,0,0,181,49,1,0,0,0,182,183,3,
        52,26,0,183,184,3,64,32,0,184,185,3,54,27,0,185,186,3,64,32,0,186,
        187,3,56,28,0,187,51,1,0,0,0,188,189,5,17,0,0,189,190,5,34,0,0,190,
        191,3,68,34,0,191,192,5,35,0,0,192,193,3,58,29,0,193,194,3,40,20,
        0,194,53,1,0,0,0,195,196,5,19,0,0,196,197,5,34,0,0,197,198,3,68,
        34,0,198,199,5,35,0,0,199,200,3,58,29,0,200,201,3,40,20,0,201,202,
        3,64,32,0,202,203,3,54,27,0,203,206,1,0,0,0,204,206,1,0,0,0,205,
        195,1,0,0,0,205,204,1,0,0,0,206,55,1,0,0,0,207,208,1,0,0,0,208,57,
        1,0,0,0,209,210,5,39,0,0,210,213,3,58,29,0,211,213,1,0,0,0,212,209,
        1,0,0,0,212,211,1,0,0,0,213,59,1,0,0,0,214,215,1,0,0,0,215,61,1,
        0,0,0,216,217,5,20,0,0,217,218,3,64,32,0,218,219,3,40,20,0,219,220,
        3,64,32,0,220,221,5,21,0,0,221,63,1,0,0,0,222,223,5,39,0,0,223,226,
        3,64,32,0,224,226,5,39,0,0,225,222,1,0,0,0,225,224,1,0,0,0,226,65,
        1,0,0,0,227,228,1,0,0,0,228,67,1,0,0,0,229,230,1,0,0,0,230,69,1,
        0,0,0,14,84,89,95,125,141,148,152,157,161,176,180,205,212,225
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
    RULE_list_stmt = 20
    RULE_stmt_vari_decl = 21
    RULE_stmt_assi = 22
    RULE_assi_type = 23
    RULE_assi_id = 24
    RULE_stmt_cond = 25
    RULE_stmt_if = 26
    RULE_stmt_elif = 27
    RULE_stmt_else = 28
    RULE_stmt_sepa_cond = 29
    RULE_stmt_return = 30
    RULE_stmt_block = 31
    RULE_stmt_sepa_block = 32
    RULE_expr = 33
    RULE_expr_cond = 34

    ruleNames =  [ "program", "decls_stmt", "decls_stmt_tail", "vari_decls", 
                   "vari_decls_type1", "vari_decls_type2", "vari_decls_type3", 
                   "vari_decls_type4", "vari_type", "array", "list_num", 
                   "list_num_tail", "func_decls", "func_param", "list_param", 
                   "list_param_tail", "params", "func_sepa", "func_body", 
                   "stmt", "list_stmt", "stmt_vari_decl", "stmt_assi", "assi_type", 
                   "assi_id", "stmt_cond", "stmt_if", "stmt_elif", "stmt_else", 
                   "stmt_sepa_cond", "stmt_return", "stmt_block", "stmt_sepa_block", 
                   "expr", "expr_cond" ]

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
            self.state = 70
            self.decls_stmt()
            self.state = 71
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
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.stmt()
                self.state = 74
                self.decls_stmt_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.vari_decls()
                self.state = 77
                self.decls_stmt_tail()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 79
                self.func_decls()
                self.state = 80
                self.decls_stmt_tail()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
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
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(ZCodeParser.NEWLINE)
                self.state = 87
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.vari_decls_type1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.vari_decls_type2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.vari_decls_type3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
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
            self.state = 97
            self.vari_type()
            self.state = 98
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
            self.state = 100
            self.match(ZCodeParser.VAR)
            self.state = 101
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 102
            self.match(ZCodeParser.ASSIGN)
            self.state = 103
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
            self.state = 105
            self.match(ZCodeParser.DYNAMIC)
            self.state = 106
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
            self.state = 108
            self.vari_type()
            self.state = 109
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
            self.state = 111
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
            self.state = 113
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 114
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 115
            self.list_num()
            self.state = 116
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
            self.state = 118
            self.match(ZCodeParser.NUMBER)
            self.state = 119
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
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(ZCodeParser.COMMA)
                self.state = 122
                self.match(ZCodeParser.NUMBER)
                self.state = 123
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
            self.state = 127
            self.match(ZCodeParser.FUNC)
            self.state = 128
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 129
            self.func_param()
            self.state = 130
            self.func_sepa()
            self.state = 131
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
            self.state = 133
            self.match(ZCodeParser.OPENPAREN)
            self.state = 134
            self.list_param()
            self.state = 135
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
            self.state = 141
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.params()
                self.state = 138
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
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [38]:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(ZCodeParser.COMMA)
                self.state = 144
                self.params()
                self.state = 145
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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.vari_decls_type1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.match(ZCodeParser.NEWLINE)
                self.state = 155
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
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [-1, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.stmt_return()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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


    class List_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_stmt




    def list_stmt(self):

        localctx = ZCodeParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_stmt)
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
        self.enterRule(localctx, 42, self.RULE_stmt_vari_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
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
        self.enterRule(localctx, 44, self.RULE_stmt_assi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.assi_type()
            self.state = 170
            self.assi_id()
            self.state = 171
            self.match(ZCodeParser.ASSIGN)
            self.state = 172
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
        self.enterRule(localctx, 46, self.RULE_assi_type)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
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
        self.enterRule(localctx, 48, self.RULE_assi_id)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.array()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_if(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_ifContext,0)


        def stmt_sepa_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Stmt_sepa_blockContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_blockContext,i)


        def stmt_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_elifContext,0)


        def stmt_else(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_elseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_cond




    def stmt_cond(self):

        localctx = ZCodeParser.Stmt_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.stmt_if()
            self.state = 183
            self.stmt_sepa_block()
            self.state = 184
            self.stmt_elif()
            self.state = 185
            self.stmt_sepa_block()
            self.state = 186
            self.stmt_else()
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

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def stmt_sepa_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_condContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_if




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(ZCodeParser.IF)
            self.state = 189
            self.match(ZCodeParser.OPENPAREN)
            self.state = 190
            self.expr_cond()
            self.state = 191
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 192
            self.stmt_sepa_cond()
            self.state = 193
            self.list_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_elifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def stmt_sepa_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_condContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def stmt_sepa_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_blockContext,0)


        def stmt_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_elifContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_elif




    def stmt_elif(self):

        localctx = ZCodeParser.Stmt_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_elif)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(ZCodeParser.ELIF)
                self.state = 196
                self.match(ZCodeParser.OPENPAREN)
                self.state = 197
                self.expr_cond()
                self.state = 198
                self.match(ZCodeParser.CLOSEPAREN)
                self.state = 199
                self.stmt_sepa_cond()
                self.state = 200
                self.list_stmt()
                self.state = 201
                self.stmt_sepa_block()
                self.state = 202
                self.stmt_elif()
                pass
            elif token in [39]:
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


    class Stmt_elseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_else




    def stmt_else(self):

        localctx = ZCodeParser.Stmt_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_else)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_sepa_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def stmt_sepa_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_condContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_sepa_cond




    def stmt_sepa_cond(self):

        localctx = ZCodeParser.Stmt_sepa_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_sepa_cond)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(ZCodeParser.NEWLINE)
                self.state = 210
                self.stmt_sepa_cond()
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


    class Stmt_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_return




    def stmt_return(self):

        localctx = ZCodeParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt_return)
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

        def stmt_sepa_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Stmt_sepa_blockContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_blockContext,i)


        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(ZCodeParser.BEGIN)
            self.state = 217
            self.stmt_sepa_block()
            self.state = 218
            self.list_stmt()
            self.state = 219
            self.stmt_sepa_block()
            self.state = 220
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_sepa_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def stmt_sepa_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_sepa_block




    def stmt_sepa_block(self):

        localctx = ZCodeParser.Stmt_sepa_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stmt_sepa_block)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(ZCodeParser.NEWLINE)
                self.state = 223
                self.stmt_sepa_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(ZCodeParser.NEWLINE)
                pass


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
        self.enterRule(localctx, 66, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond




    def expr_cond(self):

        localctx = ZCodeParser.Expr_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr_cond)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





