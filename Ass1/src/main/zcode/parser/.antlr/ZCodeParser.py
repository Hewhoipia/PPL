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
        4,1,45,402,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,105,8,1,1,2,1,
        2,1,2,3,2,110,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,3,3,127,8,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,151,8,9,1,
        10,1,10,1,10,1,10,1,10,3,10,158,8,10,1,11,1,11,3,11,162,8,11,1,12,
        1,12,3,12,166,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,
        1,14,1,14,1,14,3,14,180,8,14,1,15,1,15,1,15,1,15,1,15,3,15,187,8,
        15,1,16,1,16,1,16,1,17,1,17,1,17,3,17,195,8,17,1,18,1,18,1,18,3,
        18,200,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,211,
        8,19,1,20,1,20,1,20,1,20,1,20,3,20,218,8,20,1,21,1,21,1,22,1,22,
        1,22,1,22,1,23,1,23,5,23,228,8,23,10,23,12,23,231,9,23,1,23,3,23,
        234,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,3,30,
        272,8,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,3,32,
        284,8,32,1,33,1,33,1,33,1,33,1,33,3,33,291,8,33,1,34,1,34,3,34,295,
        8,34,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,3,36,305,8,36,1,37,
        1,37,1,37,3,37,310,8,37,1,38,1,38,1,39,1,39,1,39,1,39,1,39,3,39,
        319,8,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,1,40,3,40,330,8,
        40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,41,5,41,341,8,41,10,
        41,12,41,344,9,41,1,42,1,42,1,42,3,42,349,8,42,1,43,1,43,1,43,1,
        43,1,43,1,43,1,43,1,43,1,43,5,43,360,8,43,10,43,12,43,363,9,43,1,
        44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,44,5,44,377,
        8,44,10,44,12,44,380,9,44,1,45,1,45,1,45,3,45,385,8,45,1,46,1,46,
        1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,3,46,398,8,46,1,47,
        1,47,1,47,0,3,82,86,88,48,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,
        74,76,78,80,82,84,86,88,90,92,94,0,3,1,0,3,5,1,0,7,8,1,0,1,2,404,
        0,96,1,0,0,0,2,104,1,0,0,0,4,109,1,0,0,0,6,126,1,0,0,0,8,128,1,0,
        0,0,10,130,1,0,0,0,12,132,1,0,0,0,14,137,1,0,0,0,16,141,1,0,0,0,
        18,150,1,0,0,0,20,157,1,0,0,0,22,161,1,0,0,0,24,165,1,0,0,0,26,167,
        1,0,0,0,28,179,1,0,0,0,30,186,1,0,0,0,32,188,1,0,0,0,34,194,1,0,
        0,0,36,199,1,0,0,0,38,210,1,0,0,0,40,217,1,0,0,0,42,219,1,0,0,0,
        44,221,1,0,0,0,46,225,1,0,0,0,48,235,1,0,0,0,50,242,1,0,0,0,52,250,
        1,0,0,0,54,255,1,0,0,0,56,264,1,0,0,0,58,266,1,0,0,0,60,271,1,0,
        0,0,62,273,1,0,0,0,64,283,1,0,0,0,66,290,1,0,0,0,68,294,1,0,0,0,
        70,296,1,0,0,0,72,304,1,0,0,0,74,309,1,0,0,0,76,311,1,0,0,0,78,318,
        1,0,0,0,80,329,1,0,0,0,82,331,1,0,0,0,84,348,1,0,0,0,86,350,1,0,
        0,0,88,364,1,0,0,0,90,384,1,0,0,0,92,397,1,0,0,0,94,399,1,0,0,0,
        96,97,3,2,1,0,97,98,5,0,0,1,98,1,1,0,0,0,99,100,3,4,2,0,100,101,
        5,37,0,0,101,102,3,2,1,0,102,105,1,0,0,0,103,105,1,0,0,0,104,99,
        1,0,0,0,104,103,1,0,0,0,105,3,1,0,0,0,106,110,3,6,3,0,107,110,3,
        26,13,0,108,110,1,0,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,108,
        1,0,0,0,110,5,1,0,0,0,111,112,3,8,4,0,112,113,3,22,11,0,113,127,
        1,0,0,0,114,115,5,8,0,0,115,127,5,40,0,0,116,117,3,8,4,0,117,118,
        3,22,11,0,118,119,5,30,0,0,119,120,3,76,38,0,120,127,1,0,0,0,121,
        122,3,10,5,0,122,123,5,40,0,0,123,124,5,30,0,0,124,125,3,76,38,0,
        125,127,1,0,0,0,126,111,1,0,0,0,126,114,1,0,0,0,126,116,1,0,0,0,
        126,121,1,0,0,0,127,7,1,0,0,0,128,129,7,0,0,0,129,9,1,0,0,0,130,
        131,7,1,0,0,131,11,1,0,0,0,132,133,5,40,0,0,133,134,5,34,0,0,134,
        135,3,20,10,0,135,136,5,35,0,0,136,13,1,0,0,0,137,138,5,34,0,0,138,
        139,3,20,10,0,139,140,5,35,0,0,140,15,1,0,0,0,141,142,5,40,0,0,142,
        143,5,34,0,0,143,144,3,18,9,0,144,145,5,35,0,0,145,17,1,0,0,0,146,
        151,5,38,0,0,147,148,5,38,0,0,148,149,5,36,0,0,149,151,3,18,9,0,
        150,146,1,0,0,0,150,147,1,0,0,0,151,19,1,0,0,0,152,158,3,76,38,0,
        153,154,3,76,38,0,154,155,5,36,0,0,155,156,3,20,10,0,156,158,1,0,
        0,0,157,152,1,0,0,0,157,153,1,0,0,0,158,21,1,0,0,0,159,162,5,40,
        0,0,160,162,3,16,8,0,161,159,1,0,0,0,161,160,1,0,0,0,162,23,1,0,
        0,0,163,166,5,40,0,0,164,166,3,12,6,0,165,163,1,0,0,0,165,164,1,
        0,0,0,166,25,1,0,0,0,167,168,5,9,0,0,168,169,5,40,0,0,169,170,5,
        32,0,0,170,171,3,28,14,0,171,172,5,33,0,0,172,173,3,34,17,0,173,
        174,3,36,18,0,174,27,1,0,0,0,175,176,3,32,16,0,176,177,3,30,15,0,
        177,180,1,0,0,0,178,180,1,0,0,0,179,175,1,0,0,0,179,178,1,0,0,0,
        180,29,1,0,0,0,181,182,5,36,0,0,182,183,3,32,16,0,183,184,3,30,15,
        0,184,187,1,0,0,0,185,187,1,0,0,0,186,181,1,0,0,0,186,185,1,0,0,
        0,187,31,1,0,0,0,188,189,3,8,4,0,189,190,3,22,11,0,190,33,1,0,0,
        0,191,192,5,37,0,0,192,195,3,34,17,0,193,195,1,0,0,0,194,191,1,0,
        0,0,194,193,1,0,0,0,195,35,1,0,0,0,196,200,3,60,30,0,197,200,3,70,
        35,0,198,200,1,0,0,0,199,196,1,0,0,0,199,197,1,0,0,0,199,198,1,0,
        0,0,200,37,1,0,0,0,201,211,3,42,21,0,202,211,3,44,22,0,203,211,3,
        46,23,0,204,211,3,54,27,0,205,211,3,56,28,0,206,211,3,58,29,0,207,
        211,3,60,30,0,208,211,3,62,31,0,209,211,3,70,35,0,210,201,1,0,0,
        0,210,202,1,0,0,0,210,203,1,0,0,0,210,204,1,0,0,0,210,205,1,0,0,
        0,210,206,1,0,0,0,210,207,1,0,0,0,210,208,1,0,0,0,210,209,1,0,0,
        0,211,39,1,0,0,0,212,213,3,38,19,0,213,214,3,72,36,0,214,215,3,40,
        20,0,215,218,1,0,0,0,216,218,1,0,0,0,217,212,1,0,0,0,217,216,1,0,
        0,0,218,41,1,0,0,0,219,220,3,6,3,0,220,43,1,0,0,0,221,222,3,24,12,
        0,222,223,5,30,0,0,223,224,3,76,38,0,224,45,1,0,0,0,225,229,3,48,
        24,0,226,228,3,50,25,0,227,226,1,0,0,0,228,231,1,0,0,0,229,227,1,
        0,0,0,229,230,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,232,234,3,
        52,26,0,233,232,1,0,0,0,233,234,1,0,0,0,234,47,1,0,0,0,235,236,5,
        15,0,0,236,237,5,32,0,0,237,238,3,76,38,0,238,239,5,33,0,0,239,240,
        3,74,37,0,240,241,3,38,19,0,241,49,1,0,0,0,242,243,3,72,36,0,243,
        244,5,16,0,0,244,245,5,32,0,0,245,246,3,76,38,0,246,247,5,33,0,0,
        247,248,3,74,37,0,248,249,3,38,19,0,249,51,1,0,0,0,250,251,3,72,
        36,0,251,252,5,17,0,0,252,253,3,74,37,0,253,254,3,38,19,0,254,53,
        1,0,0,0,255,256,5,10,0,0,256,257,5,40,0,0,257,258,5,11,0,0,258,259,
        3,76,38,0,259,260,5,12,0,0,260,261,3,76,38,0,261,262,3,74,37,0,262,
        263,3,38,19,0,263,55,1,0,0,0,264,265,5,13,0,0,265,57,1,0,0,0,266,
        267,5,14,0,0,267,59,1,0,0,0,268,269,5,6,0,0,269,272,3,76,38,0,270,
        272,5,6,0,0,271,268,1,0,0,0,271,270,1,0,0,0,272,61,1,0,0,0,273,274,
        5,40,0,0,274,275,5,32,0,0,275,276,3,64,32,0,276,277,5,33,0,0,277,
        278,3,68,34,0,278,63,1,0,0,0,279,280,3,76,38,0,280,281,3,66,33,0,
        281,284,1,0,0,0,282,284,1,0,0,0,283,279,1,0,0,0,283,282,1,0,0,0,
        284,65,1,0,0,0,285,286,5,36,0,0,286,287,3,76,38,0,287,288,3,66,33,
        0,288,291,1,0,0,0,289,291,1,0,0,0,290,285,1,0,0,0,290,289,1,0,0,
        0,291,67,1,0,0,0,292,295,3,14,7,0,293,295,1,0,0,0,294,292,1,0,0,
        0,294,293,1,0,0,0,295,69,1,0,0,0,296,297,5,18,0,0,297,298,3,72,36,
        0,298,299,3,40,20,0,299,300,5,19,0,0,300,71,1,0,0,0,301,305,5,37,
        0,0,302,303,5,37,0,0,303,305,3,72,36,0,304,301,1,0,0,0,304,302,1,
        0,0,0,305,73,1,0,0,0,306,307,5,37,0,0,307,310,3,74,37,0,308,310,
        1,0,0,0,309,306,1,0,0,0,309,308,1,0,0,0,310,75,1,0,0,0,311,312,3,
        78,39,0,312,77,1,0,0,0,313,314,3,80,40,0,314,315,5,31,0,0,315,316,
        3,80,40,0,316,319,1,0,0,0,317,319,3,80,40,0,318,313,1,0,0,0,318,
        317,1,0,0,0,319,79,1,0,0,0,320,321,3,82,41,0,321,322,5,28,0,0,322,
        323,3,82,41,0,323,330,1,0,0,0,324,325,3,82,41,0,325,326,5,29,0,0,
        326,327,3,82,41,0,327,330,1,0,0,0,328,330,3,82,41,0,329,320,1,0,
        0,0,329,324,1,0,0,0,329,328,1,0,0,0,330,81,1,0,0,0,331,332,6,41,
        -1,0,332,333,3,86,43,0,333,342,1,0,0,0,334,335,10,3,0,0,335,336,
        5,21,0,0,336,341,3,86,43,0,337,338,10,2,0,0,338,339,5,22,0,0,339,
        341,3,86,43,0,340,334,1,0,0,0,340,337,1,0,0,0,341,344,1,0,0,0,342,
        340,1,0,0,0,342,343,1,0,0,0,343,83,1,0,0,0,344,342,1,0,0,0,345,346,
        5,20,0,0,346,349,3,84,42,0,347,349,3,90,45,0,348,345,1,0,0,0,348,
        347,1,0,0,0,349,85,1,0,0,0,350,351,6,43,-1,0,351,352,3,88,44,0,352,
        361,1,0,0,0,353,354,10,3,0,0,354,355,5,23,0,0,355,360,3,88,44,0,
        356,357,10,2,0,0,357,358,5,24,0,0,358,360,3,88,44,0,359,353,1,0,
        0,0,359,356,1,0,0,0,360,363,1,0,0,0,361,359,1,0,0,0,361,362,1,0,
        0,0,362,87,1,0,0,0,363,361,1,0,0,0,364,365,6,44,-1,0,365,366,3,84,
        42,0,366,378,1,0,0,0,367,368,10,4,0,0,368,369,5,25,0,0,369,377,3,
        84,42,0,370,371,10,3,0,0,371,372,5,26,0,0,372,377,3,84,42,0,373,
        374,10,2,0,0,374,375,5,27,0,0,375,377,3,84,42,0,376,367,1,0,0,0,
        376,370,1,0,0,0,376,373,1,0,0,0,377,380,1,0,0,0,378,376,1,0,0,0,
        378,379,1,0,0,0,379,89,1,0,0,0,380,378,1,0,0,0,381,382,5,24,0,0,
        382,385,3,90,45,0,383,385,3,92,46,0,384,381,1,0,0,0,384,383,1,0,
        0,0,385,91,1,0,0,0,386,387,5,32,0,0,387,388,3,76,38,0,388,389,5,
        33,0,0,389,398,1,0,0,0,390,398,5,40,0,0,391,398,5,38,0,0,392,398,
        5,39,0,0,393,398,3,94,47,0,394,398,3,12,6,0,395,398,3,14,7,0,396,
        398,3,62,31,0,397,386,1,0,0,0,397,390,1,0,0,0,397,391,1,0,0,0,397,
        392,1,0,0,0,397,393,1,0,0,0,397,394,1,0,0,0,397,395,1,0,0,0,397,
        396,1,0,0,0,398,93,1,0,0,0,399,400,7,2,0,0,400,95,1,0,0,0,32,104,
        109,126,150,157,161,165,179,186,194,199,210,217,229,233,271,283,
        290,294,304,309,318,329,340,342,348,359,361,376,378,384,397
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
    RULE_sfc_body = 34
    RULE_stmt_block = 35
    RULE_stmt_sepa_nonnull = 36
    RULE_stmt_sepa_null = 37
    RULE_expr = 38
    RULE_expr_string_concat = 39
    RULE_expr_compare = 40
    RULE_expr_cond_andor = 41
    RULE_expr_cond_not = 42
    RULE_e_n_addsub = 43
    RULE_e_n_muldivmod = 44
    RULE_e_n_nega = 45
    RULE_expr_other = 46
    RULE_boolval = 47

    ruleNames =  [ "program", "decls_list", "decls", "vari_decls", "vari_decls_type", 
                   "vari_decls_impli", "array", "array_tail", "array_decls", 
                   "list_num", "list_expr", "vari_decls_id", "vari_id", 
                   "func_decls", "list_param", "list_param_tail", "params", 
                   "func_sepa", "func_body", "stmt", "list_stmt", "stmt_vari_decl", 
                   "stmt_assi", "stmt_cond", "stmt_if", "stmt_elif", "stmt_else", 
                   "stmt_for", "stmt_break", "stmt_continue", "stmt_return", 
                   "stmt_func_call", "sfc_list_args", "sfc_list_args_tail", 
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




    def array(self):

        localctx = ZCodeParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 133
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 134
            self.list_expr()
            self.state = 135
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
            self.state = 137
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 138
            self.list_expr()
            self.state = 139
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
            self.state = 141
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 142
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 143
            self.list_num()
            self.state = 144
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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.match(ZCodeParser.NUMBER)
                self.state = 148
                self.match(ZCodeParser.COMMA)
                self.state = 149
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.expr()
                self.state = 154
                self.match(ZCodeParser.COMMA)
                self.state = 155
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
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
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
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
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
            self.state = 167
            self.match(ZCodeParser.FUNC)
            self.state = 168
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 169
            self.match(ZCodeParser.OPENPAREN)
            self.state = 170
            self.list_param()
            self.state = 171
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 172
            self.func_sepa()
            self.state = 173
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
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.params()
                self.state = 176
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
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(ZCodeParser.COMMA)
                self.state = 182
                self.params()
                self.state = 183
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
            self.state = 188
            self.vari_decls_type()
            self.state = 189
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
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(ZCodeParser.NEWLINE)
                self.state = 192
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
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.stmt_return()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
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
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.stmt_vari_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.stmt_assi()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.stmt_cond()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.stmt_for()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.stmt_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 206
                self.stmt_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 207
                self.stmt_return()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 208
                self.stmt_func_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 209
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
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.stmt()
                self.state = 213
                self.stmt_sepa_nonnull()
                self.state = 214
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
            self.state = 219
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
            self.state = 221
            self.vari_id()
            self.state = 222
            self.match(ZCodeParser.ASSIGN)
            self.state = 223
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
            self.state = 225
            self.stmt_if()
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 226
                    self.stmt_elif() 
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 232
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
            self.state = 235
            self.match(ZCodeParser.IF)
            self.state = 236
            self.match(ZCodeParser.OPENPAREN)
            self.state = 237
            self.expr()
            self.state = 238
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 239
            self.stmt_sepa_null()
            self.state = 240
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
            self.state = 242
            self.stmt_sepa_nonnull()
            self.state = 243
            self.match(ZCodeParser.ELIF)
            self.state = 244
            self.match(ZCodeParser.OPENPAREN)
            self.state = 245
            self.expr()
            self.state = 246
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 247
            self.stmt_sepa_null()
            self.state = 248
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
            self.state = 250
            self.stmt_sepa_nonnull()
            self.state = 251
            self.match(ZCodeParser.ELSE)
            self.state = 252
            self.stmt_sepa_null()
            self.state = 253
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
            self.state = 255
            self.match(ZCodeParser.FOR)
            self.state = 256
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 257
            self.match(ZCodeParser.UNTIL)
            self.state = 258
            self.expr()
            self.state = 259
            self.match(ZCodeParser.BY)
            self.state = 260
            self.expr()
            self.state = 261
            self.stmt_sepa_null()
            self.state = 262
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
            self.state = 264
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
            self.state = 266
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
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.match(ZCodeParser.RETURN)
                self.state = 269
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
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




    def stmt_func_call(self):

        localctx = ZCodeParser.Stmt_func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 274
            self.match(ZCodeParser.OPENPAREN)
            self.state = 275
            self.sfc_list_args()
            self.state = 276
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 277
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




    def sfc_list_args(self):

        localctx = ZCodeParser.Sfc_list_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_sfc_list_args)
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.expr()
                self.state = 280
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
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.match(ZCodeParser.COMMA)
                self.state = 286
                self.expr()
                self.state = 287
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


    class Sfc_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Array_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_body




    def sfc_body(self):

        localctx = ZCodeParser.Sfc_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_sfc_body)
        try:
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
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




    def stmt_block(self):

        localctx = ZCodeParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(ZCodeParser.BEGIN)
            self.state = 297
            self.stmt_sepa_nonnull()
            self.state = 298
            self.list_stmt()
            self.state = 299
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
        self.enterRule(localctx, 72, self.RULE_stmt_sepa_nonnull)
        try:
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(ZCodeParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(ZCodeParser.NEWLINE)
                self.state = 303
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
        self.enterRule(localctx, 74, self.RULE_stmt_sepa_null)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.match(ZCodeParser.NEWLINE)
                self.state = 307
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
        self.enterRule(localctx, 76, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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
        self.enterRule(localctx, 78, self.RULE_expr_string_concat)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.expr_compare()
                self.state = 314
                self.match(ZCodeParser.CONCAT)
                self.state = 315
                self.expr_compare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
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
        self.enterRule(localctx, 80, self.RULE_expr_compare)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.expr_cond_andor(0)
                self.state = 321
                self.match(ZCodeParser.COMPARENUM)
                self.state = 322
                self.expr_cond_andor(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 324
                self.expr_cond_andor(0)
                self.state = 325
                self.match(ZCodeParser.COMPARESTR)
                self.state = 326
                self.expr_cond_andor(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr_cond_andor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.e_n_addsub(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 340
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 334
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 335
                        self.match(ZCodeParser.AND)
                        self.state = 336
                        self.e_n_addsub(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 337
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 338
                        self.match(ZCodeParser.OR)
                        self.state = 339
                        self.e_n_addsub(0)
                        pass

             
                self.state = 344
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
        self.enterRule(localctx, 84, self.RULE_expr_cond_not)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(ZCodeParser.NOT)
                self.state = 346
                self.expr_cond_not()
                pass
            elif token in [1, 2, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_e_n_addsub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.e_n_muldivmod(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 359
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 353
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 354
                        self.match(ZCodeParser.ADD)
                        self.state = 355
                        self.e_n_muldivmod(0)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 356
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 357
                        self.match(ZCodeParser.SUB)
                        self.state = 358
                        self.e_n_muldivmod(0)
                        pass

             
                self.state = 363
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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_e_n_muldivmod, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expr_cond_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 378
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 376
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 367
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 368
                        self.match(ZCodeParser.MUL)
                        self.state = 369
                        self.expr_cond_not()
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 370
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 371
                        self.match(ZCodeParser.DIV)
                        self.state = 372
                        self.expr_cond_not()
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 373
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 374
                        self.match(ZCodeParser.MOD)
                        self.state = 375
                        self.expr_cond_not()
                        pass

             
                self.state = 380
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
        self.enterRule(localctx, 90, self.RULE_e_n_nega)
        try:
            self.state = 384
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 381
                self.match(ZCodeParser.SUB)
                self.state = 382
                self.e_n_nega()
                pass
            elif token in [1, 2, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
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




    def expr_other(self):

        localctx = ZCodeParser.Expr_otherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr_other)
        try:
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.match(ZCodeParser.OPENPAREN)
                self.state = 387
                self.expr()
                self.state = 388
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 392
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 393
                self.boolval()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 394
                self.array()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 395
                self.array_tail()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 396
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




    def boolval(self):

        localctx = ZCodeParser.BoolvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_boolval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
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
        self._predicates[41] = self.expr_cond_andor_sempred
        self._predicates[43] = self.e_n_addsub_sempred
        self._predicates[44] = self.e_n_muldivmod_sempred
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
         




