# Generated from d:/Code/HK232/PPL/Ass4/assignment4-initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,1,52,367,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,3,0,80,
        8,0,1,0,1,0,1,0,1,1,4,1,86,8,1,11,1,12,1,87,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,99,8,2,1,3,1,3,1,3,1,3,1,3,3,3,106,8,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,3,4,115,8,4,1,5,1,5,1,5,1,5,1,5,3,5,122,8,
        5,1,5,1,5,1,6,5,6,127,8,6,10,6,12,6,130,9,6,1,7,1,7,1,7,1,7,1,7,
        3,7,137,8,7,1,7,1,7,1,8,1,8,3,8,143,8,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,3,9,154,8,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,
        12,1,12,3,12,166,8,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,3,
        14,176,8,14,1,14,1,14,1,15,1,15,1,15,3,15,183,8,15,1,15,1,15,1,15,
        1,16,4,16,189,8,16,11,16,12,16,190,1,17,1,17,3,17,195,8,17,1,18,
        1,18,1,18,3,18,200,8,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,3,18,214,8,18,1,18,3,18,217,8,18,1,19,1,19,1,
        19,1,19,1,19,1,19,3,19,225,8,19,1,19,1,19,3,19,229,8,19,1,19,3,19,
        232,8,19,1,20,1,20,1,20,1,20,3,20,238,8,20,1,21,1,21,1,21,1,21,1,
        21,3,21,245,8,21,1,22,1,22,1,22,1,22,1,22,1,22,3,22,253,8,22,1,23,
        1,23,1,23,1,24,1,24,1,24,1,24,3,24,262,8,24,1,25,4,25,265,8,25,11,
        25,12,25,266,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,3,27,277,8,
        27,1,28,1,28,1,29,1,29,1,29,1,29,1,29,3,29,286,8,29,1,30,1,30,1,
        30,1,30,1,30,3,30,293,8,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,301,
        8,31,10,31,12,31,304,9,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,312,
        8,32,10,32,12,32,315,9,32,1,33,1,33,1,33,1,33,1,33,1,33,5,33,323,
        8,33,10,33,12,33,326,9,33,1,34,1,34,1,34,3,34,331,8,34,1,35,1,35,
        1,35,3,35,336,8,35,1,36,1,36,1,36,1,36,1,36,3,36,343,8,36,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,353,8,36,1,37,1,37,1,37,1,
        37,1,37,1,37,3,37,361,8,37,1,38,1,38,1,38,1,38,1,38,0,3,62,64,66,
        39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,0,5,1,0,8,10,
        2,0,33,35,37,40,1,0,26,27,1,0,28,29,1,0,30,32,379,0,79,1,0,0,0,2,
        85,1,0,0,0,4,98,1,0,0,0,6,100,1,0,0,0,8,111,1,0,0,0,10,116,1,0,0,
        0,12,128,1,0,0,0,14,131,1,0,0,0,16,140,1,0,0,0,18,146,1,0,0,0,20,
        157,1,0,0,0,22,160,1,0,0,0,24,163,1,0,0,0,26,169,1,0,0,0,28,172,
        1,0,0,0,30,179,1,0,0,0,32,188,1,0,0,0,34,194,1,0,0,0,36,216,1,0,
        0,0,38,218,1,0,0,0,40,237,1,0,0,0,42,244,1,0,0,0,44,246,1,0,0,0,
        46,254,1,0,0,0,48,261,1,0,0,0,50,264,1,0,0,0,52,268,1,0,0,0,54,276,
        1,0,0,0,56,278,1,0,0,0,58,285,1,0,0,0,60,292,1,0,0,0,62,294,1,0,
        0,0,64,305,1,0,0,0,66,316,1,0,0,0,68,330,1,0,0,0,70,335,1,0,0,0,
        72,352,1,0,0,0,74,360,1,0,0,0,76,362,1,0,0,0,78,80,3,50,25,0,79,
        78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,3,32,16,0,82,83,5,0,
        0,1,83,1,1,0,0,0,84,86,3,4,2,0,85,84,1,0,0,0,86,87,1,0,0,0,87,85,
        1,0,0,0,87,88,1,0,0,0,88,3,1,0,0,0,89,99,3,36,18,0,90,99,3,6,3,0,
        91,99,3,8,4,0,92,99,3,18,9,0,93,99,3,20,10,0,94,99,3,22,11,0,95,
        99,3,24,12,0,96,99,3,26,13,0,97,99,3,30,15,0,98,89,1,0,0,0,98,90,
        1,0,0,0,98,91,1,0,0,0,98,92,1,0,0,0,98,93,1,0,0,0,98,94,1,0,0,0,
        98,95,1,0,0,0,98,96,1,0,0,0,98,97,1,0,0,0,99,5,1,0,0,0,100,105,5,
        47,0,0,101,102,5,44,0,0,102,103,3,52,26,0,103,104,5,45,0,0,104,106,
        1,0,0,0,105,101,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,
        5,36,0,0,108,109,3,56,28,0,109,110,3,50,25,0,110,7,1,0,0,0,111,112,
        3,10,5,0,112,114,3,12,6,0,113,115,3,16,8,0,114,113,1,0,0,0,114,115,
        1,0,0,0,115,9,1,0,0,0,116,117,5,20,0,0,117,118,5,42,0,0,118,119,
        3,56,28,0,119,121,5,43,0,0,120,122,3,50,25,0,121,120,1,0,0,0,121,
        122,1,0,0,0,122,123,1,0,0,0,123,124,3,4,2,0,124,11,1,0,0,0,125,127,
        3,14,7,0,126,125,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,
        1,0,0,0,129,13,1,0,0,0,130,128,1,0,0,0,131,132,5,22,0,0,132,133,
        5,42,0,0,133,134,3,56,28,0,134,136,5,43,0,0,135,137,3,50,25,0,136,
        135,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,139,3,4,2,0,139,
        15,1,0,0,0,140,142,5,21,0,0,141,143,3,50,25,0,142,141,1,0,0,0,142,
        143,1,0,0,0,143,144,1,0,0,0,144,145,3,4,2,0,145,17,1,0,0,0,146,147,
        5,15,0,0,147,148,5,47,0,0,148,149,5,16,0,0,149,150,3,56,28,0,150,
        151,5,17,0,0,151,153,3,56,28,0,152,154,3,50,25,0,153,152,1,0,0,0,
        153,154,1,0,0,0,154,155,1,0,0,0,155,156,3,4,2,0,156,19,1,0,0,0,157,
        158,5,18,0,0,158,159,3,50,25,0,159,21,1,0,0,0,160,161,5,19,0,0,161,
        162,3,50,25,0,162,23,1,0,0,0,163,165,5,11,0,0,164,166,3,56,28,0,
        165,164,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,168,3,50,25,
        0,168,25,1,0,0,0,169,170,3,28,14,0,170,171,3,50,25,0,171,27,1,0,
        0,0,172,173,5,47,0,0,173,175,5,42,0,0,174,176,3,52,26,0,175,174,
        1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,5,43,0,0,178,29,
        1,0,0,0,179,180,5,23,0,0,180,182,3,50,25,0,181,183,3,2,1,0,182,181,
        1,0,0,0,182,183,1,0,0,0,183,184,1,0,0,0,184,185,5,24,0,0,185,186,
        3,50,25,0,186,31,1,0,0,0,187,189,3,34,17,0,188,187,1,0,0,0,189,190,
        1,0,0,0,190,188,1,0,0,0,190,191,1,0,0,0,191,33,1,0,0,0,192,195,3,
        36,18,0,193,195,3,38,19,0,194,192,1,0,0,0,194,193,1,0,0,0,195,35,
        1,0,0,0,196,199,3,44,22,0,197,198,5,36,0,0,198,200,3,56,28,0,199,
        197,1,0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,202,3,50,25,0,202,
        217,1,0,0,0,203,204,5,12,0,0,204,205,5,47,0,0,205,206,5,36,0,0,206,
        207,3,56,28,0,207,208,3,50,25,0,208,217,1,0,0,0,209,210,5,13,0,0,
        210,213,5,47,0,0,211,212,5,36,0,0,212,214,3,56,28,0,213,211,1,0,
        0,0,213,214,1,0,0,0,214,215,1,0,0,0,215,217,3,50,25,0,216,196,1,
        0,0,0,216,203,1,0,0,0,216,209,1,0,0,0,217,37,1,0,0,0,218,219,5,14,
        0,0,219,220,5,47,0,0,220,221,5,42,0,0,221,222,3,40,20,0,222,231,
        5,43,0,0,223,225,3,50,25,0,224,223,1,0,0,0,224,225,1,0,0,0,225,228,
        1,0,0,0,226,229,3,30,15,0,227,229,3,24,12,0,228,226,1,0,0,0,228,
        227,1,0,0,0,229,232,1,0,0,0,230,232,3,50,25,0,231,224,1,0,0,0,231,
        230,1,0,0,0,232,39,1,0,0,0,233,234,3,44,22,0,234,235,3,42,21,0,235,
        238,1,0,0,0,236,238,1,0,0,0,237,233,1,0,0,0,237,236,1,0,0,0,238,
        41,1,0,0,0,239,240,5,46,0,0,240,241,3,44,22,0,241,242,3,42,21,0,
        242,245,1,0,0,0,243,245,1,0,0,0,244,239,1,0,0,0,244,243,1,0,0,0,
        245,43,1,0,0,0,246,247,7,0,0,0,247,252,5,47,0,0,248,249,5,44,0,0,
        249,250,3,46,23,0,250,251,5,45,0,0,251,253,1,0,0,0,252,248,1,0,0,
        0,252,253,1,0,0,0,253,45,1,0,0,0,254,255,5,1,0,0,255,256,3,48,24,
        0,256,47,1,0,0,0,257,258,5,46,0,0,258,259,5,1,0,0,259,262,3,48,24,
        0,260,262,1,0,0,0,261,257,1,0,0,0,261,260,1,0,0,0,262,49,1,0,0,0,
        263,265,5,49,0,0,264,263,1,0,0,0,265,266,1,0,0,0,266,264,1,0,0,0,
        266,267,1,0,0,0,267,51,1,0,0,0,268,269,3,56,28,0,269,270,3,54,27,
        0,270,53,1,0,0,0,271,272,5,46,0,0,272,273,3,56,28,0,273,274,3,54,
        27,0,274,277,1,0,0,0,275,277,1,0,0,0,276,271,1,0,0,0,276,275,1,0,
        0,0,277,55,1,0,0,0,278,279,3,58,29,0,279,57,1,0,0,0,280,281,3,60,
        30,0,281,282,5,41,0,0,282,283,3,60,30,0,283,286,1,0,0,0,284,286,
        3,60,30,0,285,280,1,0,0,0,285,284,1,0,0,0,286,59,1,0,0,0,287,288,
        3,62,31,0,288,289,7,1,0,0,289,290,3,62,31,0,290,293,1,0,0,0,291,
        293,3,62,31,0,292,287,1,0,0,0,292,291,1,0,0,0,293,61,1,0,0,0,294,
        295,6,31,-1,0,295,296,3,64,32,0,296,302,1,0,0,0,297,298,10,2,0,0,
        298,299,7,2,0,0,299,301,3,64,32,0,300,297,1,0,0,0,301,304,1,0,0,
        0,302,300,1,0,0,0,302,303,1,0,0,0,303,63,1,0,0,0,304,302,1,0,0,0,
        305,306,6,32,-1,0,306,307,3,66,33,0,307,313,1,0,0,0,308,309,10,2,
        0,0,309,310,7,3,0,0,310,312,3,66,33,0,311,308,1,0,0,0,312,315,1,
        0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,65,1,0,0,0,315,313,1,0,
        0,0,316,317,6,33,-1,0,317,318,3,68,34,0,318,324,1,0,0,0,319,320,
        10,2,0,0,320,321,7,4,0,0,321,323,3,68,34,0,322,319,1,0,0,0,323,326,
        1,0,0,0,324,322,1,0,0,0,324,325,1,0,0,0,325,67,1,0,0,0,326,324,1,
        0,0,0,327,328,5,25,0,0,328,331,3,68,34,0,329,331,3,70,35,0,330,327,
        1,0,0,0,330,329,1,0,0,0,331,69,1,0,0,0,332,333,7,3,0,0,333,336,3,
        70,35,0,334,336,3,72,36,0,335,332,1,0,0,0,335,334,1,0,0,0,336,71,
        1,0,0,0,337,353,5,47,0,0,338,353,3,74,37,0,339,353,3,28,14,0,340,
        343,5,47,0,0,341,343,3,28,14,0,342,340,1,0,0,0,342,341,1,0,0,0,343,
        344,1,0,0,0,344,345,5,44,0,0,345,346,3,52,26,0,346,347,5,45,0,0,
        347,353,1,0,0,0,348,349,5,42,0,0,349,350,3,56,28,0,350,351,5,43,
        0,0,351,353,1,0,0,0,352,337,1,0,0,0,352,338,1,0,0,0,352,339,1,0,
        0,0,352,342,1,0,0,0,352,348,1,0,0,0,353,73,1,0,0,0,354,361,5,1,0,
        0,355,361,5,2,0,0,356,361,5,5,0,0,357,361,5,3,0,0,358,361,5,4,0,
        0,359,361,3,76,38,0,360,354,1,0,0,0,360,355,1,0,0,0,360,356,1,0,
        0,0,360,357,1,0,0,0,360,358,1,0,0,0,360,359,1,0,0,0,361,75,1,0,0,
        0,362,363,5,44,0,0,363,364,3,52,26,0,364,365,5,45,0,0,365,77,1,0,
        0,0,37,79,87,98,105,114,121,128,136,142,153,165,175,182,190,194,
        199,213,216,224,228,231,237,244,252,261,266,276,285,292,302,313,
        324,330,335,342,352,360
    ]

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
                     "<INVALID>", "<INVALID>", "'\\n'", "'\\r'" ]

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
        self.checkVersion("4.13.1")
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




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 140737498627840) != 0)):
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
            if _la==44:
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
            if _la==49:
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
            if _la==49:
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
            if _la==49:
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
            if _la==49:
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 162728559771710) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 162728559771710) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737498627840) != 0):
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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 30464) != 0)):
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




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_declaration)
        try:
            self.state = 194
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10, 12, 13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.variable_declaration()
                pass
            elif token in [14]:
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




    def variable_declaration(self):

        localctx = ZCodeParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.parameter()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 197
                    self.match(ZCodeParser.ASSIGN)
                    self.state = 198
                    self.expression()


                self.state = 201
                self.newline_list()
                pass
            elif token in [12]:
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
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 209
                self.match(ZCodeParser.DYNAMIC)
                self.state = 210
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
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
                if _la==49:
                    self.state = 223
                    self.newline_list()


                self.state = 228
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [23]:
                    self.state = 226
                    self.block_statement()
                    pass
                elif token in [11]:
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




    def parameter_list(self):

        localctx = ZCodeParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_parameter_list)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.parameter()
                self.state = 234
                self.parameter_listtail()
                pass
            elif token in [43]:
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




    def parameter_listtail(self):

        localctx = ZCodeParser.Parameter_listtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter_listtail)
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(ZCodeParser.COMMA)
                self.state = 240
                self.parameter()
                self.state = 241
                self.parameter_listtail()
                pass
            elif token in [43]:
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




    def parameter(self):

        localctx = ZCodeParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 247
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
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




    def number_listtail(self):

        localctx = ZCodeParser.Number_listtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_number_listtail)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.match(ZCodeParser.COMMA)
                self.state = 258
                self.match(ZCodeParser.NUMBER_LITERAL)
                self.state = 259
                self.number_listtail()
                pass
            elif token in [45]:
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
                if not (_la==49):
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




    def expression_listtail(self):

        localctx = ZCodeParser.Expression_listtailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expression_listtail)
        try:
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(ZCodeParser.COMMA)
                self.state = 272
                self.expression()
                self.state = 273
                self.expression_listtail()
                pass
            elif token in [43, 45]:
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
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2121713844224) != 0)):
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
                    if not(_la==26 or _la==27):
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
                    if not(_la==28 or _la==29):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7516192768) != 0)):
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




    def not_operation(self):

        localctx = ZCodeParser.Not_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_not_operation)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(ZCodeParser.NOT)
                self.state = 328
                self.not_operation()
                pass
            elif token in [1, 2, 3, 4, 5, 28, 29, 42, 44, 47]:
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




    def sign_operation(self):

        localctx = ZCodeParser.Sign_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_sign_operation)
        self._la = 0 # Token type
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28, 29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                _la = self._input.LA(1)
                if not(_la==28 or _la==29):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 333
                self.sign_operation()
                pass
            elif token in [1, 2, 3, 4, 5, 42, 44, 47]:
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




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_literal)
        try:
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(ZCodeParser.NUMBER_LITERAL)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(ZCodeParser.STRING_LITERAL)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.match(ZCodeParser.BOOLEAN_LITERAL)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.match(ZCodeParser.UNCLOSE_STRING)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                self.match(ZCodeParser.ILLEGAL_ESCAPE)
                pass
            elif token in [44]:
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
         




