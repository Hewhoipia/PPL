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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\60")
        buf.write("\u01b3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\5\2\u0088\n\2\3\2\3\2\3\2\7\2\u008d\n\2\f\2\16\2\u0090")
        buf.write("\13\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\5\37\u0116\n\37\3\37\3\37\3\37\5\37\u011b")
        buf.write("\n\37\5\37\u011d\n\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\5)\u0138")
        buf.write("\n)\3)\5)\u013b\n)\3*\3*\5*\u013f\n*\3+\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\5\61\u0151\n\61")
        buf.write("\3\62\3\62\7\62\u0155\n\62\f\62\16\62\u0158\13\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\6\65\u0162\n\65\r")
        buf.write("\65\16\65\u0163\3\66\3\66\5\66\u0168\n\66\3\66\3\66\3")
        buf.write("\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3>")
        buf.write("\3>\7>\u017e\n>\f>\16>\u0181\13>\3>\3>\3?\6?\u0186\n?")
        buf.write("\r?\16?\u0187\3?\3?\3@\3@\7@\u018e\n@\f@\16@\u0191\13")
        buf.write("@\3@\5@\u0194\n@\3@\3@\3A\3A\7A\u019a\nA\fA\16A\u019d")
        buf.write("\13A\3A\3A\5A\u01a1\nA\3A\3A\5A\u01a5\nA\5A\u01a7\nA\3")
        buf.write("A\7A\u01aa\nA\fA\16A\u01ad\13A\3A\3A\3A\3B\3B\4\u017f")
        buf.write("\u01ab\2C\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S\2U\2W\2Y\2[\2]\2_\2a\2c+e\2g\2i\2k\2m")
        buf.write("\2o\2q\2s\2u\2w\2y\2{,}-\177.\u0081/\u0083\60\3\2\17\4")
        buf.write("\2>>@@\t\2))^^ddhhppttvv\3\2))\3\2$$\b\2\n\n\f\f\16\17")
        buf.write("$$))^^\4\2C\\c|\3\2c|\3\2\62;\4\2GGgg\4\2--//\5\2\13\13")
        buf.write("\17\17\"\"\7\3\n\n\f\f\16\17))^^\3\2^^\2\u01b5\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2")
        buf.write("\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2")
        buf.write("\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2")
        buf.write("\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2")
        buf.write("\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2c\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\3\u0087\3\2\2\2\5\u0091\3\2\2\2\7\u0096\3\2\2")
        buf.write("\2\t\u009b\3\2\2\2\13\u00a1\3\2\2\2\r\u00a8\3\2\2\2\17")
        buf.write("\u00ad\3\2\2\2\21\u00b4\3\2\2\2\23\u00bb\3\2\2\2\25\u00bf")
        buf.write("\3\2\2\2\27\u00c7\3\2\2\2\31\u00cc\3\2\2\2\33\u00d0\3")
        buf.write("\2\2\2\35\u00d6\3\2\2\2\37\u00d9\3\2\2\2!\u00df\3\2\2")
        buf.write("\2#\u00e8\3\2\2\2%\u00eb\3\2\2\2\'\u00f0\3\2\2\2)\u00f5")
        buf.write("\3\2\2\2+\u00fb\3\2\2\2-\u00ff\3\2\2\2/\u0103\3\2\2\2")
        buf.write("\61\u0107\3\2\2\2\63\u010a\3\2\2\2\65\u010c\3\2\2\2\67")
        buf.write("\u010e\3\2\2\29\u0110\3\2\2\2;\u0112\3\2\2\2=\u011c\3")
        buf.write("\2\2\2?\u011e\3\2\2\2A\u0121\3\2\2\2C\u0124\3\2\2\2E\u0128")
        buf.write("\3\2\2\2G\u012a\3\2\2\2I\u012c\3\2\2\2K\u012e\3\2\2\2")
        buf.write("M\u0130\3\2\2\2O\u0132\3\2\2\2Q\u0134\3\2\2\2S\u013e\3")
        buf.write("\2\2\2U\u0140\3\2\2\2W\u0143\3\2\2\2Y\u0146\3\2\2\2[\u0148")
        buf.write("\3\2\2\2]\u014a\3\2\2\2_\u014c\3\2\2\2a\u0150\3\2\2\2")
        buf.write("c\u0152\3\2\2\2e\u015c\3\2\2\2g\u015e\3\2\2\2i\u0161\3")
        buf.write("\2\2\2k\u0165\3\2\2\2m\u016b\3\2\2\2o\u016d\3\2\2\2q\u016f")
        buf.write("\3\2\2\2s\u0171\3\2\2\2u\u0173\3\2\2\2w\u0175\3\2\2\2")
        buf.write("y\u0177\3\2\2\2{\u0179\3\2\2\2}\u0185\3\2\2\2\177\u018b")
        buf.write("\3\2\2\2\u0081\u0197\3\2\2\2\u0083\u01b1\3\2\2\2\u0085")
        buf.write("\u0088\5e\63\2\u0086\u0088\7a\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0086\3\2\2\2\u0088\u008e\3\2\2\2\u0089\u008d\5")
        buf.write("e\63\2\u008a\u008d\5i\65\2\u008b\u008d\7a\2\2\u008c\u0089")
        buf.write("\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\4\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0092\7o\2")
        buf.write("\2\u0092\u0093\7c\2\2\u0093\u0094\7k\2\2\u0094\u0095\7")
        buf.write("p\2\2\u0095\6\3\2\2\2\u0096\u0097\7v\2\2\u0097\u0098\7")
        buf.write("t\2\2\u0098\u0099\7w\2\2\u0099\u009a\7g\2\2\u009a\b\3")
        buf.write("\2\2\2\u009b\u009c\7h\2\2\u009c\u009d\7c\2\2\u009d\u009e")
        buf.write("\7n\2\2\u009e\u009f\7u\2\2\u009f\u00a0\7g\2\2\u00a0\n")
        buf.write("\3\2\2\2\u00a1\u00a2\7p\2\2\u00a2\u00a3\7w\2\2\u00a3\u00a4")
        buf.write("\7o\2\2\u00a4\u00a5\7d\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\f\3\2\2\2\u00a8\u00a9\7d\2\2\u00a9\u00aa")
        buf.write("\7q\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7n\2\2\u00ac\16")
        buf.write("\3\2\2\2\u00ad\u00ae\7u\2\2\u00ae\u00af\7v\2\2\u00af\u00b0")
        buf.write("\7t\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3")
        buf.write("\7i\2\2\u00b3\20\3\2\2\2\u00b4\u00b5\7t\2\2\u00b5\u00b6")
        buf.write("\7g\2\2\u00b6\u00b7\7v\2\2\u00b7\u00b8\7w\2\2\u00b8\u00b9")
        buf.write("\7t\2\2\u00b9\u00ba\7p\2\2\u00ba\22\3\2\2\2\u00bb\u00bc")
        buf.write("\7x\2\2\u00bc\u00bd\7c\2\2\u00bd\u00be\7t\2\2\u00be\24")
        buf.write("\3\2\2\2\u00bf\u00c0\7f\2\2\u00c0\u00c1\7{\2\2\u00c1\u00c2")
        buf.write("\7p\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7o\2\2\u00c4\u00c5")
        buf.write("\7k\2\2\u00c5\u00c6\7e\2\2\u00c6\26\3\2\2\2\u00c7\u00c8")
        buf.write("\7h\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb")
        buf.write("\7e\2\2\u00cb\30\3\2\2\2\u00cc\u00cd\7h\2\2\u00cd\u00ce")
        buf.write("\7q\2\2\u00ce\u00cf\7t\2\2\u00cf\32\3\2\2\2\u00d0\u00d1")
        buf.write("\7w\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4")
        buf.write("\7k\2\2\u00d4\u00d5\7n\2\2\u00d5\34\3\2\2\2\u00d6\u00d7")
        buf.write("\7d\2\2\u00d7\u00d8\7{\2\2\u00d8\36\3\2\2\2\u00d9\u00da")
        buf.write("\7d\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7g\2\2\u00dc\u00dd")
        buf.write("\7c\2\2\u00dd\u00de\7m\2\2\u00de \3\2\2\2\u00df\u00e0")
        buf.write("\7e\2\2\u00e0\u00e1\7q\2\2\u00e1\u00e2\7p\2\2\u00e2\u00e3")
        buf.write("\7v\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6")
        buf.write("\7w\2\2\u00e6\u00e7\7g\2\2\u00e7\"\3\2\2\2\u00e8\u00e9")
        buf.write("\7k\2\2\u00e9\u00ea\7h\2\2\u00ea$\3\2\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec\u00ed\7n\2\2\u00ed\u00ee\7u\2\2\u00ee\u00ef")
        buf.write("\7g\2\2\u00ef&\3\2\2\2\u00f0\u00f1\7g\2\2\u00f1\u00f2")
        buf.write("\7n\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7h\2\2\u00f4(\3")
        buf.write("\2\2\2\u00f5\u00f6\7d\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8")
        buf.write("\7i\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa*\3")
        buf.write("\2\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7p\2\2\u00fd\u00fe")
        buf.write("\7f\2\2\u00fe,\3\2\2\2\u00ff\u0100\7p\2\2\u0100\u0101")
        buf.write("\7q\2\2\u0101\u0102\7v\2\2\u0102.\3\2\2\2\u0103\u0104")
        buf.write("\7c\2\2\u0104\u0105\7p\2\2\u0105\u0106\7f\2\2\u0106\60")
        buf.write("\3\2\2\2\u0107\u0108\7q\2\2\u0108\u0109\7t\2\2\u0109\62")
        buf.write("\3\2\2\2\u010a\u010b\7-\2\2\u010b\64\3\2\2\2\u010c\u010d")
        buf.write("\7/\2\2\u010d\66\3\2\2\2\u010e\u010f\7,\2\2\u010f8\3\2")
        buf.write("\2\2\u0110\u0111\7\61\2\2\u0111:\3\2\2\2\u0112\u0113\7")
        buf.write("\'\2\2\u0113<\3\2\2\2\u0114\u0116\7#\2\2\u0115\u0114\3")
        buf.write("\2\2\2\u0115\u0116\3\2\2\2\u0116\u0117\3\2\2\2\u0117\u011d")
        buf.write("\7?\2\2\u0118\u011a\t\2\2\2\u0119\u011b\7?\2\2\u011a\u0119")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c")
        buf.write("\u0115\3\2\2\2\u011c\u0118\3\2\2\2\u011d>\3\2\2\2\u011e")
        buf.write("\u011f\7?\2\2\u011f\u0120\7?\2\2\u0120@\3\2\2\2\u0121")
        buf.write("\u0122\7>\2\2\u0122\u0123\7/\2\2\u0123B\3\2\2\2\u0124")
        buf.write("\u0125\7\60\2\2\u0125\u0126\7\60\2\2\u0126\u0127\7\60")
        buf.write("\2\2\u0127D\3\2\2\2\u0128\u0129\7*\2\2\u0129F\3\2\2\2")
        buf.write("\u012a\u012b\7+\2\2\u012bH\3\2\2\2\u012c\u012d\7]\2\2")
        buf.write("\u012dJ\3\2\2\2\u012e\u012f\7_\2\2\u012fL\3\2\2\2\u0130")
        buf.write("\u0131\7.\2\2\u0131N\3\2\2\2\u0132\u0133\7\f\2\2\u0133")
        buf.write("P\3\2\2\2\u0134\u0137\5i\65\2\u0135\u0136\7\60\2\2\u0136")
        buf.write("\u0138\5i\65\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u013a\3\2\2\2\u0139\u013b\5k\66\2\u013a\u0139\3")
        buf.write("\2\2\2\u013a\u013b\3\2\2\2\u013bR\3\2\2\2\u013c\u013f")
        buf.write("\5U+\2\u013d\u013f\5W,\2\u013e\u013c\3\2\2\2\u013e\u013d")
        buf.write("\3\2\2\2\u013fT\3\2\2\2\u0140\u0141\7^\2\2\u0141\u0142")
        buf.write("\t\3\2\2\u0142V\3\2\2\2\u0143\u0144\t\4\2\2\u0144\u0145")
        buf.write("\t\5\2\2\u0145X\3\2\2\2\u0146\u0147\t\3\2\2\u0147Z\3\2")
        buf.write("\2\2\u0148\u0149\t\5\2\2\u0149\\\3\2\2\2\u014a\u014b\n")
        buf.write("\3\2\2\u014b^\3\2\2\2\u014c\u014d\n\5\2\2\u014d`\3\2\2")
        buf.write("\2\u014e\u0151\n\6\2\2\u014f\u0151\5S*\2\u0150\u014e\3")
        buf.write("\2\2\2\u0150\u014f\3\2\2\2\u0151b\3\2\2\2\u0152\u0156")
        buf.write("\7$\2\2\u0153\u0155\5a\61\2\u0154\u0153\3\2\2\2\u0155")
        buf.write("\u0158\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2")
        buf.write("\u0157\u0159\3\2\2\2\u0158\u0156\3\2\2\2\u0159\u015a\7")
        buf.write("$\2\2\u015a\u015b\b\62\2\2\u015bd\3\2\2\2\u015c\u015d")
        buf.write("\t\7\2\2\u015df\3\2\2\2\u015e\u015f\t\b\2\2\u015fh\3\2")
        buf.write("\2\2\u0160\u0162\t\t\2\2\u0161\u0160\3\2\2\2\u0162\u0163")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164")
        buf.write("j\3\2\2\2\u0165\u0167\t\n\2\2\u0166\u0168\t\13\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u0169\3\2\2\2")
        buf.write("\u0169\u016a\5i\65\2\u016al\3\2\2\2\u016b\u016c\7$\2\2")
        buf.write("\u016cn\3\2\2\2\u016d\u016e\7\n\2\2\u016ep\3\2\2\2\u016f")
        buf.write("\u0170\7\16\2\2\u0170r\3\2\2\2\u0171\u0172\7\17\2\2\u0172")
        buf.write("t\3\2\2\2\u0173\u0174\7\13\2\2\u0174v\3\2\2\2\u0175\u0176")
        buf.write("\7)\2\2\u0176x\3\2\2\2\u0177\u0178\7^\2\2\u0178z\3\2\2")
        buf.write("\2\u0179\u017a\7%\2\2\u017a\u017b\7%\2\2\u017b\u017f\3")
        buf.write("\2\2\2\u017c\u017e\13\2\2\2\u017d\u017c\3\2\2\2\u017e")
        buf.write("\u0181\3\2\2\2\u017f\u0180\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u0180\u0182\3\2\2\2\u0181\u017f\3\2\2\2\u0182\u0183\b")
        buf.write(">\3\2\u0183|\3\2\2\2\u0184\u0186\t\f\2\2\u0185\u0184\3")
        buf.write("\2\2\2\u0186\u0187\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\b?\3\2\u018a")
        buf.write("~\3\2\2\2\u018b\u018f\7$\2\2\u018c\u018e\5a\61\2\u018d")
        buf.write("\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2")
        buf.write("\u018f\u0190\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3")
        buf.write("\2\2\2\u0192\u0194\t\r\2\2\u0193\u0192\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\b@\4\2\u0196\u0080\3\2\2\2\u0197")
        buf.write("\u019b\7$\2\2\u0198\u019a\5a\61\2\u0199\u0198\3\2\2\2")
        buf.write("\u019a\u019d\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3")
        buf.write("\2\2\2\u019c\u01a6\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u01a0")
        buf.write("\t\16\2\2\u019f\u01a1\5]/\2\u01a0\u019f\3\2\2\2\u01a0")
        buf.write("\u01a1\3\2\2\2\u01a1\u01a7\3\2\2\2\u01a2\u01a4\t\4\2\2")
        buf.write("\u01a3\u01a5\5_\60\2\u01a4\u01a3\3\2\2\2\u01a4\u01a5\3")
        buf.write("\2\2\2\u01a5\u01a7\3\2\2\2\u01a6\u019e\3\2\2\2\u01a6\u01a2")
        buf.write("\3\2\2\2\u01a7\u01ab\3\2\2\2\u01a8\u01aa\13\2\2\2\u01a9")
        buf.write("\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01ac\3\2\2\2")
        buf.write("\u01ab\u01a9\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3")
        buf.write("\2\2\2\u01ae\u01af\7$\2\2\u01af\u01b0\bA\5\2\u01b0\u0082")
        buf.write("\3\2\2\2\u01b1\u01b2\13\2\2\2\u01b2\u0084\3\2\2\2\31\2")
        buf.write("\u0087\u008c\u008e\u0115\u011a\u011c\u0137\u013a\u013e")
        buf.write("\u0150\u0156\u0163\u0167\u017f\u0187\u018f\u0193\u019b")
        buf.write("\u01a0\u01a4\u01a6\u01ab\6\3\62\2\b\2\2\3@\3\3A\4")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    MAIN = 2
    TRUE = 3
    FALSE = 4
    KWNUMBER = 5
    KWBOOL = 6
    KWSTRING = 7
    RETURN = 8
    VAR = 9
    DYNAMIC = 10
    FUNC = 11
    FOR = 12
    UNTIL = 13
    BY = 14
    BREAK = 15
    CONTINUE = 16
    IF = 17
    ELSE = 18
    ELIF = 19
    BEGIN = 20
    END = 21
    NOT = 22
    AND = 23
    OR = 24
    ADD = 25
    SUB = 26
    MUL = 27
    DIV = 28
    MOD = 29
    COMPARENUM = 30
    COMPARESTR = 31
    ASSIGN = 32
    CONCAT = 33
    OPENPAREN = 34
    CLOSEPAREN = 35
    OPENSQBRACKET = 36
    CLOSESQBRACKET = 37
    COMMA = 38
    NEWLINE = 39
    NUMBER = 40
    STRING = 41
    CMT = 42
    WS = 43
    UNCLOSE_STRING = 44
    ILLEGAL_ESCAPE = 45
    ERROR_CHAR = 46

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'=='", "'<-'", "'...'", "'('", "')'", 
            "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "MAIN", "TRUE", "FALSE", "KWNUMBER", "KWBOOL", 
            "KWSTRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
            "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
            "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "COMPARENUM", 
            "COMPARESTR", "ASSIGN", "CONCAT", "OPENPAREN", "CLOSEPAREN", 
            "OPENSQBRACKET", "CLOSESQBRACKET", "COMMA", "NEWLINE", "NUMBER", 
            "STRING", "CMT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "IDENTIFIER", "MAIN", "TRUE", "FALSE", "KWNUMBER", "KWBOOL", 
                  "KWSTRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", 
                  "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
                  "BEGIN", "END", "NOT", "AND", "OR", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "COMPARENUM", "COMPARESTR", "ASSIGN", "CONCAT", 
                  "OPENPAREN", "CLOSEPAREN", "OPENSQBRACKET", "CLOSESQBRACKET", 
                  "COMMA", "NEWLINE", "NUMBER", "ES", "ES_BACKSLASH", "ES_SINGLEQUOTE", 
                  "POSTFIX_ES_BACKSLASH", "POSTFIX_ES_SINGLEQUOTE", "NOT_POSTFIX_ES_BACKSLASH", 
                  "NOT_POSTFIX_ES_SINGLEQUOTE", "STRING_CHAR", "STRING", 
                  "Char", "LowChar", "Num", "Expo", "DoubleQuote", "BACKSPACE", 
                  "FORMFEED", "CR", "TAB", "SINGLEQUOTE", "BACKSLASH", "CMT", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.STRING_action 
            actions[62] = self.UNCLOSE_STRING_action 
            actions[63] = self.ILLEGAL_ESCAPE_action 
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

                imposible = ["'",'\b','\f','\r','\n','\\']
                if(self.text[-1] in imposible): #EOF?
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

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

     


