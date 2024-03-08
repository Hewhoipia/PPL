# Generated from d:/Code/HK232/PPL/Ass1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,405,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,105,8,1,1,2,1,
        2,1,2,3,2,110,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,127,8,3,1,4,1,4,1,5,1,5,1,6,1,6,3,6,135,8,6,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,
        9,3,9,154,8,9,1,10,1,10,1,10,1,10,1,10,3,10,161,8,10,1,11,1,11,3,
        11,165,8,11,1,12,1,12,3,12,169,8,12,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,3,14,183,8,14,1,15,1,15,1,15,1,15,
        1,15,3,15,190,8,15,1,16,1,16,1,16,1,17,1,17,1,17,3,17,198,8,17,1,
        18,1,18,1,18,3,18,203,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,3,19,214,8,19,1,20,1,20,1,20,1,20,1,20,3,20,221,8,20,1,21,
        1,21,1,22,1,22,1,22,1,22,1,23,1,23,5,23,231,8,23,10,23,12,23,234,
        9,23,1,23,3,23,237,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,
        1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,29,1,29,1,30,
        1,30,1,30,3,30,275,8,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,
        1,32,3,32,286,8,32,1,33,1,33,1,33,1,33,1,33,3,33,293,8,33,1,34,1,
        34,1,34,1,34,1,34,1,35,1,35,1,35,3,35,303,8,35,1,36,1,36,1,36,3,
        36,308,8,36,1,37,1,37,1,38,1,38,1,38,1,38,1,38,3,38,317,8,38,1,39,
        1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,3,39,328,8,39,1,40,1,40,
        1,40,1,40,1,40,1,40,1,40,1,40,1,40,5,40,339,8,40,10,40,12,40,342,
        9,40,1,41,1,41,1,41,3,41,347,8,41,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,5,42,358,8,42,10,42,12,42,361,9,42,1,43,1,43,1,43,
        1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,5,43,375,8,43,10,43,
        12,43,378,9,43,1,44,1,44,1,44,3,44,383,8,44,1,45,1,45,1,45,1,45,
        1,45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,396,8,45,1,46,1,46,1,46,
        1,46,1,46,1,47,1,47,1,47,0,3,80,84,86,48,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,
        64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,0,3,1,0,3,5,1,0,
        7,8,1,0,1,2,407,0,96,1,0,0,0,2,104,1,0,0,0,4,109,1,0,0,0,6,126,1,
        0,0,0,8,128,1,0,0,0,10,130,1,0,0,0,12,134,1,0,0,0,14,140,1,0,0,0,
        16,144,1,0,0,0,18,153,1,0,0,0,20,160,1,0,0,0,22,164,1,0,0,0,24,168,
        1,0,0,0,26,170,1,0,0,0,28,182,1,0,0,0,30,189,1,0,0,0,32,191,1,0,
        0,0,34,197,1,0,0,0,36,202,1,0,0,0,38,213,1,0,0,0,40,220,1,0,0,0,
        42,222,1,0,0,0,44,224,1,0,0,0,46,228,1,0,0,0,48,238,1,0,0,0,50,245,
        1,0,0,0,52,253,1,0,0,0,54,258,1,0,0,0,56,267,1,0,0,0,58,269,1,0,
        0,0,60,274,1,0,0,0,62,276,1,0,0,0,64,285,1,0,0,0,66,292,1,0,0,0,
        68,294,1,0,0,0,70,302,1,0,0,0,72,307,1,0,0,0,74,309,1,0,0,0,76,316,
        1,0,0,0,78,327,1,0,0,0,80,329,1,0,0,0,82,346,1,0,0,0,84,348,1,0,
        0,0,86,362,1,0,0,0,88,382,1,0,0,0,90,395,1,0,0,0,92,397,1,0,0,0,
        94,402,1,0,0,0,96,97,3,2,1,0,97,98,5,0,0,1,98,1,1,0,0,0,99,100,3,
        4,2,0,100,101,5,37,0,0,101,102,3,2,1,0,102,105,1,0,0,0,103,105,1,
        0,0,0,104,99,1,0,0,0,104,103,1,0,0,0,105,3,1,0,0,0,106,110,3,6,3,
        0,107,110,3,26,13,0,108,110,1,0,0,0,109,106,1,0,0,0,109,107,1,0,
        0,0,109,108,1,0,0,0,110,5,1,0,0,0,111,112,3,8,4,0,112,113,3,22,11,
        0,113,127,1,0,0,0,114,115,5,8,0,0,115,127,5,40,0,0,116,117,3,8,4,
        0,117,118,3,22,11,0,118,119,5,30,0,0,119,120,3,74,37,0,120,127,1,
        0,0,0,121,122,3,10,5,0,122,123,5,40,0,0,123,124,5,30,0,0,124,125,
        3,74,37,0,125,127,1,0,0,0,126,111,1,0,0,0,126,114,1,0,0,0,126,116,
        1,0,0,0,126,121,1,0,0,0,127,7,1,0,0,0,128,129,7,0,0,0,129,9,1,0,
        0,0,130,131,7,1,0,0,131,11,1,0,0,0,132,135,5,40,0,0,133,135,3,92,
        46,0,134,132,1,0,0,0,134,133,1,0,0,0,135,136,1,0,0,0,136,137,5,34,
        0,0,137,138,3,20,10,0,138,139,5,35,0,0,139,13,1,0,0,0,140,141,5,
        34,0,0,141,142,3,20,10,0,142,143,5,35,0,0,143,15,1,0,0,0,144,145,
        5,40,0,0,145,146,5,34,0,0,146,147,3,18,9,0,147,148,5,35,0,0,148,
        17,1,0,0,0,149,154,5,38,0,0,150,151,5,38,0,0,151,152,5,36,0,0,152,
        154,3,18,9,0,153,149,1,0,0,0,153,150,1,0,0,0,154,19,1,0,0,0,155,
        161,3,74,37,0,156,157,3,74,37,0,157,158,5,36,0,0,158,159,3,20,10,
        0,159,161,1,0,0,0,160,155,1,0,0,0,160,156,1,0,0,0,161,21,1,0,0,0,
        162,165,5,40,0,0,163,165,3,16,8,0,164,162,1,0,0,0,164,163,1,0,0,
        0,165,23,1,0,0,0,166,169,5,40,0,0,167,169,3,12,6,0,168,166,1,0,0,
        0,168,167,1,0,0,0,169,25,1,0,0,0,170,171,5,9,0,0,171,172,5,40,0,
        0,172,173,5,32,0,0,173,174,3,28,14,0,174,175,5,33,0,0,175,176,3,
        34,17,0,176,177,3,36,18,0,177,27,1,0,0,0,178,179,3,32,16,0,179,180,
        3,30,15,0,180,183,1,0,0,0,181,183,1,0,0,0,182,178,1,0,0,0,182,181,
        1,0,0,0,183,29,1,0,0,0,184,185,5,36,0,0,185,186,3,32,16,0,186,187,
        3,30,15,0,187,190,1,0,0,0,188,190,1,0,0,0,189,184,1,0,0,0,189,188,
        1,0,0,0,190,31,1,0,0,0,191,192,3,8,4,0,192,193,3,22,11,0,193,33,
        1,0,0,0,194,195,5,37,0,0,195,198,3,34,17,0,196,198,1,0,0,0,197,194,
        1,0,0,0,197,196,1,0,0,0,198,35,1,0,0,0,199,203,3,60,30,0,200,203,
        3,68,34,0,201,203,1,0,0,0,202,199,1,0,0,0,202,200,1,0,0,0,202,201,
        1,0,0,0,203,37,1,0,0,0,204,214,3,42,21,0,205,214,3,44,22,0,206,214,
        3,46,23,0,207,214,3,54,27,0,208,214,3,56,28,0,209,214,3,58,29,0,
        210,214,3,60,30,0,211,214,3,62,31,0,212,214,3,68,34,0,213,204,1,
        0,0,0,213,205,1,0,0,0,213,206,1,0,0,0,213,207,1,0,0,0,213,208,1,
        0,0,0,213,209,1,0,0,0,213,210,1,0,0,0,213,211,1,0,0,0,213,212,1,
        0,0,0,214,39,1,0,0,0,215,216,3,38,19,0,216,217,3,70,35,0,217,218,
        3,40,20,0,218,221,1,0,0,0,219,221,1,0,0,0,220,215,1,0,0,0,220,219,
        1,0,0,0,221,41,1,0,0,0,222,223,3,6,3,0,223,43,1,0,0,0,224,225,3,
        24,12,0,225,226,5,30,0,0,226,227,3,74,37,0,227,45,1,0,0,0,228,232,
        3,48,24,0,229,231,3,50,25,0,230,229,1,0,0,0,231,234,1,0,0,0,232,
        230,1,0,0,0,232,233,1,0,0,0,233,236,1,0,0,0,234,232,1,0,0,0,235,
        237,3,52,26,0,236,235,1,0,0,0,236,237,1,0,0,0,237,47,1,0,0,0,238,
        239,5,15,0,0,239,240,5,32,0,0,240,241,3,74,37,0,241,242,5,33,0,0,
        242,243,3,72,36,0,243,244,3,38,19,0,244,49,1,0,0,0,245,246,3,70,
        35,0,246,247,5,16,0,0,247,248,5,32,0,0,248,249,3,74,37,0,249,250,
        5,33,0,0,250,251,3,72,36,0,251,252,3,38,19,0,252,51,1,0,0,0,253,
        254,3,70,35,0,254,255,5,17,0,0,255,256,3,72,36,0,256,257,3,38,19,
        0,257,53,1,0,0,0,258,259,5,10,0,0,259,260,5,40,0,0,260,261,5,11,
        0,0,261,262,3,74,37,0,262,263,5,12,0,0,263,264,3,74,37,0,264,265,
        3,72,36,0,265,266,3,38,19,0,266,55,1,0,0,0,267,268,5,13,0,0,268,
        57,1,0,0,0,269,270,5,14,0,0,270,59,1,0,0,0,271,272,5,6,0,0,272,275,
        3,74,37,0,273,275,5,6,0,0,274,271,1,0,0,0,274,273,1,0,0,0,275,61,
        1,0,0,0,276,277,5,40,0,0,277,278,5,32,0,0,278,279,3,64,32,0,279,
        280,5,33,0,0,280,63,1,0,0,0,281,282,3,74,37,0,282,283,3,66,33,0,
        283,286,1,0,0,0,284,286,1,0,0,0,285,281,1,0,0,0,285,284,1,0,0,0,
        286,65,1,0,0,0,287,288,5,36,0,0,288,289,3,74,37,0,289,290,3,66,33,
        0,290,293,1,0,0,0,291,293,1,0,0,0,292,287,1,0,0,0,292,291,1,0,0,
        0,293,67,1,0,0,0,294,295,5,18,0,0,295,296,3,70,35,0,296,297,3,40,
        20,0,297,298,5,19,0,0,298,69,1,0,0,0,299,303,5,37,0,0,300,301,5,
        37,0,0,301,303,3,70,35,0,302,299,1,0,0,0,302,300,1,0,0,0,303,71,
        1,0,0,0,304,305,5,37,0,0,305,308,3,72,36,0,306,308,1,0,0,0,307,304,
        1,0,0,0,307,306,1,0,0,0,308,73,1,0,0,0,309,310,3,76,38,0,310,75,
        1,0,0,0,311,312,3,78,39,0,312,313,5,31,0,0,313,314,3,78,39,0,314,
        317,1,0,0,0,315,317,3,78,39,0,316,311,1,0,0,0,316,315,1,0,0,0,317,
        77,1,0,0,0,318,319,3,80,40,0,319,320,5,28,0,0,320,321,3,80,40,0,
        321,328,1,0,0,0,322,323,3,80,40,0,323,324,5,29,0,0,324,325,3,80,
        40,0,325,328,1,0,0,0,326,328,3,80,40,0,327,318,1,0,0,0,327,322,1,
        0,0,0,327,326,1,0,0,0,328,79,1,0,0,0,329,330,6,40,-1,0,330,331,3,
        84,42,0,331,340,1,0,0,0,332,333,10,3,0,0,333,334,5,21,0,0,334,339,
        3,84,42,0,335,336,10,2,0,0,336,337,5,22,0,0,337,339,3,84,42,0,338,
        332,1,0,0,0,338,335,1,0,0,0,339,342,1,0,0,0,340,338,1,0,0,0,340,
        341,1,0,0,0,341,81,1,0,0,0,342,340,1,0,0,0,343,344,5,20,0,0,344,
        347,3,82,41,0,345,347,3,88,44,0,346,343,1,0,0,0,346,345,1,0,0,0,
        347,83,1,0,0,0,348,349,6,42,-1,0,349,350,3,86,43,0,350,359,1,0,0,
        0,351,352,10,3,0,0,352,353,5,23,0,0,353,358,3,86,43,0,354,355,10,
        2,0,0,355,356,5,24,0,0,356,358,3,86,43,0,357,351,1,0,0,0,357,354,
        1,0,0,0,358,361,1,0,0,0,359,357,1,0,0,0,359,360,1,0,0,0,360,85,1,
        0,0,0,361,359,1,0,0,0,362,363,6,43,-1,0,363,364,3,82,41,0,364,376,
        1,0,0,0,365,366,10,4,0,0,366,367,5,25,0,0,367,375,3,82,41,0,368,
        369,10,3,0,0,369,370,5,26,0,0,370,375,3,82,41,0,371,372,10,2,0,0,
        372,373,5,27,0,0,373,375,3,82,41,0,374,365,1,0,0,0,374,368,1,0,0,
        0,374,371,1,0,0,0,375,378,1,0,0,0,376,374,1,0,0,0,376,377,1,0,0,
        0,377,87,1,0,0,0,378,376,1,0,0,0,379,380,5,24,0,0,380,383,3,88,44,
        0,381,383,3,90,45,0,382,379,1,0,0,0,382,381,1,0,0,0,383,89,1,0,0,
        0,384,385,5,32,0,0,385,386,3,74,37,0,386,387,5,33,0,0,387,396,1,
        0,0,0,388,396,5,40,0,0,389,396,5,38,0,0,390,396,5,39,0,0,391,396,
        3,94,47,0,392,396,3,12,6,0,393,396,3,14,7,0,394,396,3,92,46,0,395,
        384,1,0,0,0,395,388,1,0,0,0,395,389,1,0,0,0,395,390,1,0,0,0,395,
        391,1,0,0,0,395,392,1,0,0,0,395,393,1,0,0,0,395,394,1,0,0,0,396,
        91,1,0,0,0,397,398,5,40,0,0,398,399,5,32,0,0,399,400,3,64,32,0,400,
        401,5,33,0,0,401,93,1,0,0,0,402,403,7,2,0,0,403,95,1,0,0,0,32,104,
        109,126,134,153,160,164,168,182,189,197,202,213,220,232,236,274,
        285,292,302,307,316,327,338,340,346,357,359,374,376,382,395
    ]

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
                     "'['", "']'", "','", "'\\n'" ]

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
    RULE_list_param = 14
    RULE_list_param_tail = 15
    RULE_params = 16
    RULE_func_sepa = 17
    RULE_func_body = 18
    RULE_stmt = 19
    RULE_list_stmt = 20
    RULE_stmt_vari_decl = 21
    RULE_stmt_assi = 22
    RULE_stmt_cond = 23
    RULE_stmt_if = 24
    RULE_stmt_elif = 25
    RULE_stmt_else = 26
    RULE_stmt_for = 27
    RULE_stmt_break = 28
    RULE_stmt_continue = 29
    RULE_stmt_return = 30
    RULE_stmt_func_call = 31
    RULE_sfc_list_args = 32
    RULE_sfc_list_args_tail = 33
    RULE_stmt_block = 34
    RULE_stmt_sepa_nonnull = 35
    RULE_stmt_sepa_null = 36
    RULE_expr = 37
    RULE_expr_string_concat = 38
    RULE_expr_compare = 39
    RULE_expr_cond_andor = 40
    RULE_expr_cond_not = 41
    RULE_e_n_addsub = 42
    RULE_e_n_muldivmod = 43
    RULE_e_n_nega = 44
    RULE_expr_other = 45
    RULE_expr_func_call = 46
    RULE_boolval = 47

    ruleNames =  [ "program", "decls_list", "decls", "vari_decls", "vari_decls_type", 
                   "vari_decls_impli", "array", "array_tail", "array_decls", 
                   "list_num", "list_expr", "vari_decls_id", "vari_id", 
                   "func_decls", "list_param", "list_param_tail", "params", 
                   "func_sepa", "func_body", "stmt", "list_stmt", "stmt_vari_decl", 
                   "stmt_assi", "stmt_cond", "stmt_if", "stmt_elif", "stmt_else", 
                   "stmt_for", "stmt_break", "stmt_continue", "stmt_return", 
                   "stmt_func_call", "sfc_list_args", "sfc_list_args_tail", 
                   "stmt_block", "stmt_sepa_nonnull", "stmt_sepa_null", 
                   "expr", "expr_string_concat", "expr_compare", "expr_cond_andor", 
                   "expr_cond_not", "e_n_addsub", "e_n_muldivmod", "e_n_nega", 
                   "expr_other", "expr_func_call", "boolval" ]

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
        self.checkVersion("4.13.1")
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




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.decls_list()
            self.state = 97
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




    def decls_list(self):

        localctx = ZCodeParser.Decls_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decls_list)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8, 9, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.decls()
                self.state = 100
                self.match(ZCodeParser.NEWLINE)
                self.state = 101
                self.decls_list()
                pass
            elif token in [-1]:
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




    def decls(self):

        localctx = ZCodeParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decls)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.vari_decls()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.func_decls()
                pass
            elif token in [37]:
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




    def vari_decls(self):

        localctx = ZCodeParser.Vari_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vari_decls)
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.vari_decls_type()
                self.state = 112
                self.vari_decls_id()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 114
                self.match(ZCodeParser.DYNAMIC)
                self.state = 115
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.vari_decls_type()
                self.state = 117
                self.vari_decls_id()
                self.state = 118
                self.match(ZCodeParser.ASSIGN)
                self.state = 119
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.vari_decls_impli()
                self.state = 122
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 123
                self.match(ZCodeParser.ASSIGN)
                self.state = 124
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




    def vari_decls_type(self):

        localctx = ZCodeParser.Vari_decls_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vari_decls_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
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




    def vari_decls_impli(self):

        localctx = ZCodeParser.Vari_decls_impliContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vari_decls_impli)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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

        def OPENSQBRACKET(self):
            return self.getToken(ZCodeParser.OPENSQBRACKET, 0)

        def list_expr(self):
            return self.getTypedRuleContext(ZCodeParser.List_exprContext,0)


        def CLOSESQBRACKET(self):
            return self.getToken(ZCodeParser.CLOSESQBRACKET, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def expr_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 132
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 133
                self.expr_func_call()
                pass


            self.state = 136
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 137
            self.list_expr()
            self.state = 138
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




    def array_tail(self):

        localctx = ZCodeParser.Array_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 141
            self.list_expr()
            self.state = 142
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




    def array_decls(self):

        localctx = ZCodeParser.Array_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 145
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 146
            self.list_num()
            self.state = 147
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




    def list_num(self):

        localctx = ZCodeParser.List_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_list_num)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(ZCodeParser.NUMBER)
                self.state = 151
                self.match(ZCodeParser.COMMA)
                self.state = 152
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




    def list_expr(self):

        localctx = ZCodeParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expr)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.expr()
                self.state = 157
                self.match(ZCodeParser.COMMA)
                self.state = 158
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




    def vari_decls_id(self):

        localctx = ZCodeParser.Vari_decls_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_vari_decls_id)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
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




    def vari_id(self):

        localctx = ZCodeParser.Vari_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vari_id)
        try:
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
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




    def func_decls(self):

        localctx = ZCodeParser.Func_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_func_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ZCodeParser.FUNC)
            self.state = 171
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 172
            self.match(ZCodeParser.OPENPAREN)
            self.state = 173
            self.list_param()
            self.state = 174
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 175
            self.func_sepa()
            self.state = 176
            self.func_body()
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




    def list_param(self):

        localctx = ZCodeParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_param)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.params()
                self.state = 179
                self.list_param_tail()
                pass
            elif token in [33]:
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




    def list_param_tail(self):

        localctx = ZCodeParser.List_param_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_list_param_tail)
        try:
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(ZCodeParser.COMMA)
                self.state = 185
                self.params()
                self.state = 186
                self.list_param_tail()
                pass
            elif token in [33]:
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




    def params(self):

        localctx = ZCodeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_params)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.vari_decls_type()
            self.state = 192
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




    def func_sepa(self):

        localctx = ZCodeParser.Func_sepaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_sepa)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(ZCodeParser.NEWLINE)
                self.state = 195
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




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_func_body)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.stmt_return()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.stmt_block()
                pass
            elif token in [37]:
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




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_stmt)
        try:
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.stmt_vari_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.stmt_assi()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 206
                self.stmt_cond()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self.stmt_for()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 208
                self.stmt_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 209
                self.stmt_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 210
                self.stmt_return()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 211
                self.stmt_func_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 212
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




    def list_stmt(self):

        localctx = ZCodeParser.List_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_stmt)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.stmt()
                self.state = 216
                self.stmt_sepa_nonnull()
                self.state = 217
                self.list_stmt()
                pass
            elif token in [19]:
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




    def stmt_vari_decl(self):

        localctx = ZCodeParser.Stmt_vari_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_stmt_vari_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
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




    def stmt_assi(self):

        localctx = ZCodeParser.Stmt_assiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stmt_assi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.vari_id()
            self.state = 225
            self.match(ZCodeParser.ASSIGN)
            self.state = 226
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




    def stmt_cond(self):

        localctx = ZCodeParser.Stmt_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.stmt_if()
            self.state = 232
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 229
                    self.stmt_elif() 
                self.state = 234
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 235
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




    def stmt_if(self):

        localctx = ZCodeParser.Stmt_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(ZCodeParser.IF)
            self.state = 239
            self.match(ZCodeParser.OPENPAREN)
            self.state = 240
            self.expr()
            self.state = 241
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 242
            self.stmt_sepa_null()
            self.state = 243
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




    def stmt_elif(self):

        localctx = ZCodeParser.Stmt_elifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmt_elif)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.stmt_sepa_nonnull()
            self.state = 246
            self.match(ZCodeParser.ELIF)
            self.state = 247
            self.match(ZCodeParser.OPENPAREN)
            self.state = 248
            self.expr()
            self.state = 249
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 250
            self.stmt_sepa_null()
            self.state = 251
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




    def stmt_else(self):

        localctx = ZCodeParser.Stmt_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt_else)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.stmt_sepa_nonnull()
            self.state = 254
            self.match(ZCodeParser.ELSE)
            self.state = 255
            self.stmt_sepa_null()
            self.state = 256
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




    def stmt_for(self):

        localctx = ZCodeParser.Stmt_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ZCodeParser.FOR)
            self.state = 259
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 260
            self.match(ZCodeParser.UNTIL)
            self.state = 261
            self.expr()
            self.state = 262
            self.match(ZCodeParser.BY)
            self.state = 263
            self.expr()
            self.state = 264
            self.stmt_sepa_null()
            self.state = 265
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




    def stmt_break(self):

        localctx = ZCodeParser.Stmt_breakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
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




    def stmt_continue(self):

        localctx = ZCodeParser.Stmt_continueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
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




    def stmt_return(self):

        localctx = ZCodeParser.Stmt_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_stmt_return)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(ZCodeParser.RETURN)
                self.state = 272
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_func_call




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 277
            self.match(ZCodeParser.OPENPAREN)
            self.state = 278
            self.sfc_list_args()
            self.state = 279
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

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def sfc_list_args_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_list_args_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_list_args




    def sfc_list_args(self):

        localctx = ZCodeParser.Sfc_list_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_sfc_list_args)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.expr()
                self.state = 282
                self.sfc_list_args_tail()
                pass
            elif token in [33]:
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




    def sfc_list_args_tail(self):

        localctx = ZCodeParser.Sfc_list_args_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_sfc_list_args_tail)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(ZCodeParser.COMMA)
                self.state = 288
                self.expr()
                self.state = 289
                self.sfc_list_args_tail()
                pass
            elif token in [33]:
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




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.BEGIN)
            self.state = 295
            self.stmt_sepa_nonnull()
            self.state = 296
            self.list_stmt()
            self.state = 297
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




    def stmt_sepa_nonnull(self):

        localctx = ZCodeParser.Stmt_sepa_nonnullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmt_sepa_nonnull)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.match(ZCodeParser.NEWLINE)
                self.state = 301
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




    def stmt_sepa_null(self):

        localctx = ZCodeParser.Stmt_sepa_nullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt_sepa_null)
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.match(ZCodeParser.NEWLINE)
                self.state = 305
                self.stmt_sepa_null()
                pass
            elif token in [3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 40]:
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




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
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




    def expr_string_concat(self):

        localctx = ZCodeParser.Expr_string_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expr_string_concat)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.expr_compare()
                self.state = 312
                self.match(ZCodeParser.CONCAT)
                self.state = 313
                self.expr_compare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
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




    def expr_compare(self):

        localctx = ZCodeParser.Expr_compareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr_compare)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.expr_cond_andor(0)
                self.state = 319
                self.match(ZCodeParser.COMPARENUM)
                self.state = 320
                self.expr_cond_andor(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.expr_cond_andor(0)
                self.state = 323
                self.match(ZCodeParser.COMPARESTR)
                self.state = 324
                self.expr_cond_andor(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 326
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



    def expr_cond_andor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expr_cond_andorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr_cond_andor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.e_n_addsub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 338
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 332
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 333
                        self.match(ZCodeParser.AND)
                        self.state = 334
                        self.e_n_addsub(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 335
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 336
                        self.match(ZCodeParser.OR)
                        self.state = 337
                        self.e_n_addsub(0)
                        pass

             
                self.state = 342
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




    def expr_cond_not(self):

        localctx = ZCodeParser.Expr_cond_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr_cond_not)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(ZCodeParser.NOT)
                self.state = 344
                self.expr_cond_not()
                pass
            elif token in [1, 2, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
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



    def e_n_addsub(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.E_n_addsubContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_e_n_addsub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.e_n_muldivmod(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 357
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 351
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 352
                        self.match(ZCodeParser.ADD)
                        self.state = 353
                        self.e_n_muldivmod(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 354
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 355
                        self.match(ZCodeParser.SUB)
                        self.state = 356
                        self.e_n_muldivmod(0)
                        pass

             
                self.state = 361
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



    def e_n_muldivmod(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.E_n_muldivmodContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_e_n_muldivmod, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.expr_cond_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 374
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 365
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 366
                        self.match(ZCodeParser.MUL)
                        self.state = 367
                        self.expr_cond_not()
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 368
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 369
                        self.match(ZCodeParser.DIV)
                        self.state = 370
                        self.expr_cond_not()
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 371
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 372
                        self.match(ZCodeParser.MOD)
                        self.state = 373
                        self.expr_cond_not()
                        pass

             
                self.state = 378
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




    def e_n_nega(self):

        localctx = ZCodeParser.E_n_negaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_e_n_nega)
        try:
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.match(ZCodeParser.SUB)
                self.state = 380
                self.e_n_nega()
                pass
            elif token in [1, 2, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
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


        def expr_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_other




    def expr_other(self):

        localctx = ZCodeParser.Expr_otherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr_other)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(ZCodeParser.OPENPAREN)
                self.state = 385
                self.expr()
                self.state = 386
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 390
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 391
                self.boolval()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 392
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 393
                self.array_tail()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 394
                self.expr_func_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_func_callContext(ParserRuleContext):
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

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_func_call




    def expr_func_call(self):

        localctx = ZCodeParser.Expr_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 398
            self.match(ZCodeParser.OPENPAREN)
            self.state = 399
            self.sfc_list_args()
            self.state = 400
            self.match(ZCodeParser.CLOSEPAREN)
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




    def boolval(self):

        localctx = ZCodeParser.BoolvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_boolval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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
        self._predicates[40] = self.expr_cond_andor_sempred
        self._predicates[42] = self.e_n_addsub_sempred
        self._predicates[43] = self.e_n_muldivmod_sempred
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
         




