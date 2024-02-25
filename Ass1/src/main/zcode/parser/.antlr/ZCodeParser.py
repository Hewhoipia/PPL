# Generated from /Users/thong/WorkSpace/PPL/Ass1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,1,45,473,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,
        1,134,8,1,1,2,1,2,1,2,1,2,1,2,3,2,141,8,2,1,3,1,3,1,3,3,3,146,8,
        3,1,4,1,4,3,4,150,8,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,170,8,10,1,11,1,11,1,11,1,
        11,1,11,3,11,177,8,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,3,
        13,187,8,13,1,14,1,14,1,14,1,14,1,14,3,14,194,8,14,1,15,1,15,3,15,
        198,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,18,
        1,18,1,18,1,18,3,18,214,8,18,1,19,1,19,1,19,1,19,1,19,3,19,221,8,
        19,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,23,1,23,1,23,3,23,233,8,
        23,1,24,1,24,1,24,3,24,238,8,24,1,25,1,25,1,25,1,25,1,25,1,25,1,
        25,1,25,1,25,3,25,249,8,25,1,26,1,26,1,26,1,26,1,26,3,26,256,8,26,
        1,27,1,27,1,28,1,28,3,28,262,8,28,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,1,30,1,30,1,31,1,31,3,31,275,8,31,1,32,1,32,1,32,1,32,1,32,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,3,34,299,8,34,1,35,1,35,1,35,1,35,1,35,3,35,
        306,8,35,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,
        1,38,1,38,1,39,1,39,1,39,3,39,324,8,39,1,40,1,40,1,40,1,41,1,41,
        1,41,1,41,1,42,1,42,1,42,1,42,3,42,337,8,42,1,43,1,43,1,43,1,43,
        1,43,3,43,344,8,43,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,46,1,46,
        1,46,1,47,1,47,1,47,3,47,359,8,47,1,48,1,48,1,48,3,48,364,8,48,1,
        49,1,49,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,5,
        51,379,8,51,10,51,12,51,382,9,51,1,52,1,52,1,52,1,52,1,52,1,52,1,
        52,1,52,1,52,5,52,393,8,52,10,52,12,52,396,9,52,1,53,1,53,1,53,3,
        53,401,8,53,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,
        55,5,55,414,8,55,10,55,12,55,417,9,55,1,56,1,56,1,56,1,56,1,56,1,
        56,1,56,1,56,1,56,1,56,1,56,1,56,5,56,431,8,56,10,56,12,56,434,9,
        56,1,57,1,57,1,57,3,57,439,8,57,1,58,1,58,1,59,1,59,1,59,1,59,1,
        59,1,59,3,59,449,8,59,1,60,1,60,1,60,1,60,1,60,3,60,456,8,60,1,61,
        1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,61,3,61,469,8,61,
        1,62,1,62,1,62,0,4,102,104,110,112,63,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,
        108,110,112,114,116,118,120,122,124,0,3,2,0,3,5,8,8,1,0,3,5,1,0,
        1,2,462,0,126,1,0,0,0,2,133,1,0,0,0,4,140,1,0,0,0,6,145,1,0,0,0,
        8,149,1,0,0,0,10,151,1,0,0,0,12,154,1,0,0,0,14,156,1,0,0,0,16,158,
        1,0,0,0,18,161,1,0,0,0,20,169,1,0,0,0,22,176,1,0,0,0,24,178,1,0,
        0,0,26,186,1,0,0,0,28,193,1,0,0,0,30,197,1,0,0,0,32,199,1,0,0,0,
        34,205,1,0,0,0,36,213,1,0,0,0,38,220,1,0,0,0,40,222,1,0,0,0,42,224,
        1,0,0,0,44,227,1,0,0,0,46,232,1,0,0,0,48,237,1,0,0,0,50,248,1,0,
        0,0,52,255,1,0,0,0,54,257,1,0,0,0,56,261,1,0,0,0,58,263,1,0,0,0,
        60,267,1,0,0,0,62,274,1,0,0,0,64,276,1,0,0,0,66,281,1,0,0,0,68,298,
        1,0,0,0,70,305,1,0,0,0,72,307,1,0,0,0,74,316,1,0,0,0,76,318,1,0,
        0,0,78,323,1,0,0,0,80,325,1,0,0,0,82,328,1,0,0,0,84,336,1,0,0,0,
        86,343,1,0,0,0,88,345,1,0,0,0,90,347,1,0,0,0,92,352,1,0,0,0,94,358,
        1,0,0,0,96,363,1,0,0,0,98,365,1,0,0,0,100,367,1,0,0,0,102,369,1,
        0,0,0,104,383,1,0,0,0,106,400,1,0,0,0,108,402,1,0,0,0,110,404,1,
        0,0,0,112,418,1,0,0,0,114,438,1,0,0,0,116,440,1,0,0,0,118,448,1,
        0,0,0,120,455,1,0,0,0,122,468,1,0,0,0,124,470,1,0,0,0,126,127,3,
        2,1,0,127,128,5,0,0,1,128,1,1,0,0,0,129,130,3,6,3,0,130,131,3,4,
        2,0,131,134,1,0,0,0,132,134,1,0,0,0,133,129,1,0,0,0,133,132,1,0,
        0,0,134,3,1,0,0,0,135,136,5,37,0,0,136,137,3,6,3,0,137,138,3,4,2,
        0,138,141,1,0,0,0,139,141,1,0,0,0,140,135,1,0,0,0,140,139,1,0,0,
        0,141,5,1,0,0,0,142,146,3,8,4,0,143,146,3,32,16,0,144,146,1,0,0,
        0,145,142,1,0,0,0,145,143,1,0,0,0,145,144,1,0,0,0,146,7,1,0,0,0,
        147,150,3,10,5,0,148,150,3,12,6,0,149,147,1,0,0,0,149,148,1,0,0,
        0,150,9,1,0,0,0,151,152,3,14,7,0,152,153,3,30,15,0,153,11,1,0,0,
        0,154,155,3,56,28,0,155,13,1,0,0,0,156,157,7,0,0,0,157,15,1,0,0,
        0,158,159,5,40,0,0,159,160,3,18,9,0,160,17,1,0,0,0,161,162,5,34,
        0,0,162,163,3,20,10,0,163,164,5,35,0,0,164,19,1,0,0,0,165,166,3,
        108,54,0,166,167,3,22,11,0,167,170,1,0,0,0,168,170,1,0,0,0,169,165,
        1,0,0,0,169,168,1,0,0,0,170,21,1,0,0,0,171,172,5,36,0,0,172,173,
        3,108,54,0,173,174,3,22,11,0,174,177,1,0,0,0,175,177,1,0,0,0,176,
        171,1,0,0,0,176,175,1,0,0,0,177,23,1,0,0,0,178,179,5,34,0,0,179,
        180,3,26,13,0,180,181,5,35,0,0,181,25,1,0,0,0,182,183,3,98,49,0,
        183,184,3,28,14,0,184,187,1,0,0,0,185,187,1,0,0,0,186,182,1,0,0,
        0,186,185,1,0,0,0,187,27,1,0,0,0,188,189,5,36,0,0,189,190,3,98,49,
        0,190,191,3,28,14,0,191,194,1,0,0,0,192,194,1,0,0,0,193,188,1,0,
        0,0,193,192,1,0,0,0,194,29,1,0,0,0,195,198,5,40,0,0,196,198,3,16,
        8,0,197,195,1,0,0,0,197,196,1,0,0,0,198,31,1,0,0,0,199,200,5,9,0,
        0,200,201,5,40,0,0,201,202,3,34,17,0,202,203,3,46,23,0,203,204,3,
        48,24,0,204,33,1,0,0,0,205,206,5,32,0,0,206,207,3,36,18,0,207,208,
        5,33,0,0,208,35,1,0,0,0,209,210,3,40,20,0,210,211,3,38,19,0,211,
        214,1,0,0,0,212,214,1,0,0,0,213,209,1,0,0,0,213,212,1,0,0,0,214,
        37,1,0,0,0,215,216,5,36,0,0,216,217,3,40,20,0,217,218,3,38,19,0,
        218,221,1,0,0,0,219,221,1,0,0,0,220,215,1,0,0,0,220,219,1,0,0,0,
        221,39,1,0,0,0,222,223,3,42,21,0,223,41,1,0,0,0,224,225,3,44,22,
        0,225,226,3,30,15,0,226,43,1,0,0,0,227,228,7,1,0,0,228,45,1,0,0,
        0,229,230,5,37,0,0,230,233,3,46,23,0,231,233,1,0,0,0,232,229,1,0,
        0,0,232,231,1,0,0,0,233,47,1,0,0,0,234,238,3,78,39,0,235,238,3,90,
        45,0,236,238,1,0,0,0,237,234,1,0,0,0,237,235,1,0,0,0,237,236,1,0,
        0,0,238,49,1,0,0,0,239,249,3,54,27,0,240,249,3,56,28,0,241,249,3,
        64,32,0,242,249,3,72,36,0,243,249,3,74,37,0,244,249,3,76,38,0,245,
        249,3,78,39,0,246,249,3,80,40,0,247,249,3,90,45,0,248,239,1,0,0,
        0,248,240,1,0,0,0,248,241,1,0,0,0,248,242,1,0,0,0,248,243,1,0,0,
        0,248,244,1,0,0,0,248,245,1,0,0,0,248,246,1,0,0,0,248,247,1,0,0,
        0,249,51,1,0,0,0,250,251,3,92,46,0,251,252,3,50,25,0,252,253,3,52,
        26,0,253,256,1,0,0,0,254,256,1,0,0,0,255,250,1,0,0,0,255,254,1,0,
        0,0,256,53,1,0,0,0,257,258,3,8,4,0,258,55,1,0,0,0,259,262,3,58,29,
        0,260,262,3,60,30,0,261,259,1,0,0,0,261,260,1,0,0,0,262,57,1,0,0,
        0,263,264,3,30,15,0,264,265,5,30,0,0,265,266,3,98,49,0,266,59,1,
        0,0,0,267,268,3,62,31,0,268,269,3,30,15,0,269,270,5,30,0,0,270,271,
        3,98,49,0,271,61,1,0,0,0,272,275,3,14,7,0,273,275,5,7,0,0,274,272,
        1,0,0,0,274,273,1,0,0,0,275,63,1,0,0,0,276,277,3,66,33,0,277,278,
        3,68,34,0,278,279,3,92,46,0,279,280,3,70,35,0,280,65,1,0,0,0,281,
        282,5,15,0,0,282,283,5,32,0,0,283,284,3,100,50,0,284,285,5,33,0,
        0,285,286,3,96,48,0,286,287,3,50,25,0,287,67,1,0,0,0,288,289,3,92,
        46,0,289,290,5,17,0,0,290,291,5,32,0,0,291,292,3,100,50,0,292,293,
        5,33,0,0,293,294,3,96,48,0,294,295,3,50,25,0,295,296,3,68,34,0,296,
        299,1,0,0,0,297,299,1,0,0,0,298,288,1,0,0,0,298,297,1,0,0,0,299,
        69,1,0,0,0,300,301,5,16,0,0,301,302,3,96,48,0,302,303,3,50,25,0,
        303,306,1,0,0,0,304,306,1,0,0,0,305,300,1,0,0,0,305,304,1,0,0,0,
        306,71,1,0,0,0,307,308,5,10,0,0,308,309,5,40,0,0,309,310,5,11,0,
        0,310,311,3,100,50,0,311,312,5,12,0,0,312,313,3,98,49,0,313,314,
        3,96,48,0,314,315,3,50,25,0,315,73,1,0,0,0,316,317,5,13,0,0,317,
        75,1,0,0,0,318,319,5,14,0,0,319,77,1,0,0,0,320,321,5,6,0,0,321,324,
        3,98,49,0,322,324,5,6,0,0,323,320,1,0,0,0,323,322,1,0,0,0,324,79,
        1,0,0,0,325,326,5,40,0,0,326,327,3,82,41,0,327,81,1,0,0,0,328,329,
        5,32,0,0,329,330,3,84,42,0,330,331,5,33,0,0,331,83,1,0,0,0,332,333,
        3,88,44,0,333,334,3,86,43,0,334,337,1,0,0,0,335,337,1,0,0,0,336,
        332,1,0,0,0,336,335,1,0,0,0,337,85,1,0,0,0,338,339,5,36,0,0,339,
        340,3,88,44,0,340,341,3,86,43,0,341,344,1,0,0,0,342,344,1,0,0,0,
        343,338,1,0,0,0,343,342,1,0,0,0,344,87,1,0,0,0,345,346,3,98,49,0,
        346,89,1,0,0,0,347,348,5,18,0,0,348,349,3,52,26,0,349,350,3,92,46,
        0,350,351,5,19,0,0,351,91,1,0,0,0,352,353,5,37,0,0,353,354,3,94,
        47,0,354,93,1,0,0,0,355,356,5,37,0,0,356,359,3,94,47,0,357,359,1,
        0,0,0,358,355,1,0,0,0,358,357,1,0,0,0,359,95,1,0,0,0,360,361,5,37,
        0,0,361,364,3,96,48,0,362,364,1,0,0,0,363,360,1,0,0,0,363,362,1,
        0,0,0,364,97,1,0,0,0,365,366,3,100,50,0,366,99,1,0,0,0,367,368,3,
        102,51,0,368,101,1,0,0,0,369,370,6,51,-1,0,370,371,3,104,52,0,371,
        380,1,0,0,0,372,373,10,3,0,0,373,374,5,28,0,0,374,379,3,102,51,4,
        375,376,10,2,0,0,376,377,5,29,0,0,377,379,3,102,51,3,378,372,1,0,
        0,0,378,375,1,0,0,0,379,382,1,0,0,0,380,378,1,0,0,0,380,381,1,0,
        0,0,381,103,1,0,0,0,382,380,1,0,0,0,383,384,6,52,-1,0,384,385,3,
        106,53,0,385,394,1,0,0,0,386,387,10,3,0,0,387,388,5,21,0,0,388,393,
        3,104,52,4,389,390,10,2,0,0,390,391,5,22,0,0,391,393,3,104,52,3,
        392,386,1,0,0,0,392,389,1,0,0,0,393,396,1,0,0,0,394,392,1,0,0,0,
        394,395,1,0,0,0,395,105,1,0,0,0,396,394,1,0,0,0,397,398,5,20,0,0,
        398,401,3,106,53,0,399,401,3,108,54,0,400,397,1,0,0,0,400,399,1,
        0,0,0,401,107,1,0,0,0,402,403,3,110,55,0,403,109,1,0,0,0,404,405,
        6,55,-1,0,405,406,3,112,56,0,406,415,1,0,0,0,407,408,10,3,0,0,408,
        409,5,23,0,0,409,414,3,110,55,4,410,411,10,2,0,0,411,412,5,24,0,
        0,412,414,3,110,55,3,413,407,1,0,0,0,413,410,1,0,0,0,414,417,1,0,
        0,0,415,413,1,0,0,0,415,416,1,0,0,0,416,111,1,0,0,0,417,415,1,0,
        0,0,418,419,6,56,-1,0,419,420,3,114,57,0,420,432,1,0,0,0,421,422,
        10,4,0,0,422,423,5,25,0,0,423,431,3,112,56,5,424,425,10,3,0,0,425,
        426,5,26,0,0,426,431,3,112,56,4,427,428,10,2,0,0,428,429,5,27,0,
        0,429,431,3,112,56,3,430,421,1,0,0,0,430,424,1,0,0,0,430,427,1,0,
        0,0,431,434,1,0,0,0,432,430,1,0,0,0,432,433,1,0,0,0,433,113,1,0,
        0,0,434,432,1,0,0,0,435,436,5,24,0,0,436,439,3,114,57,0,437,439,
        3,116,58,0,438,435,1,0,0,0,438,437,1,0,0,0,439,115,1,0,0,0,440,441,
        3,118,59,0,441,117,1,0,0,0,442,443,3,122,61,0,443,444,5,31,0,0,444,
        445,3,122,61,0,445,446,3,120,60,0,446,449,1,0,0,0,447,449,3,122,
        61,0,448,442,1,0,0,0,448,447,1,0,0,0,449,119,1,0,0,0,450,451,5,31,
        0,0,451,452,3,122,61,0,452,453,3,120,60,0,453,456,1,0,0,0,454,456,
        1,0,0,0,455,450,1,0,0,0,455,454,1,0,0,0,456,121,1,0,0,0,457,458,
        5,32,0,0,458,459,3,98,49,0,459,460,5,33,0,0,460,469,1,0,0,0,461,
        469,5,40,0,0,462,469,5,38,0,0,463,469,5,39,0,0,464,469,3,124,62,
        0,465,469,3,16,8,0,466,469,3,24,12,0,467,469,3,80,40,0,468,457,1,
        0,0,0,468,461,1,0,0,0,468,462,1,0,0,0,468,463,1,0,0,0,468,464,1,
        0,0,0,468,465,1,0,0,0,468,466,1,0,0,0,468,467,1,0,0,0,469,123,1,
        0,0,0,470,471,7,2,0,0,471,125,1,0,0,0,37,133,140,145,149,169,176,
        186,193,197,213,220,232,237,248,255,261,274,298,305,323,336,343,
        358,363,378,380,392,394,400,413,415,430,432,438,448,455,468
    ]

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
                     "'['", "']'", "','", "'\\n'" ]

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




    def decls_list_tail(self):

        localctx = ZCodeParser.Decls_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decls_list_tail)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                self.match(ZCodeParser.NEWLINE)
                self.state = 136
                self.decls()
                self.state = 137
                self.decls_list_tail()
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
        self.enterRule(localctx, 6, self.RULE_decls)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.vari_decls()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.func_decls()
                pass
            elif token in [-1, 37]:
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




    def vari_decls_type(self):

        localctx = ZCodeParser.Vari_decls_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vari_decls_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 312) != 0)):
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




    def list_expr_num(self):

        localctx = ZCodeParser.List_expr_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_expr_num)
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.expr_num()
                self.state = 166
                self.list_expr_num_tail()
                pass
            elif token in [35]:
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




    def list_expr_num_tail(self):

        localctx = ZCodeParser.List_expr_num_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_expr_num_tail)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(ZCodeParser.COMMA)
                self.state = 172
                self.expr_num()
                self.state = 173
                self.list_expr_num_tail()
                pass
            elif token in [35]:
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




    def list_expr(self):

        localctx = ZCodeParser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_list_expr)
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.expr()
                self.state = 183
                self.list_expr_tail()
                pass
            elif token in [35]:
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




    def list_expr_tail(self):

        localctx = ZCodeParser.List_expr_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_list_expr_tail)
        try:
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(ZCodeParser.COMMA)
                self.state = 189
                self.expr()
                self.state = 190
                self.list_expr_tail()
                pass
            elif token in [35]:
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




    def list_param(self):

        localctx = ZCodeParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_param)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.params()
                self.state = 210
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
        self.enterRule(localctx, 38, self.RULE_list_param_tail)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(ZCodeParser.COMMA)
                self.state = 216
                self.params()
                self.state = 217
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

        def vd_for_func(self):
            return self.getTypedRuleContext(ZCodeParser.Vd_for_funcContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_params




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




    def vd_type_ff(self):

        localctx = ZCodeParser.Vd_type_ffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_vd_type_ff)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
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




    def func_body(self):

        localctx = ZCodeParser.Func_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func_body)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.stmt_return()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.stmt_block()
                pass
            elif token in [-1, 37]:
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




    def stmt_assi(self):

        localctx = ZCodeParser.Stmt_assiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_stmt_assi)
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.stmt_assi_1()
                pass
            elif token in [3, 4, 5, 7, 8]:
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




    def assi_type(self):

        localctx = ZCodeParser.Assi_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_assi_type)
        try:
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.vari_decls_type()
                pass
            elif token in [7]:
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




    def stmt_else(self):

        localctx = ZCodeParser.Stmt_elseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_stmt_else)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(ZCodeParser.ELSE)
                self.state = 301
                self.stmt_sepa_null()
                self.state = 302
                self.stmt()
                pass
            elif token in [37]:
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




    def sfc_list_args(self):

        localctx = ZCodeParser.Sfc_list_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_sfc_list_args)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.sfc_args()
                self.state = 333
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

        def sfc_args(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_argsContext,0)


        def sfc_list_args_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Sfc_list_args_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_list_args_tail




    def sfc_list_args_tail(self):

        localctx = ZCodeParser.Sfc_list_args_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_sfc_list_args_tail)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(ZCodeParser.COMMA)
                self.state = 339
                self.sfc_args()
                self.state = 340
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


    class Sfc_argsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_sfc_args




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




    def stmt_sepa_null(self):

        localctx = ZCodeParser.Stmt_sepa_nullContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmt_sepa_null)
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.match(ZCodeParser.NEWLINE)
                self.state = 361
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

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




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




    def expr_cond_not(self):

        localctx = ZCodeParser.Expr_cond_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr_cond_not)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(ZCodeParser.NOT)
                self.state = 398
                self.expr_cond_not()
                pass
            elif token in [1, 2, 24, 32, 34, 38, 39, 40]:
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




    def e_n_nega(self):

        localctx = ZCodeParser.E_n_negaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_e_n_nega)
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(ZCodeParser.SUB)
                self.state = 436
                self.e_n_nega()
                pass
            elif token in [1, 2, 32, 34, 38, 39, 40]:
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




    def boolval(self):

        localctx = ZCodeParser.BoolvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_boolval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
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
         




