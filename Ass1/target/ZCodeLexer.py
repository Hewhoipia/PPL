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
        buf.write("\u01c2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n(\3)\3)\3)\3)\3)\5)\u013b\n)\3*\3*\3*\3*\5*\u0141\n")
        buf.write("*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\5/\u014d\n/\3\60\3\60")
        buf.write("\7\60\u0151\n\60\f\60\16\60\u0154\13\60\3\60\3\60\3\60")
        buf.write("\3\61\3\61\5\61\u015b\n\61\3\61\3\61\3\61\7\61\u0160\n")
        buf.write("\61\f\61\16\61\u0163\13\61\3\62\3\62\3\63\3\63\3\64\3")
        buf.write("\64\3\65\3\65\5\65\u016d\n\65\3\65\6\65\u0170\n\65\r\65")
        buf.write("\16\65\u0171\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;")
        buf.write("\3;\3;\5;\u0181\n;\3<\3<\3<\3=\3=\3=\3=\7=\u018a\n=\f")
        buf.write("=\16=\u018d\13=\3=\3=\3>\6>\u0192\n>\r>\16>\u0193\3>\3")
        buf.write(">\3?\3?\7?\u019a\n?\f?\16?\u019d\13?\3?\3?\7?\u01a1\n")
        buf.write("?\f?\16?\u01a4\13?\3?\5?\u01a7\n?\3?\3?\5?\u01ab\n?\3")
        buf.write("@\3@\7@\u01af\n@\f@\16@\u01b2\13@\3@\3@\5@\u01b6\n@\3")
        buf.write("@\7@\u01b9\n@\f@\16@\u01bc\13@\3@\3@\3@\3A\3A\4\u018b")
        buf.write("\u01ba\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O\2Q\2S\2U\2W\2Y\2[\2]\2_)a*c\2e\2g\2i\2k\2")
        buf.write("m\2o\2q\2s\2u\2w\2y+{,}-\177.\u0081/\3\2\17\4\2>>@@\b")
        buf.write("\2))^^ddhhttvv\3\2$$\7\2\n\f\16\17$$))^^\4\2C\\c|\3\2")
        buf.write("c|\3\2\62;\4\2GGgg\4\2--//\3\2))\4\2\13\13\"\"\3\3\f\f")
        buf.write("\3\2^^\2\u01cc\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\3\u0083\3\2\2\2\5\u0088\3\2\2\2\7\u008e")
        buf.write("\3\2\2\2\t\u0095\3\2\2\2\13\u009a\3\2\2\2\r\u00a1\3\2")
        buf.write("\2\2\17\u00a8\3\2\2\2\21\u00ac\3\2\2\2\23\u00b4\3\2\2")
        buf.write("\2\25\u00b9\3\2\2\2\27\u00bd\3\2\2\2\31\u00c3\3\2\2\2")
        buf.write("\33\u00c6\3\2\2\2\35\u00cc\3\2\2\2\37\u00d5\3\2\2\2!\u00d8")
        buf.write("\3\2\2\2#\u00dd\3\2\2\2%\u00e2\3\2\2\2\'\u00e8\3\2\2\2")
        buf.write(")\u00ec\3\2\2\2+\u00f0\3\2\2\2-\u00f4\3\2\2\2/\u00f7\3")
        buf.write("\2\2\2\61\u00f9\3\2\2\2\63\u00fb\3\2\2\2\65\u00fd\3\2")
        buf.write("\2\2\67\u00ff\3\2\2\29\u0109\3\2\2\2;\u010b\3\2\2\2=\u010e")
        buf.write("\3\2\2\2?\u0111\3\2\2\2A\u0115\3\2\2\2C\u0117\3\2\2\2")
        buf.write("E\u0119\3\2\2\2G\u011b\3\2\2\2I\u011d\3\2\2\2K\u011f\3")
        buf.write("\2\2\2M\u0122\3\2\2\2O\u0133\3\2\2\2Q\u013a\3\2\2\2S\u0140")
        buf.write("\3\2\2\2U\u0142\3\2\2\2W\u0144\3\2\2\2Y\u0146\3\2\2\2")
        buf.write("[\u0148\3\2\2\2]\u014c\3\2\2\2_\u014e\3\2\2\2a\u015a\3")
        buf.write("\2\2\2c\u0164\3\2\2\2e\u0166\3\2\2\2g\u0168\3\2\2\2i\u016a")
        buf.write("\3\2\2\2k\u0173\3\2\2\2m\u0175\3\2\2\2o\u0177\3\2\2\2")
        buf.write("q\u0179\3\2\2\2s\u017b\3\2\2\2u\u0180\3\2\2\2w\u0182\3")
        buf.write("\2\2\2y\u0185\3\2\2\2{\u0191\3\2\2\2}\u01aa\3\2\2\2\177")
        buf.write("\u01ac\3\2\2\2\u0081\u01c0\3\2\2\2\u0083\u0084\7v\2\2")
        buf.write("\u0084\u0085\7t\2\2\u0085\u0086\7w\2\2\u0086\u0087\7g")
        buf.write("\2\2\u0087\4\3\2\2\2\u0088\u0089\7h\2\2\u0089\u008a\7")
        buf.write("c\2\2\u008a\u008b\7n\2\2\u008b\u008c\7u\2\2\u008c\u008d")
        buf.write("\7g\2\2\u008d\6\3\2\2\2\u008e\u008f\7p\2\2\u008f\u0090")
        buf.write("\7w\2\2\u0090\u0091\7o\2\2\u0091\u0092\7d\2\2\u0092\u0093")
        buf.write("\7g\2\2\u0093\u0094\7t\2\2\u0094\b\3\2\2\2\u0095\u0096")
        buf.write("\7d\2\2\u0096\u0097\7q\2\2\u0097\u0098\7q\2\2\u0098\u0099")
        buf.write("\7n\2\2\u0099\n\3\2\2\2\u009a\u009b\7u\2\2\u009b\u009c")
        buf.write("\7v\2\2\u009c\u009d\7t\2\2\u009d\u009e\7k\2\2\u009e\u009f")
        buf.write("\7p\2\2\u009f\u00a0\7i\2\2\u00a0\f\3\2\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4\7v\2\2\u00a4\u00a5")
        buf.write("\7w\2\2\u00a5\u00a6\7t\2\2\u00a6\u00a7\7p\2\2\u00a7\16")
        buf.write("\3\2\2\2\u00a8\u00a9\7x\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\20\3\2\2\2\u00ac\u00ad\7f\2\2\u00ad\u00ae")
        buf.write("\7{\2\2\u00ae\u00af\7p\2\2\u00af\u00b0\7c\2\2\u00b0\u00b1")
        buf.write("\7o\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3\7e\2\2\u00b3\22")
        buf.write("\3\2\2\2\u00b4\u00b5\7h\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7p\2\2\u00b7\u00b8\7e\2\2\u00b8\24\3\2\2\2\u00b9\u00ba")
        buf.write("\7h\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc\7t\2\2\u00bc\26")
        buf.write("\3\2\2\2\u00bd\u00be\7w\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0")
        buf.write("\7v\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2\7n\2\2\u00c2\30")
        buf.write("\3\2\2\2\u00c3\u00c4\7d\2\2\u00c4\u00c5\7{\2\2\u00c5\32")
        buf.write("\3\2\2\2\u00c6\u00c7\7d\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb\7m\2\2\u00cb\34")
        buf.write("\3\2\2\2\u00cc\u00cd\7e\2\2\u00cd\u00ce\7q\2\2\u00ce\u00cf")
        buf.write("\7p\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2")
        buf.write("\7p\2\2\u00d2\u00d3\7w\2\2\u00d3\u00d4\7g\2\2\u00d4\36")
        buf.write("\3\2\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7h\2\2\u00d7 ")
        buf.write("\3\2\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7n\2\2\u00da\u00db")
        buf.write("\7u\2\2\u00db\u00dc\7g\2\2\u00dc\"\3\2\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7n\2\2\u00df\u00e0\7k\2\2\u00e0\u00e1")
        buf.write("\7h\2\2\u00e1$\3\2\2\2\u00e2\u00e3\7d\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\u00e5\7i\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7&\3\2\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea")
        buf.write("\7p\2\2\u00ea\u00eb\7f\2\2\u00eb(\3\2\2\2\u00ec\u00ed")
        buf.write("\7p\2\2\u00ed\u00ee\7q\2\2\u00ee\u00ef\7v\2\2\u00ef*\3")
        buf.write("\2\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2\7p\2\2\u00f2\u00f3")
        buf.write("\7f\2\2\u00f3,\3\2\2\2\u00f4\u00f5\7q\2\2\u00f5\u00f6")
        buf.write("\7t\2\2\u00f6.\3\2\2\2\u00f7\u00f8\7-\2\2\u00f8\60\3\2")
        buf.write("\2\2\u00f9\u00fa\7/\2\2\u00fa\62\3\2\2\2\u00fb\u00fc\7")
        buf.write(",\2\2\u00fc\64\3\2\2\2\u00fd\u00fe\7\61\2\2\u00fe\66\3")
        buf.write("\2\2\2\u00ff\u0100\7\'\2\2\u01008\3\2\2\2\u0101\u0103")
        buf.write("\7#\2\2\u0102\u0101\3\2\2\2\u0102\u0103\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u010a\7?\2\2\u0105\u0107\t\2\2\2")
        buf.write("\u0106\u0108\7?\2\2\u0107\u0106\3\2\2\2\u0107\u0108\3")
        buf.write("\2\2\2\u0108\u010a\3\2\2\2\u0109\u0102\3\2\2\2\u0109\u0105")
        buf.write("\3\2\2\2\u010a:\3\2\2\2\u010b\u010c\7?\2\2\u010c\u010d")
        buf.write("\7?\2\2\u010d<\3\2\2\2\u010e\u010f\7>\2\2\u010f\u0110")
        buf.write("\7/\2\2\u0110>\3\2\2\2\u0111\u0112\7\60\2\2\u0112\u0113")
        buf.write("\7\60\2\2\u0113\u0114\7\60\2\2\u0114@\3\2\2\2\u0115\u0116")
        buf.write("\7*\2\2\u0116B\3\2\2\2\u0117\u0118\7+\2\2\u0118D\3\2\2")
        buf.write("\2\u0119\u011a\7]\2\2\u011aF\3\2\2\2\u011b\u011c\7_\2")
        buf.write("\2\u011cH\3\2\2\2\u011d\u011e\7.\2\2\u011eJ\3\2\2\2\u011f")
        buf.write("\u0120\7\f\2\2\u0120L\3\2\2\2\u0121\u0123\5g\64\2\u0122")
        buf.write("\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0122\3\2\2\2")
        buf.write("\u0124\u0125\3\2\2\2\u0125\u012c\3\2\2\2\u0126\u0128\7")
        buf.write("\60\2\2\u0127\u0129\5g\64\2\u0128\u0127\3\2\2\2\u0129")
        buf.write("\u012a\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012d\3\2\2\2\u012c\u0126\3\2\2\2\u012c\u012d\3")
        buf.write("\2\2\2\u012d\u012f\3\2\2\2\u012e\u0130\5i\65\2\u012f\u012e")
        buf.write("\3\2\2\2\u012f\u0130\3\2\2\2\u0130N\3\2\2\2\u0131\u0134")
        buf.write("\5Q)\2\u0132\u0134\5S*\2\u0133\u0131\3\2\2\2\u0133\u0132")
        buf.write("\3\2\2\2\u0134P\3\2\2\2\u0135\u013b\5m\67\2\u0136\u013b")
        buf.write("\5o8\2\u0137\u013b\5q9\2\u0138\u013b\5s:\2\u0139\u013b")
        buf.write("\5w<\2\u013a\u0135\3\2\2\2\u013a\u0136\3\2\2\2\u013a\u0137")
        buf.write("\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013b")
        buf.write("R\3\2\2\2\u013c\u013d\5u;\2\u013d\u013e\5k\66\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u0141\5u;\2\u0140\u013c\3\2\2\2\u0140")
        buf.write("\u013f\3\2\2\2\u0141T\3\2\2\2\u0142\u0143\t\3\2\2\u0143")
        buf.write("V\3\2\2\2\u0144\u0145\t\4\2\2\u0145X\3\2\2\2\u0146\u0147")
        buf.write("\n\3\2\2\u0147Z\3\2\2\2\u0148\u0149\n\4\2\2\u0149\\\3")
        buf.write("\2\2\2\u014a\u014d\n\5\2\2\u014b\u014d\5O(\2\u014c\u014a")
        buf.write("\3\2\2\2\u014c\u014b\3\2\2\2\u014d^\3\2\2\2\u014e\u0152")
        buf.write("\5k\66\2\u014f\u0151\5]/\2\u0150\u014f\3\2\2\2\u0151\u0154")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0155\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156\5k\66\2")
        buf.write("\u0156\u0157\b\60\2\2\u0157`\3\2\2\2\u0158\u015b\5c\62")
        buf.write("\2\u0159\u015b\7a\2\2\u015a\u0158\3\2\2\2\u015a\u0159")
        buf.write("\3\2\2\2\u015b\u0161\3\2\2\2\u015c\u0160\5c\62\2\u015d")
        buf.write("\u0160\5g\64\2\u015e\u0160\7a\2\2\u015f\u015c\3\2\2\2")
        buf.write("\u015f\u015d\3\2\2\2\u015f\u015e\3\2\2\2\u0160\u0163\3")
        buf.write("\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162b")
        buf.write("\3\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\t\6\2\2\u0165")
        buf.write("d\3\2\2\2\u0166\u0167\t\7\2\2\u0167f\3\2\2\2\u0168\u0169")
        buf.write("\t\b\2\2\u0169h\3\2\2\2\u016a\u016c\t\t\2\2\u016b\u016d")
        buf.write("\t\n\2\2\u016c\u016b\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("\u016f\3\2\2\2\u016e\u0170\5g\64\2\u016f\u016e\3\2\2\2")
        buf.write("\u0170\u0171\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3")
        buf.write("\2\2\2\u0172j\3\2\2\2\u0173\u0174\7$\2\2\u0174l\3\2\2")
        buf.write("\2\u0175\u0176\7\n\2\2\u0176n\3\2\2\2\u0177\u0178\7\16")
        buf.write("\2\2\u0178p\3\2\2\2\u0179\u017a\7\17\2\2\u017ar\3\2\2")
        buf.write("\2\u017b\u017c\7\13\2\2\u017ct\3\2\2\2\u017d\u017e\7^")
        buf.write("\2\2\u017e\u0181\t\13\2\2\u017f\u0181\t\13\2\2\u0180\u017d")
        buf.write("\3\2\2\2\u0180\u017f\3\2\2\2\u0181v\3\2\2\2\u0182\u0183")
        buf.write("\7^\2\2\u0183\u0184\7^\2\2\u0184x\3\2\2\2\u0185\u0186")
        buf.write("\7%\2\2\u0186\u0187\7%\2\2\u0187\u018b\3\2\2\2\u0188\u018a")
        buf.write("\13\2\2\2\u0189\u0188\3\2\2\2\u018a\u018d\3\2\2\2\u018b")
        buf.write("\u018c\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u018e\3\2\2\2")
        buf.write("\u018d\u018b\3\2\2\2\u018e\u018f\b=\3\2\u018fz\3\2\2\2")
        buf.write("\u0190\u0192\t\f\2\2\u0191\u0190\3\2\2\2\u0192\u0193\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u0196\b>\3\2\u0196|\3\2\2\2\u0197\u019b")
        buf.write("\5k\66\2\u0198\u019a\5]/\2\u0199\u0198\3\2\2\2\u019a\u019d")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c")
        buf.write("\u01ab\3\2\2\2\u019d\u019b\3\2\2\2\u019e\u01a2\5k\66\2")
        buf.write("\u019f\u01a1\5]/\2\u01a0\u019f\3\2\2\2\u01a1\u01a4\3\2")
        buf.write("\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a6")
        buf.write("\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a7\t\r\2\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\5k\66\2")
        buf.write("\u01a9\u01ab\3\2\2\2\u01aa\u0197\3\2\2\2\u01aa\u019e\3")
        buf.write("\2\2\2\u01ab~\3\2\2\2\u01ac\u01b0\5k\66\2\u01ad\u01af")
        buf.write("\5]/\2\u01ae\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b3\3\2\2\2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b3\u01b5\t\16\2\2\u01b4\u01b6\5Y-\2")
        buf.write("\u01b5\u01b4\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01ba\3")
        buf.write("\2\2\2\u01b7\u01b9\13\2\2\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("\u01bc\3\2\2\2\u01ba\u01bb\3\2\2\2\u01ba\u01b8\3\2\2\2")
        buf.write("\u01bb\u01bd\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd\u01be\5")
        buf.write("k\66\2\u01be\u01bf\b@\4\2\u01bf\u0080\3\2\2\2\u01c0\u01c1")
        buf.write("\13\2\2\2\u01c1\u0082\3\2\2\2\36\2\u0102\u0107\u0109\u0124")
        buf.write("\u012a\u012c\u012f\u0133\u013a\u0140\u014c\u0152\u015a")
        buf.write("\u015f\u0161\u016c\u0171\u0180\u018b\u0193\u019b\u01a2")
        buf.write("\u01a6\u01aa\u01b0\u01b5\u01ba\5\3\60\2\b\2\2\3@\3")
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


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[46] = self.STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

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

     


