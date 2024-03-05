# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/")
        buf.write("\u019a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3m\n\3\3\4\3\4\3\4\5\4r\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u0083")
        buf.write("\n\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u009b")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\5\f\u00a2\n\f\3\r\3\r\5\r\u00a6")
        buf.write("\n\r\3\16\3\16\5\16\u00aa\n\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00bc\n\21\3\22\3\22\3\22\3\22\3\22\5\22\u00c3\n")
        buf.write("\22\3\23\3\23\3\23\3\24\3\24\3\24\5\24\u00cb\n\24\3\25")
        buf.write("\3\25\3\25\5\25\u00d0\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\3\26\5\26\u00db\n\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u00e2\n\27\3\30\3\30\3\31\3\31\3\31\3\31\3")
        buf.write("\32\3\32\7\32\u00ec\n\32\f\32\16\32\u00ef\13\32\3\32\5")
        buf.write("\32\u00f2\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\5!\u0118\n!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\5#\u0124\n#\3$\3$\3$\3$\3$\5$\u012b\n$")
        buf.write("\3%\3%\5%\u012f\n%\3&\3&\3&\3&\3&\3\'\3\'\3\'\5\'\u0139")
        buf.write("\n\'\3(\3(\3(\5(\u013e\n(\3)\3)\3*\3*\3*\3*\3*\5*\u0147")
        buf.write("\n*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0152\n+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\7,\u015d\n,\f,\16,\u0160\13,\3-\3-\3")
        buf.write("-\5-\u0165\n-\3.\3.\3.\3.\3.\3.\3.\3.\3.\7.\u0170\n.\f")
        buf.write(".\16.\u0173\13.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\7")
        buf.write("/\u0181\n/\f/\16/\u0184\13/\3\60\3\60\3\60\5\60\u0189")
        buf.write("\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u0196\n\61\3\62\3\62\3\62\2\5VZ\\\63\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`b\2\5\3\2\5\7\3\2\t\n\3\2\3\4\2")
        buf.write("\u019b\2d\3\2\2\2\4l\3\2\2\2\6q\3\2\2\2\b\u0082\3\2\2")
        buf.write("\2\n\u0084\3\2\2\2\f\u0086\3\2\2\2\16\u0088\3\2\2\2\20")
        buf.write("\u008d\3\2\2\2\22\u0091\3\2\2\2\24\u009a\3\2\2\2\26\u00a1")
        buf.write("\3\2\2\2\30\u00a5\3\2\2\2\32\u00a9\3\2\2\2\34\u00ab\3")
        buf.write("\2\2\2\36\u00b3\3\2\2\2 \u00bb\3\2\2\2\"\u00c2\3\2\2\2")
        buf.write("$\u00c4\3\2\2\2&\u00ca\3\2\2\2(\u00cf\3\2\2\2*\u00da\3")
        buf.write("\2\2\2,\u00e1\3\2\2\2.\u00e3\3\2\2\2\60\u00e5\3\2\2\2")
        buf.write("\62\u00e9\3\2\2\2\64\u00f3\3\2\2\2\66\u00fa\3\2\2\28\u0102")
        buf.write("\3\2\2\2:\u0107\3\2\2\2<\u0110\3\2\2\2>\u0112\3\2\2\2")
        buf.write("@\u0117\3\2\2\2B\u0119\3\2\2\2D\u0123\3\2\2\2F\u012a\3")
        buf.write("\2\2\2H\u012e\3\2\2\2J\u0130\3\2\2\2L\u0138\3\2\2\2N\u013d")
        buf.write("\3\2\2\2P\u013f\3\2\2\2R\u0146\3\2\2\2T\u0151\3\2\2\2")
        buf.write("V\u0153\3\2\2\2X\u0164\3\2\2\2Z\u0166\3\2\2\2\\\u0174")
        buf.write("\3\2\2\2^\u0188\3\2\2\2`\u0195\3\2\2\2b\u0197\3\2\2\2")
        buf.write("de\5\4\3\2ef\7\2\2\3f\3\3\2\2\2gh\5\6\4\2hi\7\'\2\2ij")
        buf.write("\5\4\3\2jm\3\2\2\2km\3\2\2\2lg\3\2\2\2lk\3\2\2\2m\5\3")
        buf.write("\2\2\2nr\5\b\5\2or\5\34\17\2pr\3\2\2\2qn\3\2\2\2qo\3\2")
        buf.write("\2\2qp\3\2\2\2r\7\3\2\2\2st\5\n\6\2tu\5\30\r\2u\u0083")
        buf.write("\3\2\2\2vw\7\n\2\2w\u0083\7*\2\2xy\5\n\6\2yz\5\30\r\2")
        buf.write("z{\7 \2\2{|\5P)\2|\u0083\3\2\2\2}~\5\f\7\2~\177\7*\2\2")
        buf.write("\177\u0080\7 \2\2\u0080\u0081\5P)\2\u0081\u0083\3\2\2")
        buf.write("\2\u0082s\3\2\2\2\u0082v\3\2\2\2\u0082x\3\2\2\2\u0082")
        buf.write("}\3\2\2\2\u0083\t\3\2\2\2\u0084\u0085\t\2\2\2\u0085\13")
        buf.write("\3\2\2\2\u0086\u0087\t\3\2\2\u0087\r\3\2\2\2\u0088\u0089")
        buf.write("\7*\2\2\u0089\u008a\7$\2\2\u008a\u008b\5\26\f\2\u008b")
        buf.write("\u008c\7%\2\2\u008c\17\3\2\2\2\u008d\u008e\7$\2\2\u008e")
        buf.write("\u008f\5\26\f\2\u008f\u0090\7%\2\2\u0090\21\3\2\2\2\u0091")
        buf.write("\u0092\7*\2\2\u0092\u0093\7$\2\2\u0093\u0094\5\24\13\2")
        buf.write("\u0094\u0095\7%\2\2\u0095\23\3\2\2\2\u0096\u009b\7(\2")
        buf.write("\2\u0097\u0098\7(\2\2\u0098\u0099\7&\2\2\u0099\u009b\5")
        buf.write("\24\13\2\u009a\u0096\3\2\2\2\u009a\u0097\3\2\2\2\u009b")
        buf.write("\25\3\2\2\2\u009c\u00a2\5P)\2\u009d\u009e\5P)\2\u009e")
        buf.write("\u009f\7&\2\2\u009f\u00a0\5\26\f\2\u00a0\u00a2\3\2\2\2")
        buf.write("\u00a1\u009c\3\2\2\2\u00a1\u009d\3\2\2\2\u00a2\27\3\2")
        buf.write("\2\2\u00a3\u00a6\7*\2\2\u00a4\u00a6\5\22\n\2\u00a5\u00a3")
        buf.write("\3\2\2\2\u00a5\u00a4\3\2\2\2\u00a6\31\3\2\2\2\u00a7\u00aa")
        buf.write("\7*\2\2\u00a8\u00aa\5\16\b\2\u00a9\u00a7\3\2\2\2\u00a9")
        buf.write("\u00a8\3\2\2\2\u00aa\33\3\2\2\2\u00ab\u00ac\7\13\2\2\u00ac")
        buf.write("\u00ad\7*\2\2\u00ad\u00ae\7\"\2\2\u00ae\u00af\5 \21\2")
        buf.write("\u00af\u00b0\7#\2\2\u00b0\u00b1\5&\24\2\u00b1\u00b2\5")
        buf.write("(\25\2\u00b2\35\3\2\2\2\u00b3\u00b4\7\"\2\2\u00b4\u00b5")
        buf.write("\5 \21\2\u00b5\u00b6\7#\2\2\u00b6\37\3\2\2\2\u00b7\u00b8")
        buf.write("\5$\23\2\u00b8\u00b9\5\"\22\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b7\3\2\2\2\u00bb\u00ba\3\2\2\2")
        buf.write("\u00bc!\3\2\2\2\u00bd\u00be\7&\2\2\u00be\u00bf\5$\23\2")
        buf.write("\u00bf\u00c0\5\"\22\2\u00c0\u00c3\3\2\2\2\u00c1\u00c3")
        buf.write("\3\2\2\2\u00c2\u00bd\3\2\2\2\u00c2\u00c1\3\2\2\2\u00c3")
        buf.write("#\3\2\2\2\u00c4\u00c5\5\n\6\2\u00c5\u00c6\5\30\r\2\u00c6")
        buf.write("%\3\2\2\2\u00c7\u00c8\7\'\2\2\u00c8\u00cb\5&\24\2\u00c9")
        buf.write("\u00cb\3\2\2\2\u00ca\u00c7\3\2\2\2\u00ca\u00c9\3\2\2\2")
        buf.write("\u00cb\'\3\2\2\2\u00cc\u00d0\5@!\2\u00cd\u00d0\5J&\2\u00ce")
        buf.write("\u00d0\3\2\2\2\u00cf\u00cc\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00ce\3\2\2\2\u00d0)\3\2\2\2\u00d1\u00db\5.\30")
        buf.write("\2\u00d2\u00db\5\60\31\2\u00d3\u00db\5\62\32\2\u00d4\u00db")
        buf.write("\5:\36\2\u00d5\u00db\5<\37\2\u00d6\u00db\5> \2\u00d7\u00db")
        buf.write("\5@!\2\u00d8\u00db\5B\"\2\u00d9\u00db\5J&\2\u00da\u00d1")
        buf.write("\3\2\2\2\u00da\u00d2\3\2\2\2\u00da\u00d3\3\2\2\2\u00da")
        buf.write("\u00d4\3\2\2\2\u00da\u00d5\3\2\2\2\u00da\u00d6\3\2\2\2")
        buf.write("\u00da\u00d7\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00d9\3")
        buf.write("\2\2\2\u00db+\3\2\2\2\u00dc\u00dd\5*\26\2\u00dd\u00de")
        buf.write("\5L\'\2\u00de\u00df\5,\27\2\u00df\u00e2\3\2\2\2\u00e0")
        buf.write("\u00e2\3\2\2\2\u00e1\u00dc\3\2\2\2\u00e1\u00e0\3\2\2\2")
        buf.write("\u00e2-\3\2\2\2\u00e3\u00e4\5\b\5\2\u00e4/\3\2\2\2\u00e5")
        buf.write("\u00e6\5\32\16\2\u00e6\u00e7\7 \2\2\u00e7\u00e8\5P)\2")
        buf.write("\u00e8\61\3\2\2\2\u00e9\u00ed\5\64\33\2\u00ea\u00ec\5")
        buf.write("\66\34\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00f1\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00f0\u00f2\58\35\2\u00f1\u00f0\3")
        buf.write("\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\63\3\2\2\2\u00f3\u00f4")
        buf.write("\7\21\2\2\u00f4\u00f5\7\"\2\2\u00f5\u00f6\5P)\2\u00f6")
        buf.write("\u00f7\7#\2\2\u00f7\u00f8\5N(\2\u00f8\u00f9\5*\26\2\u00f9")
        buf.write("\65\3\2\2\2\u00fa\u00fb\5L\'\2\u00fb\u00fc\7\22\2\2\u00fc")
        buf.write("\u00fd\7\"\2\2\u00fd\u00fe\5P)\2\u00fe\u00ff\7#\2\2\u00ff")
        buf.write("\u0100\5N(\2\u0100\u0101\5*\26\2\u0101\67\3\2\2\2\u0102")
        buf.write("\u0103\5L\'\2\u0103\u0104\7\23\2\2\u0104\u0105\5N(\2\u0105")
        buf.write("\u0106\5*\26\2\u01069\3\2\2\2\u0107\u0108\7\f\2\2\u0108")
        buf.write("\u0109\7*\2\2\u0109\u010a\7\r\2\2\u010a\u010b\5P)\2\u010b")
        buf.write("\u010c\7\16\2\2\u010c\u010d\5P)\2\u010d\u010e\5N(\2\u010e")
        buf.write("\u010f\5*\26\2\u010f;\3\2\2\2\u0110\u0111\7\17\2\2\u0111")
        buf.write("=\3\2\2\2\u0112\u0113\7\20\2\2\u0113?\3\2\2\2\u0114\u0115")
        buf.write("\7\b\2\2\u0115\u0118\5P)\2\u0116\u0118\7\b\2\2\u0117\u0114")
        buf.write("\3\2\2\2\u0117\u0116\3\2\2\2\u0118A\3\2\2\2\u0119\u011a")
        buf.write("\7*\2\2\u011a\u011b\7\"\2\2\u011b\u011c\5D#\2\u011c\u011d")
        buf.write("\7#\2\2\u011d\u011e\5H%\2\u011eC\3\2\2\2\u011f\u0120\5")
        buf.write("P)\2\u0120\u0121\5F$\2\u0121\u0124\3\2\2\2\u0122\u0124")
        buf.write("\3\2\2\2\u0123\u011f\3\2\2\2\u0123\u0122\3\2\2\2\u0124")
        buf.write("E\3\2\2\2\u0125\u0126\7&\2\2\u0126\u0127\5P)\2\u0127\u0128")
        buf.write("\5F$\2\u0128\u012b\3\2\2\2\u0129\u012b\3\2\2\2\u012a\u0125")
        buf.write("\3\2\2\2\u012a\u0129\3\2\2\2\u012bG\3\2\2\2\u012c\u012f")
        buf.write("\5\20\t\2\u012d\u012f\3\2\2\2\u012e\u012c\3\2\2\2\u012e")
        buf.write("\u012d\3\2\2\2\u012fI\3\2\2\2\u0130\u0131\7\24\2\2\u0131")
        buf.write("\u0132\5L\'\2\u0132\u0133\5,\27\2\u0133\u0134\7\25\2\2")
        buf.write("\u0134K\3\2\2\2\u0135\u0139\7\'\2\2\u0136\u0137\7\'\2")
        buf.write("\2\u0137\u0139\5L\'\2\u0138\u0135\3\2\2\2\u0138\u0136")
        buf.write("\3\2\2\2\u0139M\3\2\2\2\u013a\u013b\7\'\2\2\u013b\u013e")
        buf.write("\5N(\2\u013c\u013e\3\2\2\2\u013d\u013a\3\2\2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013eO\3\2\2\2\u013f\u0140\5R*\2\u0140Q\3\2\2")
        buf.write("\2\u0141\u0142\5T+\2\u0142\u0143\7!\2\2\u0143\u0144\5")
        buf.write("T+\2\u0144\u0147\3\2\2\2\u0145\u0147\5T+\2\u0146\u0141")
        buf.write("\3\2\2\2\u0146\u0145\3\2\2\2\u0147S\3\2\2\2\u0148\u0149")
        buf.write("\5V,\2\u0149\u014a\7\36\2\2\u014a\u014b\5V,\2\u014b\u0152")
        buf.write("\3\2\2\2\u014c\u014d\5V,\2\u014d\u014e\7\37\2\2\u014e")
        buf.write("\u014f\5V,\2\u014f\u0152\3\2\2\2\u0150\u0152\5V,\2\u0151")
        buf.write("\u0148\3\2\2\2\u0151\u014c\3\2\2\2\u0151\u0150\3\2\2\2")
        buf.write("\u0152U\3\2\2\2\u0153\u0154\b,\1\2\u0154\u0155\5Z.\2\u0155")
        buf.write("\u015e\3\2\2\2\u0156\u0157\f\5\2\2\u0157\u0158\7\27\2")
        buf.write("\2\u0158\u015d\5Z.\2\u0159\u015a\f\4\2\2\u015a\u015b\7")
        buf.write("\30\2\2\u015b\u015d\5Z.\2\u015c\u0156\3\2\2\2\u015c\u0159")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015fW\3\2\2\2\u0160\u015e\3\2\2\2\u0161")
        buf.write("\u0162\7\26\2\2\u0162\u0165\5X-\2\u0163\u0165\5^\60\2")
        buf.write("\u0164\u0161\3\2\2\2\u0164\u0163\3\2\2\2\u0165Y\3\2\2")
        buf.write("\2\u0166\u0167\b.\1\2\u0167\u0168\5\\/\2\u0168\u0171\3")
        buf.write("\2\2\2\u0169\u016a\f\5\2\2\u016a\u016b\7\31\2\2\u016b")
        buf.write("\u0170\5\\/\2\u016c\u016d\f\4\2\2\u016d\u016e\7\32\2\2")
        buf.write("\u016e\u0170\5\\/\2\u016f\u0169\3\2\2\2\u016f\u016c\3")
        buf.write("\2\2\2\u0170\u0173\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172")
        buf.write("\3\2\2\2\u0172[\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175")
        buf.write("\b/\1\2\u0175\u0176\5X-\2\u0176\u0182\3\2\2\2\u0177\u0178")
        buf.write("\f\6\2\2\u0178\u0179\7\33\2\2\u0179\u0181\5X-\2\u017a")
        buf.write("\u017b\f\5\2\2\u017b\u017c\7\34\2\2\u017c\u0181\5X-\2")
        buf.write("\u017d\u017e\f\4\2\2\u017e\u017f\7\35\2\2\u017f\u0181")
        buf.write("\5X-\2\u0180\u0177\3\2\2\2\u0180\u017a\3\2\2\2\u0180\u017d")
        buf.write("\3\2\2\2\u0181\u0184\3\2\2\2\u0182\u0180\3\2\2\2\u0182")
        buf.write("\u0183\3\2\2\2\u0183]\3\2\2\2\u0184\u0182\3\2\2\2\u0185")
        buf.write("\u0186\7\32\2\2\u0186\u0189\5^\60\2\u0187\u0189\5`\61")
        buf.write("\2\u0188\u0185\3\2\2\2\u0188\u0187\3\2\2\2\u0189_\3\2")
        buf.write("\2\2\u018a\u018b\7\"\2\2\u018b\u018c\5P)\2\u018c\u018d")
        buf.write("\7#\2\2\u018d\u0196\3\2\2\2\u018e\u0196\7*\2\2\u018f\u0196")
        buf.write("\7(\2\2\u0190\u0196\7)\2\2\u0191\u0196\5b\62\2\u0192\u0196")
        buf.write("\5\16\b\2\u0193\u0196\5\20\t\2\u0194\u0196\5B\"\2\u0195")
        buf.write("\u018a\3\2\2\2\u0195\u018e\3\2\2\2\u0195\u018f\3\2\2\2")
        buf.write("\u0195\u0190\3\2\2\2\u0195\u0191\3\2\2\2\u0195\u0192\3")
        buf.write("\2\2\2\u0195\u0193\3\2\2\2\u0195\u0194\3\2\2\2\u0196a")
        buf.write("\3\2\2\2\u0197\u0198\t\4\2\2\u0198c\3\2\2\2\"lq\u0082")
        buf.write("\u009a\u00a1\u00a5\u00a9\u00bb\u00c2\u00ca\u00cf\u00da")
        buf.write("\u00e1\u00ed\u00f1\u0117\u0123\u012a\u012e\u0138\u013d")
        buf.write("\u0146\u0151\u015c\u015e\u0164\u016f\u0171\u0180\u0182")
        buf.write("\u0188\u0195")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'elif'", "'else'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "<INVALID>", "'=='", "'<-'", "'...'", "'('", "')'", 
                     "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "KWNUMBER", "KWBOOL", 
                      "KWSTRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELIF", 
                      "ELSE", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "COMPARENUM", "COMPARESTR", 
                      "ASSIGN", "CONCAT", "OPENPAREN", "CLOSEPAREN", "OPENSQBRACKET", 
                      "CLOSESQBRACKET", "COMMA", "NEWLINE", "NUMBER", "STRING", 
                      "IDENTIFIER", "CMT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls_list = 1
    RULE_decls = 2
    RULE_vari_decls = 3
    RULE_vari_decls_type = 4
    RULE_vari_decls_impli = 5
    RULE_array = 6
    RULE_array_tail = 7
    RULE_array_decls = 8
    RULE_list_num = 9
    RULE_list_expr = 10
    RULE_vari_decls_id = 11
    RULE_vari_id = 12
    RULE_func_decls = 13
    RULE_func_param = 14
    RULE_list_param = 15
    RULE_list_param_tail = 16
    RULE_params = 17
    RULE_func_sepa = 18
    RULE_func_body = 19
    RULE_stmt = 20
    RULE_list_stmt = 21
    RULE_stmt_vari_decl = 22
    RULE_stmt_assi = 23
    RULE_stmt_cond = 24
    RULE_stmt_if = 25
    RULE_stmt_elif = 26
    RULE_stmt_else = 27
    RULE_stmt_for = 28
    RULE_stmt_break = 29
    RULE_stmt_continue = 30
    RULE_stmt_return = 31
    RULE_stmt_func_call = 32
    RULE_sfc_list_args = 33
    RULE_sfc_list_args_tail = 34
    RULE_sfc_body = 35
    RULE_stmt_block = 36
    RULE_stmt_sepa_nonnull = 37
    RULE_stmt_sepa_null = 38
    RULE_expr = 39
    RULE_expr_string_concat = 40
    RULE_expr_compare = 41
    RULE_expr_cond_andor = 42
    RULE_expr_cond_not = 43
    RULE_e_n_addsub = 44
    RULE_e_n_muldivmod = 45
    RULE_e_n_nega = 46
    RULE_expr_other = 47
    RULE_boolval = 48

    ruleNames =  [ "program", "decls_list", "decls", "vari_decls", "vari_decls_type", 
                   "vari_decls_impli", "array", "array_tail", "array_decls", 
                   "list_num", "list_expr", "vari_decls_id", "vari_id", 
                   "func_decls", "func_param", "list_param", "list_param_tail", 
                   "params", "func_sepa", "func_body", "stmt", "list_stmt", 
                   "stmt_vari_decl", "stmt_assi", "stmt_cond", "stmt_if", 
                   "stmt_elif", "stmt_else", "stmt_for", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_func_call", "sfc_list_args", "sfc_list_args_tail", 
                   "sfc_body", "stmt_block", "stmt_sepa_nonnull", "stmt_sepa_null", 
                   "expr", "expr_string_concat", "expr_compare", "expr_cond_andor", 
                   "expr_cond_not", "e_n_addsub", "e_n_muldivmod", "e_n_nega", 
                   "expr_other", "boolval" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    KWNUMBER=3
    KWBOOL=4
    KWSTRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELIF=16
    ELSE=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    COMPARENUM=28
    COMPARESTR=29
    ASSIGN=30
    CONCAT=31
    OPENPAREN=32
    CLOSEPAREN=33
    OPENSQBRACKET=34
    CLOSESQBRACKET=35
    COMMA=36
    NEWLINE=37
    NUMBER=38
    STRING=39
    IDENTIFIER=40
    CMT=41
    WS=42
    UNCLOSE_STRING=43
    ILLEGAL_ESCAPE=44
    ERROR_CHAR=45

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

        def decls_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.decls_list()
            self.state = 99
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decls_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decls(self):
            return self.getTypedRuleContext(ZCodeParser.DeclsContext,0)


        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def decls_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decls_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls_list" ):
                return visitor.visitDecls_list(self)
            else:
                return visitor.visitChildren(self)




    def decls_list(self):

        localctx = ZCodeParser.Decls_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls_list)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.decls()
                self.state = 102
                self.match(ZCodeParser.NEWLINE)
                self.state = 103
                self.decls_list()
                pass
            elif token in [ZCodeParser.EOF]:
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


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_declsContext,0)


        def func_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Func_declsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls" ):
                return visitor.visitDecls(self)
            else:
                return visitor.visitChildren(self)




    def decls(self):

        localctx = ZCodeParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decls)
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.vari_decls()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.func_decls()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)

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

        def vari_decls_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_typeContext,0)


        def vari_decls_id(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_idContext,0)


        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def vari_decls_impli(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_impliContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls" ):
                return visitor.visitVari_decls(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls(self):

        localctx = ZCodeParser.Vari_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vari_decls)
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.vari_decls_type()
                self.state = 114
                self.vari_decls_id()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.match(ZCodeParser.DYNAMIC)
                self.state = 117
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 118
                self.vari_decls_type()
                self.state = 119
                self.vari_decls_id()
                self.state = 120
                self.match(ZCodeParser.ASSIGN)
                self.state = 121
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.vari_decls_impli()
                self.state = 124
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 125
                self.match(ZCodeParser.ASSIGN)
                self.state = 126
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_typeContext(ParserRuleContext):
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
            return ZCodeParser.RULE_vari_decls_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_type" ):
                return visitor.visitVari_decls_type(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_type(self):

        localctx = ZCodeParser.Vari_decls_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vari_decls_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KWNUMBER) | (1 << ZCodeParser.KWBOOL) | (1 << ZCodeParser.KWSTRING))) != 0)):
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


    class Vari_decls_impliContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_impli

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_impli" ):
                return visitor.visitVari_decls_impli(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_impli(self):

        localctx = ZCodeParser.Vari_decls_impliContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vari_decls_impli)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.VAR or _la==ZCodeParser.DYNAMIC):
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

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def CLOSESQBRACKET(self):
            return self.getToken(ZCodeParser.CLOSESQBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 135
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 136
            self.list_expr()
            self.state = 137
            self.match(ZCodeParser.CLOSESQBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENSQBRACKET(self):
            return self.getToken(ZCodeParser.OPENSQBRACKET, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def CLOSESQBRACKET(self):
            return self.getToken(ZCodeParser.CLOSESQBRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_tail" ):
                return visitor.visitArray_tail(self)
            else:
                return visitor.visitChildren(self)




    def array_tail(self):

        localctx = ZCodeParser.Array_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 140
            self.list_expr()
            self.state = 141
            self.match(ZCodeParser.CLOSESQBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declsContext(ParserRuleContext):
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
            return ZCodeParser.RULE_array_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decls" ):
                return visitor.visitArray_decls(self)
            else:
                return visitor.visitChildren(self)




    def array_decls(self):

        localctx = ZCodeParser.Array_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 144
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 145
            self.list_num()
            self.state = 146
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

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_num(self):
            return self.getTypedRuleContext(ZCodeParser.List_numContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_num

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_num" ):
                return visitor.visitList_num(self)
            else:
                return visitor.visitChildren(self)




    def list_num(self):

        localctx = ZCodeParser.List_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_num)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(ZCodeParser.NUMBER)
                self.state = 150
                self.match(ZCodeParser.COMMA)
                self.state = 151
                self.list_num()
                pass


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
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = ZCodeParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expr)
        try:
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.expr()
                self.state = 156
                self.match(ZCodeParser.COMMA)
                self.state = 157
                self.list_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Array_declsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_id" ):
                return visitor.visitVari_decls_id(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_id(self):

        localctx = ZCodeParser.Vari_decls_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vari_decls_id)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.array_decls()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_id

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_id" ):
                return visitor.visitVari_id(self)
            else:
                return visitor.visitChildren(self)




    def vari_id(self):

        localctx = ZCodeParser.Vari_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vari_id)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.array()
                pass


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

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def list_param(self):
            return self.getTypedRuleContext(ZCodeParser.List_paramContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def func_sepa(self):
            return self.getTypedRuleContext(ZCodeParser.Func_sepaContext,0)


        def func_body(self):
            return self.getTypedRuleContext(ZCodeParser.Func_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decls" ):
                return visitor.visitFunc_decls(self)
            else:
                return visitor.visitChildren(self)




    def func_decls(self):

        localctx = ZCodeParser.Func_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(ZCodeParser.FUNC)
            self.state = 170
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 171
            self.match(ZCodeParser.OPENPAREN)
            self.state = 172
            self.list_param()
            self.state = 173
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 174
            self.func_sepa()
            self.state = 175
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_param" ):
                return visitor.visitFunc_param(self)
            else:
                return visitor.visitChildren(self)




    def func_param(self):

        localctx = ZCodeParser.Func_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(ZCodeParser.OPENPAREN)
            self.state = 178
            self.list_param()
            self.state = 179
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param" ):
                return visitor.visitList_param(self)
            else:
                return visitor.visitChildren(self)




    def list_param(self):

        localctx = ZCodeParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_param)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.params()
                self.state = 182
                self.list_param_tail()
                pass
            elif token in [ZCodeParser.CLOSEPAREN]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param_tail" ):
                return visitor.visitList_param_tail(self)
            else:
                return visitor.visitChildren(self)




    def list_param_tail(self):

        localctx = ZCodeParser.List_param_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_list_param_tail)
        try:
            self.state = 192
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.match(ZCodeParser.COMMA)
                self.state = 188
                self.params()
                self.state = 189
                self.list_param_tail()
                pass
            elif token in [ZCodeParser.CLOSEPAREN]:
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

        def vari_decls_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_typeContext,0)


        def vari_decls_id(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_idContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ZCodeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.vari_decls_type()
            self.state = 195
            self.vari_decls_id()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_sepa" ):
                return visitor.visitFunc_sepa(self)
            else:
                return visitor.visitChildren(self)




    def func_sepa(self):

        localctx = ZCodeParser.Func_sepaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_func_sepa)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(ZCodeParser.NEWLINE)
                self.state = 198
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_body" ):
                return visitor.visitFunc_body(self)
            else:
                return visitor.visitChildren(self)




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_func_body)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.stmt_return()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.stmt_block()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)

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

        def stmt_vari_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_vari_declContext,0)


        def stmt_assi(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_assiContext,0)


        def stmt_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_condContext,0)


        def stmt_for(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_forContext,0)


        def stmt_break(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_breakContext,0)


        def stmt_continue(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_continueContext,0)


        def stmt_return(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_returnContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_stmt)
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.stmt_vari_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 208
                self.stmt_assi()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.stmt_cond()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 210
                self.stmt_for()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 211
                self.stmt_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 212
                self.stmt_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 213
                self.stmt_return()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 214
                self.stmt_func_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 215
                self.stmt_block()
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

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmt" ):
                return visitor.visitList_stmt(self)
            else:
                return visitor.visitChildren(self)




    def list_stmt(self):

        localctx = ZCodeParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_stmt)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.stmt()
                self.state = 219
                self.stmt_sepa_nonnull()
                self.state = 220
                self.list_stmt()
                pass
            elif token in [ZCodeParser.END]:
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


    class Stmt_vari_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_decls(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_declsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_vari_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_vari_decl" ):
                return visitor.visitStmt_vari_decl(self)
            else:
                return visitor.visitChildren(self)




    def stmt_vari_decl(self):

        localctx = ZCodeParser.Stmt_vari_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt_vari_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
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

        def vari_id(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_idContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_assi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assi" ):
                return visitor.visitStmt_assi(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assi(self):

        localctx = ZCodeParser.Stmt_assiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt_assi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.vari_id()
            self.state = 228
            self.match(ZCodeParser.ASSIGN)
            self.state = 229
            self.expr()
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


        def stmt_elif(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Stmt_elifContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Stmt_elifContext,i)


        def stmt_else(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_elseContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_cond" ):
                return visitor.visitStmt_cond(self)
            else:
                return visitor.visitChildren(self)




    def stmt_cond(self):

        localctx = ZCodeParser.Stmt_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.stmt_if()
            self.state = 235
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 232
                    self.stmt_elif() 
                self.state = 237
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 238
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def stmt_sepa_null(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nullContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_if

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_if" ):
                return visitor.visitStmt_if(self)
            else:
                return visitor.visitChildren(self)




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ZCodeParser.IF)
            self.state = 242
            self.match(ZCodeParser.OPENPAREN)
            self.state = 243
            self.expr()
            self.state = 244
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 245
            self.stmt_sepa_null()
            self.state = 246
            self.stmt()
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

        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def stmt_sepa_null(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nullContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_elif" ):
                return visitor.visitStmt_elif(self)
            else:
                return visitor.visitChildren(self)




    def stmt_elif(self):

        localctx = ZCodeParser.Stmt_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.stmt_sepa_nonnull()
            self.state = 249
            self.match(ZCodeParser.ELIF)
            self.state = 250
            self.match(ZCodeParser.OPENPAREN)
            self.state = 251
            self.expr()
            self.state = 252
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 253
            self.stmt_sepa_null()
            self.state = 254
            self.stmt()
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

        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def stmt_sepa_null(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nullContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_else

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_else" ):
                return visitor.visitStmt_else(self)
            else:
                return visitor.visitChildren(self)




    def stmt_else(self):

        localctx = ZCodeParser.Stmt_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.stmt_sepa_nonnull()
            self.state = 257
            self.match(ZCodeParser.ELSE)
            self.state = 258
            self.stmt_sepa_null()
            self.state = 259
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExprContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExprContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt_sepa_null(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nullContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_for

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_for" ):
                return visitor.visitStmt_for(self)
            else:
                return visitor.visitChildren(self)




    def stmt_for(self):

        localctx = ZCodeParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(ZCodeParser.FOR)
            self.state = 262
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 263
            self.match(ZCodeParser.UNTIL)
            self.state = 264
            self.expr()
            self.state = 265
            self.match(ZCodeParser.BY)
            self.state = 266
            self.expr()
            self.state = 267
            self.stmt_sepa_null()
            self.state = 268
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_breakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_break" ):
                return visitor.visitStmt_break(self)
            else:
                return visitor.visitChildren(self)




    def stmt_break(self):

        localctx = ZCodeParser.Stmt_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_continueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_continue" ):
                return visitor.visitStmt_continue(self)
            else:
                return visitor.visitChildren(self)




    def stmt_continue(self):

        localctx = ZCodeParser.Stmt_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(ZCodeParser.CONTINUE)
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

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_return

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_return" ):
                return visitor.visitStmt_return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_return(self):

        localctx = ZCodeParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stmt_return)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
                self.match(ZCodeParser.RETURN)
                self.state = 275
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(ZCodeParser.RETURN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def sfc_list_args(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_list_argsContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def sfc_body(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_bodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_call" ):
                return visitor.visitStmt_func_call(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 280
            self.match(ZCodeParser.OPENPAREN)
            self.state = 281
            self.sfc_list_args()
            self.state = 282
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 283
            self.sfc_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sfc_list_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def sfc_list_args_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_list_args_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_list_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSfc_list_args" ):
                return visitor.visitSfc_list_args(self)
            else:
                return visitor.visitChildren(self)




    def sfc_list_args(self):

        localctx = ZCodeParser.Sfc_list_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_sfc_list_args)
        try:
            self.state = 289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.expr()
                self.state = 286
                self.sfc_list_args_tail()
                pass
            elif token in [ZCodeParser.CLOSEPAREN]:
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


    class Sfc_list_args_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def sfc_list_args_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_list_args_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_list_args_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSfc_list_args_tail" ):
                return visitor.visitSfc_list_args_tail(self)
            else:
                return visitor.visitChildren(self)




    def sfc_list_args_tail(self):

        localctx = ZCodeParser.Sfc_list_args_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_sfc_list_args_tail)
        try:
            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(ZCodeParser.COMMA)
                self.state = 292
                self.expr()
                self.state = 293
                self.sfc_list_args_tail()
                pass
            elif token in [ZCodeParser.CLOSEPAREN]:
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


    class Sfc_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSfc_body" ):
                return visitor.visitSfc_body(self)
            else:
                return visitor.visitChildren(self)




    def sfc_body(self):

        localctx = ZCodeParser.Sfc_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_sfc_body)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.array_tail()
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


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(ZCodeParser.BEGIN)
            self.state = 303
            self.stmt_sepa_nonnull()
            self.state = 304
            self.list_stmt()
            self.state = 305
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_sepa_nonnullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_sepa_nonnull

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_sepa_nonnull" ):
                return visitor.visitStmt_sepa_nonnull(self)
            else:
                return visitor.visitChildren(self)




    def stmt_sepa_nonnull(self):

        localctx = ZCodeParser.Stmt_sepa_nonnullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmt_sepa_nonnull)
        try:
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 308
                self.match(ZCodeParser.NEWLINE)
                self.state = 309
                self.stmt_sepa_nonnull()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_sepa_nullContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def stmt_sepa_null(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nullContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_sepa_null

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_sepa_null" ):
                return visitor.visitStmt_sepa_null(self)
            else:
                return visitor.visitChildren(self)




    def stmt_sepa_null(self):

        localctx = ZCodeParser.Stmt_sepa_nullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt_sepa_null)
        try:
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 312
                self.match(ZCodeParser.NEWLINE)
                self.state = 313
                self.stmt_sepa_null()
                pass
            elif token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.IDENTIFIER]:
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_string_concat(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_string_concatContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expr_string_concat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_string_concatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_compare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_compareContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_compareContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string_concat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_string_concat" ):
                return visitor.visitExpr_string_concat(self)
            else:
                return visitor.visitChildren(self)




    def expr_string_concat(self):

        localctx = ZCodeParser.Expr_string_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr_string_concat)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.expr_compare()
                self.state = 320
                self.match(ZCodeParser.CONCAT)
                self.state = 321
                self.expr_compare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
                self.expr_compare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_compareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_cond_andor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_cond_andorContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_cond_andorContext,i)


        def COMPARENUM(self):
            return self.getToken(ZCodeParser.COMPARENUM, 0)

        def COMPARESTR(self):
            return self.getToken(ZCodeParser.COMPARESTR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_compare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_compare" ):
                return visitor.visitExpr_compare(self)
            else:
                return visitor.visitChildren(self)




    def expr_compare(self):

        localctx = ZCodeParser.Expr_compareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr_compare)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.expr_cond_andor(0)
                self.state = 327
                self.match(ZCodeParser.COMPARENUM)
                self.state = 328
                self.expr_cond_andor(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.expr_cond_andor(0)
                self.state = 331
                self.match(ZCodeParser.COMPARESTR)
                self.state = 332
                self.expr_cond_andor(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 334
                self.expr_cond_andor(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_cond_andorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e_n_addsub(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_addsubContext,0)


        def expr_cond_andor(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_andorContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond_andor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cond_andor" ):
                return visitor.visitExpr_cond_andor(self)
            else:
                return visitor.visitChildren(self)



    def expr_cond_andor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_cond_andorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr_cond_andor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.e_n_addsub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 346
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 340
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 341
                        self.match(ZCodeParser.AND)
                        self.state = 342
                        self.e_n_addsub(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 343
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 344
                        self.match(ZCodeParser.OR)
                        self.state = 345
                        self.e_n_addsub(0)
                        pass

             
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_cond_notContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expr_cond_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_notContext,0)


        def e_n_nega(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_negaContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cond_not" ):
                return visitor.visitExpr_cond_not(self)
            else:
                return visitor.visitChildren(self)




    def expr_cond_not(self):

        localctx = ZCodeParser.Expr_cond_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr_cond_not)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(ZCodeParser.NOT)
                self.state = 352
                self.expr_cond_not()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.e_n_nega()
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


    class E_n_addsubContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e_n_muldivmod(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_muldivmodContext,0)


        def e_n_addsub(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_addsubContext,0)


        def ADD(self):
            return self.getToken(ZCodeParser.ADD, 0)

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_e_n_addsub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_n_addsub" ):
                return visitor.visitE_n_addsub(self)
            else:
                return visitor.visitChildren(self)



    def e_n_addsub(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.E_n_addsubContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_e_n_addsub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.e_n_muldivmod(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 367
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 365
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 359
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 360
                        self.match(ZCodeParser.ADD)
                        self.state = 361
                        self.e_n_muldivmod(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 362
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 363
                        self.match(ZCodeParser.SUB)
                        self.state = 364
                        self.e_n_muldivmod(0)
                        pass

             
                self.state = 369
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class E_n_muldivmodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_cond_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_notContext,0)


        def e_n_muldivmod(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_muldivmodContext,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_e_n_muldivmod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_n_muldivmod" ):
                return visitor.visitE_n_muldivmod(self)
            else:
                return visitor.visitChildren(self)



    def e_n_muldivmod(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.E_n_muldivmodContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_e_n_muldivmod, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.expr_cond_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 382
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 373
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 374
                        self.match(ZCodeParser.MUL)
                        self.state = 375
                        self.expr_cond_not()
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 376
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 377
                        self.match(ZCodeParser.DIV)
                        self.state = 378
                        self.expr_cond_not()
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 379
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 380
                        self.match(ZCodeParser.MOD)
                        self.state = 381
                        self.expr_cond_not()
                        pass

             
                self.state = 386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class E_n_negaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(ZCodeParser.SUB, 0)

        def e_n_nega(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_negaContext,0)


        def expr_other(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_otherContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_e_n_nega

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_n_nega" ):
                return visitor.visitE_n_nega(self)
            else:
                return visitor.visitChildren(self)




    def e_n_nega(self):

        localctx = ZCodeParser.E_n_negaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_e_n_nega)
        try:
            self.state = 390
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(ZCodeParser.SUB)
                self.state = 388
                self.e_n_nega()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.expr_other()
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


    class Expr_otherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def boolval(self):
            return self.getTypedRuleContext(ZCodeParser.BoolvalContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def array_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_tailContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_other

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_other" ):
                return visitor.visitExpr_other(self)
            else:
                return visitor.visitChildren(self)




    def expr_other(self):

        localctx = ZCodeParser.Expr_otherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr_other)
        try:
            self.state = 403
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 392
                self.match(ZCodeParser.OPENPAREN)
                self.state = 393
                self.expr()
                self.state = 394
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 397
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 398
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 399
                self.boolval()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 400
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 401
                self.array_tail()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 402
                self.stmt_func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_boolval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolval" ):
                return visitor.visitBoolval(self)
            else:
                return visitor.visitChildren(self)




    def boolval(self):

        localctx = ZCodeParser.BoolvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_boolval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.TRUE or _la==ZCodeParser.FALSE):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[42] = self.expr_cond_andor_sempred
        self._predicates[44] = self.e_n_addsub_sempred
        self._predicates[45] = self.e_n_muldivmod_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_cond_andor_sempred(self, localctx:Expr_cond_andorContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def e_n_addsub_sempred(self, localctx:E_n_addsubContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def e_n_muldivmod_sempred(self, localctx:E_n_muldivmodContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




