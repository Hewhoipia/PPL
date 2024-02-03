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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\60")
        buf.write("\u01e7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u008d\n\3\3\4\3\4\3\4")
        buf.write("\5\4\u0092\n\4\3\5\3\5\3\5\3\5\5\5\u0098\n\5\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u00b5")
        buf.write("\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00bc\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\5\20\u00c6\n\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00cd\n\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u00dd\n\24\3\25\3\25\3\25\3\25\3\25\5\25\u00e4\n\25\3")
        buf.write("\26\3\26\5\26\u00e8\n\26\3\27\3\27\3\27\5\27\u00ed\n\27")
        buf.write("\3\30\3\30\5\30\u00f1\n\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\5\31\u00fc\n\31\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u0102\n\32\3\33\3\33\3\33\3\33\3\33\5\33\u0109\n")
        buf.write("\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\5\36")
        buf.write("\u0114\n\36\3\37\3\37\5\37\u0118\n\37\3 \3 \3 \3 \3 \3")
        buf.write(" \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\5\"\u0131\n\"\3#\3#\3#\3#\3#\5#\u0138\n#\3$\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3)\3)\3)\3)\3*\3*\3*\3*\5*\u0155\n*\3+\3+\3+\3+\3+\5")
        buf.write("+\u015c\n+\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\5.\u0169\n")
        buf.write(".\3/\3/\3/\5/\u016e\n/\3\60\3\60\3\60\5\60\u0173\n\60")
        buf.write("\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\7\62\u0180\n\62\f\62\16\62\u0183\13\62\3\63\3\63\3\63")
        buf.write("\5\63\u0188\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\5\64\u0193\n\64\3\65\3\65\3\66\3\66\5\66\u0199")
        buf.write("\n\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\58\u01a5")
        buf.write("\n8\39\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u01b4\n")
        buf.write(":\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\7<\u01c1\n<\f<\16<")
        buf.write("\u01c4\13<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3=\7=\u01d2")
        buf.write("\n=\f=\16=\u01d5\13=\3>\3>\3>\5>\u01da\n>\3?\3?\3?\3?")
        buf.write("\3?\3?\3?\3?\3?\5?\u01e5\n?\3?\2\5bvx@\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz|\2\4\3\2\7\t\3\2\5\6\2\u01e7")
        buf.write("\2~\3\2\2\2\4\u008c\3\2\2\2\6\u0091\3\2\2\2\b\u0097\3")
        buf.write("\2\2\2\n\u0099\3\2\2\2\f\u009c\3\2\2\2\16\u00a1\3\2\2")
        buf.write("\2\20\u00a4\3\2\2\2\22\u00a7\3\2\2\2\24\u00a9\3\2\2\2")
        buf.write("\26\u00ac\3\2\2\2\30\u00b4\3\2\2\2\32\u00bb\3\2\2\2\34")
        buf.write("\u00bd\3\2\2\2\36\u00c5\3\2\2\2 \u00cc\3\2\2\2\"\u00ce")
        buf.write("\3\2\2\2$\u00d4\3\2\2\2&\u00dc\3\2\2\2(\u00e3\3\2\2\2")
        buf.write("*\u00e7\3\2\2\2,\u00ec\3\2\2\2.\u00f0\3\2\2\2\60\u00fb")
        buf.write("\3\2\2\2\62\u0101\3\2\2\2\64\u0108\3\2\2\2\66\u010a\3")
        buf.write("\2\2\28\u010c\3\2\2\2:\u0113\3\2\2\2<\u0117\3\2\2\2>\u0119")
        buf.write("\3\2\2\2@\u011f\3\2\2\2B\u0130\3\2\2\2D\u0137\3\2\2\2")
        buf.write("F\u0139\3\2\2\2H\u0142\3\2\2\2J\u0144\3\2\2\2L\u0146\3")
        buf.write("\2\2\2N\u0149\3\2\2\2P\u014c\3\2\2\2R\u0154\3\2\2\2T\u015b")
        buf.write("\3\2\2\2V\u015d\3\2\2\2X\u015f\3\2\2\2Z\u0168\3\2\2\2")
        buf.write("\\\u016d\3\2\2\2^\u0172\3\2\2\2`\u0174\3\2\2\2b\u0176")
        buf.write("\3\2\2\2d\u0187\3\2\2\2f\u0192\3\2\2\2h\u0194\3\2\2\2")
        buf.write("j\u0198\3\2\2\2l\u019a\3\2\2\2n\u01a4\3\2\2\2p\u01a6\3")
        buf.write("\2\2\2r\u01b3\3\2\2\2t\u01b5\3\2\2\2v\u01b7\3\2\2\2x\u01c5")
        buf.write("\3\2\2\2z\u01d9\3\2\2\2|\u01e4\3\2\2\2~\177\5\4\3\2\177")
        buf.write("\u0080\7\2\2\3\u0080\3\3\2\2\2\u0081\u0082\5\60\31\2\u0082")
        buf.write("\u0083\5\6\4\2\u0083\u008d\3\2\2\2\u0084\u0085\5\b\5\2")
        buf.write("\u0085\u0086\5\6\4\2\u0086\u008d\3\2\2\2\u0087\u0088\5")
        buf.write("\"\22\2\u0088\u0089\5\6\4\2\u0089\u008d\3\2\2\2\u008a")
        buf.write("\u008d\7)\2\2\u008b\u008d\3\2\2\2\u008c\u0081\3\2\2\2")
        buf.write("\u008c\u0084\3\2\2\2\u008c\u0087\3\2\2\2\u008c\u008a\3")
        buf.write("\2\2\2\u008c\u008b\3\2\2\2\u008d\5\3\2\2\2\u008e\u008f")
        buf.write("\7)\2\2\u008f\u0092\5\4\3\2\u0090\u0092\3\2\2\2\u0091")
        buf.write("\u008e\3\2\2\2\u0091\u0090\3\2\2\2\u0092\7\3\2\2\2\u0093")
        buf.write("\u0098\5\n\6\2\u0094\u0098\5\f\7\2\u0095\u0098\5\16\b")
        buf.write("\2\u0096\u0098\5\20\t\2\u0097\u0093\3\2\2\2\u0097\u0094")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\t\3\2\2\2\u0099\u009a\5\22\n\2\u009a\u009b\7\3\2\2\u009b")
        buf.write("\13\3\2\2\2\u009c\u009d\7\13\2\2\u009d\u009e\7\3\2\2\u009e")
        buf.write("\u009f\7\"\2\2\u009f\u00a0\5^\60\2\u00a0\r\3\2\2\2\u00a1")
        buf.write("\u00a2\7\f\2\2\u00a2\u00a3\7\3\2\2\u00a3\17\3\2\2\2\u00a4")
        buf.write("\u00a5\5\22\n\2\u00a5\u00a6\5\24\13\2\u00a6\21\3\2\2\2")
        buf.write("\u00a7\u00a8\t\2\2\2\u00a8\23\3\2\2\2\u00a9\u00aa\7\3")
        buf.write("\2\2\u00aa\u00ab\5\26\f\2\u00ab\25\3\2\2\2\u00ac\u00ad")
        buf.write("\7&\2\2\u00ad\u00ae\5\30\r\2\u00ae\u00af\7\'\2\2\u00af")
        buf.write("\27\3\2\2\2\u00b0\u00b1\5t;\2\u00b1\u00b2\5\32\16\2\u00b2")
        buf.write("\u00b5\3\2\2\2\u00b3\u00b5\5t;\2\u00b4\u00b0\3\2\2\2\u00b4")
        buf.write("\u00b3\3\2\2\2\u00b5\31\3\2\2\2\u00b6\u00b7\7(\2\2\u00b7")
        buf.write("\u00b8\5t;\2\u00b8\u00b9\5\32\16\2\u00b9\u00bc\3\2\2\2")
        buf.write("\u00ba\u00bc\3\2\2\2\u00bb\u00b6\3\2\2\2\u00bb\u00ba\3")
        buf.write("\2\2\2\u00bc\33\3\2\2\2\u00bd\u00be\7&\2\2\u00be\u00bf")
        buf.write("\5\36\20\2\u00bf\u00c0\7\'\2\2\u00c0\35\3\2\2\2\u00c1")
        buf.write("\u00c2\5^\60\2\u00c2\u00c3\5 \21\2\u00c3\u00c6\3\2\2\2")
        buf.write("\u00c4\u00c6\3\2\2\2\u00c5\u00c1\3\2\2\2\u00c5\u00c4\3")
        buf.write("\2\2\2\u00c6\37\3\2\2\2\u00c7\u00c8\7(\2\2\u00c8\u00c9")
        buf.write("\5^\60\2\u00c9\u00ca\5 \21\2\u00ca\u00cd\3\2\2\2\u00cb")
        buf.write("\u00cd\3\2\2\2\u00cc\u00c7\3\2\2\2\u00cc\u00cb\3\2\2\2")
        buf.write("\u00cd!\3\2\2\2\u00ce\u00cf\7\r\2\2\u00cf\u00d0\7\3\2")
        buf.write("\2\u00d0\u00d1\5$\23\2\u00d1\u00d2\5,\27\2\u00d2\u00d3")
        buf.write("\5.\30\2\u00d3#\3\2\2\2\u00d4\u00d5\7$\2\2\u00d5\u00d6")
        buf.write("\5&\24\2\u00d6\u00d7\7%\2\2\u00d7%\3\2\2\2\u00d8\u00d9")
        buf.write("\5*\26\2\u00d9\u00da\5(\25\2\u00da\u00dd\3\2\2\2\u00db")
        buf.write("\u00dd\3\2\2\2\u00dc\u00d8\3\2\2\2\u00dc\u00db\3\2\2\2")
        buf.write("\u00dd\'\3\2\2\2\u00de\u00df\7(\2\2\u00df\u00e0\5*\26")
        buf.write("\2\u00e0\u00e1\5(\25\2\u00e1\u00e4\3\2\2\2\u00e2\u00e4")
        buf.write("\3\2\2\2\u00e3\u00de\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4")
        buf.write(")\3\2\2\2\u00e5\u00e8\5\n\6\2\u00e6\u00e8\5\20\t\2\u00e7")
        buf.write("\u00e5\3\2\2\2\u00e7\u00e6\3\2\2\2\u00e8+\3\2\2\2\u00e9")
        buf.write("\u00ea\7)\2\2\u00ea\u00ed\5,\27\2\u00eb\u00ed\3\2\2\2")
        buf.write("\u00ec\u00e9\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed-\3\2\2")
        buf.write("\2\u00ee\u00f1\5L\'\2\u00ef\u00f1\5X-\2\u00f0\u00ee\3")
        buf.write("\2\2\2\u00f0\u00ef\3\2\2\2\u00f1/\3\2\2\2\u00f2\u00fc")
        buf.write("\5\66\34\2\u00f3\u00fc\58\35\2\u00f4\u00fc\5> \2\u00f5")
        buf.write("\u00fc\5F$\2\u00f6\u00fc\5H%\2\u00f7\u00fc\5J&\2\u00f8")
        buf.write("\u00fc\5L\'\2\u00f9\u00fc\5N(\2\u00fa\u00fc\5X-\2\u00fb")
        buf.write("\u00f2\3\2\2\2\u00fb\u00f3\3\2\2\2\u00fb\u00f4\3\2\2\2")
        buf.write("\u00fb\u00f5\3\2\2\2\u00fb\u00f6\3\2\2\2\u00fb\u00f7\3")
        buf.write("\2\2\2\u00fb\u00f8\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fa")
        buf.write("\3\2\2\2\u00fc\61\3\2\2\2\u00fd\u00fe\5\60\31\2\u00fe")
        buf.write("\u00ff\5\64\33\2\u00ff\u0102\3\2\2\2\u0100\u0102\3\2\2")
        buf.write("\2\u0101\u00fd\3\2\2\2\u0101\u0100\3\2\2\2\u0102\63\3")
        buf.write("\2\2\2\u0103\u0104\5Z.\2\u0104\u0105\5\60\31\2\u0105\u0106")
        buf.write("\5\64\33\2\u0106\u0109\3\2\2\2\u0107\u0109\3\2\2\2\u0108")
        buf.write("\u0103\3\2\2\2\u0108\u0107\3\2\2\2\u0109\65\3\2\2\2\u010a")
        buf.write("\u010b\5\b\5\2\u010b\67\3\2\2\2\u010c\u010d\5:\36\2\u010d")
        buf.write("\u010e\5<\37\2\u010e\u010f\7\"\2\2\u010f\u0110\5^\60\2")
        buf.write("\u01109\3\2\2\2\u0111\u0114\5\22\n\2\u0112\u0114\3\2\2")
        buf.write("\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114;\3\2")
        buf.write("\2\2\u0115\u0118\7\3\2\2\u0116\u0118\5\24\13\2\u0117\u0115")
        buf.write("\3\2\2\2\u0117\u0116\3\2\2\2\u0118=\3\2\2\2\u0119\u011a")
        buf.write("\5@!\2\u011a\u011b\5Z.\2\u011b\u011c\5B\"\2\u011c\u011d")
        buf.write("\5Z.\2\u011d\u011e\5D#\2\u011e?\3\2\2\2\u011f\u0120\7")
        buf.write("\23\2\2\u0120\u0121\7$\2\2\u0121\u0122\5`\61\2\u0122\u0123")
        buf.write("\7%\2\2\u0123\u0124\5\\/\2\u0124\u0125\5\60\31\2\u0125")
        buf.write("A\3\2\2\2\u0126\u0127\7\25\2\2\u0127\u0128\7$\2\2\u0128")
        buf.write("\u0129\5`\61\2\u0129\u012a\7%\2\2\u012a\u012b\5\\/\2\u012b")
        buf.write("\u012c\5\60\31\2\u012c\u012d\5Z.\2\u012d\u012e\5B\"\2")
        buf.write("\u012e\u0131\3\2\2\2\u012f\u0131\3\2\2\2\u0130\u0126\3")
        buf.write("\2\2\2\u0130\u012f\3\2\2\2\u0131C\3\2\2\2\u0132\u0133")
        buf.write("\7\24\2\2\u0133\u0134\5\\/\2\u0134\u0135\5\60\31\2\u0135")
        buf.write("\u0138\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0132\3\2\2\2")
        buf.write("\u0137\u0136\3\2\2\2\u0138E\3\2\2\2\u0139\u013a\7\16\2")
        buf.write("\2\u013a\u013b\7\3\2\2\u013b\u013c\7\17\2\2\u013c\u013d")
        buf.write("\5`\61\2\u013d\u013e\7\20\2\2\u013e\u013f\5^\60\2\u013f")
        buf.write("\u0140\5\\/\2\u0140\u0141\5\60\31\2\u0141G\3\2\2\2\u0142")
        buf.write("\u0143\7\21\2\2\u0143I\3\2\2\2\u0144\u0145\7\22\2\2\u0145")
        buf.write("K\3\2\2\2\u0146\u0147\7\n\2\2\u0147\u0148\5^\60\2\u0148")
        buf.write("M\3\2\2\2\u0149\u014a\7\3\2\2\u014a\u014b\5P)\2\u014b")
        buf.write("O\3\2\2\2\u014c\u014d\7$\2\2\u014d\u014e\5R*\2\u014e\u014f")
        buf.write("\7%\2\2\u014fQ\3\2\2\2\u0150\u0151\5V,\2\u0151\u0152\5")
        buf.write("T+\2\u0152\u0155\3\2\2\2\u0153\u0155\3\2\2\2\u0154\u0150")
        buf.write("\3\2\2\2\u0154\u0153\3\2\2\2\u0155S\3\2\2\2\u0156\u0157")
        buf.write("\7(\2\2\u0157\u0158\5V,\2\u0158\u0159\5T+\2\u0159\u015c")
        buf.write("\3\2\2\2\u015a\u015c\3\2\2\2\u015b\u0156\3\2\2\2\u015b")
        buf.write("\u015a\3\2\2\2\u015cU\3\2\2\2\u015d\u015e\5^\60\2\u015e")
        buf.write("W\3\2\2\2\u015f\u0160\7\26\2\2\u0160\u0161\5Z.\2\u0161")
        buf.write("\u0162\5\62\32\2\u0162\u0163\5Z.\2\u0163\u0164\7\27\2")
        buf.write("\2\u0164Y\3\2\2\2\u0165\u0166\7)\2\2\u0166\u0169\5Z.\2")
        buf.write("\u0167\u0169\7)\2\2\u0168\u0165\3\2\2\2\u0168\u0167\3")
        buf.write("\2\2\2\u0169[\3\2\2\2\u016a\u016b\7)\2\2\u016b\u016e\5")
        buf.write("\\/\2\u016c\u016e\3\2\2\2\u016d\u016a\3\2\2\2\u016d\u016c")
        buf.write("\3\2\2\2\u016e]\3\2\2\2\u016f\u0173\5`\61\2\u0170\u0173")
        buf.write("\5j\66\2\u0171\u0173\5t;\2\u0172\u016f\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0171\3\2\2\2\u0173_\3\2\2\2\u0174\u0175")
        buf.write("\5b\62\2\u0175a\3\2\2\2\u0176\u0177\b\62\1\2\u0177\u0178")
        buf.write("\5d\63\2\u0178\u0181\3\2\2\2\u0179\u017a\f\5\2\2\u017a")
        buf.write("\u017b\7\31\2\2\u017b\u0180\5b\62\6\u017c\u017d\f\4\2")
        buf.write("\2\u017d\u017e\7\32\2\2\u017e\u0180\5b\62\5\u017f\u0179")
        buf.write("\3\2\2\2\u017f\u017c\3\2\2\2\u0180\u0183\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182c\3\2\2\2\u0183")
        buf.write("\u0181\3\2\2\2\u0184\u0185\7\30\2\2\u0185\u0188\5d\63")
        buf.write("\2\u0186\u0188\5f\64\2\u0187\u0184\3\2\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188e\3\2\2\2\u0189\u018a\7$\2\2\u018a\u018b")
        buf.write("\5`\61\2\u018b\u018c\7%\2\2\u018c\u0193\3\2\2\2\u018d")
        buf.write("\u0193\7\3\2\2\u018e\u0193\5h\65\2\u018f\u0193\5\24\13")
        buf.write("\2\u0190\u0193\5\34\17\2\u0191\u0193\5N(\2\u0192\u0189")
        buf.write("\3\2\2\2\u0192\u018d\3\2\2\2\u0192\u018e\3\2\2\2\u0192")
        buf.write("\u018f\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2")
        buf.write("\u0193g\3\2\2\2\u0194\u0195\t\3\2\2\u0195i\3\2\2\2\u0196")
        buf.write("\u0199\5p9\2\u0197\u0199\5l\67\2\u0198\u0196\3\2\2\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199k\3\2\2\2\u019a\u019b\5r:\2\u019b")
        buf.write("\u019c\7#\2\2\u019c\u019d\5r:\2\u019d\u019e\5n8\2\u019e")
        buf.write("m\3\2\2\2\u019f\u01a0\7#\2\2\u01a0\u01a1\5r:\2\u01a1\u01a2")
        buf.write("\5n8\2\u01a2\u01a5\3\2\2\2\u01a3\u01a5\3\2\2\2\u01a4\u019f")
        buf.write("\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5o\3\2\2\2\u01a6\u01a7")
        buf.write("\5r:\2\u01a7\u01a8\7!\2\2\u01a8\u01a9\5r:\2\u01a9q\3\2")
        buf.write("\2\2\u01aa\u01ab\7$\2\2\u01ab\u01ac\5j\66\2\u01ac\u01ad")
        buf.write("\7%\2\2\u01ad\u01b4\3\2\2\2\u01ae\u01b4\7\3\2\2\u01af")
        buf.write("\u01b4\7+\2\2\u01b0\u01b4\5\24\13\2\u01b1\u01b4\5\34\17")
        buf.write("\2\u01b2\u01b4\5N(\2\u01b3\u01aa\3\2\2\2\u01b3\u01ae\3")
        buf.write("\2\2\2\u01b3\u01af\3\2\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4s\3\2\2\2\u01b5\u01b6")
        buf.write("\5v<\2\u01b6u\3\2\2\2\u01b7\u01b8\b<\1\2\u01b8\u01b9\5")
        buf.write("x=\2\u01b9\u01c2\3\2\2\2\u01ba\u01bb\f\5\2\2\u01bb\u01bc")
        buf.write("\7\33\2\2\u01bc\u01c1\5v<\6\u01bd\u01be\f\4\2\2\u01be")
        buf.write("\u01bf\7\34\2\2\u01bf\u01c1\5v<\5\u01c0\u01ba\3\2\2\2")
        buf.write("\u01c0\u01bd\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0\3")
        buf.write("\2\2\2\u01c2\u01c3\3\2\2\2\u01c3w\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c5\u01c6\b=\1\2\u01c6\u01c7\5z>\2\u01c7\u01d3")
        buf.write("\3\2\2\2\u01c8\u01c9\f\6\2\2\u01c9\u01ca\7\35\2\2\u01ca")
        buf.write("\u01d2\5x=\7\u01cb\u01cc\f\5\2\2\u01cc\u01cd\7\36\2\2")
        buf.write("\u01cd\u01d2\5x=\6\u01ce\u01cf\f\4\2\2\u01cf\u01d0\7\37")
        buf.write("\2\2\u01d0\u01d2\5x=\5\u01d1\u01c8\3\2\2\2\u01d1\u01cb")
        buf.write("\3\2\2\2\u01d1\u01ce\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4y\3\2\2\2\u01d5")
        buf.write("\u01d3\3\2\2\2\u01d6\u01d7\7\34\2\2\u01d7\u01da\5z>\2")
        buf.write("\u01d8\u01da\5|?\2\u01d9\u01d6\3\2\2\2\u01d9\u01d8\3\2")
        buf.write("\2\2\u01da{\3\2\2\2\u01db\u01dc\7$\2\2\u01dc\u01dd\5t")
        buf.write(";\2\u01dd\u01de\7%\2\2\u01de\u01e5\3\2\2\2\u01df\u01e5")
        buf.write("\7\3\2\2\u01e0\u01e5\7*\2\2\u01e1\u01e5\5\24\13\2\u01e2")
        buf.write("\u01e5\5\34\17\2\u01e3\u01e5\5N(\2\u01e4\u01db\3\2\2\2")
        buf.write("\u01e4\u01df\3\2\2\2\u01e4\u01e0\3\2\2\2\u01e4\u01e1\3")
        buf.write("\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5}")
        buf.write("\3\2\2\2\'\u008c\u0091\u0097\u00b4\u00bb\u00c5\u00cc\u00dc")
        buf.write("\u00e3\u00e7\u00ec\u00f0\u00fb\u0101\u0108\u0113\u0117")
        buf.write("\u0130\u0137\u0154\u015b\u0168\u016d\u0172\u017f\u0181")
        buf.write("\u0187\u0192\u0198\u01a4\u01b3\u01c0\u01c2\u01d1\u01d3")
        buf.write("\u01d9\u01e4")
        return buf.getvalue()


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
                     "'...'", "'('", "')'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "MAIN", "TRUE", "FALSE", 
                      "KWNUMBER", "KWBOOL", "KWSTRING", "RETURN", "VAR", 
                      "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "COMPARENUM", "COMPARESTR", "ASSIGN", "CONCAT", "OPENPAREN", 
                      "CLOSEPAREN", "OPENSQBRACKET", "CLOSESQBRACKET", "COMMA", 
                      "NEWLINE", "NUMBER", "STRING", "CMT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
    RULE_array_tail = 10
    RULE_list_expr_num = 11
    RULE_list_expr_num_tail = 12
    RULE_array_val = 13
    RULE_list_expr = 14
    RULE_list_expr_tail = 15
    RULE_func_decls = 16
    RULE_func_param = 17
    RULE_list_param = 18
    RULE_list_param_tail = 19
    RULE_params = 20
    RULE_func_sepa = 21
    RULE_func_body = 22
    RULE_stmt = 23
    RULE_list_stmt = 24
    RULE_list_stmt_tail = 25
    RULE_stmt_vari_decl = 26
    RULE_stmt_assi = 27
    RULE_assi_type = 28
    RULE_assi_id = 29
    RULE_stmt_cond = 30
    RULE_stmt_if = 31
    RULE_stmt_elif = 32
    RULE_stmt_else = 33
    RULE_stmt_for = 34
    RULE_stmt_break = 35
    RULE_stmt_continue = 36
    RULE_stmt_return = 37
    RULE_stmt_func_call = 38
    RULE_sfc_param = 39
    RULE_sfc_list_args = 40
    RULE_sfc_list_args_tail = 41
    RULE_sfc_args = 42
    RULE_stmt_block = 43
    RULE_stmt_sepa_nonnull = 44
    RULE_stmt_sepa_null = 45
    RULE_expr = 46
    RULE_expr_cond = 47
    RULE_expr_cond_andor = 48
    RULE_expr_cond_not = 49
    RULE_expr_cond_other = 50
    RULE_boolval = 51
    RULE_expr_string = 52
    RULE_expr_string_concat = 53
    RULE_e_s_c_tail = 54
    RULE_expr_string_compare = 55
    RULE_stringval = 56
    RULE_expr_num = 57
    RULE_e_n_addsub = 58
    RULE_e_n_muldivmod = 59
    RULE_e_n_nega = 60
    RULE_e_n_other = 61

    ruleNames =  [ "program", "decls_stmt", "decls_stmt_tail", "vari_decls", 
                   "vari_decls_type1", "vari_decls_type2", "vari_decls_type3", 
                   "vari_decls_type4", "vari_type", "array", "array_tail", 
                   "list_expr_num", "list_expr_num_tail", "array_val", "list_expr", 
                   "list_expr_tail", "func_decls", "func_param", "list_param", 
                   "list_param_tail", "params", "func_sepa", "func_body", 
                   "stmt", "list_stmt", "list_stmt_tail", "stmt_vari_decl", 
                   "stmt_assi", "assi_type", "assi_id", "stmt_cond", "stmt_if", 
                   "stmt_elif", "stmt_else", "stmt_for", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_func_call", "sfc_param", "sfc_list_args", 
                   "sfc_list_args_tail", "sfc_args", "stmt_block", "stmt_sepa_nonnull", 
                   "stmt_sepa_null", "expr", "expr_cond", "expr_cond_andor", 
                   "expr_cond_not", "expr_cond_other", "boolval", "expr_string", 
                   "expr_string_concat", "e_s_c_tail", "expr_string_compare", 
                   "stringval", "expr_num", "e_n_addsub", "e_n_muldivmod", 
                   "e_n_nega", "e_n_other" ]

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
    UNCLOSE_STRING=44
    ILLEGAL_ESCAPE=45
    ERROR_CHAR=46

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

        def decls_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_stmtContext,0)


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
            self.state = 124
            self.decls_stmt()
            self.state = 125
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls_stmt" ):
                return visitor.visitDecls_stmt(self)
            else:
                return visitor.visitChildren(self)




    def decls_stmt(self):

        localctx = ZCodeParser.Decls_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls_stmt)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.stmt()
                self.state = 128
                self.decls_stmt_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.vari_decls()
                self.state = 131
                self.decls_stmt_tail()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.func_decls()
                self.state = 134
                self.decls_stmt_tail()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls_stmt_tail" ):
                return visitor.visitDecls_stmt_tail(self)
            else:
                return visitor.visitChildren(self)




    def decls_stmt_tail(self):

        localctx = ZCodeParser.Decls_stmt_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decls_stmt_tail)
        try:
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(ZCodeParser.NEWLINE)
                self.state = 141
                self.decls_stmt()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls" ):
                return visitor.visitVari_decls(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls(self):

        localctx = ZCodeParser.Vari_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vari_decls)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.vari_decls_type1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.vari_decls_type2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.vari_decls_type3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_type1" ):
                return visitor.visitVari_decls_type1(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_type1(self):

        localctx = ZCodeParser.Vari_decls_type1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vari_decls_type1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.vari_type()
            self.state = 152
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_type2" ):
                return visitor.visitVari_decls_type2(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_type2(self):

        localctx = ZCodeParser.Vari_decls_type2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vari_decls_type2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ZCodeParser.VAR)
            self.state = 155
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 156
            self.match(ZCodeParser.ASSIGN)
            self.state = 157
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_type3" ):
                return visitor.visitVari_decls_type3(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_type3(self):

        localctx = ZCodeParser.Vari_decls_type3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vari_decls_type3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ZCodeParser.DYNAMIC)
            self.state = 160
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_type4" ):
                return visitor.visitVari_decls_type4(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_type4(self):

        localctx = ZCodeParser.Vari_decls_type4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vari_decls_type4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.vari_type()
            self.state = 163
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_type" ):
                return visitor.visitVari_type(self)
            else:
                return visitor.visitChildren(self)




    def vari_type(self):

        localctx = ZCodeParser.Vari_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vari_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 168
            self.array_tail()
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

        def list_expr_num(self):
            return self.getTypedRuleContext(ZCodeParser.List_expr_numContext,0)


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
        self.enterRule(localctx, 20, self.RULE_array_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 171
            self.list_expr_num()
            self.state = 172
            self.match(ZCodeParser.CLOSESQBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expr_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_num(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_numContext,0)


        def list_expr_num_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_expr_num_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expr_num

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr_num" ):
                return visitor.visitList_expr_num(self)
            else:
                return visitor.visitChildren(self)




    def list_expr_num(self):

        localctx = ZCodeParser.List_expr_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_expr_num)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.expr_num()
                self.state = 175
                self.list_expr_num_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.expr_num()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expr_num_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr_num(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_numContext,0)


        def list_expr_num_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_expr_num_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expr_num_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr_num_tail" ):
                return visitor.visitList_expr_num_tail(self)
            else:
                return visitor.visitChildren(self)




    def list_expr_num_tail(self):

        localctx = ZCodeParser.List_expr_num_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_list_expr_num_tail)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(ZCodeParser.COMMA)
                self.state = 181
                self.expr_num()
                self.state = 182
                self.list_expr_num_tail()
                pass
            elif token in [ZCodeParser.CLOSESQBRACKET]:
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


    class Array_valContext(ParserRuleContext):
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
            return ZCodeParser.RULE_array_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_val" ):
                return visitor.visitArray_val(self)
            else:
                return visitor.visitChildren(self)




    def array_val(self):

        localctx = ZCodeParser.Array_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_array_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 188
            self.list_expr()
            self.state = 189
            self.match(ZCodeParser.CLOSESQBRACKET)
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


        def list_expr_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_expr_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = ZCodeParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_expr)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.expr()
                self.state = 192
                self.list_expr_tail()
                pass
            elif token in [ZCodeParser.CLOSESQBRACKET]:
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


    class List_expr_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def list_expr_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_expr_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_expr_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr_tail" ):
                return visitor.visitList_expr_tail(self)
            else:
                return visitor.visitChildren(self)




    def list_expr_tail(self):

        localctx = ZCodeParser.List_expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_expr_tail)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(ZCodeParser.COMMA)
                self.state = 198
                self.expr()
                self.state = 199
                self.list_expr_tail()
                pass
            elif token in [ZCodeParser.CLOSESQBRACKET]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decls" ):
                return visitor.visitFunc_decls(self)
            else:
                return visitor.visitChildren(self)




    def func_decls(self):

        localctx = ZCodeParser.Func_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ZCodeParser.FUNC)
            self.state = 205
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 206
            self.func_param()
            self.state = 207
            self.func_sepa()
            self.state = 208
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
        self.enterRule(localctx, 34, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ZCodeParser.OPENPAREN)
            self.state = 211
            self.list_param()
            self.state = 212
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
        self.enterRule(localctx, 36, self.RULE_list_param)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.params()
                self.state = 215
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
        self.enterRule(localctx, 38, self.RULE_list_param_tail)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(ZCodeParser.COMMA)
                self.state = 221
                self.params()
                self.state = 222
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

        def vari_decls_type1(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type1Context,0)


        def vari_decls_type4(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type4Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = ZCodeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_params)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.vari_decls_type1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_sepa" ):
                return visitor.visitFunc_sepa(self)
            else:
                return visitor.visitChildren(self)




    def func_sepa(self):

        localctx = ZCodeParser.Func_sepaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_func_sepa)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(ZCodeParser.NEWLINE)
                self.state = 232
                self.func_sepa()
                pass
            elif token in [ZCodeParser.RETURN, ZCodeParser.BEGIN]:
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
        self.enterRule(localctx, 44, self.RULE_func_body)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.stmt_return()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
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
        self.enterRule(localctx, 46, self.RULE_stmt)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.stmt_vari_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.stmt_assi()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.stmt_cond()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.stmt_for()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.stmt_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.stmt_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 246
                self.stmt_return()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 247
                self.stmt_func_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 248
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


        def list_stmt_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmt_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmt" ):
                return visitor.visitList_stmt(self)
            else:
                return visitor.visitChildren(self)




    def list_stmt(self):

        localctx = ZCodeParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_list_stmt)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER, ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.stmt()
                self.state = 252
                self.list_stmt_tail()
                pass
            elif token in [ZCodeParser.NEWLINE]:
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


    class List_stmt_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def list_stmt_tail(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmt_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_stmt_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_stmt_tail" ):
                return visitor.visitList_stmt_tail(self)
            else:
                return visitor.visitChildren(self)




    def list_stmt_tail(self):

        localctx = ZCodeParser.List_stmt_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_list_stmt_tail)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.stmt_sepa_nonnull()
                self.state = 258
                self.stmt()
                self.state = 259
                self.list_stmt_tail()
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
        self.enterRule(localctx, 52, self.RULE_stmt_vari_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assi" ):
                return visitor.visitStmt_assi(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assi(self):

        localctx = ZCodeParser.Stmt_assiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_assi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.assi_type()
            self.state = 267
            self.assi_id()
            self.state = 268
            self.match(ZCodeParser.ASSIGN)
            self.state = 269
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssi_type" ):
                return visitor.visitAssi_type(self)
            else:
                return visitor.visitChildren(self)




    def assi_type(self):

        localctx = ZCodeParser.Assi_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assi_type)
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.vari_type()
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssi_id" ):
                return visitor.visitAssi_id(self)
            else:
                return visitor.visitChildren(self)




    def assi_id(self):

        localctx = ZCodeParser.Assi_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assi_id)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
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


        def stmt_sepa_nonnull(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Stmt_sepa_nonnullContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,i)


        def stmt_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_elifContext,0)


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
        self.enterRule(localctx, 60, self.RULE_stmt_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.stmt_if()
            self.state = 280
            self.stmt_sepa_nonnull()
            self.state = 281
            self.stmt_elif()
            self.state = 282
            self.stmt_sepa_nonnull()
            self.state = 283
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
        self.enterRule(localctx, 62, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(ZCodeParser.IF)
            self.state = 286
            self.match(ZCodeParser.OPENPAREN)
            self.state = 287
            self.expr_cond()
            self.state = 288
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 289
            self.stmt_sepa_null()
            self.state = 290
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

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def stmt_sepa_null(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nullContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


        def stmt_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_elifContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_elif

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_elif" ):
                return visitor.visitStmt_elif(self)
            else:
                return visitor.visitChildren(self)




    def stmt_elif(self):

        localctx = ZCodeParser.Stmt_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stmt_elif)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(ZCodeParser.ELIF)
                self.state = 293
                self.match(ZCodeParser.OPENPAREN)
                self.state = 294
                self.expr_cond()
                self.state = 295
                self.match(ZCodeParser.CLOSEPAREN)
                self.state = 296
                self.stmt_sepa_null()
                self.state = 297
                self.stmt()
                self.state = 298
                self.stmt_sepa_nonnull()
                self.state = 299
                self.stmt_elif()
                pass
            elif token in [ZCodeParser.NEWLINE]:
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
        self.enterRule(localctx, 66, self.RULE_stmt_else)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(ZCodeParser.ELSE)
                self.state = 305
                self.stmt_sepa_null()
                self.state = 306
                self.stmt()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NEWLINE]:
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

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


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
        self.enterRule(localctx, 68, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ZCodeParser.FOR)
            self.state = 312
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 313
            self.match(ZCodeParser.UNTIL)
            self.state = 314
            self.expr_cond()
            self.state = 315
            self.match(ZCodeParser.BY)
            self.state = 316
            self.expr()
            self.state = 317
            self.stmt_sepa_null()
            self.state = 318
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
        self.enterRule(localctx, 70, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
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
        self.enterRule(localctx, 72, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
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
        self.enterRule(localctx, 74, self.RULE_stmt_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(ZCodeParser.RETURN)
            self.state = 325
            self.expr()
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

        def sfc_param(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_paramContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_call" ):
                return visitor.visitStmt_func_call(self)
            else:
                return visitor.visitChildren(self)




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 328
            self.sfc_param()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sfc_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def sfc_list_args(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_list_argsContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSfc_param" ):
                return visitor.visitSfc_param(self)
            else:
                return visitor.visitChildren(self)




    def sfc_param(self):

        localctx = ZCodeParser.Sfc_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_sfc_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(ZCodeParser.OPENPAREN)
            self.state = 331
            self.sfc_list_args()
            self.state = 332
            self.match(ZCodeParser.CLOSEPAREN)
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

        def sfc_args(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_argsContext,0)


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
        self.enterRule(localctx, 80, self.RULE_sfc_list_args)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.sfc_args()
                self.state = 335
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

        def sfc_args(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_argsContext,0)


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
        self.enterRule(localctx, 82, self.RULE_sfc_list_args_tail)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(ZCodeParser.COMMA)
                self.state = 341
                self.sfc_args()
                self.state = 342
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


    class Sfc_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSfc_args" ):
                return visitor.visitSfc_args(self)
            else:
                return visitor.visitChildren(self)




    def sfc_args(self):

        localctx = ZCodeParser.Sfc_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_sfc_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.expr()
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

        def stmt_sepa_nonnull(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Stmt_sepa_nonnullContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,i)


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
        self.enterRule(localctx, 86, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(ZCodeParser.BEGIN)
            self.state = 350
            self.stmt_sepa_nonnull()
            self.state = 351
            self.list_stmt()
            self.state = 352
            self.stmt_sepa_nonnull()
            self.state = 353
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
        self.enterRule(localctx, 88, self.RULE_stmt_sepa_nonnull)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(ZCodeParser.NEWLINE)
                self.state = 356
                self.stmt_sepa_nonnull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
                self.match(ZCodeParser.NEWLINE)
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
        self.enterRule(localctx, 90, self.RULE_stmt_sepa_null)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(ZCodeParser.NEWLINE)
                self.state = 361
                self.stmt_sepa_null()
                pass
            elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN]:
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

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def expr_num(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_numContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr)
        try:
            self.state = 368
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.expr_cond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.expr_string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 367
                self.expr_num()
                pass


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

        def expr_cond_andor(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_andorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cond" ):
                return visitor.visitExpr_cond(self)
            else:
                return visitor.visitChildren(self)




    def expr_cond(self):

        localctx = ZCodeParser.Expr_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.expr_cond_andor(0)
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

        def expr_cond_not(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_notContext,0)


        def expr_cond_andor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_cond_andorContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_cond_andorContext,i)


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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr_cond_andor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.expr_cond_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 381
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 375
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 376
                        self.match(ZCodeParser.AND)
                        self.state = 377
                        self.expr_cond_andor(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 378
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 379
                        self.match(ZCodeParser.OR)
                        self.state = 380
                        self.expr_cond_andor(3)
                        pass

             
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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


        def expr_cond_other(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_otherContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cond_not" ):
                return visitor.visitExpr_cond_not(self)
            else:
                return visitor.visitChildren(self)




    def expr_cond_not(self):

        localctx = ZCodeParser.Expr_cond_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr_cond_not)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.match(ZCodeParser.NOT)
                self.state = 387
                self.expr_cond_not()
                pass
            elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.expr_cond_other()
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


    class Expr_cond_otherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def boolval(self):
            return self.getTypedRuleContext(ZCodeParser.BoolvalContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond_other

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cond_other" ):
                return visitor.visitExpr_cond_other(self)
            else:
                return visitor.visitChildren(self)




    def expr_cond_other(self):

        localctx = ZCodeParser.Expr_cond_otherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr_cond_other)
        try:
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.match(ZCodeParser.OPENPAREN)
                self.state = 392
                self.expr_cond()
                self.state = 393
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 395
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 396
                self.boolval()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 397
                self.array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 398
                self.array_val()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 399
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
        self.enterRule(localctx, 102, self.RULE_boolval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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


    class Expr_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_string_compare(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_string_compareContext,0)


        def expr_string_concat(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_string_concatContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_string" ):
                return visitor.visitExpr_string(self)
            else:
                return visitor.visitChildren(self)




    def expr_string(self):

        localctx = ZCodeParser.Expr_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expr_string)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.expr_string_compare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.expr_string_concat()
                pass


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

        def stringval(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StringvalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StringvalContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def e_s_c_tail(self):
            return self.getTypedRuleContext(ZCodeParser.E_s_c_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string_concat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_string_concat" ):
                return visitor.visitExpr_string_concat(self)
            else:
                return visitor.visitChildren(self)




    def expr_string_concat(self):

        localctx = ZCodeParser.Expr_string_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr_string_concat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.stringval()
            self.state = 409
            self.match(ZCodeParser.CONCAT)
            self.state = 410
            self.stringval()
            self.state = 411
            self.e_s_c_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class E_s_c_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def stringval(self):
            return self.getTypedRuleContext(ZCodeParser.StringvalContext,0)


        def e_s_c_tail(self):
            return self.getTypedRuleContext(ZCodeParser.E_s_c_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_e_s_c_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_s_c_tail" ):
                return visitor.visitE_s_c_tail(self)
            else:
                return visitor.visitChildren(self)




    def e_s_c_tail(self):

        localctx = ZCodeParser.E_s_c_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_e_s_c_tail)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.CONCAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(ZCodeParser.CONCAT)
                self.state = 414
                self.stringval()
                self.state = 415
                self.e_s_c_tail()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.IDENTIFIER, ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.CLOSEPAREN, ZCodeParser.CLOSESQBRACKET, ZCodeParser.COMMA, ZCodeParser.NEWLINE]:
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


    class Expr_string_compareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringval(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StringvalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StringvalContext,i)


        def COMPARESTR(self):
            return self.getToken(ZCodeParser.COMPARESTR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string_compare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_string_compare" ):
                return visitor.visitExpr_string_compare(self)
            else:
                return visitor.visitChildren(self)




    def expr_string_compare(self):

        localctx = ZCodeParser.Expr_string_compareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expr_string_compare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.stringval()
            self.state = 421
            self.match(ZCodeParser.COMPARESTR)
            self.state = 422
            self.stringval()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stringval

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringval" ):
                return visitor.visitStringval(self)
            else:
                return visitor.visitChildren(self)




    def stringval(self):

        localctx = ZCodeParser.StringvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_stringval)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(ZCodeParser.OPENPAREN)
                self.state = 425
                self.expr_string()
                self.state = 426
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 431
                self.array_val()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 432
                self.stmt_func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def e_n_addsub(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_addsubContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_num

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_num" ):
                return visitor.visitExpr_num(self)
            else:
                return visitor.visitChildren(self)




    def expr_num(self):

        localctx = ZCodeParser.Expr_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_expr_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.e_n_addsub(0)
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


        def e_n_addsub(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.E_n_addsubContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.E_n_addsubContext,i)


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
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_e_n_addsub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.e_n_muldivmod(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 446
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 440
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 441
                        self.match(ZCodeParser.ADD)
                        self.state = 442
                        self.e_n_addsub(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 443
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 444
                        self.match(ZCodeParser.SUB)
                        self.state = 445
                        self.e_n_addsub(3)
                        pass

             
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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

        def e_n_nega(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_negaContext,0)


        def e_n_muldivmod(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.E_n_muldivmodContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.E_n_muldivmodContext,i)


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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_e_n_muldivmod, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.e_n_nega()
            self._ctx.stop = self._input.LT(-1)
            self.state = 465
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 463
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 454
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 455
                        self.match(ZCodeParser.MUL)
                        self.state = 456
                        self.e_n_muldivmod(5)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 457
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 458
                        self.match(ZCodeParser.DIV)
                        self.state = 459
                        self.e_n_muldivmod(4)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 460
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 461
                        self.match(ZCodeParser.MOD)
                        self.state = 462
                        self.e_n_muldivmod(3)
                        pass

             
                self.state = 467
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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


        def e_n_other(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_otherContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_e_n_nega

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_n_nega" ):
                return visitor.visitE_n_nega(self)
            else:
                return visitor.visitChildren(self)




    def e_n_nega(self):

        localctx = ZCodeParser.E_n_negaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_e_n_nega)
        try:
            self.state = 471
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.match(ZCodeParser.SUB)
                self.state = 469
                self.e_n_nega()
                pass
            elif token in [ZCodeParser.IDENTIFIER, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.e_n_other()
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


    class E_n_otherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_num(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_numContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_e_n_other

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_n_other" ):
                return visitor.visitE_n_other(self)
            else:
                return visitor.visitChildren(self)




    def e_n_other(self):

        localctx = ZCodeParser.E_n_otherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_e_n_other)
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(ZCodeParser.OPENPAREN)
                self.state = 474
                self.expr_num()
                self.state = 475
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 478
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 479
                self.array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 480
                self.array_val()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 481
                self.stmt_func_call()
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
        self._predicates[48] = self.expr_cond_andor_sempred
        self._predicates[58] = self.e_n_addsub_sempred
        self._predicates[59] = self.e_n_muldivmod_sempred
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
         




