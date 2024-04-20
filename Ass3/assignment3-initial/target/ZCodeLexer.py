# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


# 2153043
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u018b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\3\2\3\2\5\2z\n\2\3\2\5\2}\n\2\3\3\6\3\u0080\n\3")
        buf.write("\r\3\16\3\u0081\3\4\3\4\7\4\u0086\n\4\f\4\16\4\u0089\13")
        buf.write("\4\3\5\3\5\5\5\u008d\n\5\3\5\6\5\u0090\n\5\r\5\16\5\u0091")
        buf.write("\3\6\3\6\7\6\u0096\n\6\f\6\16\6\u0099\13\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\7\7\u00a0\n\7\f\7\16\7\u00a3\13\7\3\7\3\7\5\7")
        buf.write("\u00a7\n\7\3\7\3\7\3\b\3\b\7\b\u00ad\n\b\f\b\16\b\u00b0")
        buf.write("\13\b\3\b\3\b\3\b\3\t\3\t\5\t\u00b7\n\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\7\63\u015c\n\63\f\63\16\63\u015f\13\63\3\64\3\64\3")
        buf.write("\64\3\64\7\64\u0165\n\64\f\64\16\64\u0168\13\64\3\64\3")
        buf.write("\64\3\65\3\65\3\66\3\66\3\66\3\66\3\67\6\67\u0173\n\67")
        buf.write("\r\67\16\67\u0174\3\67\3\67\38\38\58\u017b\n8\39\39\3")
        buf.write("9\39\59\u0181\n9\3:\3:\3:\3:\5:\u0187\n:\3;\3;\3;\5\u0097")
        buf.write("\u00a1\u00ae\2<\3\3\5\2\7\2\t\2\13\4\r\5\17\6\21\7\23")
        buf.write("\b\25\t\27\n\31\13\33\f\35\r\37\16!\17#\20%\21\'\22)\23")
        buf.write("+\24-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A")
        buf.write("\37C E!G\"I#K$M%O&Q\'S(U)W*Y+[,]-_.a/c\60e\61g\62i\63")
        buf.write("k\64m\65o\2q\2s\2u\66\3\2\f\3\2\62;\4\2GGgg\4\2--//\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\f\f\5\2\n\13\16\16\"\"\5")
        buf.write("\2\f\f$$^^\n\2\"\"))^^ddhhppttvv\3\2$$\2\u0195\2\3\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("u\3\2\2\2\3w\3\2\2\2\5\177\3\2\2\2\7\u0083\3\2\2\2\t\u008a")
        buf.write("\3\2\2\2\13\u0093\3\2\2\2\r\u009d\3\2\2\2\17\u00aa\3\2")
        buf.write("\2\2\21\u00b6\3\2\2\2\23\u00b8\3\2\2\2\25\u00bd\3\2\2")
        buf.write("\2\27\u00c3\3\2\2\2\31\u00ca\3\2\2\2\33\u00cf\3\2\2\2")
        buf.write("\35\u00d6\3\2\2\2\37\u00dd\3\2\2\2!\u00e1\3\2\2\2#\u00e9")
        buf.write("\3\2\2\2%\u00ee\3\2\2\2\'\u00f2\3\2\2\2)\u00f8\3\2\2\2")
        buf.write("+\u00fb\3\2\2\2-\u0101\3\2\2\2/\u010a\3\2\2\2\61\u010d")
        buf.write("\3\2\2\2\63\u0112\3\2\2\2\65\u0117\3\2\2\2\67\u011d\3")
        buf.write("\2\2\29\u0121\3\2\2\2;\u0125\3\2\2\2=\u0129\3\2\2\2?\u012c")
        buf.write("\3\2\2\2A\u012e\3\2\2\2C\u0130\3\2\2\2E\u0132\3\2\2\2")
        buf.write("G\u0134\3\2\2\2I\u0136\3\2\2\2K\u0138\3\2\2\2M\u013b\3")
        buf.write("\2\2\2O\u013e\3\2\2\2Q\u0141\3\2\2\2S\u0143\3\2\2\2U\u0146")
        buf.write("\3\2\2\2W\u0148\3\2\2\2Y\u014b\3\2\2\2[\u014f\3\2\2\2")
        buf.write("]\u0151\3\2\2\2_\u0153\3\2\2\2a\u0155\3\2\2\2c\u0157\3")
        buf.write("\2\2\2e\u0159\3\2\2\2g\u0160\3\2\2\2i\u016b\3\2\2\2k\u016d")
        buf.write("\3\2\2\2m\u0172\3\2\2\2o\u017a\3\2\2\2q\u0180\3\2\2\2")
        buf.write("s\u0186\3\2\2\2u\u0188\3\2\2\2wy\5\5\3\2xz\5\7\4\2yx\3")
        buf.write("\2\2\2yz\3\2\2\2z|\3\2\2\2{}\5\t\5\2|{\3\2\2\2|}\3\2\2")
        buf.write("\2}\4\3\2\2\2~\u0080\t\2\2\2\177~\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\6")
        buf.write("\3\2\2\2\u0083\u0087\7\60\2\2\u0084\u0086\t\2\2\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\b\3\2\2\2\u0089\u0087\3\2\2")
        buf.write("\2\u008a\u008c\t\3\2\2\u008b\u008d\t\4\2\2\u008c\u008b")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e")
        buf.write("\u0090\t\2\2\2\u008f\u008e\3\2\2\2\u0090\u0091\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092\n\3\2\2")
        buf.write("\2\u0093\u0097\7$\2\2\u0094\u0096\5o8\2\u0095\u0094\3")
        buf.write("\2\2\2\u0096\u0099\3\2\2\2\u0097\u0098\3\2\2\2\u0097\u0095")
        buf.write("\3\2\2\2\u0098\u009a\3\2\2\2\u0099\u0097\3\2\2\2\u009a")
        buf.write("\u009b\7$\2\2\u009b\u009c\b\6\2\2\u009c\f\3\2\2\2\u009d")
        buf.write("\u00a1\7$\2\2\u009e\u00a0\5o8\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a2\u00a6\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a7\5")
        buf.write("i\65\2\u00a5\u00a7\7\2\2\3\u00a6\u00a4\3\2\2\2\u00a6\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\b\7\3\2\u00a9")
        buf.write("\16\3\2\2\2\u00aa\u00ae\7$\2\2\u00ab\u00ad\5o8\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00af\3\2\2\2")
        buf.write("\u00ae\u00ac\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b1\u00b2\5s:\2\u00b2\u00b3\b\b\4\2\u00b3\20")
        buf.write("\3\2\2\2\u00b4\u00b7\5\23\n\2\u00b5\u00b7\5\25\13\2\u00b6")
        buf.write("\u00b4\3\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\22\3\2\2\2\u00b8")
        buf.write("\u00b9\7v\2\2\u00b9\u00ba\7t\2\2\u00ba\u00bb\7w\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\24\3\2\2\2\u00bd\u00be\7h\2\2\u00be")
        buf.write("\u00bf\7c\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7u\2\2\u00c1")
        buf.write("\u00c2\7g\2\2\u00c2\26\3\2\2\2\u00c3\u00c4\7p\2\2\u00c4")
        buf.write("\u00c5\7w\2\2\u00c5\u00c6\7o\2\2\u00c6\u00c7\7d\2\2\u00c7")
        buf.write("\u00c8\7g\2\2\u00c8\u00c9\7t\2\2\u00c9\30\3\2\2\2\u00ca")
        buf.write("\u00cb\7d\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7q\2\2\u00cd")
        buf.write("\u00ce\7n\2\2\u00ce\32\3\2\2\2\u00cf\u00d0\7u\2\2\u00d0")
        buf.write("\u00d1\7v\2\2\u00d1\u00d2\7t\2\2\u00d2\u00d3\7k\2\2\u00d3")
        buf.write("\u00d4\7p\2\2\u00d4\u00d5\7i\2\2\u00d5\34\3\2\2\2\u00d6")
        buf.write("\u00d7\7t\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7v\2\2\u00d9")
        buf.write("\u00da\7w\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7p\2\2\u00dc")
        buf.write("\36\3\2\2\2\u00dd\u00de\7x\2\2\u00de\u00df\7c\2\2\u00df")
        buf.write("\u00e0\7t\2\2\u00e0 \3\2\2\2\u00e1\u00e2\7f\2\2\u00e2")
        buf.write("\u00e3\7{\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7c\2\2\u00e5")
        buf.write("\u00e6\7o\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7e\2\2\u00e8")
        buf.write("\"\3\2\2\2\u00e9\u00ea\7h\2\2\u00ea\u00eb\7w\2\2\u00eb")
        buf.write("\u00ec\7p\2\2\u00ec\u00ed\7e\2\2\u00ed$\3\2\2\2\u00ee")
        buf.write("\u00ef\7h\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7t\2\2\u00f1")
        buf.write("&\3\2\2\2\u00f2\u00f3\7w\2\2\u00f3\u00f4\7p\2\2\u00f4")
        buf.write("\u00f5\7v\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7n\2\2\u00f7")
        buf.write("(\3\2\2\2\u00f8\u00f9\7d\2\2\u00f9\u00fa\7{\2\2\u00fa")
        buf.write("*\3\2\2\2\u00fb\u00fc\7d\2\2\u00fc\u00fd\7t\2\2\u00fd")
        buf.write("\u00fe\7g\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7m\2\2\u0100")
        buf.write(",\3\2\2\2\u0101\u0102\7e\2\2\u0102\u0103\7q\2\2\u0103")
        buf.write("\u0104\7p\2\2\u0104\u0105\7v\2\2\u0105\u0106\7k\2\2\u0106")
        buf.write("\u0107\7p\2\2\u0107\u0108\7w\2\2\u0108\u0109\7g\2\2\u0109")
        buf.write(".\3\2\2\2\u010a\u010b\7k\2\2\u010b\u010c\7h\2\2\u010c")
        buf.write("\60\3\2\2\2\u010d\u010e\7g\2\2\u010e\u010f\7n\2\2\u010f")
        buf.write("\u0110\7u\2\2\u0110\u0111\7g\2\2\u0111\62\3\2\2\2\u0112")
        buf.write("\u0113\7g\2\2\u0113\u0114\7n\2\2\u0114\u0115\7k\2\2\u0115")
        buf.write("\u0116\7h\2\2\u0116\64\3\2\2\2\u0117\u0118\7d\2\2\u0118")
        buf.write("\u0119\7g\2\2\u0119\u011a\7i\2\2\u011a\u011b\7k\2\2\u011b")
        buf.write("\u011c\7p\2\2\u011c\66\3\2\2\2\u011d\u011e\7g\2\2\u011e")
        buf.write("\u011f\7p\2\2\u011f\u0120\7f\2\2\u01208\3\2\2\2\u0121")
        buf.write("\u0122\7p\2\2\u0122\u0123\7q\2\2\u0123\u0124\7v\2\2\u0124")
        buf.write(":\3\2\2\2\u0125\u0126\7c\2\2\u0126\u0127\7p\2\2\u0127")
        buf.write("\u0128\7f\2\2\u0128<\3\2\2\2\u0129\u012a\7q\2\2\u012a")
        buf.write("\u012b\7t\2\2\u012b>\3\2\2\2\u012c\u012d\7-\2\2\u012d")
        buf.write("@\3\2\2\2\u012e\u012f\7/\2\2\u012fB\3\2\2\2\u0130\u0131")
        buf.write("\7,\2\2\u0131D\3\2\2\2\u0132\u0133\7\61\2\2\u0133F\3\2")
        buf.write("\2\2\u0134\u0135\7\'\2\2\u0135H\3\2\2\2\u0136\u0137\7")
        buf.write("?\2\2\u0137J\3\2\2\2\u0138\u0139\7?\2\2\u0139\u013a\7")
        buf.write("?\2\2\u013aL\3\2\2\2\u013b\u013c\7#\2\2\u013c\u013d\7")
        buf.write("?\2\2\u013dN\3\2\2\2\u013e\u013f\7>\2\2\u013f\u0140\7")
        buf.write("/\2\2\u0140P\3\2\2\2\u0141\u0142\7>\2\2\u0142R\3\2\2\2")
        buf.write("\u0143\u0144\7>\2\2\u0144\u0145\7?\2\2\u0145T\3\2\2\2")
        buf.write("\u0146\u0147\7@\2\2\u0147V\3\2\2\2\u0148\u0149\7@\2\2")
        buf.write("\u0149\u014a\7?\2\2\u014aX\3\2\2\2\u014b\u014c\7\60\2")
        buf.write("\2\u014c\u014d\7\60\2\2\u014d\u014e\7\60\2\2\u014eZ\3")
        buf.write("\2\2\2\u014f\u0150\7*\2\2\u0150\\\3\2\2\2\u0151\u0152")
        buf.write("\7+\2\2\u0152^\3\2\2\2\u0153\u0154\7]\2\2\u0154`\3\2\2")
        buf.write("\2\u0155\u0156\7_\2\2\u0156b\3\2\2\2\u0157\u0158\7.\2")
        buf.write("\2\u0158d\3\2\2\2\u0159\u015d\t\5\2\2\u015a\u015c\t\6")
        buf.write("\2\2\u015b\u015a\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015ef\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u0160\u0161\7%\2\2\u0161\u0162\7%\2\2\u0162\u0166")
        buf.write("\3\2\2\2\u0163\u0165\n\7\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2")
        buf.write("\u0167\u0169\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u016a\b")
        buf.write("\64\5\2\u016ah\3\2\2\2\u016b\u016c\7\f\2\2\u016cj\3\2")
        buf.write("\2\2\u016d\u016e\7\17\2\2\u016e\u016f\3\2\2\2\u016f\u0170")
        buf.write("\b\66\5\2\u0170l\3\2\2\2\u0171\u0173\t\b\2\2\u0172\u0171")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0172\3\2\2\2\u0174")
        buf.write("\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176\u0177\b\67\5")
        buf.write("\2\u0177n\3\2\2\2\u0178\u017b\5q9\2\u0179\u017b\n\t\2")
        buf.write("\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2\2\u017bp\3\2")
        buf.write("\2\2\u017c\u017d\7^\2\2\u017d\u0181\t\n\2\2\u017e\u017f")
        buf.write("\7)\2\2\u017f\u0181\7$\2\2\u0180\u017c\3\2\2\2\u0180\u017e")
        buf.write("\3\2\2\2\u0181r\3\2\2\2\u0182\u0183\7^\2\2\u0183\u0187")
        buf.write("\n\n\2\2\u0184\u0185\7)\2\2\u0185\u0187\n\13\2\2\u0186")
        buf.write("\u0182\3\2\2\2\u0186\u0184\3\2\2\2\u0187t\3\2\2\2\u0188")
        buf.write("\u0189\13\2\2\2\u0189\u018a\b;\6\2\u018av\3\2\2\2\24\2")
        buf.write("y|\u0081\u0087\u008c\u0091\u0097\u00a1\u00a6\u00ae\u00b6")
        buf.write("\u015d\u0166\u0174\u017a\u0180\u0186\7\3\6\2\3\7\3\3\b")
        buf.write("\4\b\2\2\3;\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER_LITERAL = 1
    STRING_LITERAL = 2
    UNCLOSE_STRING = 3
    ILLEGAL_ESCAPE = 4
    BOOLEAN_LITERAL = 5
    TRUE = 6
    FALSE = 7
    NUMBER = 8
    BOOLEAN = 9
    STRING = 10
    RETURN = 11
    VAR = 12
    DYNAMIC = 13
    FUNC = 14
    FOR = 15
    UNTIL = 16
    BY = 17
    BREAK = 18
    CONTINUE = 19
    IF = 20
    ELSE = 21
    ELIF = 22
    BEGIN = 23
    END = 24
    NOT = 25
    AND = 26
    OR = 27
    PLUS = 28
    MINUS = 29
    MULTIPLY = 30
    DIVIDE = 31
    MODULO = 32
    EQUAL_NUMBER = 33
    EQUAL_STRING = 34
    NOT_EQUAL = 35
    ASSIGN = 36
    LESS_THAN = 37
    LESS_THAN_OR_EQUAL = 38
    GREATER_THAN = 39
    GREATER_THAN_OR_EQUAL = 40
    CONCAT = 41
    OPEN_ROUND_BRACKET = 42
    CLOSE_ROUND_BRACKET = 43
    OPEN_SQUARE_BRACKET = 44
    CLOSE_SQUARE_BRACKET = 45
    COMMA = 46
    IDENTIFIER = 47
    COMMENT = 48
    NEWLINE = 49
    CARRIAGE_RETURN = 50
    WHITESPACE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'true'", "'false'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'=='", "'!='", "'<-'", "'<'", "'<='", "'>'", 
            "'>='", "'...'", "'('", "')'", "'['", "']'", "','", "'\n'", 
            "'\r'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER_LITERAL", "STRING_LITERAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "BOOLEAN_LITERAL", "TRUE", "FALSE", "NUMBER", "BOOLEAN", "STRING", 
            "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", 
            "OR", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", "EQUAL_NUMBER", 
            "EQUAL_STRING", "NOT_EQUAL", "ASSIGN", "LESS_THAN", "LESS_THAN_OR_EQUAL", 
            "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "CONCAT", "OPEN_ROUND_BRACKET", 
            "CLOSE_ROUND_BRACKET", "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", 
            "COMMA", "IDENTIFIER", "COMMENT", "NEWLINE", "CARRIAGE_RETURN", 
            "WHITESPACE", "ERROR_CHAR" ]

    ruleNames = [ "NUMBER_LITERAL", "INTERGER_PART", "DECIMAL_PART", "EXPONENT_PART", 
                  "STRING_LITERAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "BOOLEAN_LITERAL", "TRUE", "FALSE", "NUMBER", "BOOLEAN", 
                  "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                  "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                  "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MULTIPLY", 
                  "DIVIDE", "MODULO", "EQUAL_NUMBER", "EQUAL_STRING", "NOT_EQUAL", 
                  "ASSIGN", "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
                  "GREATER_THAN_OR_EQUAL", "CONCAT", "OPEN_ROUND_BRACKET", 
                  "CLOSE_ROUND_BRACKET", "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", 
                  "COMMA", "IDENTIFIER", "COMMENT", "NEWLINE", "CARRIAGE_RETURN", 
                  "WHITESPACE", "CHARACTERS_IN_STRING", "LEGAL_ESCAPE_CHARS", 
                  "ILLEGAL_ESCAPE_CHARS", "ERROR_CHAR" ]

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
            actions[4] = self.STRING_LITERAL_action 
            actions[5] = self.UNCLOSE_STRING_action 
            actions[6] = self.ILLEGAL_ESCAPE_action 
            actions[57] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text[1:-1];

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	raise UncloseString(self.text[1:].replace('\r\n', '\n'));

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:]);

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


