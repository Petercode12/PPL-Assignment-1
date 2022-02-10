# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u02a4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00d8\n\16\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\7\21\u00e4\n\21\f\21\16")
        buf.write("\21\u00e7\13\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\7\22\u00f2\n\22\f\22\16\22\u00f5\13\22\3\23\3\23")
        buf.write("\3\23\7\23\u00fa\n\23\f\23\16\23\u00fd\13\23\5\23\u00ff")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\7\24\u0106\n\24\f\24\16")
        buf.write("\24\u0109\13\24\3\25\3\25\3\25\3\25\5\25\u010f\n\25\3")
        buf.write("\25\3\25\3\25\3\25\7\25\u0115\n\25\f\25\16\25\u0118\13")
        buf.write("\25\3\26\3\26\3\26\3\26\5\26\u011e\n\26\3\26\3\26\3\26")
        buf.write("\3\26\7\26\u0124\n\26\f\26\16\26\u0127\13\26\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u012d\n\27\3\27\3\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\5\30\u0140\n\30\3\31\3\31\5\31\u0144\n\31\3\31\3")
        buf.write("\31\7\31\u0148\n\31\f\31\16\31\u014b\13\31\3\31\3\31\5")
        buf.write("\31\u014f\n\31\3\31\3\31\3\31\5\31\u0154\n\31\3\31\6\31")
        buf.write("\u0157\n\31\r\31\16\31\u0158\3\31\3\31\5\31\u015d\n\31")
        buf.write("\3\31\3\31\7\31\u0161\n\31\f\31\16\31\u0164\13\31\3\31")
        buf.write("\3\31\3\31\5\31\u0169\n\31\3\31\6\31\u016c\n\31\r\31\16")
        buf.write("\31\u016d\3\31\3\31\7\31\u0172\n\31\f\31\16\31\u0175\13")
        buf.write("\31\3\31\3\31\3\31\5\31\u017a\n\31\3\31\6\31\u017d\n\31")
        buf.write("\r\31\16\31\u017e\5\31\u0181\n\31\3\31\3\31\3\32\3\32")
        buf.write("\5\32\u0187\n\32\3\33\3\33\7\33\u018b\n\33\f\33\16\33")
        buf.write("\u018e\13\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3")
        buf.write("<\3=\3=\3>\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\3B\3C\3C\3")
        buf.write("C\3C\3D\3D\3D\3E\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3")
        buf.write("K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\5P\u0267\nP\3P\3P\3")
        buf.write("P\7P\u026c\nP\fP\16P\u026f\13P\3Q\3Q\3Q\3Q\6Q\u0275\n")
        buf.write("Q\rQ\16Q\u0276\3R\3R\3R\3S\3S\3S\3T\3T\3T\5T\u0282\nT")
        buf.write("\3U\3U\5U\u0286\nU\3V\6V\u0289\nV\rV\16V\u028a\3V\3V\3")
        buf.write("W\3W\7W\u0291\nW\fW\16W\u0294\13W\3W\3W\3X\3X\3X\3Y\3")
        buf.write("Y\7Y\u029d\nY\fY\16Y\u02a0\13Y\3Y\3Y\3Y\3\u00e5\2Z\3\3")
        buf.write("\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33")
        buf.write("\2\35\2\37\2!\4#\2%\2\'\2)\2+\2-\5/\6\61\7\63\b\65\t\67")
        buf.write("\n9\13;\f=\r?\16A\17C\20E\21G\22I\23K\24M\25O\26Q\27S")
        buf.write("\30U\31W\32Y\33[\34]\35_\36a\37c e!g\"i#k$m%o&q\'s(u)")
        buf.write("w*y+{,}-\177.\u0081/\u0083\60\u0085\61\u0087\62\u0089")
        buf.write("\63\u008b\64\u008d\65\u008f\66\u0091\67\u00938\u00959")
        buf.write("\u0097:\u0099;\u009b<\u009d=\u009f>\u00a1?\u00a3\2\u00a5")
        buf.write("\2\u00a7\2\u00a9\2\u00ab@\u00adA\u00afB\u00b1C\3\2\16")
        buf.write("\4\2C\\c|\3\2\62;\4\2GGgg\3\2\63;\3\2\639\3\2\629\4\2")
        buf.write("\63;CH\4\2\62;CH\3\2\62\63\t\2))^^ddhhppttvv\6\2\n\f\16")
        buf.write("\17$$^^\5\2\13\f\17\17\"\"\2\u02c7\2\3\3\2\2\2\2!\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2")
        buf.write("\2\3\u00b3\3\2\2\2\5\u00b6\3\2\2\2\7\u00b8\3\2\2\2\t\u00ba")
        buf.write("\3\2\2\2\13\u00bc\3\2\2\2\r\u00be\3\2\2\2\17\u00c0\3\2")
        buf.write("\2\2\21\u00c2\3\2\2\2\23\u00c5\3\2\2\2\25\u00c8\3\2\2")
        buf.write("\2\27\u00cb\3\2\2\2\31\u00ce\3\2\2\2\33\u00d7\3\2\2\2")
        buf.write("\35\u00d9\3\2\2\2\37\u00dc\3\2\2\2!\u00df\3\2\2\2#\u00ed")
        buf.write("\3\2\2\2%\u00fe\3\2\2\2\'\u0100\3\2\2\2)\u010e\3\2\2\2")
        buf.write("+\u011d\3\2\2\2-\u012c\3\2\2\2/\u013f\3\2\2\2\61\u0180")
        buf.write("\3\2\2\2\63\u0186\3\2\2\2\65\u0188\3\2\2\2\67\u0192\3")
        buf.write("\2\2\29\u0198\3\2\2\2;\u01a1\3\2\2\2=\u01a4\3\2\2\2?\u01ab")
        buf.write("\3\2\2\2A\u01b0\3\2\2\2C\u01b8\3\2\2\2E\u01bd\3\2\2\2")
        buf.write("G\u01c3\3\2\2\2I\u01c9\3\2\2\2K\u01cc\3\2\2\2M\u01d0\3")
        buf.write("\2\2\2O\u01d6\3\2\2\2Q\u01de\3\2\2\2S\u01e5\3\2\2\2U\u01ec")
        buf.write("\3\2\2\2W\u01f1\3\2\2\2Y\u01f7\3\2\2\2[\u01fb\3\2\2\2")
        buf.write("]\u01ff\3\2\2\2_\u020b\3\2\2\2a\u0216\3\2\2\2c\u021a\3")
        buf.write("\2\2\2e\u021d\3\2\2\2g\u0222\3\2\2\2i\u0224\3\2\2\2k\u0226")
        buf.write("\3\2\2\2m\u0228\3\2\2\2o\u022a\3\2\2\2q\u022c\3\2\2\2")
        buf.write("s\u022e\3\2\2\2u\u0231\3\2\2\2w\u0234\3\2\2\2y\u0237\3")
        buf.write("\2\2\2{\u0239\3\2\2\2}\u023c\3\2\2\2\177\u023e\3\2\2\2")
        buf.write("\u0081\u0241\3\2\2\2\u0083\u0243\3\2\2\2\u0085\u0246\3")
        buf.write("\2\2\2\u0087\u024a\3\2\2\2\u0089\u024d\3\2\2\2\u008b\u0250")
        buf.write("\3\2\2\2\u008d\u0252\3\2\2\2\u008f\u0254\3\2\2\2\u0091")
        buf.write("\u0256\3\2\2\2\u0093\u0258\3\2\2\2\u0095\u025a\3\2\2\2")
        buf.write("\u0097\u025c\3\2\2\2\u0099\u025e\3\2\2\2\u009b\u0260\3")
        buf.write("\2\2\2\u009d\u0262\3\2\2\2\u009f\u0266\3\2\2\2\u00a1\u0270")
        buf.write("\3\2\2\2\u00a3\u0278\3\2\2\2\u00a5\u027b\3\2\2\2\u00a7")
        buf.write("\u0281\3\2\2\2\u00a9\u0283\3\2\2\2\u00ab\u0288\3\2\2\2")
        buf.write("\u00ad\u028e\3\2\2\2\u00af\u0297\3\2\2\2\u00b1\u029a\3")
        buf.write("\2\2\2\u00b3\u00b4\7\60\2\2\u00b4\u00b5\7\60\2\2\u00b5")
        buf.write("\4\3\2\2\2\u00b6\u00b7\t\2\2\2\u00b7\6\3\2\2\2\u00b8\u00b9")
        buf.write("\t\3\2\2\u00b9\b\3\2\2\2\u00ba\u00bb\7&\2\2\u00bb\n\3")
        buf.write("\2\2\2\u00bc\u00bd\t\4\2\2\u00bd\f\3\2\2\2\u00be\u00bf")
        buf.write("\7$\2\2\u00bf\16\3\2\2\2\u00c0\u00c1\7\"\2\2\u00c1\20")
        buf.write("\3\2\2\2\u00c2\u00c3\7^\2\2\u00c3\u00c4\7v\2\2\u00c4\22")
        buf.write("\3\2\2\2\u00c5\u00c6\7^\2\2\u00c6\u00c7\7d\2\2\u00c7\24")
        buf.write("\3\2\2\2\u00c8\u00c9\7^\2\2\u00c9\u00ca\7h\2\2\u00ca\26")
        buf.write("\3\2\2\2\u00cb\u00cc\7^\2\2\u00cc\u00cd\7t\2\2\u00cd\30")
        buf.write("\3\2\2\2\u00ce\u00cf\7^\2\2\u00cf\u00d0\7p\2\2\u00d0\32")
        buf.write("\3\2\2\2\u00d1\u00d8\5\17\b\2\u00d2\u00d8\5\21\t\2\u00d3")
        buf.write("\u00d8\5\23\n\2\u00d4\u00d8\5\25\13\2\u00d5\u00d8\5\27")
        buf.write("\f\2\u00d6\u00d8\5\31\r\2\u00d7\u00d1\3\2\2\2\u00d7\u00d2")
        buf.write("\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d7\u00d4\3\2\2\2\u00d7")
        buf.write("\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8\34\3\2\2\2\u00d9")
        buf.write("\u00da\7^\2\2\u00da\u00db\7)\2\2\u00db\36\3\2\2\2\u00dc")
        buf.write("\u00dd\7^\2\2\u00dd\u00de\7^\2\2\u00de \3\2\2\2\u00df")
        buf.write("\u00e0\7%\2\2\u00e0\u00e1\7%\2\2\u00e1\u00e5\3\2\2\2\u00e2")
        buf.write("\u00e4\13\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2\2")
        buf.write("\2\u00e5\u00e6\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e8")
        buf.write("\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8\u00e9\7%\2\2\u00e9")
        buf.write("\u00ea\7%\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ec\b\21\2\2")
        buf.write("\u00ec\"\3\2\2\2\u00ed\u00f3\t\5\2\2\u00ee\u00f2\5\7\4")
        buf.write("\2\u00ef\u00f0\7a\2\2\u00f0\u00f2\5\7\4\2\u00f1\u00ee")
        buf.write("\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4$\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00ff\7\62\2\2\u00f7\u00fb\t\5\2")
        buf.write("\2\u00f8\u00fa\5\7\4\2\u00f9\u00f8\3\2\2\2\u00fa\u00fd")
        buf.write("\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00ff\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00f6\3\2\2\2")
        buf.write("\u00fe\u00f7\3\2\2\2\u00ff&\3\2\2\2\u0100\u0101\7\62\2")
        buf.write("\2\u0101\u0107\t\6\2\2\u0102\u0106\t\7\2\2\u0103\u0104")
        buf.write("\7a\2\2\u0104\u0106\t\7\2\2\u0105\u0102\3\2\2\2\u0105")
        buf.write("\u0103\3\2\2\2\u0106\u0109\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0107\u0108\3\2\2\2\u0108(\3\2\2\2\u0109\u0107\3\2\2")
        buf.write("\2\u010a\u010b\7\62\2\2\u010b\u010f\7z\2\2\u010c\u010d")
        buf.write("\7\62\2\2\u010d\u010f\7Z\2\2\u010e\u010a\3\2\2\2\u010e")
        buf.write("\u010c\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0116\t\b\2\2")
        buf.write("\u0111\u0115\t\t\2\2\u0112\u0113\7a\2\2\u0113\u0115\t")
        buf.write("\t\2\2\u0114\u0111\3\2\2\2\u0114\u0112\3\2\2\2\u0115\u0118")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117")
        buf.write("*\3\2\2\2\u0118\u0116\3\2\2\2\u0119\u011a\7\62\2\2\u011a")
        buf.write("\u011e\7d\2\2\u011b\u011c\7\62\2\2\u011c\u011e\7D\2\2")
        buf.write("\u011d\u0119\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\3")
        buf.write("\2\2\2\u011f\u0125\7\63\2\2\u0120\u0124\t\n\2\2\u0121")
        buf.write("\u0122\7a\2\2\u0122\u0124\t\n\2\2\u0123\u0120\3\2\2\2")
        buf.write("\u0123\u0121\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3")
        buf.write("\2\2\2\u0125\u0126\3\2\2\2\u0126,\3\2\2\2\u0127\u0125")
        buf.write("\3\2\2\2\u0128\u012d\5#\22\2\u0129\u012d\5\'\24\2\u012a")
        buf.write("\u012d\5)\25\2\u012b\u012d\5+\26\2\u012c\u0128\3\2\2\2")
        buf.write("\u012c\u0129\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012b\3")
        buf.write("\2\2\2\u012d\u012e\3\2\2\2\u012e\u012f\b\27\3\2\u012f")
        buf.write(".\3\2\2\2\u0130\u0140\7\62\2\2\u0131\u0132\7\62\2\2\u0132")
        buf.write("\u0140\7\62\2\2\u0133\u0134\7\62\2\2\u0134\u0135\7z\2")
        buf.write("\2\u0135\u0140\7\62\2\2\u0136\u0137\7\62\2\2\u0137\u0138")
        buf.write("\7Z\2\2\u0138\u0140\7\62\2\2\u0139\u013a\7\62\2\2\u013a")
        buf.write("\u013b\7d\2\2\u013b\u0140\7\62\2\2\u013c\u013d\7\62\2")
        buf.write("\2\u013d\u013e\7D\2\2\u013e\u0140\7\62\2\2\u013f\u0130")
        buf.write("\3\2\2\2\u013f\u0131\3\2\2\2\u013f\u0133\3\2\2\2\u013f")
        buf.write("\u0136\3\2\2\2\u013f\u0139\3\2\2\2\u013f\u013c\3\2\2\2")
        buf.write("\u0140\60\3\2\2\2\u0141\u0144\5#\22\2\u0142\u0144\7\62")
        buf.write("\2\2\u0143\u0141\3\2\2\2\u0143\u0142\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\u0149\5\u0095K\2\u0146\u0148\5\7\4\2\u0147")
        buf.write("\u0146\3\2\2\2\u0148\u014b\3\2\2\2\u0149\u0147\3\2\2\2")
        buf.write("\u0149\u014a\3\2\2\2\u014a\u0181\3\2\2\2\u014b\u0149\3")
        buf.write("\2\2\2\u014c\u014f\5#\22\2\u014d\u014f\7\62\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0153\5\13\6\2\u0151\u0154\5g\64\2\u0152\u0154")
        buf.write("\5i\65\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u0156\3\2\2\2\u0155\u0157\5\7\4\2")
        buf.write("\u0156\u0155\3\2\2\2\u0157\u0158\3\2\2\2\u0158\u0156\3")
        buf.write("\2\2\2\u0158\u0159\3\2\2\2\u0159\u0181\3\2\2\2\u015a\u015d")
        buf.write("\5#\22\2\u015b\u015d\7\62\2\2\u015c\u015a\3\2\2\2\u015c")
        buf.write("\u015b\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0162\5\u0095")
        buf.write("K\2\u015f\u0161\5\7\4\2\u0160\u015f\3\2\2\2\u0161\u0164")
        buf.write("\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0168\5\13\6")
        buf.write("\2\u0166\u0169\5g\64\2\u0167\u0169\5i\65\2\u0168\u0166")
        buf.write("\3\2\2\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2\2\2\u0169")
        buf.write("\u016b\3\2\2\2\u016a\u016c\5\7\4\2\u016b\u016a\3\2\2\2")
        buf.write("\u016c\u016d\3\2\2\2\u016d\u016b\3\2\2\2\u016d\u016e\3")
        buf.write("\2\2\2\u016e\u0181\3\2\2\2\u016f\u0173\5\u0095K\2\u0170")
        buf.write("\u0172\5\7\4\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0176\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0176\u0179\5\13\6\2\u0177")
        buf.write("\u017a\5g\64\2\u0178\u017a\5i\65\2\u0179\u0177\3\2\2\2")
        buf.write("\u0179\u0178\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017c\3")
        buf.write("\2\2\2\u017b\u017d\5\7\4\2\u017c\u017b\3\2\2\2\u017d\u017e")
        buf.write("\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f")
        buf.write("\u0181\3\2\2\2\u0180\u0143\3\2\2\2\u0180\u014e\3\2\2\2")
        buf.write("\u0180\u015c\3\2\2\2\u0180\u016f\3\2\2\2\u0181\u0182\3")
        buf.write("\2\2\2\u0182\u0183\b\31\4\2\u0183\62\3\2\2\2\u0184\u0187")
        buf.write("\5C\"\2\u0185\u0187\5E#\2\u0186\u0184\3\2\2\2\u0186\u0185")
        buf.write("\3\2\2\2\u0187\64\3\2\2\2\u0188\u018c\5\r\7\2\u0189\u018b")
        buf.write("\5\u00a7T\2\u018a\u0189\3\2\2\2\u018b\u018e\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018f\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018f\u0190\5\r\7\2\u0190\u0191\b")
        buf.write("\33\5\2\u0191\66\3\2\2\2\u0192\u0193\7D\2\2\u0193\u0194")
        buf.write("\7t\2\2\u0194\u0195\7g\2\2\u0195\u0196\7c\2\2\u0196\u0197")
        buf.write("\7m\2\2\u01978\3\2\2\2\u0198\u0199\7E\2\2\u0199\u019a")
        buf.write("\7q\2\2\u019a\u019b\7p\2\2\u019b\u019c\7v\2\2\u019c\u019d")
        buf.write("\7k\2\2\u019d\u019e\7p\2\2\u019e\u019f\7w\2\2\u019f\u01a0")
        buf.write("\7g\2\2\u01a0:\3\2\2\2\u01a1\u01a2\7K\2\2\u01a2\u01a3")
        buf.write("\7h\2\2\u01a3<\3\2\2\2\u01a4\u01a5\7G\2\2\u01a5\u01a6")
        buf.write("\7n\2\2\u01a6\u01a7\7u\2\2\u01a7\u01a8\7g\2\2\u01a8\u01a9")
        buf.write("\7k\2\2\u01a9\u01aa\7h\2\2\u01aa>\3\2\2\2\u01ab\u01ac")
        buf.write("\7G\2\2\u01ac\u01ad\7n\2\2\u01ad\u01ae\7u\2\2\u01ae\u01af")
        buf.write("\7g\2\2\u01af@\3\2\2\2\u01b0\u01b1\7H\2\2\u01b1\u01b2")
        buf.write("\7q\2\2\u01b2\u01b3\7t\2\2\u01b3\u01b4\7g\2\2\u01b4\u01b5")
        buf.write("\7c\2\2\u01b5\u01b6\7e\2\2\u01b6\u01b7\7j\2\2\u01b7B\3")
        buf.write("\2\2\2\u01b8\u01b9\7V\2\2\u01b9\u01ba\7t\2\2\u01ba\u01bb")
        buf.write("\7w\2\2\u01bb\u01bc\7g\2\2\u01bcD\3\2\2\2\u01bd\u01be")
        buf.write("\7H\2\2\u01be\u01bf\7c\2\2\u01bf\u01c0\7n\2\2\u01c0\u01c1")
        buf.write("\7u\2\2\u01c1\u01c2\7g\2\2\u01c2F\3\2\2\2\u01c3\u01c4")
        buf.write("\7C\2\2\u01c4\u01c5\7t\2\2\u01c5\u01c6\7t\2\2\u01c6\u01c7")
        buf.write("\7c\2\2\u01c7\u01c8\7{\2\2\u01c8H\3\2\2\2\u01c9\u01ca")
        buf.write("\7K\2\2\u01ca\u01cb\7p\2\2\u01cbJ\3\2\2\2\u01cc\u01cd")
        buf.write("\7K\2\2\u01cd\u01ce\7p\2\2\u01ce\u01cf\7v\2\2\u01cfL\3")
        buf.write("\2\2\2\u01d0\u01d1\7H\2\2\u01d1\u01d2\7n\2\2\u01d2\u01d3")
        buf.write("\7q\2\2\u01d3\u01d4\7c\2\2\u01d4\u01d5\7v\2\2\u01d5N\3")
        buf.write("\2\2\2\u01d6\u01d7\7D\2\2\u01d7\u01d8\7q\2\2\u01d8\u01d9")
        buf.write("\7q\2\2\u01d9\u01da\7n\2\2\u01da\u01db\7g\2\2\u01db\u01dc")
        buf.write("\7c\2\2\u01dc\u01dd\7p\2\2\u01ddP\3\2\2\2\u01de\u01df")
        buf.write("\7U\2\2\u01df\u01e0\7v\2\2\u01e0\u01e1\7t\2\2\u01e1\u01e2")
        buf.write("\7k\2\2\u01e2\u01e3\7p\2\2\u01e3\u01e4\7i\2\2\u01e4R\3")
        buf.write("\2\2\2\u01e5\u01e6\7T\2\2\u01e6\u01e7\7g\2\2\u01e7\u01e8")
        buf.write("\7v\2\2\u01e8\u01e9\7w\2\2\u01e9\u01ea\7t\2\2\u01ea\u01eb")
        buf.write("\7p\2\2\u01ebT\3\2\2\2\u01ec\u01ed\7P\2\2\u01ed\u01ee")
        buf.write("\7w\2\2\u01ee\u01ef\7n\2\2\u01ef\u01f0\7n\2\2\u01f0V\3")
        buf.write("\2\2\2\u01f1\u01f2\7E\2\2\u01f2\u01f3\7n\2\2\u01f3\u01f4")
        buf.write("\7c\2\2\u01f4\u01f5\7u\2\2\u01f5\u01f6\7u\2\2\u01f6X\3")
        buf.write("\2\2\2\u01f7\u01f8\7X\2\2\u01f8\u01f9\7c\2\2\u01f9\u01fa")
        buf.write("\7n\2\2\u01faZ\3\2\2\2\u01fb\u01fc\7X\2\2\u01fc\u01fd")
        buf.write("\7c\2\2\u01fd\u01fe\7t\2\2\u01fe\\\3\2\2\2\u01ff\u0200")
        buf.write("\7E\2\2\u0200\u0201\7q\2\2\u0201\u0202\7p\2\2\u0202\u0203")
        buf.write("\7u\2\2\u0203\u0204\7v\2\2\u0204\u0205\7t\2\2\u0205\u0206")
        buf.write("\7w\2\2\u0206\u0207\7e\2\2\u0207\u0208\7v\2\2\u0208\u0209")
        buf.write("\7q\2\2\u0209\u020a\7t\2\2\u020a^\3\2\2\2\u020b\u020c")
        buf.write("\7F\2\2\u020c\u020d\7g\2\2\u020d\u020e\7u\2\2\u020e\u020f")
        buf.write("\7v\2\2\u020f\u0210\7t\2\2\u0210\u0211\7w\2\2\u0211\u0212")
        buf.write("\7e\2\2\u0212\u0213\7v\2\2\u0213\u0214\7q\2\2\u0214\u0215")
        buf.write("\7t\2\2\u0215`\3\2\2\2\u0216\u0217\7P\2\2\u0217\u0218")
        buf.write("\7g\2\2\u0218\u0219\7y\2\2\u0219b\3\2\2\2\u021a\u021b")
        buf.write("\7D\2\2\u021b\u021c\7{\2\2\u021cd\3\2\2\2\u021d\u021e")
        buf.write("\7U\2\2\u021e\u021f\7g\2\2\u021f\u0220\7n\2\2\u0220\u0221")
        buf.write("\7h\2\2\u0221f\3\2\2\2\u0222\u0223\7-\2\2\u0223h\3\2\2")
        buf.write("\2\u0224\u0225\7/\2\2\u0225j\3\2\2\2\u0226\u0227\7,\2")
        buf.write("\2\u0227l\3\2\2\2\u0228\u0229\7\61\2\2\u0229n\3\2\2\2")
        buf.write("\u022a\u022b\7\'\2\2\u022bp\3\2\2\2\u022c\u022d\7#\2\2")
        buf.write("\u022dr\3\2\2\2\u022e\u022f\7(\2\2\u022f\u0230\7(\2\2")
        buf.write("\u0230t\3\2\2\2\u0231\u0232\7~\2\2\u0232\u0233\7~\2\2")
        buf.write("\u0233v\3\2\2\2\u0234\u0235\7?\2\2\u0235\u0236\7?\2\2")
        buf.write("\u0236x\3\2\2\2\u0237\u0238\7?\2\2\u0238z\3\2\2\2\u0239")
        buf.write("\u023a\7#\2\2\u023a\u023b\7?\2\2\u023b|\3\2\2\2\u023c")
        buf.write("\u023d\7@\2\2\u023d~\3\2\2\2\u023e\u023f\7>\2\2\u023f")
        buf.write("\u0240\7?\2\2\u0240\u0080\3\2\2\2\u0241\u0242\7>\2\2\u0242")
        buf.write("\u0082\3\2\2\2\u0243\u0244\7@\2\2\u0244\u0245\7?\2\2\u0245")
        buf.write("\u0084\3\2\2\2\u0246\u0247\7?\2\2\u0247\u0248\7?\2\2\u0248")
        buf.write("\u0249\7\60\2\2\u0249\u0086\3\2\2\2\u024a\u024b\7-\2\2")
        buf.write("\u024b\u024c\7\60\2\2\u024c\u0088\3\2\2\2\u024d\u024e")
        buf.write("\7<\2\2\u024e\u024f\7<\2\2\u024f\u008a\3\2\2\2\u0250\u0251")
        buf.write("\7<\2\2\u0251\u008c\3\2\2\2\u0252\u0253\7*\2\2\u0253\u008e")
        buf.write("\3\2\2\2\u0254\u0255\7+\2\2\u0255\u0090\3\2\2\2\u0256")
        buf.write("\u0257\7]\2\2\u0257\u0092\3\2\2\2\u0258\u0259\7_\2\2\u0259")
        buf.write("\u0094\3\2\2\2\u025a\u025b\7\60\2\2\u025b\u0096\3\2\2")
        buf.write("\2\u025c\u025d\7.\2\2\u025d\u0098\3\2\2\2\u025e\u025f")
        buf.write("\7=\2\2\u025f\u009a\3\2\2\2\u0260\u0261\7}\2\2\u0261\u009c")
        buf.write("\3\2\2\2\u0262\u0263\7\177\2\2\u0263\u009e\3\2\2\2\u0264")
        buf.write("\u0267\5\5\3\2\u0265\u0267\7a\2\2\u0266\u0264\3\2\2\2")
        buf.write("\u0266\u0265\3\2\2\2\u0267\u026d\3\2\2\2\u0268\u026c\5")
        buf.write("\5\3\2\u0269\u026c\5\7\4\2\u026a\u026c\7a\2\2\u026b\u0268")
        buf.write("\3\2\2\2\u026b\u0269\3\2\2\2\u026b\u026a\3\2\2\2\u026c")
        buf.write("\u026f\3\2\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2")
        buf.write("\u026e\u00a0\3\2\2\2\u026f\u026d\3\2\2\2\u0270\u0274\5")
        buf.write("\t\5\2\u0271\u0275\5\5\3\2\u0272\u0275\5\7\4\2\u0273\u0275")
        buf.write("\7a\2\2\u0274\u0271\3\2\2\2\u0274\u0272\3\2\2\2\u0274")
        buf.write("\u0273\3\2\2\2\u0275\u0276\3\2\2\2\u0276\u0274\3\2\2\2")
        buf.write("\u0276\u0277\3\2\2\2\u0277\u00a2\3\2\2\2\u0278\u0279\7")
        buf.write(")\2\2\u0279\u027a\7$\2\2\u027a\u00a4\3\2\2\2\u027b\u027c")
        buf.write("\7^\2\2\u027c\u027d\t\13\2\2\u027d\u00a6\3\2\2\2\u027e")
        buf.write("\u0282\n\f\2\2\u027f\u0282\5\u00a5S\2\u0280\u0282\5\u00a3")
        buf.write("R\2\u0281\u027e\3\2\2\2\u0281\u027f\3\2\2\2\u0281\u0280")
        buf.write("\3\2\2\2\u0282\u00a8\3\2\2\2\u0283\u0285\7^\2\2\u0284")
        buf.write("\u0286\n\13\2\2\u0285\u0284\3\2\2\2\u0285\u0286\3\2\2")
        buf.write("\2\u0286\u00aa\3\2\2\2\u0287\u0289\t\r\2\2\u0288\u0287")
        buf.write("\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u0288\3\2\2\2\u028a")
        buf.write("\u028b\3\2\2\2\u028b\u028c\3\2\2\2\u028c\u028d\bV\2\2")
        buf.write("\u028d\u00ac\3\2\2\2\u028e\u0292\5\r\7\2\u028f\u0291\5")
        buf.write("\u00a7T\2\u0290\u028f\3\2\2\2\u0291\u0294\3\2\2\2\u0292")
        buf.write("\u0290\3\2\2\2\u0292\u0293\3\2\2\2\u0293\u0295\3\2\2\2")
        buf.write("\u0294\u0292\3\2\2\2\u0295\u0296\bW\6\2\u0296\u00ae\3")
        buf.write("\2\2\2\u0297\u0298\13\2\2\2\u0298\u0299\bX\7\2\u0299\u00b0")
        buf.write("\3\2\2\2\u029a\u029e\5\r\7\2\u029b\u029d\5\u00a7T\2\u029c")
        buf.write("\u029b\3\2\2\2\u029d\u02a0\3\2\2\2\u029e\u029c\3\2\2\2")
        buf.write("\u029e\u029f\3\2\2\2\u029f\u02a1\3\2\2\2\u02a0\u029e\3")
        buf.write("\2\2\2\u02a1\u02a2\5\u00a9U\2\u02a2\u02a3\bY\b\2\u02a3")
        buf.write("\u00b2\3\2\2\2,\2\u00d7\u00e5\u00f1\u00f3\u00fb\u00fe")
        buf.write("\u0105\u0107\u010e\u0114\u0116\u011d\u0123\u0125\u012c")
        buf.write("\u013f\u0143\u0149\u014e\u0153\u0158\u015c\u0162\u0168")
        buf.write("\u016d\u0173\u0179\u017e\u0180\u0186\u018c\u0266\u026b")
        buf.write("\u026d\u0274\u0276\u0281\u0285\u028a\u0292\u029e\t\b\2")
        buf.write("\2\3\27\2\3\31\3\3\33\4\3W\5\3X\6\3Y\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COMMENT = 2
    INTLIT = 3
    ZERO = 4
    FLOATLIT = 5
    BOOLLIT = 6
    STRINGLIT = 7
    BREAK = 8
    CONTINUE = 9
    IF = 10
    ELSEIF = 11
    ELSE = 12
    FOREACH = 13
    TRUE = 14
    FALSE = 15
    ARRAY = 16
    IN = 17
    INT = 18
    FLOAT = 19
    BOOLEAN = 20
    STRING = 21
    RETURN = 22
    NULL = 23
    CLASS = 24
    VAL = 25
    VAR = 26
    CONSTRUCTOR = 27
    DESTRUCTOR = 28
    NEW = 29
    BY = 30
    SELF = 31
    ADD = 32
    MINUS = 33
    MULTIPLY = 34
    DIVIDE = 35
    MODULUS = 36
    NOT = 37
    AND = 38
    OR = 39
    EQUAL = 40
    ASSIGN = 41
    UNEQUAL = 42
    GREATER = 43
    LESS_EQ = 44
    LESS = 45
    GREATER_EQ = 46
    COMPARE_STR = 47
    CONCAT_STR = 48
    DOUBLE_COLON = 49
    COLON = 50
    LP = 51
    RP = 52
    LSB = 53
    RSB = 54
    DOT = 55
    COMMA = 56
    SEMI = 57
    LCB = 58
    RCB = 59
    ID = 60
    STATIC_ID = 61
    WS = 62
    UNCLOSE_STRING = 63
    ERROR_CHAR = 64
    ILLEGAL_ESCAPE = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'..'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", "'<='", "'<'", 
            "'>='", "'==.'", "'+.'", "'::'", "':'", "'('", "')'", "'['", 
            "']'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "INTLIT", "ZERO", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "ADD", "MINUS", "MULTIPLY", "DIVIDE", "MODULUS", 
            "NOT", "AND", "OR", "EQUAL", "ASSIGN", "UNEQUAL", "GREATER", 
            "LESS_EQ", "LESS", "GREATER_EQ", "COMPARE_STR", "CONCAT_STR", 
            "DOUBLE_COLON", "COLON", "LP", "RP", "LSB", "RSB", "DOT", "COMMA", 
            "SEMI", "LCB", "RCB", "ID", "STATIC_ID", "WS", "UNCLOSE_STRING", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "LETTER", "DIGIT", "DOLLAR", "EXPONENT", "DOUBLE_QUOTE", 
                  "BLANK", "TAB", "BACKSPACE", "FORM_FEED", "CARRIAGE_RETURN", 
                  "NEWLINE", "WHITE_CHAR", "SINGLE_QUOTE", "BACKSLASH", 
                  "COMMENT", "DECIMAL", "DEC_NO_", "OCTAL", "HEXA", "BINARY", 
                  "INTLIT", "ZERO", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "MINUS", "MULTIPLY", 
                  "DIVIDE", "MODULUS", "NOT", "AND", "OR", "EQUAL", "ASSIGN", 
                  "UNEQUAL", "GREATER", "LESS_EQ", "LESS", "GREATER_EQ", 
                  "COMPARE_STR", "CONCAT_STR", "DOUBLE_COLON", "COLON", 
                  "LP", "RP", "LSB", "RSB", "DOT", "COMMA", "SEMI", "LCB", 
                  "RCB", "ID", "STATIC_ID", "DBQUOTE_IN_STR", "ESCAPE_SEQUENCE", 
                  "VALID_CHARACTER", "ILLEGAL_CHARACTER", "WS", "UNCLOSE_STRING", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[21] = self.INTLIT_action 
            actions[23] = self.FLOATLIT_action 
            actions[25] = self.STRINGLIT_action 
            actions[85] = self.UNCLOSE_STRING_action 
            actions[86] = self.ERROR_CHAR_action 
            actions[87] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise UncloseString(self.text[1:])
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		raise IllegalEscape(self.text[1:])

     


