# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("&\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\6\4\36\n\4\r\4\16\4\37\3\4\3\4\3\5\3\5\3\5\2\2\6\3")
        buf.write("\3\5\4\7\5\t\6\3\2\3\5\2\13\f\17\17\"\"\2&\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\23")
        buf.write("\3\2\2\2\7\35\3\2\2\2\t#\3\2\2\2\13\f\7x\2\2\f\r\7c\2")
        buf.write("\2\r\16\7t\2\2\16\17\7f\2\2\17\20\7g\2\2\20\21\7e\2\2")
        buf.write("\21\22\7n\2\2\22\4\3\2\2\2\23\24\7h\2\2\24\25\7w\2\2\25")
        buf.write("\26\7p\2\2\26\27\7e\2\2\27\30\7f\2\2\30\31\7g\2\2\31\32")
        buf.write("\7e\2\2\32\33\7n\2\2\33\6\3\2\2\2\34\36\t\2\2\2\35\34")
        buf.write("\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2")
        buf.write("\2\2!\"\b\4\2\2\"\b\3\2\2\2#$\13\2\2\2$%\b\5\3\2%\n\3")
        buf.write("\2\2\2\4\2\37\4\b\2\2\3\5\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS = 3
    ERROR_CHAR = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'vardecl'", "'funcdecl'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


