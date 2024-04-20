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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u0171\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\5\2R\n\2\3\2\3\2\3\2\3\3\6\3X\n\3")
        buf.write("\r\3\16\3Y\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4e\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\5\5l\n\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\5\6u\n\6\3\7\3\7\3\7\3\7\3\7\5\7|\n\7\3\7\3\7\3")
        buf.write("\b\7\b\u0081\n\b\f\b\16\b\u0084\13\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\t\u008b\n\t\3\t\3\t\3\n\3\n\5\n\u0091\n\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u009c\n\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\5\16\u00a8")
        buf.write("\n\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u00b2")
        buf.write("\n\20\3\20\3\20\3\21\3\21\3\21\5\21\u00b9\n\21\3\21\3")
        buf.write("\21\3\21\3\22\6\22\u00bf\n\22\r\22\16\22\u00c0\3\23\3")
        buf.write("\23\5\23\u00c5\n\23\3\24\3\24\3\24\5\24\u00ca\n\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u00d8\n\24\3\24\5\24\u00db\n\24\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u00e3\n\25\3\25\3\25\5\25\u00e7\n\25")
        buf.write("\3\25\5\25\u00ea\n\25\3\26\3\26\3\26\3\26\5\26\u00f0\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\5\27\u00f7\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u00ff\n\30\3\31\3\31\3\31\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u0108\n\32\3\33\6\33\u010b\n\33")
        buf.write("\r\33\16\33\u010c\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u0117\n\35\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\5\37\u0120\n\37\3 \3 \3 \3 \3 \5 \u0127\n \3!\3!\3!\3")
        buf.write("!\3!\3!\7!\u012f\n!\f!\16!\u0132\13!\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\7\"\u013a\n\"\f\"\16\"\u013d\13\"\3#\3#\3#\3#\3")
        buf.write("#\3#\7#\u0145\n#\f#\16#\u0148\13#\3$\3$\3$\5$\u014d\n")
        buf.write("$\3%\3%\3%\5%\u0152\n%\3&\3&\3&\3&\3&\5&\u0159\n&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\5&\u0163\n&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\5\'\u016b\n\'\3(\3(\3(\3(\3(\2\5@BD)\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLN\2\7\3\2\n\f\4\2#%\'*\3\2\34\35\3\2\36\37\3\2 \"\2")
        buf.write("\u017d\2Q\3\2\2\2\4W\3\2\2\2\6d\3\2\2\2\bf\3\2\2\2\nq")
        buf.write("\3\2\2\2\fv\3\2\2\2\16\u0082\3\2\2\2\20\u0085\3\2\2\2")
        buf.write("\22\u008e\3\2\2\2\24\u0094\3\2\2\2\26\u009f\3\2\2\2\30")
        buf.write("\u00a2\3\2\2\2\32\u00a5\3\2\2\2\34\u00ab\3\2\2\2\36\u00ae")
        buf.write("\3\2\2\2 \u00b5\3\2\2\2\"\u00be\3\2\2\2$\u00c4\3\2\2\2")
        buf.write("&\u00da\3\2\2\2(\u00dc\3\2\2\2*\u00ef\3\2\2\2,\u00f6\3")
        buf.write("\2\2\2.\u00f8\3\2\2\2\60\u0100\3\2\2\2\62\u0107\3\2\2")
        buf.write("\2\64\u010a\3\2\2\2\66\u010e\3\2\2\28\u0116\3\2\2\2:\u0118")
        buf.write("\3\2\2\2<\u011f\3\2\2\2>\u0126\3\2\2\2@\u0128\3\2\2\2")
        buf.write("B\u0133\3\2\2\2D\u013e\3\2\2\2F\u014c\3\2\2\2H\u0151\3")
        buf.write("\2\2\2J\u0162\3\2\2\2L\u016a\3\2\2\2N\u016c\3\2\2\2PR")
        buf.write("\5\64\33\2QP\3\2\2\2QR\3\2\2\2RS\3\2\2\2ST\5\"\22\2TU")
        buf.write("\7\2\2\3U\3\3\2\2\2VX\5\6\4\2WV\3\2\2\2XY\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z\5\3\2\2\2[e\5&\24\2\\e\5\b\5\2]e\5\n")
        buf.write("\6\2^e\5\24\13\2_e\5\26\f\2`e\5\30\r\2ae\5\32\16\2be\5")
        buf.write("\34\17\2ce\5 \21\2d[\3\2\2\2d\\\3\2\2\2d]\3\2\2\2d^\3")
        buf.write("\2\2\2d_\3\2\2\2d`\3\2\2\2da\3\2\2\2db\3\2\2\2dc\3\2\2")
        buf.write("\2e\7\3\2\2\2fk\7\61\2\2gh\7.\2\2hi\5\66\34\2ij\7/\2\2")
        buf.write("jl\3\2\2\2kg\3\2\2\2kl\3\2\2\2lm\3\2\2\2mn\7&\2\2no\5")
        buf.write(":\36\2op\5\64\33\2p\t\3\2\2\2qr\5\f\7\2rt\5\16\b\2su\5")
        buf.write("\22\n\2ts\3\2\2\2tu\3\2\2\2u\13\3\2\2\2vw\7\26\2\2wx\7")
        buf.write(",\2\2xy\5:\36\2y{\7-\2\2z|\5\64\33\2{z\3\2\2\2{|\3\2\2")
        buf.write("\2|}\3\2\2\2}~\5\6\4\2~\r\3\2\2\2\177\u0081\5\20\t\2\u0080")
        buf.write("\177\3\2\2\2\u0081\u0084\3\2\2\2\u0082\u0080\3\2\2\2\u0082")
        buf.write("\u0083\3\2\2\2\u0083\17\3\2\2\2\u0084\u0082\3\2\2\2\u0085")
        buf.write("\u0086\7\30\2\2\u0086\u0087\7,\2\2\u0087\u0088\5:\36\2")
        buf.write("\u0088\u008a\7-\2\2\u0089\u008b\5\64\33\2\u008a\u0089")
        buf.write("\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c")
        buf.write("\u008d\5\6\4\2\u008d\21\3\2\2\2\u008e\u0090\7\27\2\2\u008f")
        buf.write("\u0091\5\64\33\2\u0090\u008f\3\2\2\2\u0090\u0091\3\2\2")
        buf.write("\2\u0091\u0092\3\2\2\2\u0092\u0093\5\6\4\2\u0093\23\3")
        buf.write("\2\2\2\u0094\u0095\7\21\2\2\u0095\u0096\7\61\2\2\u0096")
        buf.write("\u0097\7\22\2\2\u0097\u0098\5:\36\2\u0098\u0099\7\23\2")
        buf.write("\2\u0099\u009b\5:\36\2\u009a\u009c\5\64\33\2\u009b\u009a")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u009d\3\2\2\2\u009d")
        buf.write("\u009e\5\6\4\2\u009e\25\3\2\2\2\u009f\u00a0\7\24\2\2\u00a0")
        buf.write("\u00a1\5\64\33\2\u00a1\27\3\2\2\2\u00a2\u00a3\7\25\2\2")
        buf.write("\u00a3\u00a4\5\64\33\2\u00a4\31\3\2\2\2\u00a5\u00a7\7")
        buf.write("\r\2\2\u00a6\u00a8\5:\36\2\u00a7\u00a6\3\2\2\2\u00a7\u00a8")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\5\64\33\2\u00aa")
        buf.write("\33\3\2\2\2\u00ab\u00ac\5\36\20\2\u00ac\u00ad\5\64\33")
        buf.write("\2\u00ad\35\3\2\2\2\u00ae\u00af\7\61\2\2\u00af\u00b1\7")
        buf.write(",\2\2\u00b0\u00b2\5\66\34\2\u00b1\u00b0\3\2\2\2\u00b1")
        buf.write("\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\7-\2\2")
        buf.write("\u00b4\37\3\2\2\2\u00b5\u00b6\7\31\2\2\u00b6\u00b8\5\64")
        buf.write("\33\2\u00b7\u00b9\5\4\3\2\u00b8\u00b7\3\2\2\2\u00b8\u00b9")
        buf.write("\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\7\32\2\2\u00bb")
        buf.write("\u00bc\5\64\33\2\u00bc!\3\2\2\2\u00bd\u00bf\5$\23\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c0\u00c1\3\2\2\2\u00c1#\3\2\2\2\u00c2\u00c5\5&\24")
        buf.write("\2\u00c3\u00c5\5(\25\2\u00c4\u00c2\3\2\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5%\3\2\2\2\u00c6\u00c9\5.\30\2\u00c7\u00c8")
        buf.write("\7&\2\2\u00c8\u00ca\5:\36\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\5\64\33")
        buf.write("\2\u00cc\u00db\3\2\2\2\u00cd\u00ce\7\16\2\2\u00ce\u00cf")
        buf.write("\7\61\2\2\u00cf\u00d0\7&\2\2\u00d0\u00d1\5:\36\2\u00d1")
        buf.write("\u00d2\5\64\33\2\u00d2\u00db\3\2\2\2\u00d3\u00d4\7\17")
        buf.write("\2\2\u00d4\u00d7\7\61\2\2\u00d5\u00d6\7&\2\2\u00d6\u00d8")
        buf.write("\5:\36\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\u00db\5\64\33\2\u00da\u00c6\3\2\2")
        buf.write("\2\u00da\u00cd\3\2\2\2\u00da\u00d3\3\2\2\2\u00db\'\3\2")
        buf.write("\2\2\u00dc\u00dd\7\20\2\2\u00dd\u00de\7\61\2\2\u00de\u00df")
        buf.write("\7,\2\2\u00df\u00e0\5*\26\2\u00e0\u00e9\7-\2\2\u00e1\u00e3")
        buf.write("\5\64\33\2\u00e2\u00e1\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e6\3\2\2\2\u00e4\u00e7\5 \21\2\u00e5\u00e7\5\32\16")
        buf.write("\2\u00e6\u00e4\3\2\2\2\u00e6\u00e5\3\2\2\2\u00e7\u00ea")
        buf.write("\3\2\2\2\u00e8\u00ea\5\64\33\2\u00e9\u00e2\3\2\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea)\3\2\2\2\u00eb\u00ec\5.\30\2\u00ec")
        buf.write("\u00ed\5,\27\2\u00ed\u00f0\3\2\2\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00eb\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0+\3\2\2")
        buf.write("\2\u00f1\u00f2\7\60\2\2\u00f2\u00f3\5.\30\2\u00f3\u00f4")
        buf.write("\5,\27\2\u00f4\u00f7\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f1\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7-\3\2\2\2\u00f8")
        buf.write("\u00f9\t\2\2\2\u00f9\u00fe\7\61\2\2\u00fa\u00fb\7.\2\2")
        buf.write("\u00fb\u00fc\5\60\31\2\u00fc\u00fd\7/\2\2\u00fd\u00ff")
        buf.write("\3\2\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("/\3\2\2\2\u0100\u0101\7\3\2\2\u0101\u0102\5\62\32\2\u0102")
        buf.write("\61\3\2\2\2\u0103\u0104\7\60\2\2\u0104\u0105\7\3\2\2\u0105")
        buf.write("\u0108\5\62\32\2\u0106\u0108\3\2\2\2\u0107\u0103\3\2\2")
        buf.write("\2\u0107\u0106\3\2\2\2\u0108\63\3\2\2\2\u0109\u010b\7")
        buf.write("\63\2\2\u010a\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\65\3\2\2\2\u010e")
        buf.write("\u010f\5:\36\2\u010f\u0110\58\35\2\u0110\67\3\2\2\2\u0111")
        buf.write("\u0112\7\60\2\2\u0112\u0113\5:\36\2\u0113\u0114\58\35")
        buf.write("\2\u0114\u0117\3\2\2\2\u0115\u0117\3\2\2\2\u0116\u0111")
        buf.write("\3\2\2\2\u0116\u0115\3\2\2\2\u01179\3\2\2\2\u0118\u0119")
        buf.write("\5<\37\2\u0119;\3\2\2\2\u011a\u011b\5> \2\u011b\u011c")
        buf.write("\7+\2\2\u011c\u011d\5> \2\u011d\u0120\3\2\2\2\u011e\u0120")
        buf.write("\5> \2\u011f\u011a\3\2\2\2\u011f\u011e\3\2\2\2\u0120=")
        buf.write("\3\2\2\2\u0121\u0122\5@!\2\u0122\u0123\t\3\2\2\u0123\u0124")
        buf.write("\5@!\2\u0124\u0127\3\2\2\2\u0125\u0127\5@!\2\u0126\u0121")
        buf.write("\3\2\2\2\u0126\u0125\3\2\2\2\u0127?\3\2\2\2\u0128\u0129")
        buf.write("\b!\1\2\u0129\u012a\5B\"\2\u012a\u0130\3\2\2\2\u012b\u012c")
        buf.write("\f\4\2\2\u012c\u012d\t\4\2\2\u012d\u012f\5B\"\2\u012e")
        buf.write("\u012b\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2")
        buf.write("\u0130\u0131\3\2\2\2\u0131A\3\2\2\2\u0132\u0130\3\2\2")
        buf.write("\2\u0133\u0134\b\"\1\2\u0134\u0135\5D#\2\u0135\u013b\3")
        buf.write("\2\2\2\u0136\u0137\f\4\2\2\u0137\u0138\t\5\2\2\u0138\u013a")
        buf.write("\5D#\2\u0139\u0136\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139")
        buf.write("\3\2\2\2\u013b\u013c\3\2\2\2\u013cC\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013e\u013f\b#\1\2\u013f\u0140\5F$\2\u0140\u0146")
        buf.write("\3\2\2\2\u0141\u0142\f\4\2\2\u0142\u0143\t\6\2\2\u0143")
        buf.write("\u0145\5F$\2\u0144\u0141\3\2\2\2\u0145\u0148\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147E\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0149\u014a\7\33\2\2\u014a\u014d\5F$\2")
        buf.write("\u014b\u014d\5H%\2\u014c\u0149\3\2\2\2\u014c\u014b\3\2")
        buf.write("\2\2\u014dG\3\2\2\2\u014e\u014f\t\5\2\2\u014f\u0152\5")
        buf.write("H%\2\u0150\u0152\5J&\2\u0151\u014e\3\2\2\2\u0151\u0150")
        buf.write("\3\2\2\2\u0152I\3\2\2\2\u0153\u0163\7\61\2\2\u0154\u0163")
        buf.write("\5L\'\2\u0155\u0163\5\36\20\2\u0156\u0159\7\61\2\2\u0157")
        buf.write("\u0159\5\36\20\2\u0158\u0156\3\2\2\2\u0158\u0157\3\2\2")
        buf.write("\2\u0159\u015a\3\2\2\2\u015a\u015b\7.\2\2\u015b\u015c")
        buf.write("\5\66\34\2\u015c\u015d\7/\2\2\u015d\u0163\3\2\2\2\u015e")
        buf.write("\u015f\7,\2\2\u015f\u0160\5:\36\2\u0160\u0161\7-\2\2\u0161")
        buf.write("\u0163\3\2\2\2\u0162\u0153\3\2\2\2\u0162\u0154\3\2\2\2")
        buf.write("\u0162\u0155\3\2\2\2\u0162\u0158\3\2\2\2\u0162\u015e\3")
        buf.write("\2\2\2\u0163K\3\2\2\2\u0164\u016b\7\3\2\2\u0165\u016b")
        buf.write("\7\4\2\2\u0166\u016b\7\7\2\2\u0167\u016b\7\5\2\2\u0168")
        buf.write("\u016b\7\6\2\2\u0169\u016b\5N(\2\u016a\u0164\3\2\2\2\u016a")
        buf.write("\u0165\3\2\2\2\u016a\u0166\3\2\2\2\u016a\u0167\3\2\2\2")
        buf.write("\u016a\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016bM\3\2\2")
        buf.write("\2\u016c\u016d\7.\2\2\u016d\u016e\5\66\34\2\u016e\u016f")
        buf.write("\7/\2\2\u016fO\3\2\2\2\'QYdkt{\u0082\u008a\u0090\u009b")
        buf.write("\u00a7\u00b1\u00b8\u00c0\u00c4\u00c9\u00d7\u00da\u00e2")
        buf.write("\u00e6\u00e9\u00ef\u00f6\u00fe\u0107\u010c\u0116\u011f")
        buf.write("\u0126\u0130\u013b\u0146\u014c\u0151\u0158\u0162\u016a")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'true'", "'false'", "'number'", 
                     "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
                     "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'=='", "'!='", "'<-'", "'<'", "'<='", "'>'", 
                     "'>='", "'...'", "'('", "')'", "'['", "']'", "','", 
                     "<INVALID>", "<INVALID>", "'\n'", "'\r'" ]

    symbolicNames = [ "<INVALID>", "NUMBER_LITERAL", "STRING_LITERAL", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "BOOLEAN_LITERAL", "TRUE", "FALSE", 
                      "NUMBER", "BOOLEAN", "STRING", "RETURN", "VAR", "DYNAMIC", 
                      "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", 
                      "OR", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MODULO", 
                      "EQUAL_NUMBER", "EQUAL_STRING", "NOT_EQUAL", "ASSIGN", 
                      "LESS_THAN", "LESS_THAN_OR_EQUAL", "GREATER_THAN", 
                      "GREATER_THAN_OR_EQUAL", "CONCAT", "OPEN_ROUND_BRACKET", 
                      "CLOSE_ROUND_BRACKET", "OPEN_SQUARE_BRACKET", "CLOSE_SQUARE_BRACKET", 
                      "COMMA", "IDENTIFIER", "COMMENT", "NEWLINE", "CARRIAGE_RETURN", 
                      "WHITESPACE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement_list = 1
    RULE_statement = 2
    RULE_assignment_statement = 3
    RULE_if_statement = 4
    RULE_if_part = 5
    RULE_elif_list = 6
    RULE_elif_part = 7
    RULE_else_part = 8
    RULE_for_statement = 9
    RULE_break_statement = 10
    RULE_continue_statement = 11
    RULE_return_statement = 12
    RULE_function_call_statement = 13
    RULE_function_call = 14
    RULE_block_statement = 15
    RULE_declaration_list = 16
    RULE_declaration = 17
    RULE_variable_declaration = 18
    RULE_function_declaration = 19
    RULE_parameter_list = 20
    RULE_parameter_listtail = 21
    RULE_parameter = 22
    RULE_number_list = 23
    RULE_number_listtail = 24
    RULE_newline_list = 25
    RULE_expression_list = 26
    RULE_expression_listtail = 27
    RULE_expression = 28
    RULE_string_operation = 29
    RULE_relational_operation = 30
    RULE_logical_operation = 31
    RULE_adding_operation = 32
    RULE_multiplying_operation = 33
    RULE_not_operation = 34
    RULE_sign_operation = 35
    RULE_element = 36
    RULE_literal = 37
    RULE_array_literal = 38

    ruleNames =  [ "program", "statement_list", "statement", "assignment_statement", 
                   "if_statement", "if_part", "elif_list", "elif_part", 
                   "else_part", "for_statement", "break_statement", "continue_statement", 
                   "return_statement", "function_call_statement", "function_call", 
                   "block_statement", "declaration_list", "declaration", 
                   "variable_declaration", "function_declaration", "parameter_list", 
                   "parameter_listtail", "parameter", "number_list", "number_listtail", 
                   "newline_list", "expression_list", "expression_listtail", 
                   "expression", "string_operation", "relational_operation", 
                   "logical_operation", "adding_operation", "multiplying_operation", 
                   "not_operation", "sign_operation", "element", "literal", 
                   "array_literal" ]

    EOF = Token.EOF
    NUMBER_LITERAL=1
    STRING_LITERAL=2
    UNCLOSE_STRING=3
    ILLEGAL_ESCAPE=4
    BOOLEAN_LITERAL=5
    TRUE=6
    FALSE=7
    NUMBER=8
    BOOLEAN=9
    STRING=10
    RETURN=11
    VAR=12
    DYNAMIC=13
    FUNC=14
    FOR=15
    UNTIL=16
    BY=17
    BREAK=18
    CONTINUE=19
    IF=20
    ELSE=21
    ELIF=22
    BEGIN=23
    END=24
    NOT=25
    AND=26
    OR=27
    PLUS=28
    MINUS=29
    MULTIPLY=30
    DIVIDE=31
    MODULO=32
    EQUAL_NUMBER=33
    EQUAL_STRING=34
    NOT_EQUAL=35
    ASSIGN=36
    LESS_THAN=37
    LESS_THAN_OR_EQUAL=38
    GREATER_THAN=39
    GREATER_THAN_OR_EQUAL=40
    CONCAT=41
    OPEN_ROUND_BRACKET=42
    CLOSE_ROUND_BRACKET=43
    OPEN_SQUARE_BRACKET=44
    CLOSE_SQUARE_BRACKET=45
    COMMA=46
    IDENTIFIER=47
    COMMENT=48
    NEWLINE=49
    CARRIAGE_RETURN=50
    WHITESPACE=51
    ERROR_CHAR=52

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

        def declaration_list(self):
            return self.getTypedRuleContext(ZCodeParser.Declaration_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 78
                self.newline_list()


            self.state = 81
            self.declaration_list()
            self.state = 82
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = ZCodeParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 84
                self.statement()
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def assignment_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Assignment_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ZCodeParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(ZCodeParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def function_call_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Function_call_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.assignment_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 95
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 96
                self.function_call_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 97
                self.block_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assignment_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statement" ):
                return visitor.visitAssignment_statement(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statement(self):

        localctx = ZCodeParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OPEN_SQUARE_BRACKET:
                self.state = 101
                self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
                self.state = 102
                self.expression_list()
                self.state = 103
                self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)


            self.state = 107
            self.match(ZCodeParser.ASSIGN)
            self.state = 108
            self.expression()
            self.state = 109
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_part(self):
            return self.getTypedRuleContext(ZCodeParser.If_partContext,0)


        def elif_list(self):
            return self.getTypedRuleContext(ZCodeParser.Elif_listContext,0)


        def else_part(self):
            return self.getTypedRuleContext(ZCodeParser.Else_partContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = ZCodeParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.if_part()
            self.state = 112
            self.elif_list()
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 113
                self.else_part()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_if_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_part" ):
                return visitor.visitIf_part(self)
            else:
                return visitor.visitChildren(self)




    def if_part(self):

        localctx = ZCodeParser.If_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(ZCodeParser.IF)
            self.state = 117
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 118
            self.expression()
            self.state = 119
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 120
                self.newline_list()


            self.state = 123
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elif_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Elif_partContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Elif_partContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_list" ):
                return visitor.visitElif_list(self)
            else:
                return visitor.visitChildren(self)




    def elif_list(self):

        localctx = ZCodeParser.Elif_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elif_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 125
                    self.elif_part() 
                self.state = 130
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elif_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElif_part" ):
                return visitor.visitElif_part(self)
            else:
                return visitor.visitChildren(self)




    def elif_part(self):

        localctx = ZCodeParser.Elif_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_elif_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ZCodeParser.ELIF)
            self.state = 132
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 133
            self.expression()
            self.state = 134
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 135
                self.newline_list()


            self.state = 138
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_else_part

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_part" ):
                return visitor.visitElse_part(self)
            else:
                return visitor.visitChildren(self)




    def else_part(self):

        localctx = ZCodeParser.Else_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_else_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ZCodeParser.ELSE)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 141
                self.newline_list()


            self.state = 144
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpressionContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = ZCodeParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ZCodeParser.FOR)
            self.state = 147
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 148
            self.match(ZCodeParser.UNTIL)
            self.state = 149
            self.expression()
            self.state = 150
            self.match(ZCodeParser.BY)
            self.state = 151
            self.expression()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 152
                self.newline_list()


            self.state = 155
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = ZCodeParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ZCodeParser.BREAK)
            self.state = 158
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = ZCodeParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(ZCodeParser.CONTINUE)
            self.state = 161
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = ZCodeParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(ZCodeParser.RETURN)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.UNCLOSE_STRING) | (1 << ZCodeParser.ILLEGAL_ESCAPE) | (1 << ZCodeParser.BOOLEAN_LITERAL) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.OPEN_ROUND_BRACKET) | (1 << ZCodeParser.OPEN_SQUARE_BRACKET) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 164
                self.expression()


            self.state = 167
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call_statement" ):
                return visitor.visitFunction_call_statement(self)
            else:
                return visitor.visitChildren(self)




    def function_call_statement(self):

        localctx = ZCodeParser.Function_call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.function_call()
            self.state = 170
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = ZCodeParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 173
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER_LITERAL) | (1 << ZCodeParser.STRING_LITERAL) | (1 << ZCodeParser.UNCLOSE_STRING) | (1 << ZCodeParser.ILLEGAL_ESCAPE) | (1 << ZCodeParser.BOOLEAN_LITERAL) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.PLUS) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.OPEN_ROUND_BRACKET) | (1 << ZCodeParser.OPEN_SQUARE_BRACKET) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 174
                self.expression_list()


            self.state = 177
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def newline_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Newline_listContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Newline_listContext,i)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def statement_list(self):
            return self.getTypedRuleContext(ZCodeParser.Statement_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = ZCodeParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(ZCodeParser.BEGIN)
            self.state = 180
            self.newline_list()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.RETURN) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FOR) | (1 << ZCodeParser.BREAK) | (1 << ZCodeParser.CONTINUE) | (1 << ZCodeParser.IF) | (1 << ZCodeParser.BEGIN) | (1 << ZCodeParser.IDENTIFIER))) != 0):
                self.state = 181
                self.statement_list()


            self.state = 184
            self.match(ZCodeParser.END)
            self.state = 185
            self.newline_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_list" ):
                return visitor.visitDeclaration_list(self)
            else:
                return visitor.visitChildren(self)




    def declaration_list(self):

        localctx = ZCodeParser.Declaration_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_declaration_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 187
                self.declaration()
                self.state = 190 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.STRING) | (1 << ZCodeParser.VAR) | (1 << ZCodeParser.DYNAMIC) | (1 << ZCodeParser.FUNC))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Variable_declarationContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(ZCodeParser.Function_declarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_declaration)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.variable_declaration()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.function_declaration()
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


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = ZCodeParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.parameter()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 197
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 198
                    self.expression()


                self.state = 201
                self.newline_list()
                pass
            elif token in [ZCodeParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.match(ZCodeParser.VAR)
                self.state = 204
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 205
                self.match(ZCodeParser.ASSIGN)
                self.state = 206
                self.expression()
                self.state = 207
                self.newline_list()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(ZCodeParser.DYNAMIC)
                self.state = 210
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.ASSIGN:
                    self.state = 211
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 212
                    self.expression()


                self.state = 215
                self.newline_list()
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


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def parameter_list(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def newline_list(self):
            return self.getTypedRuleContext(ZCodeParser.Newline_listContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Block_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(ZCodeParser.Return_statementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = ZCodeParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(ZCodeParser.FUNC)
            self.state = 219
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 220
            self.match(ZCodeParser.OPEN_ROUND_BRACKET)
            self.state = 221
            self.parameter_list()
            self.state = 222
            self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 223
                    self.newline_list()


                self.state = 228
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZCodeParser.BEGIN]:
                    self.state = 226
                    self.block_statement()
                    pass
                elif token in [ZCodeParser.RETURN]:
                    self.state = 227
                    self.return_statement()
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.state = 230
                self.newline_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def parameter_listtail(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameter_list)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOLEAN, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.parameter()
                self.state = 234
                self.parameter_listtail()
                pass
            elif token in [ZCodeParser.CLOSE_ROUND_BRACKET]:
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


    class Parameter_listtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def parameter(self):
            return self.getTypedRuleContext(ZCodeParser.ParameterContext,0)


        def parameter_listtail(self):
            return self.getTypedRuleContext(ZCodeParser.Parameter_listtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter_listtail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_listtail" ):
                return visitor.visitParameter_listtail(self)
            else:
                return visitor.visitChildren(self)




    def parameter_listtail(self):

        localctx = ZCodeParser.Parameter_listtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter_listtail)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(ZCodeParser.COMMA)
                self.state = 240
                self.parameter()
                self.state = 241
                self.parameter_listtail()
                pass
            elif token in [ZCodeParser.CLOSE_ROUND_BRACKET]:
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


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOLEAN(self):
            return self.getToken(ZCodeParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def number_list(self):
            return self.getTypedRuleContext(ZCodeParser.Number_listContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOLEAN) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 247
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OPEN_SQUARE_BRACKET:
                self.state = 248
                self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
                self.state = 249
                self.number_list()
                self.state = 250
                self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def number_listtail(self):
            return self.getTypedRuleContext(ZCodeParser.Number_listtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_list" ):
                return visitor.visitNumber_list(self)
            else:
                return visitor.visitChildren(self)




    def number_list(self):

        localctx = ZCodeParser.Number_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_number_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(ZCodeParser.NUMBER_LITERAL)
            self.state = 255
            self.number_listtail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_listtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def number_listtail(self):
            return self.getTypedRuleContext(ZCodeParser.Number_listtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_listtail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_listtail" ):
                return visitor.visitNumber_listtail(self)
            else:
                return visitor.visitChildren(self)




    def number_listtail(self):

        localctx = ZCodeParser.Number_listtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_number_listtail)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(ZCodeParser.COMMA)
                self.state = 258
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 259
                self.number_listtail()
                pass
            elif token in [ZCodeParser.CLOSE_SQUARE_BRACKET]:
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


    class Newline_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_newline_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNewline_list" ):
                return visitor.visitNewline_list(self)
            else:
                return visitor.visitChildren(self)




    def newline_list(self):

        localctx = ZCodeParser.Newline_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_newline_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 263
                self.match(ZCodeParser.NEWLINE)
                self.state = 266 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def expression_listtail(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_list" ):
                return visitor.visitExpression_list(self)
            else:
                return visitor.visitChildren(self)




    def expression_list(self):

        localctx = ZCodeParser.Expression_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.expression()
            self.state = 269
            self.expression_listtail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_listtailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def expression_listtail(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listtailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression_listtail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_listtail" ):
                return visitor.visitExpression_listtail(self)
            else:
                return visitor.visitChildren(self)




    def expression_listtail(self):

        localctx = ZCodeParser.Expression_listtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression_listtail)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(ZCodeParser.COMMA)
                self.state = 272
                self.expression()
                self.state = 273
                self.expression_listtail()
                pass
            elif token in [ZCodeParser.CLOSE_ROUND_BRACKET, ZCodeParser.CLOSE_SQUARE_BRACKET]:
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


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_operation(self):
            return self.getTypedRuleContext(ZCodeParser.String_operationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.string_operation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Relational_operationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Relational_operationContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_string_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_operation" ):
                return visitor.visitString_operation(self)
            else:
                return visitor.visitChildren(self)




    def string_operation(self):

        localctx = ZCodeParser.String_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_string_operation)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.relational_operation()
                self.state = 281
                self.match(ZCodeParser.CONCAT)
                self.state = 282
                self.relational_operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.relational_operation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logical_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Logical_operationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Logical_operationContext,i)


        def EQUAL_NUMBER(self):
            return self.getToken(ZCodeParser.EQUAL_NUMBER, 0)

        def EQUAL_STRING(self):
            return self.getToken(ZCodeParser.EQUAL_STRING, 0)

        def NOT_EQUAL(self):
            return self.getToken(ZCodeParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(ZCodeParser.LESS_THAN, 0)

        def LESS_THAN_OR_EQUAL(self):
            return self.getToken(ZCodeParser.LESS_THAN_OR_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(ZCodeParser.GREATER_THAN, 0)

        def GREATER_THAN_OR_EQUAL(self):
            return self.getToken(ZCodeParser.GREATER_THAN_OR_EQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_relational_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operation" ):
                return visitor.visitRelational_operation(self)
            else:
                return visitor.visitChildren(self)




    def relational_operation(self):

        localctx = ZCodeParser.Relational_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_relational_operation)
        self._la = 0 # Token type
        try:
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.logical_operation(0)
                self.state = 288
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQUAL_NUMBER) | (1 << ZCodeParser.EQUAL_STRING) | (1 << ZCodeParser.NOT_EQUAL) | (1 << ZCodeParser.LESS_THAN) | (1 << ZCodeParser.LESS_THAN_OR_EQUAL) | (1 << ZCodeParser.GREATER_THAN) | (1 << ZCodeParser.GREATER_THAN_OR_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 289
                self.logical_operation(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.logical_operation(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def adding_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_operationContext,0)


        def logical_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Logical_operationContext,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_logical_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_operation" ):
                return visitor.visitLogical_operation(self)
            else:
                return visitor.visitChildren(self)



    def logical_operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Logical_operationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_logical_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.adding_operation(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Logical_operationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_operation)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 299
                    self.adding_operation(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Adding_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplying_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_operationContext,0)


        def adding_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Adding_operationContext,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_adding_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_operation" ):
                return visitor.visitAdding_operation(self)
            else:
                return visitor.visitChildren(self)



    def adding_operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Adding_operationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_adding_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.multiplying_operation(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Adding_operationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_adding_operation)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.multiplying_operation(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Multiplying_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def not_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Not_operationContext,0)


        def multiplying_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Multiplying_operationContext,0)


        def MULTIPLY(self):
            return self.getToken(ZCodeParser.MULTIPLY, 0)

        def DIVIDE(self):
            return self.getToken(ZCodeParser.DIVIDE, 0)

        def MODULO(self):
            return self.getToken(ZCodeParser.MODULO, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_multiplying_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_operation" ):
                return visitor.visitMultiplying_operation(self)
            else:
                return visitor.visitChildren(self)



    def multiplying_operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Multiplying_operationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_multiplying_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.not_operation()
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Multiplying_operationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplying_operation)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MULTIPLY) | (1 << ZCodeParser.DIVIDE) | (1 << ZCodeParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 321
                    self.not_operation() 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Not_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def not_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Not_operationContext,0)


        def sign_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_operationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_not_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_operation" ):
                return visitor.visitNot_operation(self)
            else:
                return visitor.visitChildren(self)




    def not_operation(self):

        localctx = ZCodeParser.Not_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_not_operation)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(ZCodeParser.NOT)
                self.state = 328
                self.not_operation()
                pass
            elif token in [ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.UNCLOSE_STRING, ZCodeParser.ILLEGAL_ESCAPE, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.PLUS, ZCodeParser.MINUS, ZCodeParser.OPEN_ROUND_BRACKET, ZCodeParser.OPEN_SQUARE_BRACKET, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.sign_operation()
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


    class Sign_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_operation(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_operationContext,0)


        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def element(self):
            return self.getTypedRuleContext(ZCodeParser.ElementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_operation" ):
                return visitor.visitSign_operation(self)
            else:
                return visitor.visitChildren(self)




    def sign_operation(self):

        localctx = ZCodeParser.Sign_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_sign_operation)
        self._la = 0 # Token type
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.PLUS, ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                _la = self._input.LA(1)
                if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 333
                self.sign_operation()
                pass
            elif token in [ZCodeParser.NUMBER_LITERAL, ZCodeParser.STRING_LITERAL, ZCodeParser.UNCLOSE_STRING, ZCodeParser.ILLEGAL_ESCAPE, ZCodeParser.BOOLEAN_LITERAL, ZCodeParser.OPEN_ROUND_BRACKET, ZCodeParser.OPEN_SQUARE_BRACKET, ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.element()
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


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def function_call(self):
            return self.getTypedRuleContext(ZCodeParser.Function_callContext,0)


        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

        def OPEN_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_ROUND_BRACKET, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def CLOSE_ROUND_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_ROUND_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = ZCodeParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_element)
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 342
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 340
                    self.match(ZCodeParser.IDENTIFIER)
                    pass

                elif la_ == 2:
                    self.state = 341
                    self.function_call()
                    pass


                self.state = 344
                self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
                self.state = 345
                self.expression_list()
                self.state = 346
                self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 348
                self.match(ZCodeParser.OPEN_ROUND_BRACKET)
                self.state = 349
                self.expression()
                self.state = 350
                self.match(ZCodeParser.CLOSE_ROUND_BRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER_LITERAL(self):
            return self.getToken(ZCodeParser.NUMBER_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(ZCodeParser.STRING_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(ZCodeParser.BOOLEAN_LITERAL, 0)

        def UNCLOSE_STRING(self):
            return self.getToken(ZCodeParser.UNCLOSE_STRING, 0)

        def ILLEGAL_ESCAPE(self):
            return self.getToken(ZCodeParser.ILLEGAL_ESCAPE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(ZCodeParser.Array_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_literal)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass
            elif token in [ZCodeParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(ZCodeParser.STRING_LITERAL)
                pass
            elif token in [ZCodeParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.match(ZCodeParser.BOOLEAN_LITERAL)
                pass
            elif token in [ZCodeParser.UNCLOSE_STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.match(ZCodeParser.UNCLOSE_STRING)
                pass
            elif token in [ZCodeParser.ILLEGAL_ESCAPE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                self.match(ZCodeParser.ILLEGAL_ESCAPE)
                pass
            elif token in [ZCodeParser.OPEN_SQUARE_BRACKET]:
                self.enterOuterAlt(localctx, 6)
                self.state = 359
                self.array_literal()
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.OPEN_SQUARE_BRACKET, 0)

        def expression_list(self):
            return self.getTypedRuleContext(ZCodeParser.Expression_listContext,0)


        def CLOSE_SQUARE_BRACKET(self):
            return self.getToken(ZCodeParser.CLOSE_SQUARE_BRACKET, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = ZCodeParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ZCodeParser.OPEN_SQUARE_BRACKET)
            self.state = 363
            self.expression_list()
            self.state = 364
            self.match(ZCodeParser.CLOSE_SQUARE_BRACKET)
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
        self._predicates[31] = self.logical_operation_sempred
        self._predicates[32] = self.adding_operation_sempred
        self._predicates[33] = self.multiplying_operation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logical_operation_sempred(self, localctx:Logical_operationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def adding_operation_sempred(self, localctx:Adding_operationContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multiplying_operation_sempred(self, localctx:Multiplying_operationContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




