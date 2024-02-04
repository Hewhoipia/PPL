import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
            
    def test_101(self):
        "test_101"
        self.assertTrue(TestLexer.test("kissme\t","kissme,<EOF>",101))

    def test_102(self):
        """test_102"""
        self.assertTrue(TestLexer.test(""" "No you \'"don't have to\'"" ""","""No you \'"don't have to\'",<EOF>""",102))

    def test_103(self):
        """test_103"""
        self.assertTrue(TestLexer.test(""" "think too much" ""","think too much,<EOF>",103))

    def test_104(self):
        """test_104"""
        self.assertTrue(TestLexer.test(""" "love me '''" ""","love me ''',<EOF>",104))
    
    def test_105(self):
        """test_105"""
        self.assertTrue(TestLexer.test(""" "just\\htell me sth"  ""","""Illegal Escape In String: just\\h""",105))

    def test_106(self):
        """test string"""
        input = """((em % anh = 0) or (we % they = 0))"""
        expected = "(,(,a,%,e,=,0,),or,(,we,%,they,=,0,),),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 106))

    def test_107(self):
        self.assertTrue(TestLexer.test(""" "toyouu'"c\\n hoho"  ""","""toyouu'"c\\n hoho,<EOF>""",107))       
    def test_108(self):
        self.assertTrue(TestLexer.test("lam#","l,a,m,Error Token #",108))
    def test_109(self):
        self.assertTrue(TestLexer.test(""" "'githilam"  ""","""'githilam,<EOF>""",109))
    def test_110(self):
        input = '"lam\f\t\na\nu\nme"'
        expected = "Unclosed String: lam\f\t\n"
        self.assertTrue(TestLexer.test(input, expected, 110))
    def test_111(self):
        self.assertTrue(TestLexer.test(""" "hang'\' toi" """, "hang'\' toi,<EOF>", 111))
    def test_112(self):
        self.assertTrue(TestLexer.test('"aluon\mo\ve\e\\"','Illegal Escape In String: aluon\\',112))
    def test_113(self):
        input = """ "nguoi \\\\ voi \t khien \n anh" """
        expected = 'Unclosed String: nguoi \\\\ voi \t khien \n"'
        self.assertTrue(TestLexer.test (input, expected, 113))
    def test_114(self):
        input = """ "\\\\phaquaycuong\\\\" """
        expected = '\\\\phaquaycuong\\\\,<EOF>'
        self.assertTrue(TestLexer.test(input,expected, 114))
    def test_115(self):
        input = '"tu\tu\thoi\\\\beoi"'
        expected = "tu\tu\thoi\\\\beoi,<EOF>"
        self.assertTrue(TestLexer.test(input,expected, 115)) 
    def test_116(self):
        input = """ -343e-532 "thoi" "beoi" """
        expected = """-,343e-532,thoi,beoi,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected, 116))
    def test_117(self):
        input = '''"tu 'tu'"'''
        expected = "tu 'tu',<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 117))
    def test_118(self):
        input = '"beoi\ntu"tuvi"""'
        expected = "Unclosed String: beoi\n"
        self.assertTrue(TestLexer.test(input, expected, 118))
    def test_119(self):
        input = """ "a biet em ##cangi " """
        expected = "Unclosed String: a biet em "
        self.assertTrue(TestLexer.test(input, expected, 119))
    def test_120(self):
        input = """ tatden[54] """
        expected = "tatden,[,54,],<EOF>"
        self.assertTrue(TestLexer.test (input,expected, 120))
    def test_121(self):
        input = """ "du de thay" "doi moi tham thi" """
        expected = "du de thay,doi moi tham thi,<EOF>"
        self.assertTrue(TestLexer.test (input, expected, 121 ))
    def test_122(self):
        """test string"""
        input = """de anh den duong"""
        expected = "de,anh,den,duong,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 122))
    def test_123(self):
        input = 'func hat () ;'
        expected = "func,hat,(,),Error Token ;"
        self.assertTrue(TestLexer.test(input, expected, 123))
    def test_124(self):
        input = """ "hat"vao """
        expected = "hat,v,a,o,<EOF>"
        self.assertTrue(TestLexer.test (input,expected, 124 ))
    def test_125(self):
        input = """ "\f mai toc em \n" """
        expected = "Unclosed String: \f mai toc em \n"
        self.assertTrue(TestLexer.test (input,expected, 125 ))
    def test_126(self):
        input = '"ba\'by"'
        expected = '''ba\'by,<EOF>'''
        self.assertTrue(TestLexer.test(input, expected, 126))
    def test_127(self):
        input = """ lai##"gan '"em hon'"" """
        expected = "lai,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 127))
    def test_128(self):
        input = """ de nghe """
        expected = "de,nghe,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 128))
    def test_129(self):
        input = """ 1. or "that**--$#><>"{// " \ """
        expected = "1.,or,that**--$#><>,Error Token {"
        self.assertTrue(TestLexer.test(input, expected, 129))
    def test_130(self):
        input = """ tieng double tim | """
        expected = "tieng,double,tim,Error Token |"
        self.assertTrue(TestLexer.test(input, expected, 130))
    def test_131(self):
        input = """ dap """
        expected = "dap,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 131))
    def test_132(self):
        input = """ moi "'" thu """
        expected = """moi,Unclosed String: '" thu """
        self.assertTrue(TestLexer.test(input, expected, 132))
    def test_133(self):
        input = """## nhu da dc sap dat"""
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 133))
    def test_134(self):
        input = """number gioem <- 54.45e-2## baby  """
        expected = "number,gioem,<-,54.45e-2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 134))
    def test_135(self):
        input = """ "muonlamgi """
        expected = "Unclosed String: muonlamgi "
        self.assertTrue(TestLexer.test(input, expected, 135))
    def test_136(self):
        input = """ nguoi #cu dua "anh" """
        expected = "nguoi,Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 136))
    def test_137(self):
        """hmmm"""
        input = """ "moi \tvet\rthuong\n" """
        expect = """Unclosed String: moi \tvet\rthuong\n"""
        self.assertTrue(TestLexer.test(input,expect,137))
    def test_138(self):
        input = """ "a se \\tlam\\rem\\nquen" """
        expect = """Unclosed String: a se \\tlam\\r"""
        self.assertTrue(TestLexer.test(input,expect,138))
    def test_139(self):
        input = """ "\i hetdi" """
        expected = "Illegal Escape In String: \i"
        self.assertTrue(TestLexer.test(input, expected, 139))
    def test_140(self):
        input = """ "haydenbenanh\t \va " """
        expected = "Illegal Escape In String: haydenbenanh\t \v"
        self.assertTrue(TestLexer.test(input, expected, 140))
    def test_141(self):
        input = """ giuthatchat@"""
        expected = "giuthatchat,Error Token @"
        self.assertTrue(TestLexer.test(input, expected, 141))
    def test_142(self):
        input = """ nhudayla;lancui"""
        expected = "nhudayla,Error Token ;"
        self.assertTrue(TestLexer.test(input, expected, 142))
    def test_143(self):
        input = """ em:= "tin" vao}"""
        expected = "em,Error Token :"
        self.assertTrue(TestLexer.test(input, expected, 143))
    def test_144(self):
        input = """ mot dieu '.^"""
        expected = "mot,dieu,',.,Error Token ^"
        self.assertTrue(TestLexer.test(input, expected, 144))
    def test_145(self):
        input = """ chi co ("o noi anh") *"""
        expected = "chi,co,(,o noi anh,),*,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 145))
    def test_146(self):
        input = """b,b,b,be oi tu tu """
        expected = "b,,,b,,,b,,,be,oi,tu,tu,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 146))
    def test_147(self):
        input = """be oi tu tu"""
        expected = "be,oi,tu,tu,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 147))
    def test_148(self):
        input = """beoitutu?"""
        expected = "beoitutu,Error Token ?"
        self.assertTrue(TestLexer.test(input, expected, 148))
    def test_149(self):
        input = """nanana"""
        expected = "nanana,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 149))
    def test_150(self):
        input = """nanana \n nana"""
        expected = "nanana,\n,nana,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 150))
    def test_151(self):
        input = """54."""
        expected = "54.,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 151))
    def test_152(self):
        input = """4e65"""
        expected = "4e65,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 152))
    def test_153(self):
        input = """1dungbolai2"""
        expected = "1dungbolai2,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 153))
    def test_154(self):
        input = """3e-87"""
        expected = "3e-87,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 154))
    def test_155(self):
        input = """mot nguoi yeu-e"""
        expected = "mot,nguoi,yeu-em,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 155))
    def test_156(self):
        input = """mai mai"""
        expected = "mai,mai,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 156))
    def test_157(self):
        """test string"""
        input = """1+2+3"""
        expected = "1,+,2,+,3,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 157))
    def test_158(self):
        input = """-23+76"""
        expected = "-,23,+,76,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 158))
    def test_159(self):
        input = """khi e noi true"""
        expected = "khi,em,noi,true,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 159))
    def test_160(self):
        input = """ma em dau biet false"""
        expected = "ma,em,dau,biet,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 160))
    def test_161(self):
        input = """or "nguoi cho em o day" and"""
        expected = "or,nguoi cho em o day,and,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 161))
    def test_162(self):
        input = """"e dau biet" not"""
        expected = "em dau biet,not,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 162))
    def test_163(self):
        input = """ "anh van luon tin vao"! """
        expected = "anh van luon tin vao,Error Token !"
        self.assertTrue(TestLexer.test(input, expected, 163))
    def test_164(self):
        input = """return "chicannguoi" """
        expected = "return,chicannguoi,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 200))
    def test_165(self):
        input = """1e"noicho" #"""
        expected = "1e,noicho,Error Token #"
        self.assertTrue(TestLexer.test(input, expected, 165))
    def test_166(self):
        input = """##a ##mot cau ## thanh loi ##"""
        expected = "<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 166))
    def test_167(self):
        input = """##anh hua voi em\n tron doi $"""
        expected = "\n,tron,doi,Error Token $"
        self.assertTrue(TestLexer.test(input, expected, 167))
    def test_168(self):
        input = """rang anh *"""
        expected = "rang,anh,Error Token *"
        self.assertTrue(TestLexer.test(input, expected, 168))
    def test_169(self):
        input = """ ##"luon dap say\n"wao" ~ """
        expected = "\n,wao,Error Token ~"
        self.assertTrue(TestLexer.test(input, expected, 169))
    def test_170(self):
        input = """ "'"'"'"'" chi co nguoi "  """
        expected = """'"'"'"'" chi co nguoi ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expected, 170))
    def test_171(self):
        """test string"""
        self.assertTrue(TestLexer.test(""" "van: '"cho'"'"o?'"day ma'" """,
                                            """Unclosed String: van: '"cho'"'"o?'"day ma'" """,171))
    def test_172(self):
        input = """ "vinguoi\q" """
        expected = """Illegal Escape In String: vinguoi\q"""
        self.assertTrue(TestLexer.test(input, expected, 172))
    def test_173(self):
        input = """ "vanchoem den'" khi em quay lai" """
        expected = """vanchoem den'" khi em quay lai,<EOF>"""
        self.assertTrue(TestLexer.test(input, expected, 173))
    def test_174(self):
        input = """ "vay" toinay|em dung di"""
        expected = """vay,toinay,Error Token |"""
        self.assertTrue(TestLexer.test(input, expected, 174))
    def test_175(self):
        input = """ "di\n D \b D \f D \n"  """
        expected = """Unclosed String: di\n"""
        self.assertTrue(TestLexer.test(input, expected, 175))
    def test_176(self):
        input = """ di di "D D D di\dau?" """
        expected = """di,di,Illegal Escape In String: D D D di\d"""
        self.assertTrue(TestLexer.test(input, expected, 176))
    def test_177(self):
        input = """co con mua nao \ """
        expected = "co,con,mua,nao,Error Token \\"
        self.assertTrue(TestLexer.test(input, expected, 177))
    def test_178(self):
        input = """' doi minh"""
        expected = "Error Token '"
        self.assertTrue(TestLexer.test(input, expected, 178))
    def test_179(self):
        input = """di qua"""
        expected = "di,qua,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 179))
    def test_180(self):
        input = '"\'"\\\\\n"'
        expected = """Unclosed String: '"\\\\\n"""
        self.assertTrue(TestLexer.test(input, expected,110))  
    def test_181(self):
        input = """a den ben e #######"""
        expected = "a,den,ben,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 181))
    def test_182(self):
        input = """"ngay doi minh" ############"""
        expected = "ngay doi minh,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 182))
    def test_183(self):
        input = """ "hmm" "hee'"" """
        expected =  """hmm,hee'",<EOF>"""
        self.assertTrue(TestLexer.test (input,expected, 183 ))
    def test_184(self):
        """test string"""
        input = '"chia xa"'
        expected = "chia xa,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 184))
    def test_185(self):
        input = """moi la"""
        expected = "moi,la,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 185))
    def test_186(self):
        input = '"roi ben ho^tom^tum^tim^tem^tam^ttt^"'
        expected = "roi ben ho^tom^tum^tim^tem^tam^ttt^,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 186))
    def test_187(self):
        input = """ "noi co don \n lon len!" """
        expect = "Unclosed String: noi co don "
        self.assertTrue(TestLexer.test(input,expect,187))
    def test_188(self):
        input = """mua thu ay ## 12"""
        expected = "mua,thu,ay,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 188))
    def test_189(self):
        input = """(em (khong) con)"""
        expected = "(,em,(,khong,),con,),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 189))
    def test_190(self):
        """test string"""
        input = '"\\\\a\nben canh anh nua"'
        expected = "Unclosed String: \\\\a\n"
        self.assertTrue(TestLexer.test(input, expected, 190))
    def test_191(self):
        input = """ "anh dung noi day" """
        expected = "anh dung noi day,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 191))
    def test_192(self):
        input = """cho em ## cung\n con mua ##now it is"""
        expected = "cho,em,\n,con,mua,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 192))
    def test_193(self):
        input = """chung ta"""
        expected = "chung,ta,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 193))
    def test_194(self):
        input = """sau nay^%"""
        expected = "sau,nay,Error Token ^"
        self.assertTrue(TestLexer.test(input, expected, 194))
    def test_195(self):
        input = """chang co"""
        expected = "chang,co,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 195))
    def test_196(self):
        input = """ "chung ta" """
        expected = "chung ta,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 196))
    def test_197(self):
        input = """func main(var checkvardichue)"""
        expected = "func,main,(,var,checkvardichue,),<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 197))
    def test_198(self):
        self.assertTrue(TestLexer.test(""" "show me the way ""","""Unclosed String: show me the way """,198))
    def test_199(self):
        input = """if (anhiuem) return emkhongiua"""
        expected = "if,(,anhiuem,),return,emkhongiua,<EOF>"
        self.assertTrue(TestLexer.test(input, expected, 199))
    def test_200(self):
        input = """ khong thanh doi? "thi thanh khuc!" """
        expected = "khong,thanh,doi,Error Token &"
        self.assertTrue(TestLexer.test(input, expected, 200))
    