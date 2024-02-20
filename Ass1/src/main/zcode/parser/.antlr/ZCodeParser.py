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
        4,1,45,477,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,132,8,1,
        1,2,1,2,1,2,1,2,1,2,3,2,139,8,2,1,3,1,3,1,3,3,3,144,8,3,1,4,1,4,
        1,4,1,4,3,4,150,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,3,12,179,8,12,1,13,1,13,1,13,1,13,1,13,3,13,186,8,13,1,
        14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,196,8,15,1,16,1,16,1,
        16,1,16,1,16,3,16,203,8,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,
        18,1,18,1,18,1,19,1,19,1,19,1,19,3,19,219,8,19,1,20,1,20,1,20,1,
        20,1,20,3,20,226,8,20,1,21,1,21,3,21,230,8,21,1,22,1,22,1,22,3,22,
        235,8,22,1,23,1,23,3,23,239,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,3,24,250,8,24,1,25,1,25,1,25,1,25,1,25,3,25,257,8,25,
        1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,3,28,268,8,28,1,29,
        1,29,3,29,272,8,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,
        1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,
        3,32,296,8,32,1,33,1,33,1,33,1,33,1,33,3,33,303,8,33,1,34,1,34,1,
        34,1,34,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,
        37,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,3,40,332,
        8,40,1,41,1,41,1,41,1,41,1,41,3,41,339,8,41,1,42,1,42,1,43,1,43,
        1,43,1,43,1,43,1,44,1,44,1,44,3,44,351,8,44,1,45,1,45,1,45,3,45,
        356,8,45,1,46,1,46,1,46,3,46,361,8,46,1,47,1,47,1,48,1,48,1,48,1,
        48,1,48,1,48,1,48,1,48,1,48,5,48,374,8,48,10,48,12,48,377,9,48,1,
        49,1,49,1,49,3,49,382,8,49,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,
        50,1,50,3,50,393,8,50,1,51,1,51,1,52,1,52,3,52,399,8,52,1,53,1,53,
        1,53,1,53,1,53,1,54,1,54,1,54,1,54,1,54,3,54,411,8,54,1,55,1,55,
        1,55,1,55,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,1,56,3,56,426,
        8,56,1,57,1,57,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,5,58,
        439,8,58,10,58,12,58,442,9,58,1,59,1,59,1,59,1,59,1,59,1,59,1,59,
        1,59,1,59,1,59,1,59,1,59,5,59,456,8,59,10,59,12,59,459,9,59,1,60,
        1,60,1,60,3,60,464,8,60,1,61,1,61,1,61,1,61,1,61,1,61,1,61,1,61,
        1,61,3,61,475,8,61,1,61,0,3,96,116,118,62,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,
        104,106,108,110,112,114,116,118,120,122,0,2,1,0,3,5,1,0,1,2,475,
        0,124,1,0,0,0,2,131,1,0,0,0,4,138,1,0,0,0,6,143,1,0,0,0,8,149,1,
        0,0,0,10,151,1,0,0,0,12,154,1,0,0,0,14,159,1,0,0,0,16,162,1,0,0,
        0,18,165,1,0,0,0,20,167,1,0,0,0,22,170,1,0,0,0,24,178,1,0,0,0,26,
        185,1,0,0,0,28,187,1,0,0,0,30,195,1,0,0,0,32,202,1,0,0,0,34,204,
        1,0,0,0,36,210,1,0,0,0,38,218,1,0,0,0,40,225,1,0,0,0,42,229,1,0,
        0,0,44,234,1,0,0,0,46,238,1,0,0,0,48,249,1,0,0,0,50,256,1,0,0,0,
        52,258,1,0,0,0,54,260,1,0,0,0,56,267,1,0,0,0,58,271,1,0,0,0,60,273,
        1,0,0,0,62,278,1,0,0,0,64,295,1,0,0,0,66,302,1,0,0,0,68,304,1,0,
        0,0,70,313,1,0,0,0,72,315,1,0,0,0,74,317,1,0,0,0,76,320,1,0,0,0,
        78,323,1,0,0,0,80,331,1,0,0,0,82,338,1,0,0,0,84,340,1,0,0,0,86,342,
        1,0,0,0,88,350,1,0,0,0,90,355,1,0,0,0,92,360,1,0,0,0,94,362,1,0,
        0,0,96,364,1,0,0,0,98,381,1,0,0,0,100,392,1,0,0,0,102,394,1,0,0,
        0,104,398,1,0,0,0,106,400,1,0,0,0,108,410,1,0,0,0,110,412,1,0,0,
        0,112,425,1,0,0,0,114,427,1,0,0,0,116,429,1,0,0,0,118,443,1,0,0,
        0,120,463,1,0,0,0,122,474,1,0,0,0,124,125,3,2,1,0,125,126,5,0,0,
        1,126,1,1,0,0,0,127,128,3,6,3,0,128,129,3,4,2,0,129,132,1,0,0,0,
        130,132,1,0,0,0,131,127,1,0,0,0,131,130,1,0,0,0,132,3,1,0,0,0,133,
        134,5,37,0,0,134,135,3,6,3,0,135,136,3,4,2,0,136,139,1,0,0,0,137,
        139,1,0,0,0,138,133,1,0,0,0,138,137,1,0,0,0,139,5,1,0,0,0,140,144,
        3,8,4,0,141,144,3,34,17,0,142,144,1,0,0,0,143,140,1,0,0,0,143,141,
        1,0,0,0,143,142,1,0,0,0,144,7,1,0,0,0,145,150,3,10,5,0,146,150,3,
        12,6,0,147,150,3,14,7,0,148,150,3,16,8,0,149,145,1,0,0,0,149,146,
        1,0,0,0,149,147,1,0,0,0,149,148,1,0,0,0,150,9,1,0,0,0,151,152,3,
        18,9,0,152,153,5,40,0,0,153,11,1,0,0,0,154,155,5,7,0,0,155,156,5,
        40,0,0,156,157,5,30,0,0,157,158,3,92,46,0,158,13,1,0,0,0,159,160,
        5,8,0,0,160,161,5,40,0,0,161,15,1,0,0,0,162,163,3,18,9,0,163,164,
        3,20,10,0,164,17,1,0,0,0,165,166,7,0,0,0,166,19,1,0,0,0,167,168,
        5,40,0,0,168,169,3,22,11,0,169,21,1,0,0,0,170,171,5,34,0,0,171,172,
        3,24,12,0,172,173,5,35,0,0,173,23,1,0,0,0,174,175,3,114,57,0,175,
        176,3,26,13,0,176,179,1,0,0,0,177,179,3,114,57,0,178,174,1,0,0,0,
        178,177,1,0,0,0,179,25,1,0,0,0,180,181,5,36,0,0,181,182,3,114,57,
        0,182,183,3,26,13,0,183,186,1,0,0,0,184,186,1,0,0,0,185,180,1,0,
        0,0,185,184,1,0,0,0,186,27,1,0,0,0,187,188,5,34,0,0,188,189,3,30,
        15,0,189,190,5,35,0,0,190,29,1,0,0,0,191,192,3,92,46,0,192,193,3,
        32,16,0,193,196,1,0,0,0,194,196,1,0,0,0,195,191,1,0,0,0,195,194,
        1,0,0,0,196,31,1,0,0,0,197,198,5,36,0,0,198,199,3,92,46,0,199,200,
        3,32,16,0,200,203,1,0,0,0,201,203,1,0,0,0,202,197,1,0,0,0,202,201,
        1,0,0,0,203,33,1,0,0,0,204,205,5,9,0,0,205,206,5,40,0,0,206,207,
        3,36,18,0,207,208,3,44,22,0,208,209,3,46,23,0,209,35,1,0,0,0,210,
        211,5,32,0,0,211,212,3,38,19,0,212,213,5,33,0,0,213,37,1,0,0,0,214,
        215,3,42,21,0,215,216,3,40,20,0,216,219,1,0,0,0,217,219,1,0,0,0,
        218,214,1,0,0,0,218,217,1,0,0,0,219,39,1,0,0,0,220,221,5,36,0,0,
        221,222,3,42,21,0,222,223,3,40,20,0,223,226,1,0,0,0,224,226,1,0,
        0,0,225,220,1,0,0,0,225,224,1,0,0,0,226,41,1,0,0,0,227,230,3,10,
        5,0,228,230,3,16,8,0,229,227,1,0,0,0,229,228,1,0,0,0,230,43,1,0,
        0,0,231,232,5,37,0,0,232,235,3,44,22,0,233,235,1,0,0,0,234,231,1,
        0,0,0,234,233,1,0,0,0,235,45,1,0,0,0,236,239,3,74,37,0,237,239,3,
        86,43,0,238,236,1,0,0,0,238,237,1,0,0,0,239,47,1,0,0,0,240,250,3,
        52,26,0,241,250,3,54,27,0,242,250,3,60,30,0,243,250,3,68,34,0,244,
        250,3,70,35,0,245,250,3,72,36,0,246,250,3,74,37,0,247,250,3,76,38,
        0,248,250,3,86,43,0,249,240,1,0,0,0,249,241,1,0,0,0,249,242,1,0,
        0,0,249,243,1,0,0,0,249,244,1,0,0,0,249,245,1,0,0,0,249,246,1,0,
        0,0,249,247,1,0,0,0,249,248,1,0,0,0,250,49,1,0,0,0,251,252,3,88,
        44,0,252,253,3,48,24,0,253,254,3,50,25,0,254,257,1,0,0,0,255,257,
        1,0,0,0,256,251,1,0,0,0,256,255,1,0,0,0,257,51,1,0,0,0,258,259,3,
        8,4,0,259,53,1,0,0,0,260,261,3,56,28,0,261,262,3,58,29,0,262,263,
        5,30,0,0,263,264,3,92,46,0,264,55,1,0,0,0,265,268,3,18,9,0,266,268,
        1,0,0,0,267,265,1,0,0,0,267,266,1,0,0,0,268,57,1,0,0,0,269,272,5,
        40,0,0,270,272,3,20,10,0,271,269,1,0,0,0,271,270,1,0,0,0,272,59,
        1,0,0,0,273,274,3,62,31,0,274,275,3,64,32,0,275,276,3,88,44,0,276,
        277,3,66,33,0,277,61,1,0,0,0,278,279,5,15,0,0,279,280,5,32,0,0,280,
        281,3,94,47,0,281,282,5,33,0,0,282,283,3,90,45,0,283,284,3,48,24,
        0,284,63,1,0,0,0,285,286,3,88,44,0,286,287,5,17,0,0,287,288,5,32,
        0,0,288,289,3,94,47,0,289,290,5,33,0,0,290,291,3,90,45,0,291,292,
        3,48,24,0,292,293,3,64,32,0,293,296,1,0,0,0,294,296,1,0,0,0,295,
        285,1,0,0,0,295,294,1,0,0,0,296,65,1,0,0,0,297,298,5,16,0,0,298,
        299,3,90,45,0,299,300,3,48,24,0,300,303,1,0,0,0,301,303,1,0,0,0,
        302,297,1,0,0,0,302,301,1,0,0,0,303,67,1,0,0,0,304,305,5,10,0,0,
        305,306,5,40,0,0,306,307,5,11,0,0,307,308,3,94,47,0,308,309,5,12,
        0,0,309,310,3,92,46,0,310,311,3,90,45,0,311,312,3,48,24,0,312,69,
        1,0,0,0,313,314,5,13,0,0,314,71,1,0,0,0,315,316,5,14,0,0,316,73,
        1,0,0,0,317,318,5,6,0,0,318,319,3,92,46,0,319,75,1,0,0,0,320,321,
        5,40,0,0,321,322,3,78,39,0,322,77,1,0,0,0,323,324,5,32,0,0,324,325,
        3,80,40,0,325,326,5,33,0,0,326,79,1,0,0,0,327,328,3,84,42,0,328,
        329,3,82,41,0,329,332,1,0,0,0,330,332,1,0,0,0,331,327,1,0,0,0,331,
        330,1,0,0,0,332,81,1,0,0,0,333,334,5,36,0,0,334,335,3,84,42,0,335,
        336,3,82,41,0,336,339,1,0,0,0,337,339,1,0,0,0,338,333,1,0,0,0,338,
        337,1,0,0,0,339,83,1,0,0,0,340,341,3,92,46,0,341,85,1,0,0,0,342,
        343,5,18,0,0,343,344,3,50,25,0,344,345,3,88,44,0,345,346,5,19,0,
        0,346,87,1,0,0,0,347,348,5,37,0,0,348,351,3,88,44,0,349,351,5,37,
        0,0,350,347,1,0,0,0,350,349,1,0,0,0,351,89,1,0,0,0,352,353,5,37,
        0,0,353,356,3,90,45,0,354,356,1,0,0,0,355,352,1,0,0,0,355,354,1,
        0,0,0,356,91,1,0,0,0,357,361,3,94,47,0,358,361,3,104,52,0,359,361,
        3,114,57,0,360,357,1,0,0,0,360,358,1,0,0,0,360,359,1,0,0,0,361,93,
        1,0,0,0,362,363,3,96,48,0,363,95,1,0,0,0,364,365,6,48,-1,0,365,366,
        3,98,49,0,366,375,1,0,0,0,367,368,10,3,0,0,368,369,5,21,0,0,369,
        374,3,96,48,4,370,371,10,2,0,0,371,372,5,22,0,0,372,374,3,96,48,
        3,373,367,1,0,0,0,373,370,1,0,0,0,374,377,1,0,0,0,375,373,1,0,0,
        0,375,376,1,0,0,0,376,97,1,0,0,0,377,375,1,0,0,0,378,379,5,20,0,
        0,379,382,3,98,49,0,380,382,3,100,50,0,381,378,1,0,0,0,381,380,1,
        0,0,0,382,99,1,0,0,0,383,384,5,32,0,0,384,385,3,94,47,0,385,386,
        5,33,0,0,386,393,1,0,0,0,387,393,5,40,0,0,388,393,3,102,51,0,389,
        393,3,20,10,0,390,393,3,28,14,0,391,393,3,76,38,0,392,383,1,0,0,
        0,392,387,1,0,0,0,392,388,1,0,0,0,392,389,1,0,0,0,392,390,1,0,0,
        0,392,391,1,0,0,0,393,101,1,0,0,0,394,395,7,1,0,0,395,103,1,0,0,
        0,396,399,3,110,55,0,397,399,3,106,53,0,398,396,1,0,0,0,398,397,
        1,0,0,0,399,105,1,0,0,0,400,401,3,112,56,0,401,402,5,31,0,0,402,
        403,3,112,56,0,403,404,3,108,54,0,404,107,1,0,0,0,405,406,5,31,0,
        0,406,407,3,112,56,0,407,408,3,108,54,0,408,411,1,0,0,0,409,411,
        1,0,0,0,410,405,1,0,0,0,410,409,1,0,0,0,411,109,1,0,0,0,412,413,
        3,112,56,0,413,414,5,29,0,0,414,415,3,112,56,0,415,111,1,0,0,0,416,
        417,5,32,0,0,417,418,3,104,52,0,418,419,5,33,0,0,419,426,1,0,0,0,
        420,426,5,40,0,0,421,426,5,39,0,0,422,426,3,20,10,0,423,426,3,28,
        14,0,424,426,3,76,38,0,425,416,1,0,0,0,425,420,1,0,0,0,425,421,1,
        0,0,0,425,422,1,0,0,0,425,423,1,0,0,0,425,424,1,0,0,0,426,113,1,
        0,0,0,427,428,3,116,58,0,428,115,1,0,0,0,429,430,6,58,-1,0,430,431,
        3,118,59,0,431,440,1,0,0,0,432,433,10,3,0,0,433,434,5,23,0,0,434,
        439,3,116,58,4,435,436,10,2,0,0,436,437,5,24,0,0,437,439,3,116,58,
        3,438,432,1,0,0,0,438,435,1,0,0,0,439,442,1,0,0,0,440,438,1,0,0,
        0,440,441,1,0,0,0,441,117,1,0,0,0,442,440,1,0,0,0,443,444,6,59,-1,
        0,444,445,3,120,60,0,445,457,1,0,0,0,446,447,10,4,0,0,447,448,5,
        25,0,0,448,456,3,118,59,5,449,450,10,3,0,0,450,451,5,26,0,0,451,
        456,3,118,59,4,452,453,10,2,0,0,453,454,5,27,0,0,454,456,3,118,59,
        3,455,446,1,0,0,0,455,449,1,0,0,0,455,452,1,0,0,0,456,459,1,0,0,
        0,457,455,1,0,0,0,457,458,1,0,0,0,458,119,1,0,0,0,459,457,1,0,0,
        0,460,461,5,24,0,0,461,464,3,120,60,0,462,464,3,122,61,0,463,460,
        1,0,0,0,463,462,1,0,0,0,464,121,1,0,0,0,465,466,5,32,0,0,466,467,
        3,114,57,0,467,468,5,33,0,0,468,475,1,0,0,0,469,475,5,40,0,0,470,
        475,5,38,0,0,471,475,3,20,10,0,472,475,3,28,14,0,473,475,3,76,38,
        0,474,465,1,0,0,0,474,469,1,0,0,0,474,470,1,0,0,0,474,471,1,0,0,
        0,474,472,1,0,0,0,474,473,1,0,0,0,475,123,1,0,0,0,37,131,138,143,
        149,178,185,195,202,218,225,229,234,238,249,256,267,271,295,302,
        331,338,350,355,360,373,375,381,392,398,410,425,438,440,455,457,
        463,474
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
    RULE_vari_decls_type1 = 5
    RULE_vari_decls_type2 = 6
    RULE_vari_decls_type3 = 7
    RULE_vari_decls_type4 = 8
    RULE_vari_type = 9
    RULE_array = 10
    RULE_array_tail = 11
    RULE_list_expr_num = 12
    RULE_list_expr_num_tail = 13
    RULE_array_val = 14
    RULE_list_expr = 15
    RULE_list_expr_tail = 16
    RULE_func_decls = 17
    RULE_func_param = 18
    RULE_list_param = 19
    RULE_list_param_tail = 20
    RULE_params = 21
    RULE_func_sepa = 22
    RULE_func_body = 23
    RULE_stmt = 24
    RULE_list_stmt = 25
    RULE_stmt_vari_decl = 26
    RULE_stmt_assi = 27
    RULE_assi_type = 28
    RULE_assi_id = 29
    RULE_stmt_cond = 30
    RULE_stmt_if = 31
    RULE_stmt_elif = 32
    RULE_stmt_else = 33
    RULE_stmt_for = 34
    RULE_stmt_break = 35
    RULE_stmt_continue = 36
    RULE_stmt_return = 37
    RULE_stmt_func_call = 38
    RULE_sfc_param = 39
    RULE_sfc_list_args = 40
    RULE_sfc_list_args_tail = 41
    RULE_sfc_args = 42
    RULE_stmt_block = 43
    RULE_stmt_sepa_nonnull = 44
    RULE_stmt_sepa_null = 45
    RULE_expr = 46
    RULE_expr_cond = 47
    RULE_expr_cond_andor = 48
    RULE_expr_cond_not = 49
    RULE_expr_cond_other = 50
    RULE_boolval = 51
    RULE_expr_string = 52
    RULE_expr_string_concat = 53
    RULE_e_s_c_tail = 54
    RULE_expr_string_compare = 55
    RULE_stringval = 56
    RULE_expr_num = 57
    RULE_e_n_addsub = 58
    RULE_e_n_muldivmod = 59
    RULE_e_n_nega = 60
    RULE_e_n_other = 61

    ruleNames =  [ "program", "decls_list", "decls_list_tail", "decls", 
                   "vari_decls", "vari_decls_type1", "vari_decls_type2", 
                   "vari_decls_type3", "vari_decls_type4", "vari_type", 
                   "array", "array_tail", "list_expr_num", "list_expr_num_tail", 
                   "array_val", "list_expr", "list_expr_tail", "func_decls", 
                   "func_param", "list_param", "list_param_tail", "params", 
                   "func_sepa", "func_body", "stmt", "list_stmt", "stmt_vari_decl", 
                   "stmt_assi", "assi_type", "assi_id", "stmt_cond", "stmt_if", 
                   "stmt_elif", "stmt_else", "stmt_for", "stmt_break", "stmt_continue", 
                   "stmt_return", "stmt_func_call", "sfc_param", "sfc_list_args", 
                   "sfc_list_args_tail", "sfc_args", "stmt_block", "stmt_sepa_nonnull", 
                   "stmt_sepa_null", "expr", "expr_cond", "expr_cond_andor", 
                   "expr_cond_not", "expr_cond_other", "boolval", "expr_string", 
                   "expr_string_concat", "e_s_c_tail", "expr_string_compare", 
                   "stringval", "expr_num", "e_n_addsub", "e_n_muldivmod", 
                   "e_n_nega", "e_n_other" ]

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
            self.state = 124
            self.decls_list()
            self.state = 125
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
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.decls()
                self.state = 128
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
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 133
                self.match(ZCodeParser.NEWLINE)
                self.state = 134
                self.decls()
                self.state = 135
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
            self.state = 143
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.vari_decls()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
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

        def vari_decls_type1(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type1Context,0)


        def vari_decls_type2(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type2Context,0)


        def vari_decls_type3(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type3Context,0)


        def vari_decls_type4(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type4Context,0)


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
                self.state = 145
                self.vari_decls_type1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.vari_decls_type2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.vari_decls_type3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.vari_decls_type4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_type1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_typeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type1




    def vari_decls_type1(self):

        localctx = ZCodeParser.Vari_decls_type1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vari_decls_type1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.vari_type()
            self.state = 152
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_type2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type2




    def vari_decls_type2(self):

        localctx = ZCodeParser.Vari_decls_type2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vari_decls_type2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(ZCodeParser.VAR)
            self.state = 155
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 156
            self.match(ZCodeParser.ASSIGN)
            self.state = 157
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_type3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type3




    def vari_decls_type3(self):

        localctx = ZCodeParser.Vari_decls_type3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vari_decls_type3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(ZCodeParser.DYNAMIC)
            self.state = 160
            self.match(ZCodeParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_decls_type4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vari_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_typeContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vari_decls_type4




    def vari_decls_type4(self):

        localctx = ZCodeParser.Vari_decls_type4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vari_decls_type4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.vari_type()
            self.state = 163
            self.array()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vari_typeContext(ParserRuleContext):
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
            return ZCodeParser.RULE_vari_type




    def vari_type(self):

        localctx = ZCodeParser.Vari_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vari_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
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
        self.enterRule(localctx, 20, self.RULE_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 168
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
        self.enterRule(localctx, 22, self.RULE_array_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 171
            self.list_expr_num()
            self.state = 172
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
        self.enterRule(localctx, 24, self.RULE_list_expr_num)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.expr_num()
                self.state = 175
                self.list_expr_num_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.expr_num()
                pass


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
        self.enterRule(localctx, 26, self.RULE_list_expr_num_tail)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(ZCodeParser.COMMA)
                self.state = 181
                self.expr_num()
                self.state = 182
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
        self.enterRule(localctx, 28, self.RULE_array_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ZCodeParser.OPENSQBRACKET)
            self.state = 188
            self.list_expr()
            self.state = 189
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
        self.enterRule(localctx, 30, self.RULE_list_expr)
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.expr()
                self.state = 192
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
        self.enterRule(localctx, 32, self.RULE_list_expr_tail)
        try:
            self.state = 202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(ZCodeParser.COMMA)
                self.state = 198
                self.expr()
                self.state = 199
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
        self.enterRule(localctx, 34, self.RULE_func_decls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(ZCodeParser.FUNC)
            self.state = 205
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 206
            self.func_param()
            self.state = 207
            self.func_sepa()
            self.state = 208
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
        self.enterRule(localctx, 36, self.RULE_func_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(ZCodeParser.OPENPAREN)
            self.state = 211
            self.list_param()
            self.state = 212
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
        self.enterRule(localctx, 38, self.RULE_list_param)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.params()
                self.state = 215
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
        self.enterRule(localctx, 40, self.RULE_list_param_tail)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(ZCodeParser.COMMA)
                self.state = 221
                self.params()
                self.state = 222
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

        def vari_decls_type1(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type1Context,0)


        def vari_decls_type4(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_decls_type4Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_params




    def params(self):

        localctx = ZCodeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_params)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.vari_decls_type1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.vari_decls_type4()
                pass


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
        self.enterRule(localctx, 44, self.RULE_func_sepa)
        try:
            self.state = 234
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(ZCodeParser.NEWLINE)
                self.state = 232
                self.func_sepa()
                pass
            elif token in [6, 18]:
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
        self.enterRule(localctx, 46, self.RULE_func_body)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.stmt_return()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.stmt_block()
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
        self.enterRule(localctx, 48, self.RULE_stmt)
        try:
            self.state = 249
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.stmt_vari_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.stmt_assi()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.stmt_cond()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.stmt_for()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.stmt_break()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.stmt_continue()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 246
                self.stmt_return()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 247
                self.stmt_func_call()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 248
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
        self.enterRule(localctx, 50, self.RULE_list_stmt)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.stmt_sepa_nonnull()
                self.state = 252
                self.stmt()
                self.state = 253
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
        self.enterRule(localctx, 52, self.RULE_stmt_vari_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
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

        def assi_type(self):
            return self.getTypedRuleContext(ZCodeParser.Assi_typeContext,0)


        def assi_id(self):
            return self.getTypedRuleContext(ZCodeParser.Assi_idContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(ZCodeParser.ExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt_assi




    def stmt_assi(self):

        localctx = ZCodeParser.Stmt_assiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_stmt_assi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.assi_type()
            self.state = 261
            self.assi_id()
            self.state = 262
            self.match(ZCodeParser.ASSIGN)
            self.state = 263
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

        def vari_type(self):
            return self.getTypedRuleContext(ZCodeParser.Vari_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assi_type




    def assi_type(self):

        localctx = ZCodeParser.Assi_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assi_type)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.vari_type()
                pass
            elif token in [40]:
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


    class Assi_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assi_id




    def assi_id(self):

        localctx = ZCodeParser.Assi_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assi_id)
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.array()
                pass


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
        self.enterRule(localctx, 60, self.RULE_stmt_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.stmt_if()
            self.state = 274
            self.stmt_elif()
            self.state = 275
            self.stmt_sepa_nonnull()
            self.state = 276
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
        self.enterRule(localctx, 62, self.RULE_stmt_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(ZCodeParser.IF)
            self.state = 279
            self.match(ZCodeParser.OPENPAREN)
            self.state = 280
            self.expr_cond()
            self.state = 281
            self.match(ZCodeParser.CLOSEPAREN)
            self.state = 282
            self.stmt_sepa_null()
            self.state = 283
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
        self.enterRule(localctx, 64, self.RULE_stmt_elif)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.stmt_sepa_nonnull()
                self.state = 286
                self.match(ZCodeParser.ELIF)
                self.state = 287
                self.match(ZCodeParser.OPENPAREN)
                self.state = 288
                self.expr_cond()
                self.state = 289
                self.match(ZCodeParser.CLOSEPAREN)
                self.state = 290
                self.stmt_sepa_null()
                self.state = 291
                self.stmt()
                self.state = 292
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
        self.enterRule(localctx, 66, self.RULE_stmt_else)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.match(ZCodeParser.ELSE)
                self.state = 298
                self.stmt_sepa_null()
                self.state = 299
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
        self.enterRule(localctx, 68, self.RULE_stmt_for)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(ZCodeParser.FOR)
            self.state = 305
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 306
            self.match(ZCodeParser.UNTIL)
            self.state = 307
            self.expr_cond()
            self.state = 308
            self.match(ZCodeParser.BY)
            self.state = 309
            self.expr()
            self.state = 310
            self.stmt_sepa_null()
            self.state = 311
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
        self.enterRule(localctx, 70, self.RULE_stmt_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
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
        self.enterRule(localctx, 72, self.RULE_stmt_continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
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
        self.enterRule(localctx, 74, self.RULE_stmt_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(ZCodeParser.RETURN)
            self.state = 318
            self.expr()
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
        self.enterRule(localctx, 76, self.RULE_stmt_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 321
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
        self.enterRule(localctx, 78, self.RULE_sfc_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.OPENPAREN)
            self.state = 324
            self.sfc_list_args()
            self.state = 325
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
        self.enterRule(localctx, 80, self.RULE_sfc_list_args)
        try:
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 24, 32, 34, 38, 39, 40]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.sfc_args()
                self.state = 328
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
        self.enterRule(localctx, 82, self.RULE_sfc_list_args_tail)
        try:
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.match(ZCodeParser.COMMA)
                self.state = 334
                self.sfc_args()
                self.state = 335
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
        self.enterRule(localctx, 84, self.RULE_sfc_args)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
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
        self.enterRule(localctx, 86, self.RULE_stmt_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.BEGIN)
            self.state = 343
            self.list_stmt()
            self.state = 344
            self.stmt_sepa_nonnull()
            self.state = 345
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
        self.enterRule(localctx, 88, self.RULE_stmt_sepa_nonnull)
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(ZCodeParser.NEWLINE)
                self.state = 348
                self.stmt_sepa_nonnull()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(ZCodeParser.NEWLINE)
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
        self.enterRule(localctx, 90, self.RULE_stmt_sepa_null)
        try:
            self.state = 355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.match(ZCodeParser.NEWLINE)
                self.state = 353
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


        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def expr_num(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_numContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr




    def expr(self):

        localctx = ZCodeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.expr_cond()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.expr_string()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
                self.expr_num()
                pass


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

        def expr_cond_andor(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_andorContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond




    def expr_cond(self):

        localctx = ZCodeParser.Expr_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.expr_cond_andor(0)
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
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr_cond_andor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expr_cond_not()
            self._ctx.stop = self._input.LT(-1)
            self.state = 375
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 373
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 367
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 368
                        self.match(ZCodeParser.AND)
                        self.state = 369
                        self.expr_cond_andor(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.Expr_cond_andorContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_cond_andor)
                        self.state = 370
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 371
                        self.match(ZCodeParser.OR)
                        self.state = 372
                        self.expr_cond_andor(3)
                        pass

             
                self.state = 377
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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


        def expr_cond_other(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_cond_otherContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond_not




    def expr_cond_not(self):

        localctx = ZCodeParser.Expr_cond_notContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr_cond_not)
        try:
            self.state = 381
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(ZCodeParser.NOT)
                self.state = 379
                self.expr_cond_not()
                pass
            elif token in [1, 2, 32, 34, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.expr_cond_other()
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


    class Expr_cond_otherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_cond(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_condContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def boolval(self):
            return self.getTypedRuleContext(ZCodeParser.BoolvalContext,0)


        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_cond_other




    def expr_cond_other(self):

        localctx = ZCodeParser.Expr_cond_otherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr_cond_other)
        try:
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.match(ZCodeParser.OPENPAREN)
                self.state = 384
                self.expr_cond()
                self.state = 385
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
                self.boolval()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 389
                self.array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 390
                self.array_val()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 391
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
        self.enterRule(localctx, 102, self.RULE_boolval)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
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


    class Expr_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_string_compare(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_string_compareContext,0)


        def expr_string_concat(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_string_concatContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string




    def expr_string(self):

        localctx = ZCodeParser.Expr_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expr_string)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 396
                self.expr_string_compare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 397
                self.expr_string_concat()
                pass


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

        def stringval(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StringvalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StringvalContext,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def e_s_c_tail(self):
            return self.getTypedRuleContext(ZCodeParser.E_s_c_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string_concat




    def expr_string_concat(self):

        localctx = ZCodeParser.Expr_string_concatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr_string_concat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.stringval()
            self.state = 401
            self.match(ZCodeParser.CONCAT)
            self.state = 402
            self.stringval()
            self.state = 403
            self.e_s_c_tail()
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

        def stringval(self):
            return self.getTypedRuleContext(ZCodeParser.StringvalContext,0)


        def e_s_c_tail(self):
            return self.getTypedRuleContext(ZCodeParser.E_s_c_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_e_s_c_tail




    def e_s_c_tail(self):

        localctx = ZCodeParser.E_s_c_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_e_s_c_tail)
        try:
            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.match(ZCodeParser.CONCAT)
                self.state = 406
                self.stringval()
                self.state = 407
                self.e_s_c_tail()
                pass
            elif token in [-1, 3, 4, 5, 6, 7, 8, 10, 13, 14, 15, 18, 33, 35, 36, 37, 40]:
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


    class Expr_string_compareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stringval(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StringvalContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StringvalContext,i)


        def COMPARESTR(self):
            return self.getToken(ZCodeParser.COMPARESTR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expr_string_compare




    def expr_string_compare(self):

        localctx = ZCodeParser.Expr_string_compareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expr_string_compare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.stringval()
            self.state = 413
            self.match(ZCodeParser.COMPARESTR)
            self.state = 414
            self.stringval()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringvalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_string(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_stringContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stringval




    def stringval(self):

        localctx = ZCodeParser.StringvalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_stringval)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(ZCodeParser.OPENPAREN)
                self.state = 417
                self.expr_string()
                self.state = 418
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 421
                self.match(ZCodeParser.STRING)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 422
                self.array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 423
                self.array_val()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 424
                self.stmt_func_call()
                pass


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
        self.enterRule(localctx, 114, self.RULE_expr_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
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
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_e_n_addsub, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.e_n_muldivmod(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 440
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 438
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 432
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 433
                        self.match(ZCodeParser.ADD)
                        self.state = 434
                        self.e_n_addsub(4)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_addsubContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_addsub)
                        self.state = 435
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 436
                        self.match(ZCodeParser.SUB)
                        self.state = 437
                        self.e_n_addsub(3)
                        pass

             
                self.state = 442
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_e_n_muldivmod, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.e_n_nega()
            self._ctx.stop = self._input.LT(-1)
            self.state = 457
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 455
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 446
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 447
                        self.match(ZCodeParser.MUL)
                        self.state = 448
                        self.e_n_muldivmod(5)
                        pass

                    elif la_ == 2:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 449
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 450
                        self.match(ZCodeParser.DIV)
                        self.state = 451
                        self.e_n_muldivmod(4)
                        pass

                    elif la_ == 3:
                        localctx = ZCodeParser.E_n_muldivmodContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_e_n_muldivmod)
                        self.state = 452
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 453
                        self.match(ZCodeParser.MOD)
                        self.state = 454
                        self.e_n_muldivmod(3)
                        pass

             
                self.state = 459
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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


        def e_n_other(self):
            return self.getTypedRuleContext(ZCodeParser.E_n_otherContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_e_n_nega




    def e_n_nega(self):

        localctx = ZCodeParser.E_n_negaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_e_n_nega)
        try:
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.match(ZCodeParser.SUB)
                self.state = 461
                self.e_n_nega()
                pass
            elif token in [32, 34, 38, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.e_n_other()
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


    class E_n_otherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPENPAREN(self):
            return self.getToken(ZCodeParser.OPENPAREN, 0)

        def expr_num(self):
            return self.getTypedRuleContext(ZCodeParser.Expr_numContext,0)


        def CLOSEPAREN(self):
            return self.getToken(ZCodeParser.CLOSEPAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def array(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayContext,0)


        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


        def stmt_func_call(self):
            return self.getTypedRuleContext(ZCodeParser.Stmt_func_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_e_n_other




    def e_n_other(self):

        localctx = ZCodeParser.E_n_otherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_e_n_other)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.match(ZCodeParser.OPENPAREN)
                self.state = 466
                self.expr_num()
                self.state = 467
                self.match(ZCodeParser.CLOSEPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 469
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 470
                self.match(ZCodeParser.NUMBER)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 471
                self.array()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 472
                self.array_val()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 473
                self.stmt_func_call()
                pass


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
        self._predicates[48] = self.expr_cond_andor_sempred
        self._predicates[58] = self.e_n_addsub_sempred
        self._predicates[59] = self.e_n_muldivmod_sempred
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
         




