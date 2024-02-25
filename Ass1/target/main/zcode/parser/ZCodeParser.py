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
        buf.write("\u01db\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u0088\n\3\3\4\3\4\3\4\3\4\3\4\5\4\u008f\n\4")
        buf.write("\3\5\3\5\3\5\5\5\u0094\n\5\3\6\3\6\5\6\u0098\n\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u00ac\n\f\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u00b3\n\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17")
        buf.write("\u00bd\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00c4\n\20\3")
        buf.write("\21\3\21\5\21\u00c8\n\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\5\24\u00d8\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\5\25\u00df\n\25\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\5\31\u00eb\n")
        buf.write("\31\3\32\3\32\3\32\5\32\u00f0\n\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\5\33\u00fb\n\33\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u0102\n\34\3\35\3\35\3\36\3\36\5\36")
        buf.write("\u0108\n\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\5")
        buf.write("!\u0115\n!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u012d\n$\3%\3%\3%\3%\3")
        buf.write("%\5%\u0134\n%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\3)\3)\5)\u0146\n)\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\5,\u0153\n,\3-\3-\3-\3-\3-\5-\u015a\n-\3.\3.\3/\3/\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\5\61\u0169\n\61")
        buf.write("\3\62\3\62\3\62\5\62\u016e\n\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u017d")
        buf.write("\n\65\f\65\16\65\u0180\13\65\3\66\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\7\66\u018b\n\66\f\66\16\66\u018e")
        buf.write("\13\66\3\67\3\67\3\67\5\67\u0193\n\67\38\38\39\39\39\3")
        buf.write("9\39\39\39\39\39\79\u01a0\n9\f9\169\u01a3\139\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3:\7:\u01b1\n:\f:\16:\u01b4")
        buf.write("\13:\3;\3;\3;\5;\u01b9\n;\3<\3<\3=\3=\3=\3=\3=\3=\5=\u01c3")
        buf.write("\n=\3>\3>\3>\3>\3>\5>\u01ca\n>\3?\3?\3?\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\5?\u01d7\n?\3@\3@\3@\2\6hjprA\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\2\5\4\2\5\7\n\n\3\2\5\7")
        buf.write("\3\2\3\4\2\u01d0\2\u0080\3\2\2\2\4\u0087\3\2\2\2\6\u008e")
        buf.write("\3\2\2\2\b\u0093\3\2\2\2\n\u0097\3\2\2\2\f\u0099\3\2\2")
        buf.write("\2\16\u009c\3\2\2\2\20\u009e\3\2\2\2\22\u00a0\3\2\2\2")
        buf.write("\24\u00a3\3\2\2\2\26\u00ab\3\2\2\2\30\u00b2\3\2\2\2\32")
        buf.write("\u00b4\3\2\2\2\34\u00bc\3\2\2\2\36\u00c3\3\2\2\2 \u00c7")
        buf.write("\3\2\2\2\"\u00c9\3\2\2\2$\u00cf\3\2\2\2&\u00d7\3\2\2\2")
        buf.write("(\u00de\3\2\2\2*\u00e0\3\2\2\2,\u00e2\3\2\2\2.\u00e5\3")
        buf.write("\2\2\2\60\u00ea\3\2\2\2\62\u00ef\3\2\2\2\64\u00fa\3\2")
        buf.write("\2\2\66\u0101\3\2\2\28\u0103\3\2\2\2:\u0107\3\2\2\2<\u0109")
        buf.write("\3\2\2\2>\u010d\3\2\2\2@\u0114\3\2\2\2B\u0116\3\2\2\2")
        buf.write("D\u011b\3\2\2\2F\u012c\3\2\2\2H\u0133\3\2\2\2J\u0135\3")
        buf.write("\2\2\2L\u013e\3\2\2\2N\u0140\3\2\2\2P\u0145\3\2\2\2R\u0147")
        buf.write("\3\2\2\2T\u014a\3\2\2\2V\u0152\3\2\2\2X\u0159\3\2\2\2")
        buf.write("Z\u015b\3\2\2\2\\\u015d\3\2\2\2^\u0162\3\2\2\2`\u0168")
        buf.write("\3\2\2\2b\u016d\3\2\2\2d\u016f\3\2\2\2f\u0171\3\2\2\2")
        buf.write("h\u0173\3\2\2\2j\u0181\3\2\2\2l\u0192\3\2\2\2n\u0194\3")
        buf.write("\2\2\2p\u0196\3\2\2\2r\u01a4\3\2\2\2t\u01b8\3\2\2\2v\u01ba")
        buf.write("\3\2\2\2x\u01c2\3\2\2\2z\u01c9\3\2\2\2|\u01d6\3\2\2\2")
        buf.write("~\u01d8\3\2\2\2\u0080\u0081\5\4\3\2\u0081\u0082\7\2\2")
        buf.write("\3\u0082\3\3\2\2\2\u0083\u0084\5\b\5\2\u0084\u0085\5\6")
        buf.write("\4\2\u0085\u0088\3\2\2\2\u0086\u0088\3\2\2\2\u0087\u0083")
        buf.write("\3\2\2\2\u0087\u0086\3\2\2\2\u0088\5\3\2\2\2\u0089\u008a")
        buf.write("\7\'\2\2\u008a\u008b\5\b\5\2\u008b\u008c\5\6\4\2\u008c")
        buf.write("\u008f\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u0089\3\2\2\2")
        buf.write("\u008e\u008d\3\2\2\2\u008f\7\3\2\2\2\u0090\u0094\5\n\6")
        buf.write("\2\u0091\u0094\5\"\22\2\u0092\u0094\3\2\2\2\u0093\u0090")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2\u0094")
        buf.write("\t\3\2\2\2\u0095\u0098\5\f\7\2\u0096\u0098\5\16\b\2\u0097")
        buf.write("\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098\13\3\2\2\2\u0099")
        buf.write("\u009a\5\20\t\2\u009a\u009b\5 \21\2\u009b\r\3\2\2\2\u009c")
        buf.write("\u009d\5:\36\2\u009d\17\3\2\2\2\u009e\u009f\t\2\2\2\u009f")
        buf.write("\21\3\2\2\2\u00a0\u00a1\7*\2\2\u00a1\u00a2\5\24\13\2\u00a2")
        buf.write("\23\3\2\2\2\u00a3\u00a4\7$\2\2\u00a4\u00a5\5\26\f\2\u00a5")
        buf.write("\u00a6\7%\2\2\u00a6\25\3\2\2\2\u00a7\u00a8\5n8\2\u00a8")
        buf.write("\u00a9\5\30\r\2\u00a9\u00ac\3\2\2\2\u00aa\u00ac\3\2\2")
        buf.write("\2\u00ab\u00a7\3\2\2\2\u00ab\u00aa\3\2\2\2\u00ac\27\3")
        buf.write("\2\2\2\u00ad\u00ae\7&\2\2\u00ae\u00af\5n8\2\u00af\u00b0")
        buf.write("\5\30\r\2\u00b0\u00b3\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2")
        buf.write("\u00ad\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\31\3\2\2\2\u00b4")
        buf.write("\u00b5\7$\2\2\u00b5\u00b6\5\34\17\2\u00b6\u00b7\7%\2\2")
        buf.write("\u00b7\33\3\2\2\2\u00b8\u00b9\5d\63\2\u00b9\u00ba\5\36")
        buf.write("\20\2\u00ba\u00bd\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00b8")
        buf.write("\3\2\2\2\u00bc\u00bb\3\2\2\2\u00bd\35\3\2\2\2\u00be\u00bf")
        buf.write("\7&\2\2\u00bf\u00c0\5d\63\2\u00c0\u00c1\5\36\20\2\u00c1")
        buf.write("\u00c4\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00be\3\2\2\2")
        buf.write("\u00c3\u00c2\3\2\2\2\u00c4\37\3\2\2\2\u00c5\u00c8\7*\2")
        buf.write("\2\u00c6\u00c8\5\22\n\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8!\3\2\2\2\u00c9\u00ca\7\13\2\2\u00ca\u00cb")
        buf.write("\7*\2\2\u00cb\u00cc\5$\23\2\u00cc\u00cd\5\60\31\2\u00cd")
        buf.write("\u00ce\5\62\32\2\u00ce#\3\2\2\2\u00cf\u00d0\7\"\2\2\u00d0")
        buf.write("\u00d1\5&\24\2\u00d1\u00d2\7#\2\2\u00d2%\3\2\2\2\u00d3")
        buf.write("\u00d4\5*\26\2\u00d4\u00d5\5(\25\2\u00d5\u00d8\3\2\2\2")
        buf.write("\u00d6\u00d8\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d7\u00d6\3")
        buf.write("\2\2\2\u00d8\'\3\2\2\2\u00d9\u00da\7&\2\2\u00da\u00db")
        buf.write("\5*\26\2\u00db\u00dc\5(\25\2\u00dc\u00df\3\2\2\2\u00dd")
        buf.write("\u00df\3\2\2\2\u00de\u00d9\3\2\2\2\u00de\u00dd\3\2\2\2")
        buf.write("\u00df)\3\2\2\2\u00e0\u00e1\5,\27\2\u00e1+\3\2\2\2\u00e2")
        buf.write("\u00e3\5.\30\2\u00e3\u00e4\5 \21\2\u00e4-\3\2\2\2\u00e5")
        buf.write("\u00e6\t\3\2\2\u00e6/\3\2\2\2\u00e7\u00e8\7\'\2\2\u00e8")
        buf.write("\u00eb\5\60\31\2\u00e9\u00eb\3\2\2\2\u00ea\u00e7\3\2\2")
        buf.write("\2\u00ea\u00e9\3\2\2\2\u00eb\61\3\2\2\2\u00ec\u00f0\5")
        buf.write("P)\2\u00ed\u00f0\5\\/\2\u00ee\u00f0\3\2\2\2\u00ef\u00ec")
        buf.write("\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\63\3\2\2\2\u00f1\u00fb\58\35\2\u00f2\u00fb\5:\36\2\u00f3")
        buf.write("\u00fb\5B\"\2\u00f4\u00fb\5J&\2\u00f5\u00fb\5L\'\2\u00f6")
        buf.write("\u00fb\5N(\2\u00f7\u00fb\5P)\2\u00f8\u00fb\5R*\2\u00f9")
        buf.write("\u00fb\5\\/\2\u00fa\u00f1\3\2\2\2\u00fa\u00f2\3\2\2\2")
        buf.write("\u00fa\u00f3\3\2\2\2\u00fa\u00f4\3\2\2\2\u00fa\u00f5\3")
        buf.write("\2\2\2\u00fa\u00f6\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\65\3\2\2\2\u00fc\u00fd")
        buf.write("\5^\60\2\u00fd\u00fe\5\64\33\2\u00fe\u00ff\5\66\34\2\u00ff")
        buf.write("\u0102\3\2\2\2\u0100\u0102\3\2\2\2\u0101\u00fc\3\2\2\2")
        buf.write("\u0101\u0100\3\2\2\2\u0102\67\3\2\2\2\u0103\u0104\5\n")
        buf.write("\6\2\u01049\3\2\2\2\u0105\u0108\5<\37\2\u0106\u0108\5")
        buf.write("> \2\u0107\u0105\3\2\2\2\u0107\u0106\3\2\2\2\u0108;\3")
        buf.write("\2\2\2\u0109\u010a\5 \21\2\u010a\u010b\7 \2\2\u010b\u010c")
        buf.write("\5d\63\2\u010c=\3\2\2\2\u010d\u010e\5@!\2\u010e\u010f")
        buf.write("\5 \21\2\u010f\u0110\7 \2\2\u0110\u0111\5d\63\2\u0111")
        buf.write("?\3\2\2\2\u0112\u0115\5\20\t\2\u0113\u0115\7\t\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0115A\3\2\2\2\u0116")
        buf.write("\u0117\5D#\2\u0117\u0118\5F$\2\u0118\u0119\5^\60\2\u0119")
        buf.write("\u011a\5H%\2\u011aC\3\2\2\2\u011b\u011c\7\21\2\2\u011c")
        buf.write("\u011d\7\"\2\2\u011d\u011e\5f\64\2\u011e\u011f\7#\2\2")
        buf.write("\u011f\u0120\5b\62\2\u0120\u0121\5\64\33\2\u0121E\3\2")
        buf.write("\2\2\u0122\u0123\5^\60\2\u0123\u0124\7\23\2\2\u0124\u0125")
        buf.write("\7\"\2\2\u0125\u0126\5f\64\2\u0126\u0127\7#\2\2\u0127")
        buf.write("\u0128\5b\62\2\u0128\u0129\5\64\33\2\u0129\u012a\5F$\2")
        buf.write("\u012a\u012d\3\2\2\2\u012b\u012d\3\2\2\2\u012c\u0122\3")
        buf.write("\2\2\2\u012c\u012b\3\2\2\2\u012dG\3\2\2\2\u012e\u012f")
        buf.write("\7\22\2\2\u012f\u0130\5b\62\2\u0130\u0131\5\64\33\2\u0131")
        buf.write("\u0134\3\2\2\2\u0132\u0134\3\2\2\2\u0133\u012e\3\2\2\2")
        buf.write("\u0133\u0132\3\2\2\2\u0134I\3\2\2\2\u0135\u0136\7\f\2")
        buf.write("\2\u0136\u0137\7*\2\2\u0137\u0138\7\r\2\2\u0138\u0139")
        buf.write("\5f\64\2\u0139\u013a\7\16\2\2\u013a\u013b\5d\63\2\u013b")
        buf.write("\u013c\5b\62\2\u013c\u013d\5\64\33\2\u013dK\3\2\2\2\u013e")
        buf.write("\u013f\7\17\2\2\u013fM\3\2\2\2\u0140\u0141\7\20\2\2\u0141")
        buf.write("O\3\2\2\2\u0142\u0143\7\b\2\2\u0143\u0146\5d\63\2\u0144")
        buf.write("\u0146\7\b\2\2\u0145\u0142\3\2\2\2\u0145\u0144\3\2\2\2")
        buf.write("\u0146Q\3\2\2\2\u0147\u0148\7*\2\2\u0148\u0149\5T+\2\u0149")
        buf.write("S\3\2\2\2\u014a\u014b\7\"\2\2\u014b\u014c\5V,\2\u014c")
        buf.write("\u014d\7#\2\2\u014dU\3\2\2\2\u014e\u014f\5Z.\2\u014f\u0150")
        buf.write("\5X-\2\u0150\u0153\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u014e")
        buf.write("\3\2\2\2\u0152\u0151\3\2\2\2\u0153W\3\2\2\2\u0154\u0155")
        buf.write("\7&\2\2\u0155\u0156\5Z.\2\u0156\u0157\5X-\2\u0157\u015a")
        buf.write("\3\2\2\2\u0158\u015a\3\2\2\2\u0159\u0154\3\2\2\2\u0159")
        buf.write("\u0158\3\2\2\2\u015aY\3\2\2\2\u015b\u015c\5d\63\2\u015c")
        buf.write("[\3\2\2\2\u015d\u015e\7\24\2\2\u015e\u015f\5\66\34\2\u015f")
        buf.write("\u0160\5^\60\2\u0160\u0161\7\25\2\2\u0161]\3\2\2\2\u0162")
        buf.write("\u0163\7\'\2\2\u0163\u0164\5`\61\2\u0164_\3\2\2\2\u0165")
        buf.write("\u0166\7\'\2\2\u0166\u0169\5`\61\2\u0167\u0169\3\2\2\2")
        buf.write("\u0168\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169a\3\2\2")
        buf.write("\2\u016a\u016b\7\'\2\2\u016b\u016e\5b\62\2\u016c\u016e")
        buf.write("\3\2\2\2\u016d\u016a\3\2\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("c\3\2\2\2\u016f\u0170\5f\64\2\u0170e\3\2\2\2\u0171\u0172")
        buf.write("\5h\65\2\u0172g\3\2\2\2\u0173\u0174\b\65\1\2\u0174\u0175")
        buf.write("\5j\66\2\u0175\u017e\3\2\2\2\u0176\u0177\f\5\2\2\u0177")
        buf.write("\u0178\7\36\2\2\u0178\u017d\5h\65\6\u0179\u017a\f\4\2")
        buf.write("\2\u017a\u017b\7\37\2\2\u017b\u017d\5h\65\5\u017c\u0176")
        buf.write("\3\2\2\2\u017c\u0179\3\2\2\2\u017d\u0180\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fi\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0181\u0182\b\66\1\2\u0182\u0183\5l\67")
        buf.write("\2\u0183\u018c\3\2\2\2\u0184\u0185\f\5\2\2\u0185\u0186")
        buf.write("\7\27\2\2\u0186\u018b\5j\66\6\u0187\u0188\f\4\2\2\u0188")
        buf.write("\u0189\7\30\2\2\u0189\u018b\5j\66\5\u018a\u0184\3\2\2")
        buf.write("\2\u018a\u0187\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a")
        buf.write("\3\2\2\2\u018c\u018d\3\2\2\2\u018dk\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018f\u0190\7\26\2\2\u0190\u0193\5l\67\2\u0191")
        buf.write("\u0193\5n8\2\u0192\u018f\3\2\2\2\u0192\u0191\3\2\2\2\u0193")
        buf.write("m\3\2\2\2\u0194\u0195\5p9\2\u0195o\3\2\2\2\u0196\u0197")
        buf.write("\b9\1\2\u0197\u0198\5r:\2\u0198\u01a1\3\2\2\2\u0199\u019a")
        buf.write("\f\5\2\2\u019a\u019b\7\31\2\2\u019b\u01a0\5p9\6\u019c")
        buf.write("\u019d\f\4\2\2\u019d\u019e\7\32\2\2\u019e\u01a0\5p9\5")
        buf.write("\u019f\u0199\3\2\2\2\u019f\u019c\3\2\2\2\u01a0\u01a3\3")
        buf.write("\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2q")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\b:\1\2\u01a5")
        buf.write("\u01a6\5t;\2\u01a6\u01b2\3\2\2\2\u01a7\u01a8\f\6\2\2\u01a8")
        buf.write("\u01a9\7\33\2\2\u01a9\u01b1\5r:\7\u01aa\u01ab\f\5\2\2")
        buf.write("\u01ab\u01ac\7\34\2\2\u01ac\u01b1\5r:\6\u01ad\u01ae\f")
        buf.write("\4\2\2\u01ae\u01af\7\35\2\2\u01af\u01b1\5r:\5\u01b0\u01a7")
        buf.write("\3\2\2\2\u01b0\u01aa\3\2\2\2\u01b0\u01ad\3\2\2\2\u01b1")
        buf.write("\u01b4\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3s\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7\32\2")
        buf.write("\2\u01b6\u01b9\5t;\2\u01b7\u01b9\5v<\2\u01b8\u01b5\3\2")
        buf.write("\2\2\u01b8\u01b7\3\2\2\2\u01b9u\3\2\2\2\u01ba\u01bb\5")
        buf.write("x=\2\u01bbw\3\2\2\2\u01bc\u01bd\5|?\2\u01bd\u01be\7!\2")
        buf.write("\2\u01be\u01bf\5|?\2\u01bf\u01c0\5z>\2\u01c0\u01c3\3\2")
        buf.write("\2\2\u01c1\u01c3\5|?\2\u01c2\u01bc\3\2\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3y\3\2\2\2\u01c4\u01c5\7!\2\2\u01c5\u01c6")
        buf.write("\5|?\2\u01c6\u01c7\5z>\2\u01c7\u01ca\3\2\2\2\u01c8\u01ca")
        buf.write("\3\2\2\2\u01c9\u01c4\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca")
        buf.write("{\3\2\2\2\u01cb\u01cc\7\"\2\2\u01cc\u01cd\5d\63\2\u01cd")
        buf.write("\u01ce\7#\2\2\u01ce\u01d7\3\2\2\2\u01cf\u01d7\7*\2\2\u01d0")
        buf.write("\u01d7\7(\2\2\u01d1\u01d7\7)\2\2\u01d2\u01d7\5~@\2\u01d3")
        buf.write("\u01d7\5\22\n\2\u01d4\u01d7\5\32\16\2\u01d5\u01d7\5R*")
        buf.write("\2\u01d6\u01cb\3\2\2\2\u01d6\u01cf\3\2\2\2\u01d6\u01d0")
        buf.write("\3\2\2\2\u01d6\u01d1\3\2\2\2\u01d6\u01d2\3\2\2\2\u01d6")
        buf.write("\u01d3\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2")
        buf.write("\u01d7}\3\2\2\2\u01d8\u01d9\t\4\2\2\u01d9\177\3\2\2\2")
        buf.write("\'\u0087\u008e\u0093\u0097\u00ab\u00b2\u00bc\u00c3\u00c7")
        buf.write("\u00d7\u00de\u00ea\u00ef\u00fa\u0101\u0107\u0114\u012c")
        buf.write("\u0133\u0145\u0152\u0159\u0168\u016d\u017c\u017e\u018a")
        buf.write("\u018c\u0192\u019f\u01a1\u01b0\u01b2\u01b8\u01c2\u01c9")
        buf.write("\u01d6")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "<INVALID>", "'=='", "'<-'", "'...'", "'('", "')'", 
                     "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "KWNUMBER", "KWBOOL", 
                      "KWSTRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                      "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                      "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "COMPARENUM", "COMPARESTR", 
                      "ASSIGN", "CONCAT", "OPENPAREN", "CLOSEPAREN", "OPENSQBRACKET", 
                      "CLOSESQBRACKET", "COMMA", "NEWLINE", "NUMBER", "STRING", 
                      "IDENTIFIER", "CMT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decls_list = 1
    RULE_decls_list_tail = 2
    RULE_decls = 3
    RULE_vari_decls = 4
    RULE_vari_decls_1 = 5
    RULE_vari_decls_2 = 6
    RULE_vari_decls_type = 7
    RULE_array = 8
    RULE_array_tail = 9
    RULE_list_expr_num = 10
    RULE_list_expr_num_tail = 11
    RULE_array_val = 12
    RULE_list_expr = 13
    RULE_list_expr_tail = 14
    RULE_vari_id = 15
    RULE_func_decls = 16
    RULE_func_param = 17
    RULE_list_param = 18
    RULE_list_param_tail = 19
    RULE_params = 20
    RULE_vd_for_func = 21
    RULE_vd_type_ff = 22
    RULE_func_sepa = 23
    RULE_func_body = 24
    RULE_stmt = 25
    RULE_list_stmt = 26
    RULE_stmt_vari_decl = 27
    RULE_stmt_assi = 28
    RULE_stmt_assi_1 = 29
    RULE_stmt_assi_2 = 30
    RULE_assi_type = 31
    RULE_stmt_cond = 32
    RULE_stmt_if = 33
    RULE_stmt_elif = 34
    RULE_stmt_else = 35
    RULE_stmt_for = 36
    RULE_stmt_break = 37
    RULE_stmt_continue = 38
    RULE_stmt_return = 39
    RULE_stmt_func_call = 40
    RULE_sfc_param = 41
    RULE_sfc_list_args = 42
    RULE_sfc_list_args_tail = 43
    RULE_sfc_args = 44
    RULE_stmt_block = 45
    RULE_stmt_sepa_nonnull = 46
    RULE_s_s_nn_tail = 47
    RULE_stmt_sepa_null = 48
    RULE_expr = 49
    RULE_expr_cond = 50
    RULE_expr_compare = 51
    RULE_expr_cond_andor = 52
    RULE_expr_cond_not = 53
    RULE_expr_num = 54
    RULE_e_n_addsub = 55
    RULE_e_n_muldivmod = 56
    RULE_e_n_nega = 57
    RULE_expr_string = 58
    RULE_expr_string_concat = 59
    RULE_e_s_c_tail = 60
    RULE_expr_other = 61
    RULE_boolval = 62

    ruleNames =  [ "program", "decls_list", "decls_list_tail", "decls", 
                   "vari_decls", "vari_decls_1", "vari_decls_2", "vari_decls_type", 
                   "array", "array_tail", "list_expr_num", "list_expr_num_tail", 
                   "array_val", "list_expr", "list_expr_tail", "vari_id", 
                   "func_decls", "func_param", "list_param", "list_param_tail", 
                   "params", "vd_for_func", "vd_type_ff", "func_sepa", "func_body", 
                   "stmt", "list_stmt", "stmt_vari_decl", "stmt_assi", "stmt_assi_1", 
                   "stmt_assi_2", "assi_type", "stmt_cond", "stmt_if", "stmt_elif", 
                   "stmt_else", "stmt_for", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_func_call", "sfc_param", "sfc_list_args", 
                   "sfc_list_args_tail", "sfc_args", "stmt_block", "stmt_sepa_nonnull", 
                   "s_s_nn_tail", "stmt_sepa_null", "expr", "expr_cond", 
                   "expr_compare", "expr_cond_andor", "expr_cond_not", "expr_num", 
                   "e_n_addsub", "e_n_muldivmod", "e_n_nega", "expr_string", 
                   "expr_string_concat", "e_s_c_tail", "expr_other", "boolval" ]

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
    ELSE=16
    ELIF=17
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
            self.state = 126
            self.decls_list()
            self.state = 127
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


        def decls_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_list_tailContext,0)


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
            self.state = 133
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.decls()
                self.state = 130
                self.decls_list_tail()
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


    class Decls_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def decls(self):
            return self.getTypedRuleContext(ZCodeParser.DeclsContext,0)


        def decls_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Decls_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decls_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecls_list_tail" ):
                return visitor.visitDecls_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def decls_list_tail(self):

        localctx = ZCodeParser.Decls_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decls_list_tail)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(ZCodeParser.NEWLINE)
                self.state = 136
                self.decls()
                self.state = 137
                self.decls_list_tail()
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
        self.enterRule(localctx, 6, self.RULE_decls)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.vari_decls()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.func_decls()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NEWLINE]:
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

        def vari_decls_1(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_1Context,0)


        def vari_decls_2(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_2Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls" ):
                return visitor.visitVari_decls(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls(self):

        localctx = ZCodeParser.Vari_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vari_decls)
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.vari_decls_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.vari_decls_2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_decls_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_typeContext,0)


        def vari_id(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_idContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_1" ):
                return visitor.visitVari_decls_1(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_1(self):

        localctx = ZCodeParser.Vari_decls_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vari_decls_1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.vari_decls_type()
            self.state = 152
            self.vari_id()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_assi(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_assiContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_2" ):
                return visitor.visitVari_decls_2(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_2(self):

        localctx = ZCodeParser.Vari_decls_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vari_decls_2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.stmt_assi()
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

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVari_decls_type" ):
                return visitor.visitVari_decls_type(self)
            else:
                return visitor.visitChildren(self)




    def vari_decls_type(self):

        localctx = ZCodeParser.Vari_decls_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vari_decls_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KWNUMBER) | (1 << ZCodeParser.KWBOOL) | (1 << ZCodeParser.KWSTRING) | (1 << ZCodeParser.DYNAMIC))) != 0)):
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
        self.enterRule(localctx, 16, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 159
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
        self.enterRule(localctx, 18, self.RULE_array_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 162
            self.list_expr_num()
            self.state = 163
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
        self.enterRule(localctx, 20, self.RULE_list_expr_num)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.expr_num()
                self.state = 166
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
        self.enterRule(localctx, 22, self.RULE_list_expr_num_tail)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(ZCodeParser.COMMA)
                self.state = 172
                self.expr_num()
                self.state = 173
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
        self.enterRule(localctx, 24, self.RULE_array_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 179
            self.list_expr()
            self.state = 180
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
        self.enterRule(localctx, 26, self.RULE_list_expr)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.expr()
                self.state = 183
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
        self.enterRule(localctx, 28, self.RULE_list_expr_tail)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(ZCodeParser.COMMA)
                self.state = 189
                self.expr()
                self.state = 190
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
        self.enterRule(localctx, 30, self.RULE_vari_id)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
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
            self.state = 199
            self.match(ZCodeParser.FUNC)
            self.state = 200
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 201
            self.func_param()
            self.state = 202
            self.func_sepa()
            self.state = 203
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
            self.state = 205
            self.match(ZCodeParser.OPENPAREN)
            self.state = 206
            self.list_param()
            self.state = 207
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
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.params()
                self.state = 210
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
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(ZCodeParser.COMMA)
                self.state = 216
                self.params()
                self.state = 217
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

        def vd_for_func(self):
            return self.getTypedRuleContext(ZCodeParser.Vd_for_funcContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.vd_for_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vd_for_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vd_type_ff(self):
            return self.getTypedRuleContext(ZCodeParser.Vd_type_ffContext,0)


        def vari_id(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_idContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vd_for_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVd_for_func" ):
                return visitor.visitVd_for_func(self)
            else:
                return visitor.visitChildren(self)




    def vd_for_func(self):

        localctx = ZCodeParser.Vd_for_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_vd_for_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.vd_type_ff()
            self.state = 225
            self.vari_id()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vd_type_ffContext(ParserRuleContext):
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
            return ZCodeParser.RULE_vd_type_ff

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVd_type_ff" ):
                return visitor.visitVd_type_ff(self)
            else:
                return visitor.visitChildren(self)




    def vd_type_ff(self):

        localctx = ZCodeParser.Vd_type_ffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_vd_type_ff)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
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
        self.enterRule(localctx, 46, self.RULE_func_sepa)
        try:
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(ZCodeParser.NEWLINE)
                self.state = 230
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
        self.enterRule(localctx, 48, self.RULE_func_body)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.RETURN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.stmt_return()
                pass
            elif token in [ZCodeParser.BEGIN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.stmt_block()
                pass
            elif token in [ZCodeParser.EOF, ZCodeParser.NEWLINE]:
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
        self.enterRule(localctx, 50, self.RULE_stmt)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.stmt_vari_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.stmt_assi()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.stmt_cond()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                self.stmt_for()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 243
                self.stmt_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 244
                self.stmt_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 245
                self.stmt_return()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 246
                self.stmt_func_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 247
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

        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


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
        self.enterRule(localctx, 52, self.RULE_list_stmt)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.stmt_sepa_nonnull()
                self.state = 251
                self.stmt()
                self.state = 252
                self.list_stmt()
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
        self.enterRule(localctx, 54, self.RULE_stmt_vari_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
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

        def stmt_assi_1(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_assi_1Context,0)


        def stmt_assi_2(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_assi_2Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_assi

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assi" ):
                return visitor.visitStmt_assi(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assi(self):

        localctx = ZCodeParser.Stmt_assiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_assi)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.stmt_assi_1()
                pass
            elif token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.stmt_assi_2()
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


    class Stmt_assi_1Context(ParserRuleContext):
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
            return ZCodeParser.RULE_stmt_assi_1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assi_1" ):
                return visitor.visitStmt_assi_1(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assi_1(self):

        localctx = ZCodeParser.Stmt_assi_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_assi_1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.vari_id()
            self.state = 264
            self.match(ZCodeParser.ASSIGN)
            self.state = 265
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_assi_2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assi_type(self):
            return self.getTypedRuleContext(ZCodeParser.Assi_typeContext,0)


        def vari_id(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_idContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_assi_2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assi_2" ):
                return visitor.visitStmt_assi_2(self)
            else:
                return visitor.visitChildren(self)




    def stmt_assi_2(self):

        localctx = ZCodeParser.Stmt_assi_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt_assi_2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.assi_type()
            self.state = 268
            self.vari_id()
            self.state = 269
            self.match(ZCodeParser.ASSIGN)
            self.state = 270
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

        def vari_decls_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_typeContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assi_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssi_type" ):
                return visitor.visitAssi_type(self)
            else:
                return visitor.visitChildren(self)




    def assi_type(self):

        localctx = ZCodeParser.Assi_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assi_type)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KWNUMBER, ZCodeParser.KWBOOL, ZCodeParser.KWSTRING, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.vari_decls_type()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(ZCodeParser.VAR)
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


    class Stmt_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_if(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_ifContext,0)


        def stmt_elif(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_elifContext,0)


        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


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
        self.enterRule(localctx, 64, self.RULE_stmt_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.stmt_if()
            self.state = 277
            self.stmt_elif()
            self.state = 278
            self.stmt_sepa_nonnull()
            self.state = 279
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
        self.enterRule(localctx, 66, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.IF)
            self.state = 282
            self.match(ZCodeParser.OPENPAREN)
            self.state = 283
            self.expr_cond()
            self.state = 284
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 285
            self.stmt_sepa_null()
            self.state = 286
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

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def stmt_sepa_null(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nullContext,0)


        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


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
        self.enterRule(localctx, 68, self.RULE_stmt_elif)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.stmt_sepa_nonnull()
                self.state = 289
                self.match(ZCodeParser.ELIF)
                self.state = 290
                self.match(ZCodeParser.OPENPAREN)
                self.state = 291
                self.expr_cond()
                self.state = 292
                self.match(ZCodeParser.CLOSEPAREN)
                self.state = 293
                self.stmt_sepa_null()
                self.state = 294
                self.stmt()
                self.state = 295
                self.stmt_elif()
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
        self.enterRule(localctx, 70, self.RULE_stmt_else)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(ZCodeParser.ELSE)
                self.state = 301
                self.stmt_sepa_null()
                self.state = 302
                self.stmt()
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
        self.enterRule(localctx, 72, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(ZCodeParser.FOR)
            self.state = 308
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 309
            self.match(ZCodeParser.UNTIL)
            self.state = 310
            self.expr_cond()
            self.state = 311
            self.match(ZCodeParser.BY)
            self.state = 312
            self.expr()
            self.state = 313
            self.stmt_sepa_null()
            self.state = 314
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
        self.enterRule(localctx, 74, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
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
        self.enterRule(localctx, 76, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
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
        self.enterRule(localctx, 78, self.RULE_stmt_return)
        try:
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(ZCodeParser.RETURN)
                self.state = 321
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
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
        self.enterRule(localctx, 80, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 326
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
        self.enterRule(localctx, 82, self.RULE_sfc_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(ZCodeParser.OPENPAREN)
            self.state = 329
            self.sfc_list_args()
            self.state = 330
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
        self.enterRule(localctx, 84, self.RULE_sfc_list_args)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.NOT, ZCodeParser.SUB, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.sfc_args()
                self.state = 333
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
        self.enterRule(localctx, 86, self.RULE_sfc_list_args_tail)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(ZCodeParser.COMMA)
                self.state = 339
                self.sfc_args()
                self.state = 340
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
        self.enterRule(localctx, 88, self.RULE_sfc_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
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

        def list_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.List_stmtContext,0)


        def stmt_sepa_nonnull(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_sepa_nonnullContext,0)


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
        self.enterRule(localctx, 90, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ZCodeParser.BEGIN)
            self.state = 348
            self.list_stmt()
            self.state = 349
            self.stmt_sepa_nonnull()
            self.state = 350
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

        def s_s_nn_tail(self):
            return self.getTypedRuleContext(ZCodeParser.S_s_nn_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_sepa_nonnull

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_sepa_nonnull" ):
                return visitor.visitStmt_sepa_nonnull(self)
            else:
                return visitor.visitChildren(self)




    def stmt_sepa_nonnull(self):

        localctx = ZCodeParser.Stmt_sepa_nonnullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmt_sepa_nonnull)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ZCodeParser.NEWLINE)
            self.state = 353
            self.s_s_nn_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S_s_nn_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def s_s_nn_tail(self):
            return self.getTypedRuleContext(ZCodeParser.S_s_nn_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_s_s_nn_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitS_s_nn_tail" ):
                return visitor.visitS_s_nn_tail(self)
            else:
                return visitor.visitChildren(self)




    def s_s_nn_tail(self):

        localctx = ZCodeParser.S_s_nn_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_s_s_nn_tail)
        try:
            self.state = 358
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 355
                self.match(ZCodeParser.NEWLINE)
                self.state = 356
                self.s_s_nn_tail()
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
        self.enterRule(localctx, 96, self.RULE_stmt_sepa_null)
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

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expr_cond()
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

        def expr_compare(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_compareContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cond" ):
                return visitor.visitExpr_cond(self)
            else:
                return visitor.visitChildren(self)




    def expr_cond(self):

        localctx = ZCodeParser.Expr_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.expr_compare(0)
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

        def expr_cond_andor(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_andorContext,0)


        def expr_compare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_compareContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_compareContext,i)


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



    def expr_compare(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_compareContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr_compare, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.expr_cond_andor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 380
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 378
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_compareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_compare)
                        self.state = 372
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 373
                        self.match(ZCodeParser.COMPARENUM)
                        self.state = 374
                        self.expr_compare(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_compareContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_compare)
                        self.state = 375
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 376
                        self.match(ZCodeParser.COMPARESTR)
                        self.state = 377
                        self.expr_compare(3)
                        pass

             
                self.state = 382
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expr_cond_andor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.expr_cond_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 392
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 386
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 387
                        self.match(ZCodeParser.AND)
                        self.state = 388
                        self.expr_cond_andor(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 389
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 390
                        self.match(ZCodeParser.OR)
                        self.state = 391
                        self.expr_cond_andor(3)
                        pass

             
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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


        def expr_num(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_numContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond_not

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_cond_not" ):
                return visitor.visitExpr_cond_not(self)
            else:
                return visitor.visitChildren(self)




    def expr_cond_not(self):

        localctx = ZCodeParser.Expr_cond_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr_cond_not)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(ZCodeParser.NOT)
                self.state = 398
                self.expr_cond_not()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.SUB, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.expr_num()
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
        self.enterRule(localctx, 108, self.RULE_expr_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_e_n_addsub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.e_n_muldivmod(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 415
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 413
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 407
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 408
                        self.match(ZCodeParser.ADD)
                        self.state = 409
                        self.e_n_addsub(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 410
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 411
                        self.match(ZCodeParser.SUB)
                        self.state = 412
                        self.e_n_addsub(3)
                        pass

             
                self.state = 417
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_e_n_muldivmod, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.e_n_nega()
            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 430
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 421
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 422
                        self.match(ZCodeParser.MUL)
                        self.state = 423
                        self.e_n_muldivmod(5)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 424
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 425
                        self.match(ZCodeParser.DIV)
                        self.state = 426
                        self.e_n_muldivmod(4)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 427
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 428
                        self.match(ZCodeParser.MOD)
                        self.state = 429
                        self.e_n_muldivmod(3)
                        pass

             
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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


        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_e_n_nega

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE_n_nega" ):
                return visitor.visitE_n_nega(self)
            else:
                return visitor.visitChildren(self)




    def e_n_nega(self):

        localctx = ZCodeParser.E_n_negaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_e_n_nega)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(ZCodeParser.SUB)
                self.state = 436
                self.e_n_nega()
                pass
            elif token in [ZCodeParser.TRUE, ZCodeParser.FALSE, ZCodeParser.OPENPAREN, ZCodeParser.OPENSQBRACKET, ZCodeParser.NUMBER, ZCodeParser.STRING, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
                self.expr_string()
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


    class Expr_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 116, self.RULE_expr_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
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

        def expr_other(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expr_otherContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expr_otherContext,i)


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
        self.enterRule(localctx, 118, self.RULE_expr_string_concat)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.expr_other()
                self.state = 443
                self.match(ZCodeParser.CONCAT)
                self.state = 444
                self.expr_other()
                self.state = 445
                self.e_s_c_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.expr_other()
                pass


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

        def expr_other(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_otherContext,0)


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
        self.enterRule(localctx, 120, self.RULE_e_s_c_tail)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(ZCodeParser.CONCAT)
                self.state = 451
                self.expr_other()
                self.state = 452
                self.e_s_c_tail()
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


        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


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
        self.enterRule(localctx, 122, self.RULE_expr_other)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(ZCodeParser.OPENPAREN)
                self.state = 458
                self.expr()
                self.state = 459
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 463
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 464
                self.boolval()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 465
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 466
                self.array_val()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 467
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
        self.enterRule(localctx, 124, self.RULE_boolval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
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
        self._predicates[51] = self.expr_compare_sempred
        self._predicates[52] = self.expr_cond_andor_sempred
        self._predicates[55] = self.e_n_addsub_sempred
        self._predicates[56] = self.e_n_muldivmod_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_compare_sempred(self, localctx:Expr_compareContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_cond_andor_sempred(self, localctx:Expr_cond_andorContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def e_n_addsub_sempred(self, localctx:E_n_addsubContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def e_n_muldivmod_sempred(self, localctx:E_n_muldivmodContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




