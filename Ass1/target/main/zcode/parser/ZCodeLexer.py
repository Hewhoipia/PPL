# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2/")
        buf.write("\u01bb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\5\35\u0103\n\35\3\35\3\35\3\35\5\35\u0108")
        buf.write("\n\35\5\35\u010a\n\35\3\36\3\36\3\36\3\37\3\37\3\37\3")
        buf.write(" \3 \3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\6")
        buf.write("\'\u0123\n\'\r\'\16\'\u0124\3\'\3\'\6\'\u0129\n\'\r\'")
        buf.write("\16\'\u012a\5\'\u012d\n\'\3\'\5\'\u0130\n\'\3(\3(\5(\u0134")
        buf.write("\n(\3)\3)\3)\3*\3*\3*\3*\5*\u013d\n*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\5/\u0149\n/\3\60\3\60\7\60\u014d\n\60\f")
        buf.write("\60\16\60\u0150\13\60\3\60\3\60\3\60\3\61\3\61\5\61\u0157")
        buf.write("\n\61\3\61\3\61\3\61\7\61\u015c\n\61\f\61\16\61\u015f")
        buf.write("\13\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\5\65\u0169")
        buf.write("\n\65\3\65\6\65\u016c\n\65\r\65\16\65\u016d\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3;\5;\u017d\n;\3<\3")
        buf.write("<\3=\3=\3=\3=\7=\u0185\n=\f=\16=\u0188\13=\3=\3=\3>\6")
        buf.write(">\u018d\n>\r>\16>\u018e\3>\3>\3?\3?\7?\u0195\n?\f?\16")
        buf.write("?\u0198\13?\3?\5?\u019b\n?\3?\3?\3@\3@\7@\u01a1\n@\f@")
        buf.write("\16@\u01a4\13@\3@\3@\5@\u01a8\n@\3@\3@\5@\u01ac\n@\5@")
        buf.write("\u01ae\n@\3@\7@\u01b1\n@\f@\16@\u01b4\13@\3@\3@\3@\3A")
        buf.write("\3A\3A\4\u0186\u01b2\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O\2Q\2S\2U\2W\2Y\2[\2]\2_)a*c")
        buf.write("\2e\2g\2i\2k\2m\2o\2q\2s\2u\2w\2y+{,}-\177.\u0081/\3\2")
        buf.write("\17\4\2>>@@\t\2))^^ddhhppttvv\3\2$$\7\2\n\f\16\17$$))")
        buf.write("^^\4\2C\\c|\3\2c|\3\2\62;\4\2GGgg\4\2--//\3\2))\4\2\13")
        buf.write("\13\"\"\3\3\f\f\3\2^^\2\u01c1\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("_\3\2\2\2\2a\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0088")
        buf.write("\3\2\2\2\7\u008e\3\2\2\2\t\u0095\3\2\2\2\13\u009a\3\2")
        buf.write("\2\2\r\u00a1\3\2\2\2\17\u00a8\3\2\2\2\21\u00ac\3\2\2\2")
        buf.write("\23\u00b4\3\2\2\2\25\u00b9\3\2\2\2\27\u00bd\3\2\2\2\31")
        buf.write("\u00c3\3\2\2\2\33\u00c6\3\2\2\2\35\u00cc\3\2\2\2\37\u00d5")
        buf.write("\3\2\2\2!\u00d8\3\2\2\2#\u00dd\3\2\2\2%\u00e2\3\2\2\2")
        buf.write("\'\u00e8\3\2\2\2)\u00ec\3\2\2\2+\u00f0\3\2\2\2-\u00f4")
        buf.write("\3\2\2\2/\u00f7\3\2\2\2\61\u00f9\3\2\2\2\63\u00fb\3\2")
        buf.write("\2\2\65\u00fd\3\2\2\2\67\u00ff\3\2\2\29\u0109\3\2\2\2")
        buf.write(";\u010b\3\2\2\2=\u010e\3\2\2\2?\u0111\3\2\2\2A\u0115\3")
        buf.write("\2\2\2C\u0117\3\2\2\2E\u0119\3\2\2\2G\u011b\3\2\2\2I\u011d")
        buf.write("\3\2\2\2K\u011f\3\2\2\2M\u0122\3\2\2\2O\u0133\3\2\2\2")
        buf.write("Q\u0135\3\2\2\2S\u013c\3\2\2\2U\u013e\3\2\2\2W\u0140\3")
        buf.write("\2\2\2Y\u0142\3\2\2\2[\u0144\3\2\2\2]\u0148\3\2\2\2_\u014a")
        buf.write("\3\2\2\2a\u0156\3\2\2\2c\u0160\3\2\2\2e\u0162\3\2\2\2")
        buf.write("g\u0164\3\2\2\2i\u0166\3\2\2\2k\u016f\3\2\2\2m\u0171\3")
        buf.write("\2\2\2o\u0173\3\2\2\2q\u0175\3\2\2\2s\u0177\3\2\2\2u\u017c")
        buf.write("\3\2\2\2w\u017e\3\2\2\2y\u0180\3\2\2\2{\u018c\3\2\2\2")
        buf.write("}\u0192\3\2\2\2\177\u019e\3\2\2\2\u0081\u01b8\3\2\2\2")
        buf.write("\u0083\u0084\7v\2\2\u0084\u0085\7t\2\2\u0085\u0086\7w")
        buf.write("\2\2\u0086\u0087\7g\2\2\u0087\4\3\2\2\2\u0088\u0089\7")
        buf.write("h\2\2\u0089\u008a\7c\2\2\u008a\u008b\7n\2\2\u008b\u008c")
        buf.write("\7u\2\2\u008c\u008d\7g\2\2\u008d\6\3\2\2\2\u008e\u008f")
        buf.write("\7p\2\2\u008f\u0090\7w\2\2\u0090\u0091\7o\2\2\u0091\u0092")
        buf.write("\7d\2\2\u0092\u0093\7g\2\2\u0093\u0094\7t\2\2\u0094\b")
        buf.write("\3\2\2\2\u0095\u0096\7d\2\2\u0096\u0097\7q\2\2\u0097\u0098")
        buf.write("\7q\2\2\u0098\u0099\7n\2\2\u0099\n\3\2\2\2\u009a\u009b")
        buf.write("\7u\2\2\u009b\u009c\7v\2\2\u009c\u009d\7t\2\2\u009d\u009e")
        buf.write("\7k\2\2\u009e\u009f\7p\2\2\u009f\u00a0\7i\2\2\u00a0\f")
        buf.write("\3\2\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7v\2\2\u00a4\u00a5\7w\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7")
        buf.write("\7p\2\2\u00a7\16\3\2\2\2\u00a8\u00a9\7x\2\2\u00a9\u00aa")
        buf.write("\7c\2\2\u00aa\u00ab\7t\2\2\u00ab\20\3\2\2\2\u00ac\u00ad")
        buf.write("\7f\2\2\u00ad\u00ae\7{\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7c\2\2\u00b0\u00b1\7o\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7e\2\2\u00b3\22\3\2\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6")
        buf.write("\7w\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7e\2\2\u00b8\24")
        buf.write("\3\2\2\2\u00b9\u00ba\7h\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7t\2\2\u00bc\26\3\2\2\2\u00bd\u00be\7w\2\2\u00be\u00bf")
        buf.write("\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7n\2\2\u00c2\30\3\2\2\2\u00c3\u00c4\7d\2\2\u00c4\u00c5")
        buf.write("\7{\2\2\u00c5\32\3\2\2\2\u00c6\u00c7\7d\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7m\2\2\u00cb\34\3\2\2\2\u00cc\u00cd\7e\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1")
        buf.write("\7k\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4")
        buf.write("\7g\2\2\u00d4\36\3\2\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7h\2\2\u00d7 \3\2\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da")
        buf.write("\7n\2\2\u00da\u00db\7u\2\2\u00db\u00dc\7g\2\2\u00dc\"")
        buf.write("\3\2\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7n\2\2\u00df\u00e0")
        buf.write("\7k\2\2\u00e0\u00e1\7h\2\2\u00e1$\3\2\2\2\u00e2\u00e3")
        buf.write("\7d\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7i\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7p\2\2\u00e7&\3\2\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9\u00ea\7p\2\2\u00ea\u00eb\7f\2\2\u00eb(\3")
        buf.write("\2\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef")
        buf.write("\7v\2\2\u00ef*\3\2\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7p\2\2\u00f2\u00f3\7f\2\2\u00f3,\3\2\2\2\u00f4\u00f5")
        buf.write("\7q\2\2\u00f5\u00f6\7t\2\2\u00f6.\3\2\2\2\u00f7\u00f8")
        buf.write("\7-\2\2\u00f8\60\3\2\2\2\u00f9\u00fa\7/\2\2\u00fa\62\3")
        buf.write("\2\2\2\u00fb\u00fc\7,\2\2\u00fc\64\3\2\2\2\u00fd\u00fe")
        buf.write("\7\61\2\2\u00fe\66\3\2\2\2\u00ff\u0100\7\'\2\2\u01008")
        buf.write("\3\2\2\2\u0101\u0103\7#\2\2\u0102\u0101\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u010a\7?\2\2")
        buf.write("\u0105\u0107\t\2\2\2\u0106\u0108\7?\2\2\u0107\u0106\3")
        buf.write("\2\2\2\u0107\u0108\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0102")
        buf.write("\3\2\2\2\u0109\u0105\3\2\2\2\u010a:\3\2\2\2\u010b\u010c")
        buf.write("\7?\2\2\u010c\u010d\7?\2\2\u010d<\3\2\2\2\u010e\u010f")
        buf.write("\7>\2\2\u010f\u0110\7/\2\2\u0110>\3\2\2\2\u0111\u0112")
        buf.write("\7\60\2\2\u0112\u0113\7\60\2\2\u0113\u0114\7\60\2\2\u0114")
        buf.write("@\3\2\2\2\u0115\u0116\7*\2\2\u0116B\3\2\2\2\u0117\u0118")
        buf.write("\7+\2\2\u0118D\3\2\2\2\u0119\u011a\7]\2\2\u011aF\3\2\2")
        buf.write("\2\u011b\u011c\7_\2\2\u011cH\3\2\2\2\u011d\u011e\7.\2")
        buf.write("\2\u011eJ\3\2\2\2\u011f\u0120\7\f\2\2\u0120L\3\2\2\2\u0121")
        buf.write("\u0123\5g\64\2\u0122\u0121\3\2\2\2\u0123\u0124\3\2\2\2")
        buf.write("\u0124\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\u012c\3")
        buf.write("\2\2\2\u0126\u0128\7\60\2\2\u0127\u0129\5g\64\2\u0128")
        buf.write("\u0127\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u0128\3\2\2\2")
        buf.write("\u012a\u012b\3\2\2\2\u012b\u012d\3\2\2\2\u012c\u0126\3")
        buf.write("\2\2\2\u012c\u012d\3\2\2\2\u012d\u012f\3\2\2\2\u012e\u0130")
        buf.write("\5i\65\2\u012f\u012e\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("N\3\2\2\2\u0131\u0134\5Q)\2\u0132\u0134\5S*\2\u0133\u0131")
        buf.write("\3\2\2\2\u0133\u0132\3\2\2\2\u0134P\3\2\2\2\u0135\u0136")
        buf.write("\7^\2\2\u0136\u0137\t\3\2\2\u0137R\3\2\2\2\u0138\u0139")
        buf.write("\5u;\2\u0139\u013a\5k\66\2\u013a\u013d\3\2\2\2\u013b\u013d")
        buf.write("\5u;\2\u013c\u0138\3\2\2\2\u013c\u013b\3\2\2\2\u013dT")
        buf.write("\3\2\2\2\u013e\u013f\t\3\2\2\u013fV\3\2\2\2\u0140\u0141")
        buf.write("\t\4\2\2\u0141X\3\2\2\2\u0142\u0143\n\3\2\2\u0143Z\3\2")
        buf.write("\2\2\u0144\u0145\n\4\2\2\u0145\\\3\2\2\2\u0146\u0149\n")
        buf.write("\5\2\2\u0147\u0149\5O(\2\u0148\u0146\3\2\2\2\u0148\u0147")
        buf.write("\3\2\2\2\u0149^\3\2\2\2\u014a\u014e\5k\66\2\u014b\u014d")
        buf.write("\5]/\2\u014c\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150")
        buf.write("\u014e\3\2\2\2\u0151\u0152\5k\66\2\u0152\u0153\b\60\2")
        buf.write("\2\u0153`\3\2\2\2\u0154\u0157\5c\62\2\u0155\u0157\7a\2")
        buf.write("\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157\u015d")
        buf.write("\3\2\2\2\u0158\u015c\5c\62\2\u0159\u015c\5g\64\2\u015a")
        buf.write("\u015c\7a\2\2\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2")
        buf.write("\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3")
        buf.write("\2\2\2\u015d\u015e\3\2\2\2\u015eb\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u0160\u0161\t\6\2\2\u0161d\3\2\2\2\u0162\u0163")
        buf.write("\t\7\2\2\u0163f\3\2\2\2\u0164\u0165\t\b\2\2\u0165h\3\2")
        buf.write("\2\2\u0166\u0168\t\t\2\2\u0167\u0169\t\n\2\2\u0168\u0167")
        buf.write("\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016b\3\2\2\2\u016a")
        buf.write("\u016c\5g\64\2\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016b\3\2\2\2\u016d\u016e\3\2\2\2\u016ej\3\2\2")
        buf.write("\2\u016f\u0170\7$\2\2\u0170l\3\2\2\2\u0171\u0172\7\n\2")
        buf.write("\2\u0172n\3\2\2\2\u0173\u0174\7\16\2\2\u0174p\3\2\2\2")
        buf.write("\u0175\u0176\7\17\2\2\u0176r\3\2\2\2\u0177\u0178\7\13")
        buf.write("\2\2\u0178t\3\2\2\2\u0179\u017a\7^\2\2\u017a\u017d\t\13")
        buf.write("\2\2\u017b\u017d\t\13\2\2\u017c\u0179\3\2\2\2\u017c\u017b")
        buf.write("\3\2\2\2\u017dv\3\2\2\2\u017e\u017f\7^\2\2\u017fx\3\2")
        buf.write("\2\2\u0180\u0181\7%\2\2\u0181\u0182\7%\2\2\u0182\u0186")
        buf.write("\3\2\2\2\u0183\u0185\13\2\2\2\u0184\u0183\3\2\2\2\u0185")
        buf.write("\u0188\3\2\2\2\u0186\u0187\3\2\2\2\u0186\u0184\3\2\2\2")
        buf.write("\u0187\u0189\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\b")
        buf.write("=\3\2\u018az\3\2\2\2\u018b\u018d\t\f\2\2\u018c\u018b\3")
        buf.write("\2\2\2\u018d\u018e\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f")
        buf.write("\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0191\b>\3\2\u0191")
        buf.write("|\3\2\2\2\u0192\u0196\5k\66\2\u0193\u0195\5]/\2\u0194")
        buf.write("\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196\3")
        buf.write("\2\2\2\u0199\u019b\t\r\2\2\u019a\u0199\3\2\2\2\u019b\u019c")
        buf.write("\3\2\2\2\u019c\u019d\b?\4\2\u019d~\3\2\2\2\u019e\u01a2")
        buf.write("\5k\66\2\u019f\u01a1\5]/\2\u01a0\u019f\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("\u01ad\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a7\t\16\2")
        buf.write("\2\u01a6\u01a8\5Y-\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8\3")
        buf.write("\2\2\2\u01a8\u01ae\3\2\2\2\u01a9\u01ab\t\13\2\2\u01aa")
        buf.write("\u01ac\5[.\2\u01ab\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac")
        buf.write("\u01ae\3\2\2\2\u01ad\u01a5\3\2\2\2\u01ad\u01a9\3\2\2\2")
        buf.write("\u01ae\u01b2\3\2\2\2\u01af\u01b1\13\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4\u01b2\3\2\2\2")
        buf.write("\u01b5\u01b6\5k\66\2\u01b6\u01b7\b@\5\2\u01b7\u0080\3")
        buf.write("\2\2\2\u01b8\u01b9\13\2\2\2\u01b9\u01ba\bA\6\2\u01ba\u0082")
        buf.write("\3\2\2\2\35\2\u0102\u0107\u0109\u0124\u012a\u012c\u012f")
        buf.write("\u0133\u013c\u0148\u014e\u0156\u015b\u015d\u0168\u016d")
        buf.write("\u017c\u0186\u018e\u0196\u019a\u01a2\u01a7\u01ab\u01ad")
        buf.write("\u01b2\7\3\60\2\b\2\2\3?\3\3@\4\3A\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRUE = 1
    FALSE = 2
    KWNUMBER = 3
    KWBOOL = 4
    KWSTRING = 5
    RETURN = 6
    VAR = 7
    DYNAMIC = 8
    FUNC = 9
    FOR = 10
    UNTIL = 11
    BY = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELSE = 16
    ELIF = 17
    BEGIN = 18
    END = 19
    NOT = 20
    AND = 21
    OR = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    COMPARENUM = 28
    COMPARESTR = 29
    ASSIGN = 30
    CONCAT = 31
    OPENPAREN = 32
    CLOSEPAREN = 33
    OPENSQBRACKET = 34
    CLOSESQBRACKET = 35
    COMMA = 36
    NEWLINE = 37
    NUMBER = 38
    STRING = 39
    IDENTIFIER = 40
    CMT = 41
    WS = 42
    UNCLOSE_STRING = 43
    ILLEGAL_ESCAPE = 44
    ERROR_CHAR = 45

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'=='", "'<-'", "'...'", "'('", "')'", "'['", "']'", 
            "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "TRUE", "FALSE", "KWNUMBER", "KWBOOL", "KWSTRING", "RETURN", 
            "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "COMPARENUM", "COMPARESTR", "ASSIGN", 
            "CONCAT", "OPENPAREN", "CLOSEPAREN", "OPENSQBRACKET", "CLOSESQBRACKET", 
            "COMMA", "NEWLINE", "NUMBER", "STRING", "IDENTIFIER", "CMT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "TRUE", "FALSE", "KWNUMBER", "KWBOOL", "KWSTRING", "RETURN", 
                  "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                  "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", 
                  "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "COMPARENUM", 
                  "COMPARESTR", "ASSIGN", "CONCAT", "OPENPAREN", "CLOSEPAREN", 
                  "OPENSQBRACKET", "CLOSESQBRACKET", "COMMA", "NEWLINE", 
                  "NUMBER", "ES", "ES_BACKSLASH", "ES_SINGLEQUOTE", "POSTFIX_ES_BACKSLASH", 
                  "POSTFIX_ES_SINGLEQUOTE", "NOT_POSTFIX_ES_BACKSLASH", 
                  "NOT_POSTFIX_ES_SINGLEQUOTE", "STRING_CHAR", "STRING", 
                  "IDENTIFIER", "Char", "LowChar", "Num", "Expo", "DoubleQuote", 
                  "BACKSPACE", "FORMFEED", "CR", "TAB", "SINGLEQUOTE", "BACKSLASH", 
                  "CMT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.STRING_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                text_normalized = self.text.replace('\r\n', '\n')
                raise UncloseString(text_normalized[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                for x in range(len(self.text)):
                    if self.text[x] == '\\':
                        if (self.text[x+1] == 'b') or (self.text[x+1] == 'f') or (self.text[x+1] == 'r'):
                            continue
                        elif (self.text[x+1] == 'n') or (self.text[x+1] == 't') or (self.text[x+1] == '\'') or (self.text[x+1] == '\\'):
                            continue
                        elif (x+2)==(len(self.text)):
                            x=x-1
                            break
                        else:
                            break
                    elif self.text[x] == '\'':
                        if(self.text[x+1] == '"'):
                            continue 
                        elif (x+2)==(len(self.text)):
                            x=x-1
                            break
                        else:
                            break                                      
                raise IllegalEscape(self.text[1:x+2])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


