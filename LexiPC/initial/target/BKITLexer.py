# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("\36\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\r\n\2")
        buf.write("\f\2\16\2\20\13\2\3\2\5\2\23\n\2\3\3\6\3\26\n\3\r\3\16")
        buf.write("\3\27\3\3\3\3\3\4\3\4\3\4\2\2\5\3\3\5\4\7\5\3\2\5\3\2")
        buf.write("\63;\4\2\62;aa\5\2\13\f\17\17\"\"\2 \2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\3\22\3\2\2\2\5\25\3\2\2\2\7\33\3\2")
        buf.write("\2\2\t\23\7\62\2\2\n\16\t\2\2\2\13\r\t\3\2\2\f\13\3\2")
        buf.write("\2\2\r\20\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\21\3\2")
        buf.write("\2\2\20\16\3\2\2\2\21\23\b\2\2\2\22\t\3\2\2\2\22\n\3\2")
        buf.write("\2\2\23\4\3\2\2\2\24\26\t\4\2\2\25\24\3\2\2\2\26\27\3")
        buf.write("\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32")
        buf.write("\b\3\3\2\32\6\3\2\2\2\33\34\13\2\2\2\34\35\b\4\4\2\35")
        buf.write("\b\3\2\2\2\6\2\16\22\27\5\3\2\2\b\2\2\3\4\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    WS = 2
    ERROR_CHAR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "INT", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[0] = self.INT_action 
            actions[2] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


