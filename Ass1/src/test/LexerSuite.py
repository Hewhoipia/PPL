import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    
    def test101(self):
        "test identifier"
        self.assertTrue(TestLexer.test("0123abc","0123,abc,<EOF>",101))

    def test102(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "He asked me: \'"Where is John?\'"" ""","""He asked me: '"Where is John?'",<EOF>""",102))

    def test103(self):
        """test simple string"""
        self.assertTrue(TestLexer.test(""" "Yanxi Palace - 2018" ""","Yanxi Palace - 2018,<EOF>",103))

    def test104(self):
        """test complex string"""
        self.assertTrue(TestLexer.test(""" "isn\'t' " ""","isn't' ,<EOF>",104))
    
    def test105(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.test(""" "PPL\\CO3039"  ""","""Illegal Escape In String: PPL\\C""",105))

    def test106(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.test(""" "1234 5678  ""","""Unclosed String: 1234 5678  """,106))

    def test107(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.test(""" "ab'"c\\\\n def"  ""","""ab'"c\\\\n def,<EOF>""",107))       
    def test108(self):
        """test fast"""
        self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",108))
    def test109(self):
        """random test"""
        self.assertTrue(TestLexer.test(""" "123'e456"  ""","""123'e456,<EOF>""",109))
    def test110(self):
        """random test"""
        input = '"Faker,\nwhat\nwas\nthat?"'
        expected = "Unclosed String: Faker,\n"
        self.assertTrue(TestLexer.test(input, expected, 110))
    # def testcoma(self):
    #     """random test"""
    #     self.assertTrue(TestLexer.test(""" " ' " """, " ' ,<EOF>", 111))
    # def test112(self):
    #     """random test"""
    #     self.assertTrue(TestLexer.test('"hi \ \\t\\"','Illegal Escape In String: hi \ \\t\\"',112))
    # def test113(self):
    #     """random test"""
    #     input = """ "test form feed \\ \f \n" """
    #     expected = "Unclosed String: test form feed \\ \f \n"
    #     self.assertTrue(TestLexer.test (input, expected, 111 ))
    # def test114(self):
    #     """random test"""
    #     input = """ "test\\" """
    #     expected = 'Illegal Escape In String: test\\"'
    #     self.assertTrue(TestLexer.test(input,expected, 114))
    # def test115(self):
    #     """test error token"""
    #     input = '"test" -\\123e-234 "test"'
    #     expected = "test,-,Error Token \\"
    #     self.assertTrue(TestLexer.test(input,expected, 115)) 
    # def test116(self):
    #     """random test"""
    #     input = """ "try" -999e+10 "something" """
    #     expected = """try,-,999e+10,something,<EOF>"""
    #     self.assertTrue(TestLexer.test(input,expected, 116))
    # def test117(self):
    #     """random test"""
    #     input = '''"char in 'string'"'''
    #     expected = '''Unclosed String: char in 'string'"'''
    #     self.assertTrue(TestLexer.test(input, expected, 117))
    # def test118(self):
    #     """random test"""
    #     input = '"1 \' 23 "abcd"efg"""'
    #     expected = "1 ' 23 ,abcd,efg,,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 118))
    # def test119(self):
    #     """random test"""
    #     input = """ "Comment in string ##iamsory? " """
    #     expected = "Comment in string ##iamsory? ,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 119))
    # def test120(self):
    #     """test index operation"""
    #     input = """ a[9] """
    #     expected = "a,[,9,],<EOF>"
    #     self.assertTrue(TestLexer.test (input,expected, 120))
    # def test121(self):
    #     """random test"""
    #     input = """ "Illegal string\l " "the second string" """
    #     expected = "Illegal Escape In String: Illegal string\l"
    #     self.assertTrue(TestLexer.test (input, expected, 121 ))
    # def test122(self):
    #     """random test"""
    #     input = """ "1st" "2nd" """
    #     expected = "1st,2nd,<EOF>"
    #     self.assertTrue(TestLexer.test (input,expected, 122 ))
    # def test123(self):
    #     """test lexer"""
    #     input = 'func foo () {}'
    #     expected = "func,foo,(,),Error Token {"
    #     self.assertTrue(TestLexer.test(input, expected, 123))
    # def test124(self):
    #     """test lexer"""
    #     input = """ if num == 0, 1 2 3 string "in string" " """
    #     expected = "if,num,==,0,,,1,2,3,string,in string,Unclosed String:  "
    #     self.assertTrue(TestLexer.test (input,expected, 124 ))
    # def test125(self):
    #     """test unclosed string"""
    #     input = """ "unclose \f \n" """
    #     expected = "Unclosed String: unclose \f \n"
    #     self.assertTrue(TestLexer.test (input,expected, 125 ))
    # def test126(self):
    #     """random test"""
    #     input = '"123 \'"string\n test"'
    #     expected = '''Unclosed String: 123 '"string\n'''
    #     self.assertTrue(TestLexer.test(input, expected, 126))
    # def test127(self):
    #     """test comment and string"""
    #     input = """ check##"test \i '"'\n\n var "string" """
    #     expected = "check,\n,\n,var,string,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 127))
    # def test128(self):
    #     """test illegal string"""
    #     input = """ 1.9e-12 xyz "test illegal\e" """
    #     expected = "1.9e-12,xyz,Illegal Escape In String: test illegal\e"
    #     self.assertTrue(TestLexer.test(input, expected, 128))
    # def test129(self):
    #     """test some keywords """
    #     input = """ 0. or "0var**--$#><>"{// " \ """
    #     expected = "0.,or,0var**--$#><>,Error Token {"
    #     self.assertTrue(TestLexer.test(input, expected, 129))
    # def test130(self):
    #     """test identifier"""
    #     input = """ reducto double | """
    #     expected = "reducto,double,Error Token |"
    #     self.assertTrue(TestLexer.test(input, expected, 130))
    # def test131(self):
    #     """test identifier"""
    #     input = """ 01__var """
    #     expected = "01,__var,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 131))
    # def test132(self):
    #     """random test"""
    #     input = """ final "'" for """
    #     expected = """final,Unclosed String: '" for """
    #     self.assertTrue(TestLexer.test(input, expected, 132))
    # def test133(self):
    #     """test comment"""
    #     input = """## so there will nothing except EOF"""
    #     expected = "<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 133))
    # def test134(self):
    #     """test comment with some tokens"""
    #     input = """ rfc number <- 6.9e-3## comment  """
    #     expected = "rfc,number,<-,6.9e-3,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 134))
    # def test135(self):
    #     """test string with comment"""
    #     input = """ "blank## comment """
    #     expected = "Unclosed String: blank## comment "
    #     self.assertTrue(TestLexer.test(input, expected, 135))
    # def test136(self):
    #     """random test"""
    #     input = """ #Comment can't be start with only #"""
    #     expected = "Error Token #"
    #     self.assertTrue(TestLexer.test(input, expected, 136))
    # def test137(self):
    #     """test tokens"""
    #     input = """Token for those 3. [99]"""
    #     expected = "Token,for,those,3.,[,99,],<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 137))
    # def test138(self):
    #     """random test"""
    #     input = """Legends never die \\r"""
    #     expected = "Legends,never,die,Error Token \\"
    #     self.assertTrue(TestLexer.test(input, expected, 138))
    # def test139(self):
    #     """random test"""
    #     input = """ ". \p" """
    #     expected = "Illegal Escape In String: . \p"
    #     self.assertTrue(TestLexer.test(input, expected, 139))
    # def test140(self):
    #     """random test"""
    #     input = """ "random\t \end " """
    #     expected = "Illegal Escape In String: random\t \e"
    #     self.assertTrue(TestLexer.test(input, expected, 140))
    # def test141(self):
    #     """random test"""
    #     input = """ tin@hcmut.com"""
    #     expected = "tin,Error Token @"
    #     self.assertTrue(TestLexer.test(input, expected, 141))
    # def test142(self):
    #     """test error"""
    #     input = """ nct-stuti@hcmut.com"""
    #     expected = "nct,-,stuti,Error Token @"
    #     self.assertTrue(TestLexer.test(input, expected, 142))
    # def test143(self):
    #     """test error"""
    #     input = """ for i:= 0 until n by 1}"""
    #     expected = "for,i,Error Token :"
    #     self.assertTrue(TestLexer.test(input, expected, 143))
    # def test144(self):
    #     """random test"""
    #     input = """ a, b ^.^"""
    #     expected = "a,,,b,Error Token ^"
    #     self.assertTrue(TestLexer.test(input, expected, 144))
    # def test145(self):
    #     """random test"""
    #     input = """ nothing (999) *"""
    #     expected = "nothing,(,999,),*,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 145))
    # def test146(self):
    #     """random test"""
    #     input = """*v* *-* *o* """
    #     expected = "*,v,*,*,-,*,*,o,*,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 146))
    # def test147(self):
    #     """random test"""
    #     input = """+-*/"""
    #     expected = "+,-,*,/,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 147))
    # def test148(self):
    #     """random test"""
    #     input = """?"""
    #     expected = "Error Token ?"
    #     self.assertTrue(TestLexer.test(input, expected, 148))
    # def test149(self):
    #     """random test"""
    #     input = """-_-"""
    #     expected = "-,_,-,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 149))
    # def test150(self):
    #     """random test"""
    #     input = """_"""
    #     expected = "_,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 150))
    # def test151(self):
    #     """random test"""
    #     input = """0."""
    #     expected = "0.,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 151))
    # def test152(self):
    #     """random test"""
    #     input = """09e90"""
    #     expected = "09e90,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 152))
    # def test153(self):
    #     """random test"""
    #     input = """4E5"""
    #     expected = "4E5,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 153))
    # def test154(self):
    #     """random test"""
    #     input = """1e-2"""
    #     expected = "1e-2,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 154))
    # def test155(self):
    #     """random test"""
    #     input = """-1E-2"""
    #     expected = "-,1E-2,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 155))
    # def test156(self):
    #     """random test"""
    #     input = """9.9"""
    #     expected = "9.9,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 156))
    # def test157(self):
    #     """random test"""
    #     input = """10+47"""
    #     expected = "10,+,47,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 157))
    # def test158(self):
    #     """random test"""
    #     input = """-2+60"""
    #     expected = "-,2,+,60,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 158))
    # def test159(self):
    #     """random test"""
    #     input = """true"""
    #     expected = "true,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 159))
    # def test160(self):
    #     """random test"""
    #     input = """false"""
    #     expected = "false,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 160))
    # def test161(self):
    #     """random test"""
    #     input = """or"""
    #     expected = "or,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 161))
    # def test162(self):
    #     """random test"""
    #     input = """true or false"""
    #     expected = "true,or,false,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 162))
    # def test163(self):
    #     """random test"""
    #     input = """!"""
    #     expected = "Error Token !"
    #     self.assertTrue(TestLexer.test(input, expected, 163))
    # def test164(self):
    #     """random test"""
    #     input = """&"""
    #     expected = "Error Token &"
    #     self.assertTrue(TestLexer.test(input, expected, 164))
    # def test165(self):
    #     """random test"""
    #     input = """21e-21"test" #"""
    #     expected = "21e-21,test,Error Token #"
    #     self.assertTrue(TestLexer.test(input, expected, 165))
    # def test166(self):
    #     """random test"""
    #     input = """##2e324"test" #"""
    #     expected = "<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 166))
    # def test167(self):
    #     """random test"""
    #     input = """##1e-35"test" #\n$"""
    #     expected = "\n,Error Token $"
    #     self.assertTrue(TestLexer.test(input, expected, 167))
    # def test168(self):
    #     """random test"""
    #     input = """bdbfdadcvas ^"""
    #     expected = "bdbfdadcvas,Error Token ^"
    #     self.assertTrue(TestLexer.test(input, expected, 168))
    # def test169(self):
    #     """random test"""
    #     input = """ ##"klnlknklnklnnolnioioboonn\n\n"!@#"321e-543"!@#$" ~ """
    #     expected = "\n,\n,!@#,321e-543,!@#$,Error Token ~"
    #     self.assertTrue(TestLexer.test(input, expected, 169))
    # def test170(self):
    #     """test escape string"""
    #     input = """ "lol '" \\\\ \t \b \f "  """
    #     expected = """lol '" \\\\ \t \b \f ,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expected, 170))
    # def test171(self):
    #     """random test"""
    #     input = """ This is an illegal string "Illegal \o T1 Champion \t " """
    #     expected = """This,is,an,illegal,string,Illegal Escape In String: Illegal \o"""
    #     self.assertTrue(TestLexer.test(input, expected, 171))
    # def test172(self):
    #     """random test"""
    #     input = """ "tt\q" All roads lead to me "tooot" """
    #     expected = """Illegal Escape In String: tt\q"""
    #     self.assertTrue(TestLexer.test(input, expected, 172))
    # def test173(self):
    #     """random test"""
    #     input = """ "_ '" really" """
    #     expected = """_ '" really,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expected, 173))
    # def test174(self):
    #     """random test"""
    #     input = """ "detail" -245|*&^&*&&** "svdvssdvsd" """
    #     expected = """detail,-,245,Error Token |"""
    #     self.assertTrue(TestLexer.test(input, expected, 174))
    # def test175(self):
    #     """random test"""
    #     input = """ "Escape\n testing \b \f \n"  """
    #     expected = """Unclosed String: Escape\n"""
    #     self.assertTrue(TestLexer.test(input, expected, 175))
    # def test176(self):
    #     """random test"""
    #     input = """ tick fo "Il\o\l\e\g\l  " """
    #     expected = """tick,fo,Illegal Escape In String: Il\o"""
    #     self.assertTrue(TestLexer.test(input, expected, 176))
    # def test177(self):
    #     """random test"""
    #     input = """worldcups[12] <- [[2,0,1,6],3] undefine \[SKT]"""
    #     expected = "worldcups,[,12,],<-,[,[,2,,,0,,,1,,,6,],,,3,],undefine,Error Token \\"
    #     self.assertTrue(TestLexer.test(input, expected, 177))
    # def test178(self):
    #     """random test"""
    #     input = """'"""
    #     expected = "Error Token '"
    #     self.assertTrue(TestLexer.test(input, expected, 178))
    # def test179(self):
    #     """random test"""
    #     input = """+"""
    #     expected = "+,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 179))
    # def test180(self):
    #     """random test"""
    #     input = '"\'"\\b\n"'
    #     expected = """Unclosed String: '"\\b\n"""
    #     self.assertTrue(TestLexer.test(input, expected,110))  
    # def test181(self):
    #     """random test"""
    #     input = """fbfbfgbfg ###"""
    #     expected = "fbfbfgbfg,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 181))
    # def test182(self):
    #     """random test"""
    #     input = """msi ############"""
    #     expected = "msi,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 182))
    # def test183(self):
    #     """random test"""
    #     input = """ppl"""
    #     expected = "ppl,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 183))
    # def test184(self):
    #     """random test"""
    #     input = '"a[b[2, 3]] + 4 so complicated"'
    #     expected = "a[b[2, 3]] + 4 so complicated,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 184))
    # def test185(self):
    #     """random test"""
    #     self.assertTrue(TestLexer.test(""" a[b[2, 3]] <- [[1,2,3,4],2] + 4""",
    #                     "a,[,b,[,2,,,3,],],<-,[,[,1,,,2,,,3,,,4,],,,2,],+,4,<EOF>", 185))
    # def test186(self):
    #     """random test"""
    #     input = '"what for those testcases^^^^^^^"'
    #     expected = "what for those testcases^^^^^^^,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 186))
    # def test187(self):
    #     """random test"""
    #     input = """break ## 423425252"""
    #     expected = "break,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 187))
    # def test188(self):
    #     """random test"""
    #     input = """continue ## ok12414"""
    #     expected = "continue,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 188))
    # def test189(self):
    #     """random test"""
    #     input = """(impressive)"""
    #     expected = "(,impressive,),<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 189))
    # def test190(self):
    #     """random test"""
    #     input = '"start\nrandom"'
    #     expected = "Unclosed String: start\n"
    #     self.assertTrue(TestLexer.test(input, expected, 190))
    # def test191(self):
    #     """random test"""
    #     input = """0 or 1"""
    #     expected = "0,or,1,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 191))
    # def test192(self):
    #     """random test"""
    #     input = """break ## something\n again ##gregegergre"""
    #     expected = "break,\n,again,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 192))
    # def test193(self):
    #     """random test"""
    #     input = """arr[9e-10]"""
    #     expected = "arr,[,9e-10,],<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 193))
    # def test194(self):
    #     """random test"""
    #     input = """^a%&(@()&)(NFOHA)"""
    #     expected = "Error Token ^"
    #     self.assertTrue(TestLexer.test(input, expected, 194))
    # def test195(self):
    #     """random test"""
    #     input = """var x <- readNumber()"""
    #     expected = "var,x,<-,readNumber,(,),<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 195))
    # def test196(self):
    #     """random test"""
    #     input = """if (areDivisors(num1, num2)) writeString("Yes")"""
    #     expected = "if,(,areDivisors,(,num1,,,num2,),),writeString,(,Yes,),<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 196))
    # def test197(self):
    #     """random test"""
    #     input = """func main(dynamic a)"""
    #     expected = "func,main,(,dynamic,a,),<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 197))
    # def test198(self):
    #     """random test"""
    #     input = """((num1 % num2 = 0) or (num2 % num1 = 0))"""
    #     expected = "(,(,num1,%,num2,=,0,),or,(,num2,%,num1,=,0,),),<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 198))
    # def test199(self):
    #     """random test"""
    #     input = """if (x <= 1) return false"""
    #     expected = "if,(,x,<=,1,),return,false,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 199))
    # def test200(self):
    #     """random test"""
    #     input = """return true"""
    #     expected = "return,true,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expected, 200))
