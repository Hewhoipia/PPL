import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test1(self):
        input = """
func main()
begin
    writeNumber(1)
end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 500))

    def test2(self):
        input = """
        func main ()
        begin    
            writeNumber(10)
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 501))
        
    def test3(self):
        input = """
        func main ()
        begin    
            writeNumber(3.14)
        end
        """
        expect = "3.14"
        self.assertTrue(TestCodeGen.test(input, expect, 502))
        
    def test4(self):
        input = """
        func main ()
        begin    
            writeString("true")
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 503))
        
    def test5(self):
        input = """
        func main ()
        begin    
            writeBool(true)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 504))
        
    def test6(self):
        input = """
        func main ()
        begin
            writeNumber(1)
            writeString(" is equal to ")
            writeNumber(2)
            writeString(" is ")
            writeBool(false)
        end
        """
        expect = "1.0 is equal to 2.0 is false"
        self.assertTrue(TestCodeGen.test(input, expect, 505))
        
    def test7(self):
        input = """
        func main ()
        begin
            number cuon
            a <- 3
            writeNumber(cuon)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 506))
        
    def test8(self):
        input = """
        func main ()
        begin
            number cuon <- 3
            writeNumber(cuon)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 507))
        
    def test9(self):
        input = """
        func main ()
        begin
            number bao <- 3
            writeNumber(bao)
            number chuan <- 45
            writeNumber(chuan)
        end
        """
        expect = "3.045.0"
        self.assertTrue(TestCodeGen.test(input, expect, 508))
        
    def test10(self):
        input = """
        func main ()
        begin
            number bao <- 3
            writeNumber(bao)
            bool chuan <- true
            writeBool(chuan)
        end
        """
        expect = "3.0true"
        self.assertTrue(TestCodeGen.test(input, expect, 509))
        
    def test11(self):
        input = """
        func main ()
        begin
            number bao <- 5
            writeNumber(bao)
            bool chuan <- true
            writeBool(chuan)
            string nek <- "Hello, World!"
            writeString(nek)
        end
        """
        expect = "5.0trueHello, World!"
        self.assertTrue(TestCodeGen.test(input, expect, 510))
        
    def test12(self):
        input = """
        func tinhcamnaykhonoi() begin
            string shoyo <- "This is inside test function: "
            writeString(shoyo)
            number bao
            bao <- 3.14
            writeNumber(bao)
            writeString(" ")
        end
        func main ()
        begin
            tinhcamnaykhonoi()
            string shoyo <- "This is inside main function: "
            writeString(shoyo)
            number bao <- 5
            writeNumber(bao)
            bool chuan <- true
            writeBool(chuan)
            string nek <- "Hello, World!"
            writeString(nek)
        end
        """
        expect = "This is inside test function: 3.14 This is inside main function: 5.0trueHello, World!"
        self.assertTrue(TestCodeGen.test(input, expect, 511))
        
    def test13(self):
        input = """
        func main ()
        begin
            var check <- "check var!"
            writeString(check)
        end
        """
        expect = "check var!"
        self.assertTrue(TestCodeGen.test(input, expect, 512))
        
    def test14(self):
        input = """
        func main ()
        begin
            dynamic duo
            duo <- "dynamic du o!"
            writeString(duo)
        end
        """
        expect = "dynamic du o!"
        self.assertTrue(TestCodeGen.test(input, expect, 513))
        
    def test15(self):
        input = """
        var a <- 5
        func main()
        begin
            writeString("outter world!")
            writeNumber(a)
        end
        """
        expect = "outter world! 5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 514))
        
    def test16(self):
        input = """
        number a <- 5
        func tanglen()
        begin
            a <- 6
        end
        func main()
        begin
            tanglen()
            writeNumber(a)
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 515))
        
    def test17(self):
        input = """
        dynamic a
        func ganGlob()
        begin
            a <- 6
        end
        func main()
        begin
            ganGlob()
            writeNumber(a)
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 516))
    
    def test18(self):
        input = """
        func main()
        begin
            number bao <- 3 + 15 - 8
            bao <- bao * 2
            bao <- bao / 2
            writeNumber(bao)
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 517))
        
    def test19(self):
        input = """
        func main()
        begin
            var bao <- true
            var chuan <- false
            var nek <- bao or chuan
            writeBool(nek)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 518))
        
    def test20(self):
        input = """
        func main()
        begin
            var bao <- true
            var chuan <- false
            var nek <- bao and chuan
            writeBool(nek)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 519))
        
    def test21(self):
        input = """
        func main()
        begin
            var bao <- 22
            var chuan <- 10
            var nek <- bao % chuan
            writeNumber(nek)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 520))
        
    def test22(self):
        input = """
        func main()
        begin
            var bao <- true
            bool chuan <- false
            writeBool(not bao)
            writeBool(not chuan)
        end
        """
        expect = "falsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 521))
        
    def test23(self):
        input = """
        func main()
        begin
            writeString("trongcovekho: ")
            var a <- 10 - 1/2 + 0.3 + (3 * 5 + 2) % 11
            writeNumber(a)
        end
        """
        expect = "trongcovekho: 15.8"
        self.assertTrue(TestCodeGen.test(input, expect, 522))
        
    def test24(self):
        input = """
        func main()
        begin
            writeString("trongcoveratkho: ")
            var a <- true and not false or false and false
            writeBool(a)
        end
        """
        expect = "trongcoveratkho: false"
        self.assertTrue(TestCodeGen.test(input, expect, 523))
        
    def test25(self):
        input = """
        func main()
        begin
            number a <- 5.5
            number b <- 5
            bool c <- a = b
            writeBool(c)
            number d <- 5.5
            bool e <- a = d
            writeBool(e)
            number f <- 5.6
            writeBool(a = f)
        end
        """
        expect = "falsetruefalse"
        self.assertTrue(TestCodeGen.test(input, expect, 524))
    
    def test26(self):
        input = """
        func main()
        begin
            number a <- 5.5
            number b <- 5
            bool c <- a = b
            writeBool(c)
        end
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input, expect, 525))
    
    def test27(self):
        input = """
        func main()
        begin
            number a <- 5.5
            number b <- 6
            if (a < b) writeBool(true)
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 526))
    
    def test28(self):
        input = """
        func main()
        begin
            number a <- 5.9
            number b <- 9.9
            number c <- 6.1
            if (a > b) writeString("a lon hon b")
            elif (b < c) writeString("a nho hon b va c")
            else writeString("c nho hon b")
        end
        """
        expect = "c nho hon b"
        self.assertTrue(TestCodeGen.test(input, expect, 527))
        
    def test28(self):
        input = """
        func main()
        begin
            number a <- 6
            number b <- 6
            number c <- 6
            if ((a = b) and (b = c)) writeString("a bang b bang c")
        end
        """
        expect = "a bang b bang c"
        self.assertTrue(TestCodeGen.test(input, expect, 527))
        
    def test29(self):
        input = """
        func main()
        begin
            number a <- 8.89
            number b <- 8.88
            number c <- 8.8
            if ((a = c) and (b = c)) writeString("a bang b bang c")
            elif (a < b) writeString("a < b")
            else writeString("a > b")
        end
        """
        expect = "a > b"
        self.assertTrue(TestCodeGen.test(input, expect, 528))
        
    def test30(self):
        input = """
        func main()
        begin
            dynamic a
            a <- 1000
            var b <- 888
            if (not (a = b)) writeString("a khac b")
        end
        """
        expect = "a khac b"
        self.assertTrue(TestCodeGen.test(input, expect, 529))
        
    def test31(self):
        input = """
        func main()
        begin
            dynamic a <- 5
            if (a = 0) writeString("a = 0")
            elif (a = 1) writeString("a = 1")
            elif (a = 2) writeString("a = 2")
            elif (a = 3) writeString("a = 3")
            elif (a = 4) writeString("a = 4")
            elif (a = 5) writeString("a = 5")
            elif (a = 6) writeString("a = 6")
            elif (a = 7) writeString("a = 7")
            elif (a = 8) writeString("a = 8")
            elif (a = 9) writeString("a = 9")
            else writeString("a > 9")
        end
        """
        expect = "a = 5"
        self.assertTrue(TestCodeGen.test(input, expect, 530))
        
    def test32(self):
        input = """
        func main()
        begin
            dynamic a <- 1000
            if (a = 0) writeString("a = 0")
            elif (a = 1) writeString("a = 1")
            elif (a = 2) writeString("a = 2")
            elif (a = 3) writeString("a = 3")
            elif (a = 4) writeString("a = 4")
            elif (a = 5) writeString("a = 5")
            elif (a = 6) writeString("a = 6")
            elif (a = 7) writeString("a = 7")
            elif (a = 8) writeString("a = 8")
            elif (a = 9) writeString("a = 9")
            else writeString("a > 9")
        end
        """
        expect = "a > 9"
        self.assertTrue(TestCodeGen.test(input, expect, 531))
        
    def test33(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 9 by 2-1
                writeNumber(i)
        end
        """
        expect = "0.01.02.03.04.05.06.07.08.09.0"
        self.assertTrue(TestCodeGen.test(input, expect, 532))
        
    def test33(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 9 by 1
                if (i = 5) break
            writeNumber(i)
        end
        """
        expect = "0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 532))
        
    def test34(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 9 by 1
                if (i = 5) writeNumber(i)
            writeNumber(i)
        end
        """
        expect = "5.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 533))
    
    def test34(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 9 by 1 begin
                if (i < 5) writeNumber(i)
            end
        end
        """
        expect = "0.01.02.03.04.0"
        self.assertTrue(TestCodeGen.test(input, expect, 533))
        
    def test35(self):
        input = """
        func main()
        begin
            number a <- 1
            number i <- 0
            for i until i > 9 by 1 begin
                if (i < 5) begin
                    number a <- 2
                    writeNumber(a)
                end
            end
            writeNumber(a)
        end
        """
        expect = "2.02.02.02.02.01.0"
        self.assertTrue(TestCodeGen.test(input, expect, 534))
        
    def test36(self):
        input = """
        func main()
        begin
            number a <- 0
            number i <- 0
            for i until i > 9 by 1 begin
                if (i > 5) break
                a <- a + 1
            end
            writeNumber(a)
        end
        """
        expect = "6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 535))
        
    def test37(self):
        input = """
        func main()
        begin
            number a <- 0
            number i <- 0
            for i until i > 9 by 1 begin
                if (i % 2 = 0) continue
                a <- a + 1
            end
            writeNumber(a)
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 536))
        
    def test38(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until not (i < 5) by (3 + 3 - 5) begin
                number j <- 0
                for j until not (j < 5) by -1 + 2 begin
                    writeNumber(j)
                end
            end
        end
        """
        expect = "0.01.02.03.04.00.01.02.03.04.00.01.02.03.04.00.01.02.03.04.00.01.02.03.04.0"
        self.assertTrue(TestCodeGen.test(input, expect, 537))
        
    def test39(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until not (i < 5) by (3 + 3 - 5) begin
                number j <- 0
                for j until not (j < 5) by -1 + 2 begin
                    writeNumber(j)
                end
            end
        end
        """
        expect = "0.01.02.03.04.00.01.02.03.04.00.01.02.03.04.00.01.02.03.04.00.01.02.03.04.0"
        self.assertTrue(TestCodeGen.test(input, expect, 538))
    
    def test40(self):
        input = """
        func main()
        begin
            number a <- 3 + 15 - 8
            a <- a * 2
            a <- a / 2
            writeNumber(a)
            if (a = 10.0) begin
                return
            end
            a <- 10.5
            writeNumber(a)
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 539))
        
    def test41(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until not (i < 5) by (3 + 3 - 5) begin
                writeNumber(i)
                if (i = 3) return
            end
            writeNumber(i)
        end
        """
        expect = "0.01.02.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 540))
        
    def test42(self):
        input = """
        func tinhcamnaykhonoi() return 1
        func main()
        begin
            number a <- tinhcamnaykhonoi()
            writeNumber(a)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 541))
        
    def test43(self):
        input = """
        var a <- 2
        func tinhcamnaykhonoi() begin
            return a * 2
        end
        func emnhinanhmalongboiroi()
        func main()
        begin
            number a <- tinhcamnaykhonoi()
            writeNumber(a)
            number b <- emnhinanhmalongboiroi()
            writeNumber(b)
        end
        func emnhinanhmalongboiroi() begin
            return a
        end
        """
        expect = "4.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 542))
        
    def test43(self):
        input = """
        var a <- 2
        func tinhcamnaykhonoi()
        func emnhinanhmalongboiroi()
        func main()
        begin
            if (not tinhcamnaykhonoi()) begin
                number b <- emnhinanhmalongboiroi()
                writeNumber(b)
            end
        end
        func tinhcamnaykhonoi() return false
        func emnhinanhmalongboiroi() begin
            return a
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 542))
    
    def test43(self):
        input = """
        var a <- 2
        func tinhcamnaykhonoi()
        func emnhinanhmalongboiroi()
        func main()
        begin
            if (not tinhcamnaykhonoi()) begin
                number b <- emnhinanhmalongboiroi()
                writeNumber(b)
            end
        end
        func tinhcamnaykhonoi() return false
        func emnhinanhmalongboiroi() begin
            return a
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 542))
    
    def test43(self):
        input = """
        func main()
        begin
            number a[3] <- [1, 2, 3]
            number b <- a[1]
            writeNumber(b)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 542))
    
    def test44(self):
        input = """
        func main()
        begin
            number a[3] <- [1 + 2, 2 + 3, 3 + 4]
            number b <- a[0]
            writeNumber(b)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 543))
    
    def test45(self):
        input = """
        func main()
        begin
            var a <- [1 + 2, 2 + 3, 3 + 4]
            number b <- a[0]
            writeNumber(b)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 544))
    
    def test46(self):
        input = """
        func main()
        begin
            string a[3] <- ["Hello,", "World", "?"]
            a[2] <- "!"
            number i <- 0
            for i until i > 2 by 1
            begin
                writeString(a[i * 2 / 2 + 1 - 1])
                if (i > 0) continue 
                writeString(" ")
            end
        end
        """
        expect = "Hello, World!"
        self.assertTrue(TestCodeGen.test(input, expect, 545))
        
    def test47(self):
        input = """
        func main()
        begin
            bool b[5] <- [true, false, true, false, true]
            var i <- 3
            b[i] <- true
            b[1] <- b[0]
            var j <- 0
            for j until j > 4 by 1
            begin
                writeBool(b[j])
                if (j = 4) break
                writeString(" ")
            end
        end
        """
        expect = "true true true true true"
        self.assertTrue(TestCodeGen.test(input, expect, 546))
        
    def test48(self):
        input = """
        func main()
        begin
            number a[5] <- [8, 7, 8, 4, 8]
            var i <- 3
            a[i] <- 8
            a[1] <- a[0]
            var j <- 0
            for j until j > 4 by 1
            begin
                writeNumber(a[j])
                if (j = 4) break
                writeString(" ")
            end
        end
        """
        expect = "8.0 8.0 8.0 8.0 8.0"
        self.assertTrue(TestCodeGen.test(input, expect, 547))
        
    def test49(self):
        input = """
        func main()
        begin
            string a <- "Hello, "
            string b <- "World!"
            writeString(a...b)
        end
        """
        expect = "Hello, World!"
        self.assertTrue(TestCodeGen.test(input, expect, 548))
        
    def test50(self):
        input = """
        func main()
        begin
            string a <- "Hello, "
            string b <- "World!"
            writeBool(a == b)
            string c <- "Hello, "
            writeBool(a == c)
        end
        """
        expect = "falsetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 549))
    
    def test51(self):
        input = """
        func T1vodich(string shoyo, number b) begin
            b <- b + 1
            s <- s..."method "
            writeString(shoyo)
            writeNumber(b)
        end
        
        func main()
        begin
            number a <- 5
            string abc <- "This is inside "
            T1vodich(abc, a)
            writeString(abc)
            writeNumber(a)
        end
        """
        expect = "This is inside method 6.0This is inside 5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 550))
        
    def test52(self):
        input = """
        func T1vodich(string shoyo, number b, bool c) begin
            b <- b + 1
            s <- s..."method "
            writeString(shoyo)
            writeNumber(b)
            if (c) writeBool(c)
            else c <- true
            writeBool(c)
        end
        
        func main()
        begin
            number a <- 5
            string abc <- "This is inside "
            bool c <- false
            T1vodich(abc, a, c)
            writeString(abc)
            writeNumber(a)
            writeBool(c)
        end
        """
        expect = "This is inside method 6.0trueThis is inside 5.0false"
        self.assertTrue(TestCodeGen.test(input, expect, 551))
        
    def test53(self):
        input = """
        func T1vodich(number a[5], number i) begin
            a[i] <- 0
            a[i+4] <- 0
        end
        
        func main()
        begin
            number a[5] <- [1, 2, 3, 4, 5]
            T1vodich(a, 0)
            number i <- 0
            for i until i > 4 by 1
            begin
                writeNumber(a[i])
                if (i = 4) break
                writeString(" ")
            end
        end
        """
        expect = "0.0 2.0 3.0 4.0 0.0"
        self.assertTrue(TestCodeGen.test(input, expect, 552))
        
    def test54(self):
        input = """
        func T1vodich(string shoyo)
        
        func main()
        begin
            string shoyo <- "string"
            T1vodich(s)
            writeString(shoyo)
        end
        
        func T1vodich(string shoyo) begin
            s <- "new string"
        end
        """
        expect = "string"
        self.assertTrue(TestCodeGen.test(input, expect, 553))
        
    def test55(self):
        input = """
        func T1vodich(string shoyo[2])
        
        func main()
        begin
            string shoyo[2] <- ["Hello, ", "Werld!"]
            T1vodich(s)
            number i <- 0
            for i until i > 1 by 1
                writeString(s[i])
        end
        
        func T1vodich(string a[2]) begin
            a[1] <- "World!"
        end
        """
        expect = "Hello, World!"
        self.assertTrue(TestCodeGen.test(input, expect, 554))
        
    def test56(self):
        input = """
        dynamic a <- [15, 8, 2000]
        func tinhcamnaykhonoi()
        func main()
        begin
            tinhcamnaykhonoi()
            number i <- 0
            for i until i > 2 by 1
                writeNumber(a[i])
        end
        
        func tinhcamnaykhonoi() begin
            a[2] <- 2003
        end
        """
        expect = "15.08.02003.0"
        self.assertTrue(TestCodeGen.test(input, expect, 555))
        
    def test57(self):
        input = """
        func test(number a, bool b)
        func main()
        begin
        number a <- 0
            test(0, true)
            writeNumber(a)
        end
        
        func test(number a, bool b) 
        begin
            if (b) begin
                a <- a + 1
                writeNumber(a)
                return
            end
            else begin
                writeNumber(a)
                return
            end
        end
        """
        expect = "1.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 556))
        
    def test58(self):
        input = """
        func test(number a, bool b)
        func main()
        begin
            writeNumber(test(0, true))
        end
        
        func test(number a, bool b) 
        begin
            if (b) 
                return a + 1
            else 
                return a
            
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 557))
        
    def test59(self):
        input = """
        func main()
        begin
            if (true) begin
                writeNumber(1)
                return
            end
            else begin
                writeNumber(0)
                return
            end
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 558))
        
    def test60(self):
        input = """
        func test(number a, bool b)
        func main()
        begin
            writeBool(test(0, true))
        end
        
        func test(number a, bool b) 
        begin
            if (b) 
                return b
            else 
                return not b
            
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 559))
        
    def test61(self):
        input = """
        func test(number a, bool b)
        func main()
        begin
            writeString(test(0, true))
        end
        
        func test(number a, bool b) 
        begin
            if (b) 
                return "true"
            else 
                return "false"
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 560))
    
    def test62(self):
        input = """
        dynamic a
        dynamic b
        dynamic c <- "glob"
        func glob()
        func main()
        begin
            a <- 10.5
            b <- false
            dynamic c <- "loc"
            writeNumber(a)
            writeBool(b)
            writeString(c)
            glob()
        end
        func glob() begin
            writeString(c)
        end
        """
        expect = "10.5falselocglob"
        self.assertTrue(TestCodeGen.test(input, expect, 561))
        
    def test63(self):
        input = """
        func main()
        begin
            number a <- 15.8
            number b <- 0
            if (a > 30.0)
            begin
                number b <- 99.99
            end
            elif (a < 20) begin
                writeString("here")
                b <- 88.88
                number b <- 99.99
            end
            writeNumber(b)
        end
        """
        expect = "here88.88"
        self.assertTrue(TestCodeGen.test(input, expect, 562))
    
    def test64(self):
        input = """
        func tinhcamnaykhonoi()
        begin
            number i <- 0
            for i until i > 9 by 1
            begin
                if (i = 5) begin
                    return 3
                end
            end
        end
        func main()
        begin
            var i <- tinhcamnaykhonoi()
            writeNumber(i)
        end
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input, expect, 563))
        
    def test65(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i > 9 by 1
            begin
                if (i = 5) begin
                    writeNumber(i)
                    return
                end
            end
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 564))
        
    def test66(self):
        input = """
        func tinhcamnaykhonoi()
        begin
            number i <- 0
            for i until i > 9 by 1
            begin
                if (i = 5) begin
                    writeNumber(i)
                    return
                end
            end
            writeNumber(10.0)
        end
        func main()
        begin
            tinhcamnaykhonoi()
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 565))
        
    def test67(self):
        input = """
        func tinhcamnaykhonoi()
        begin
            number i <- 0
            for i until i > 9 by 1
            begin
                if (i = 5) begin
                    return true
                end
            end
            writeNumber(10.0)
        end
        func main()
        begin
            writeBool(tinhcamnaykhonoi())
        end
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input, expect, 566))
        
    def test68(self):
        input = """
        func tinhcamnaykhonoi()
        begin
            number i <- 0
            for i until i > 9 by 1
            begin
                if (i = 5) begin
                    return "string"
                end
            end
            writeNumber(10.0)
        end
        func main()
        begin
            writeString(tinhcamnaykhonoi())
        end
        """
        expect = "string"
        self.assertTrue(TestCodeGen.test(input, expect, 567))
        
    def test69(self):
        input = """
        func tinhcamnaykhonoi()
        begin
            return [1, 2, 3, 4]
        end
        func main()
        begin
            number a[4] <- tinhcamnaykhonoi()
            number i <- 0
            for i until i > 3 by 1
            begin
                writeNumber(a[i])
                if (i = 3) break
                writeString(" ")
            end
        end
        """
        expect = "1.0 2.0 3.0 4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 568))
        
    def test70(self):
        input = """
        func main()
        begin
            number a[4] <- [1, 2, 3, 4]
            var b <- a
            number i <- 0
            for i until i > 3 by 1
            begin
                writeNumber(b[i])
                if (i = 3) break
                writeString(" ")
            end
        end
        """
        expect = "1.0 2.0 3.0 4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 569))
    
    def test71(self):
        input = """
        func tinhcamnaykhonoi()
        begin
            number a[4] <- [1,2,3,4]
            return a
        end
        func main()
        begin
            number a[4] <- tinhcamnaykhonoi()
            number i <- 0
            for i until i > 3 by 1
            begin
                writeNumber(a[i])
                if (i = 3) break
                writeString(" ")
            end
        end
        """
        expect = "1.0 2.0 3.0 4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 570))
        
    def test72(self):
        input = """
        func init()
        begin
            number a[4] <- [1,2,3,4]
            return a
        end
        var a <- init()
        func main()
        begin
            a[0] <- 5
            number i <- 0
            for i until i > 3 by 1
            begin
                writeNumber(a[i])
                if (i = 3) break
                writeString(" ")
            end
        end
        """
        expect = "5.0 2.0 3.0 4.0"
        self.assertTrue(TestCodeGen.test(input, expect, 571))
        
    def test73(self):
        input = """
        func init()
        begin
            number a[4] <- [1,2,3,4]
            return a
        end
        var a <- init()
        func main()
        begin
            var b <- a
            b[3] <- 5
            number i <- 0
            for i until i > 3 by 1
            begin
                writeNumber(a[i])
                if (i = 3) break
                writeString(" ")
            end
        end
        """
        expect = "1.0 2.0 3.0 5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 572))
        
    def test74(self):
        input = """
        func init()
        begin
            bool a[4] <- [true, true, false, false]
            return a
        end
        var a <- init()
        func main()
        begin
            var b <- a
            b[3] <- true
            number i <- 0
            for i until i > 3 by 1
            begin
                writeBool(a[i])
                if (i = 3) break
                writeString(" ")
            end
        end
        """
        expect = "true true false true"
        self.assertTrue(TestCodeGen.test(input, expect, 573))
        
    def test75(self):
        input = """
        func init()
        begin
            string a[4] <- ["T1", "vo", "dich", "vip"]
            return a
        end
        var a <- init()
        func main()
        begin
            var b <- a
            b[3] <- "ko noi nhieu"
            number i <- 0
            for i until i > 3 by 1
            begin
                writeString(a[i])
                if (i = 3) break
                writeString(" ")
            end
        end
        """
        expect = "T1 vo dich ko noi nhieu"
        self.assertTrue(TestCodeGen.test(input, expect, 574))
        
    def test76(self):
        input = """
        func main()
        begin
            number a[2, 3] <- [[1, 2, 3], [4, 5, 6]]
            number i <- 0
            for i until i > 1 by 1
            begin
                number j <- 0
                for j until j > 2 by 1
                begin
                    writeNumber(a[i, j])
                    if (j = 2) break
                    writeString(" ")
                end
                if (i = 1) break
                writeString(" ")
            end
        end
        """
        expect = "1.0 2.0 3.0 4.0 5.0 6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 575))
        
    def test77(self):
        input = """
        func main()
        begin
            number a[2, 3, 4] <- [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]
            number i <- 0
            for i until i > 1 by 1
            begin
                number j <- 0
                for j until j > 2 by 1
                begin
                    number k <- 0
                    for k until k > 3 by 1
                    begin
                        writeNumber(a[i, j, k])
                        if (k = 3) break
                        writeString(" ")
                    end
                    if (j = 2) break
                    writeString(" ")
                end
                if (i = 1) break
                writeString(" ")
            end
        end
        """
        expect = "1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0 10.0 11.0 12.0 13.0 14.0 15.0 16.0 17.0 18.0 19.0 20.0 21.0 22.0 23.0 24.0"
        self.assertTrue(TestCodeGen.test(input, expect, 576))
    
    def test78(self):
        input = """
        func main()
        begin
            number a[2, 3] <- [[1, 2, 3], [4, 5, 6]]
            a[1, 1] <- 10
            a[0] <- [-1, -2, -3]
            number i <- 0
            for i until i > 1 by 1
            begin
                number j <- 0
                for j until j > 2 by 1
                begin
                    writeNumber(a[i, j])
                    if (j = 2) break
                    writeString(" ")
                end
                if (i = 1) break
                writeString(" ")
            end
        end
        """
        expect = "-1.0 -2.0 -3.0 4.0 10.0 6.0"
        self.assertTrue(TestCodeGen.test(input, expect, 577))
        
    def test79(self):
        input = """
        func main()
        begin
            if (true)
            begin
                string a[1, 2] <- [["Hello", "World"]]
                writeString(a[0, 1])
                a[0, 0] <- "Hello,"
                number i <- 0
                for i until i > 1 by 1
                begin
                    number j <- 0
                    for j until j > 1 by 1
                    begin
                        writeString(a[i, j])
                        if (j = 1) break
                        writeString(" ")
                    end
                    if (j = 0) break
                    writeString(" ")
                end
            end
        end
        """
        expect = "WorldHello, World"
        self.assertTrue(TestCodeGen.test(input, expect, 578))
        
    def test80(self):
        input = """
        func main()
        begin
            bool b[2, 2] <- [[true, false], [false, true]]
            b[1] <- [true, true]
            writeBool(b[1,0])
            writeBool(b[1,1])
        end
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 579))
        
    def test81(self):
        input = """
        number a[3, 3] <- [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        func main()
        begin
            number i <- 0
            for i until i > 2 by 1
            begin
                number j <- 0
                for j until j > 2 by 1
                begin
                    writeNumber(a[i, j])
                    if (j = 2) break
                    writeString(" ")
                end
                if (i = 2) break
                writeString(" ")
            end
        end
        """
        expect = "1.0 2.0 3.0 4.0 5.0 6.0 7.0 8.0 9.0"
        self.assertTrue(TestCodeGen.test(input, expect, 580))
    
    def test82(self):
        input = """
        number a[3, 3] <- [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        func change()
        begin
            a[2, a[0, 1]] <- 10
            a[0] <- [-1, -2 , -3]
        end
        func main()
        begin
            change()
            number i <- 0
            for i until i > 2 by 1
            begin
                number j <- 0
                for j until j > 2 by 1
                begin
                    writeNumber(a[i, j])
                    if (j = 2) break
                    writeString(" ")
                end
                if (i = 2) break
                writeString(" ")
            end
        end
        """
        expect = "-1.0 -2.0 -3.0 4.0 5.0 6.0 7.0 8.0 10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 581))
    
    def test83(self):
        input = """
        func main()
        begin
            if (true)
            begin
                bool b[3, 2, 3] <- [[[true, false, true], [false, true, false]], [[true, false, true], [false, true, false]], [[true, false, true], [false, true, false]]]
                b[0, 1] <- [true, false, true]
                number i <- 0
                for i until i > 2 by 1
                begin
                    number j <- 0
                    for j until j > 1 by 1
                    begin
                        number k <- 0
                        for k until k > 2 by 1
                        begin
                            writeBool(b[i, j, k])
                            if (k = 2) break
                            writeString(" ")
                        end
                        if (j = 1) break
                        writeString(" ")
                    end
                    if (i = 2) break
                    writeString(" ")
                end
            end
        end
        """
        expect = "true false true true false true true false true false true false true false true false true false"
        self.assertTrue(TestCodeGen.test(input, expect, 582))
    
    def test84(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until not (i < 5) by (3 + 3 - 5) begin
                writeNumber(i)
                if (i = 3) break
            end
            writeNumber(i)
        end
        """
        expect = "0.01.02.03.00.0"
        self.assertTrue(TestCodeGen.test(input, expect, 583))
    
    def test85(self):
        input = """
        func ref1D(bool a[2])
        begin
            a <- [true, true]
            return a
        end
        func main()
        begin
            bool b[2]
            b <- [false, false]
            b <- ref1D(b)
            writeBool(b[0])
            writeBool(b[1])
        end
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input, expect, 584))
        
    def test86(self):
        input = """
        func bubbleSort(number arr[10], number n)
        begin
            number i <- 0
            for i until i >= n - 1 by 1
            begin
                number j <- 0
                for j until j >= n - 1 - i by 1
                begin
                    if (arr[j] > arr[j+1]) begin
                        number temp <- arr[j]
                        arr[j] <- arr[j+1]
                        arr[j+1] <- temp
                    end
                end
            end
        end
        func print1DArray(number arr[10], number n)
        func main()
        begin
            number arr[10] <- [64, 34, 1000, 12, 22, 11, 90, 1, -9, -2]
            bubbleSort(arr, 10)
            print1DArray(arr, 10)
        end
        func print1DArray(number arr[10], number n)
        begin
            number i <- 0
            for i until i > n - 1 by 1
            begin
                writeNumber(arr[i])
                if (i = n - 1) break
                writeString(" ")
            end
        end
        """
        expect = "-9.0 -2.0 1.0 11.0 12.0 22.0 34.0 64.0 90.0 1000.0"
        self.assertTrue(TestCodeGen.test(input, expect, 585))
        
    def test87(self):
        input = """
        func search(number arr[10], number n, number target)
        begin
            number i <- 0
            for i until i >= n - 1 by 1
            begin
                if (arr[i] = target) return i
            end
            return -1
        end
        func print1DArray(number arr[10], number n)
        func main()
        begin
            number arr[10] <- [64, 34, 1000, 12, 22, 11, 90, 1, -9, -2]
            ## print1DArray(arr, 10)
            ## writeString(" ")
            writeNumber(search(arr, 10, 1000))
        end
        func print1DArray(number arr[10], number n)
        begin
            number i <- 0
            for i until i > n - 1 by 1
            begin
                writeNumber(arr[i])
                if (i = n - 1) break
                writeString(" ")
            end
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 586))
    
    def test88(self):
        input = """
        func main()
        begin
            number a <- readNumber()
            writeNumber(a)
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 587))
        
    def test89(self):
        input = """
        func search(number arr[10], number n, number target)
        begin
            number i <- 0
            for i until i >= n - 1 by 1
            begin
                if (arr[i] = target) return i
            end
            return -1
        end
        func print1DArray(number arr[10], number n)
        func main()
        begin
            number arr[10] <- [64, 34, 1000, 12, 22, 11, 90, 1, -9, -2]
            number target <- readNumber()
            writeNumber(search(arr, 10, target))
        end
        func print1DArray(number arr[10], number n)
        begin
            number i <- 0
            for i until i > n - 1 by 1
            begin
                writeNumber(arr[i])
                if (i = n - 1) break
                writeString(" ")
            end
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 588))
        
    def test90(self):
        input = """
        func main()
        begin
            number a <- readNumber()
            number b <- readNumber()
            if (a > b) writeString("a lon hon b")
            elif (a = b) writeString("a is equal to b")
            else writeString("a is less than b")
        end
        """
        expect = "a lon hon b"
        self.assertTrue(TestCodeGen.test(input, expect, 589))
        
    def test91(self):
        input = """
        func main()
        begin
            number a <- 0
            number i <- 0
            for i until i > 9 by 1 begin
                if (i % 2 = 0) continue
                a <- a + 1
            end
            writeNumber(a)
        end
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input, expect, 590))
        
    def test92(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until not (i < 5) by (3 + 3 - 5) begin
                number j <- 0
                for j until not (j < 5) by -1 + 2 begin
                    writeNumber(j)
                end
            end
        end
        """
        expect = "0.01.02.03.04.00.01.02.03.04.00.01.02.03.04.00.01.02.03.04.00.01.02.03.04.0"
        self.assertTrue(TestCodeGen.test(input, expect, 591))
        
    def test93(self):
        input = """
        func main()
        begin
            number i <- 0
            number j <- -1
            for i until not (i < 5) by (3 + 3 - 5) begin
                number j <- 0
                for j until not (j < 5) by -1 + 2 begin
                    if (j = 3) continue
                    writeNumber(j)
                end
                writeNumber(j)
                if (i = 3) break
            end
            writeNumber(j)
        end
        """
        expect = "0.01.02.04.00.00.01.02.04.00.00.01.02.04.00.00.01.02.04.00.0-1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 592))
    
    def test94(self):
        input = """
        func main()
        begin
            number a <- 3 + 15 - 8
            a <- a * 2
            a <- a / 2
            writeNumber(a)
            if (a = 10.0) begin
                return
            end
            a <- 10.5
            writeNumber(a)
        end
        """
        expect = "10.0"
        self.assertTrue(TestCodeGen.test(input, expect, 593))
        
    def test95(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until not (i < 5) by (3 + 3 - 5) begin
                writeNumber(i)
                if (i = 3) return
            end
            writeNumber(i)
        end
        """
        expect = "0.01.02.03.0"
        self.assertTrue(TestCodeGen.test(input, expect, 594))
        
    def test96(self):
        input = """
        func tinhcamnaykhonoi() return 1
        func main()
        begin
            number a <- tinhcamnaykhonoi()
            writeNumber(a)
        end
        """
        expect = "1.0"
        self.assertTrue(TestCodeGen.test(input, expect, 595))
        
    def test97(self):
        input = """
        var a <- 2
        func tinhcamnaykhonoi() begin
            return a * 2
        end
        func emnhinanhmalongboiroi()
        func main()
        begin
            number a <- tinhcamnaykhonoi()
            writeNumber(a)
            number b <- emnhinanhmalongboiroi()
            writeNumber(b)
        end
        func emnhinanhmalongboiroi() begin
            return a
        end
        """
        expect = "4.02.0"
        self.assertTrue(TestCodeGen.test(input, expect, 596))
        
    def test98(self):
        input = """
        var a <- 2
        func tinhcamnaykhonoi()
        func emnhinanhmalongboiroi()
        func main()
        begin
            if (not tinhcamnaykhonoi()) begin
                number b <- emnhinanhmalongboiroi()
                writeNumber(b)
            end
        end
        func tinhcamnaykhonoi() return false
        func emnhinanhmalongboiroi() begin
            return a
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 597))
    
    def test99(self):
        input = """
        var a <- 2
        func tinhcamnaykhonoi()
        func emnhinanhmalongboiroi()
        func main()
        begin
            if (not tinhcamnaykhonoi()) begin
                number b <- emnhinanhmalongboiroi()
                writeNumber(b)
            end
        end
        func tinhcamnaykhonoi() return false
        func emnhinanhmalongboiroi() begin
            return a
        end
        """
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 598))
        
    def test100(self):
        input = """
        func main()
        begin
            number a <- 6
            number b <- 6
            number c <- 6
            if ((a = b) and (b = c)) writeString("a bang b bang c")
        end
        """
        expect = "a bang b bang c"
        self.assertTrue(TestCodeGen.test(input, expect, 599))
