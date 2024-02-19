import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """func main () return a[b[2, 3]] + 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_202(self):
        input = """
        func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main(1,2)
            fun()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202)) 
    def test_203(self):
        input = """
        func main()
            return func()
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 203)) 
    def test_204(self):
        input = """
        func main()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 204)) 
    def test_205(self):
        input = """var aPI <- 3.14"""
        expect = "Error on line 1 col 15: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 205))
    def test_206(self):
        input = """
        func main()
            begin   
            var i <- 0
            foo()[3 + foo(2)] <- a[b[2, 3]] + 4
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        
    def test_207(self):
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))
    def test_208(self):
        input = """
            func main()
            func therorist(number a[5],number x[5,3])
            func therorist(number num1, number num2)
                var xinchao <- 1.3e-3
            func main(number xe <- b + 3)
        """
        expect = "Error on line 6 col 32: <-"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_209(self):
        input = """ func main(string a[3])
                begin
                    begin
                        number a
                        for i until i > 5 by 1
                            begin
                                if (a = 1) a <- 2
                                else a <- 4
                                number a <- a + 1
                            end
                    end
                    return this
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
    def test_210(self):
        input = """
            func isPrime(number x)
            func main()
                begin
                    number x <- readNumber()
                    if (isPrime(x)) printString("Yes")
                    else printString("No")
                end
            func isPrime(number x)
            begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
            if (x % i = 0) return false
            end
            return true
            
            
            for i until i > x / 2 by 1 + 1 var c <- 1
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test_211(self):
        input = """
            func main()
                continue
        """
        expect = "Error on line 3 col 16: continue"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_212(self):
        input = """
            ##This is comment
            func main() var bb <- 2.3
        """
        expect = "Error on line 3 col 24: var"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_213(self):
        input = """
            number a[2] <- [1,2] ## This is comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
    def test_214(self):
        input = """var b <- 21"""
        expect = "Error on line 1 col 11: <EOF>"
        self.assertTrue(TestParser.test(input,expect,214))
    def test_215(self):
        input = """ 
            var a <- a[1] + 1
            var a <- array[1,1+2][1][2,3]
            var a <- array[1,(1)...2,array[ar[(1*2) and 1]],array[2]]
            var a <- a[1] + fun()[1,fun()] 
            var a <- 1[1]
        """
        expect = "Error on line 3 col 38: ["
        self.assertTrue(TestParser.test(input, expect, 215))
    def test_216(self):
        input = """ var ac <- "xin" ... "chao"
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
    def test_217(self):
        input = """func main() """
        expect = "Error on line 1 col 12: <EOF>"
        self.assertTrue(TestParser.test(input,expect,217))
    def test_218(self):
        input = """
            var thismy <- false >= "this" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_219(self):
        input = """
        func main()
            begin
            aPI + 1 <- 3.14
            end
        """
        expect = "Error on line 4 col 16: +"
        self.assertTrue(TestParser.test(input, expect, 219))
    def test_220(self):
        """Simple program: int main() {} """
        input = """
            var abc <- 4 and 4 and 4 or 4 or 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
    def test_221(self):
        input = """ var abc <- 1 / 4 * 1.2 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_222(self):
        input = """
            var abc <- ---1.3e-10 * not 7
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_223(self):
        input = """
        func main()
            begin   
                if (api <- 1)
            end
        """
        expect = "Error on line 4 col 24: <-"
        self.assertTrue(TestParser.test(input, expect, 223)) 
    def test_224(self):
        input = """
            var abc <- array[1][1][2]
        """
        expect = "Error on line 2 col 31: ["
        self.assertTrue(TestParser.test(input,expect,224))
    def test_225(self):
        input = """var abc <- --- not not not 5.3
        """
        expect = "Error on line 1 col 15: not"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_226(self):
        input = """
        func main()
            begin
            for i[1] until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 226))    
    def test_227(self):
        input = """dynamic abc <- foo()[]
        """
        expect = "Error on line 1 col 21: ]"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_228(self):
        input = """
            var abc <- a(ab[1])
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_229(self):
        input = """
            func main() return number a
        """
        expect = "Error on line 2 col 31: number"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_230(self):
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 230))  
    def test_231(self):
        input = """
        func main()
        func threat() begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_232(self):
        input = """
        func main()
            begin
            abc <- 3.14e-122
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_233(self):
        input = """
        func main()
            begin
            abc() <- "xinchao"
            end
        """
        expect = "Error on line 4 col 18: <-"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_234(self):
        input = """
        func main()
            return 1 + 1
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))
    def test_235(self):
        input = """
        func main()
            begin
                foo()
                number a
                abc <- 1.4e-1
                dc <- a
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_236(self):
        input = """
        func main()
            break
        """
        expect = "Error on line 3 col 12: break"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_237(self):
        input = """
        func main()
            begin
            break
            continue
            end

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_238(self):
        input = """
        func main()
            return func()
        """
        expect = "Error on line 3 col 19: func"
        self.assertTrue(TestParser.test(input, expect, 238)) 
    def test_239(self):
        input = """
        func main()
            begin
            for (i) until i >= 10 by 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input,expect,239))
    def test_240(self):
        input = """
        func main()
            for i until i >= 10 by 1
                a <- 1
        """
        expect = "Error on line 3 col 12: for"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_241(self):
        input = """
        func main()
            return break
        """
        expect = "Error on line 3 col 19: break"
        self.assertTrue(TestParser.test(input, expect, 241))
    def test_242(self):
        input = """
        number a 
        func main()
            return 1 + 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_243(self):
        input = """
        func main()
            begin
            if (a = 1)
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_244(self):
        input = """ 
            func main(number a[1,2,3]) ##12
                break
        """
        expect = "Error on line 3 col 16: break"
        self.assertTrue(TestParser.test(input, expect, 244))
    def test_245(self):
        input = """
        func main() func()
        """
        expect = "Error on line 2 col 20: func"
        self.assertTrue(TestParser.test(input,expect,245))
    def test_246(self):
        input = """
        func main()
            return 3
            return main()

        """
        expect = "Error on line 4 col 12: return"
        self.assertTrue(TestParser.test(input,expect,246))
    def test_247(self):
        input = """
        func main()
            begin
                begin
                    begin
                    end
                    begin
                    end
                end
                begin
                return true
                end             
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_248(self):
        input = """var a <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 248)) 
    def test_249(self):
        input = """var abc <- 3.14e-314
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_250(self):
        input = """ 
            number emlaai
            
            ## tu dau buoc den noi day
            number emlaai <- 0
            bool a[122,15]
            bool a[122,15] <- 1 + 1 / 2 * 3
            string b[3]
            ## diu dang chan phuong
            
            string b[3] <- 2 ... " tring"
            var i <- 0
            dynamic i
            dynamic i <- 0
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
    def test_251(self):
        input = """dynamic emlaai
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_252(self):
        input = """ 
            var khep
        """
        expect = "Error on line 2 col 23: \n"
        self.assertTrue(TestParser.test(input, expect, 252))
    def test_253(self):
        input = """
                    begin
                        number a <- 1
                    end
        """
        expect = "Error on line 2 col 20: begin"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_254(self):
        input = """ 
            bool a["string"]
            bool a[[1,2]]
            bool a[1+1]
        """
        expect = "Error on line 2 col 19: string"
        self.assertTrue(TestParser.test(input, expect, 254))
    def test_255(self):
        input = """
         func main()
             begin
             if (f(a-b)[1,2-2,3*4] < 1)
             end
         """
        expect = "Error on line 5 col 13: end"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_256(self):
        input = """ 
            bool a[1,]
        """
        expect = "Error on line 2 col 21: ]"
        self.assertTrue(TestParser.test(input, expect, 256)) 
    def test_257(self):
        input = """ 
            var a[1]
        """
        expect = "Error on line 2 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 257))
    def test_258(self):
        input = """func main () return a[3 + foo(2)] <- a[b[2, 3]] + 4
        """
        expect = "Error on line 1 col 34: <-"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_259(self):
        input = """ 
            func main()
            func main(number f1)
            func main(number a[5],bool x[5,2,3], bool a[5,2,3], string b, bool c)
            func main(number num1, number num2)
                var a <- 1
            func main(number f1 <- c)
        """
        expect = "Error on line 7 col 32: <-"
        self.assertTrue(TestParser.test(input, expect, 259))  
    def test_260(self):
        input = """func main () return foo(2.3e-10)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_261(self):
        input = """ 
            ##12
            ##12
            
            func main(number a) var c <- 1
        """
        expect = "Error on line 5 col 32: var"
        self.assertTrue(TestParser.test(input, expect, 261))
    def test_262(self):
        input = """ 
            func main(var a)
        """
        expect = "Error on line 2 col 22: var"
        self.assertTrue(TestParser.test(input, expect, 262))
    def test_263(self):
        input = """number foo(b,c) <- 8
        """
        expect = "Error on line 1 col 10: ("
        self.assertTrue(TestParser.test(input,expect,263))
    def test_264(self):
        input = """ 
            func main(string a) 
                begin 
                    break ## 12
                end
            func main(dynamic a) 
        """
        expect = "Error on line 6 col 22: dynamic"
        self.assertTrue(TestParser.test(input, expect, 264))
    def test_265(self):
        input = """func foo(number a(), string b)
                    begin
                        var i <- 0
                        for i until i >= 5 by 1
                        begin
                            a[i] <- i * i + 5
                        end
                        return -1
                    end
        """
        expect = "Error on line 1 col 17: ("
        self.assertTrue(TestParser.test(input,expect,265))
    def test_266(self):
        input = """ 
            ## 12
            
            var a <- 1 ## 12
            ## 12
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 266))  
    def test_267(self):
        input = """var a <- 1"""
        expect = "Error on line 1 col 10: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 267))
    def test_268(self):
        input = """func foo(number a, string b)
                    begin
                        begin
                            dynamic a <- a() + 1 / 2 *3 
                            var b <- "anpah" ... "beta"
                        end
                        return -1
                    end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
    def test_269(self):
        input = """ 
            ##12
            func main(number a) 
                ##12
                
                begin 
                    break
                end
                
                ##12
                ##12
            func main(number a)
            ##12        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
    def test_270(self):
        input = """func foo(number a, string b)
                    begin
                        begin
                            dynamic a <- a() + 1 / 2 *3 
                            var b <- "anpah" ... "beta"
                            main([1,2,3], 1+2, a, c ... e)
                            break
                        end
                        return -1
                    end"""
        expect = "Error on line 10 col 23: <EOF>"
        self.assertTrue(TestParser.test(input,expect,270))
    def test_271(self):
        input = """func main(number a) """
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 271))  
    def test_272(self):
        input = """func main () return 
        begin
        end
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_273(self):
        input = """func main () return 1
        if abc == "true" return false
        """
        expect = "Error on line 2 col 8: if"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_274(self):
        input = """ 
            var a <- true > "true" 
            var a <- true >= "true"
            var a <- true = "true"
            var a <- true == "true"
            var a <- true < "true"
            var a <- true <= "true"
            var a <- true >= "true" ... 1 > 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 274))
    def test_275(self):
        input = """func main () return 1
        begin
        var i <- 0
        for i until i >= 10 by 1
        writeNumbe(i)
        end
        """
        expect = "Error on line 2 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_276(self):
        input = """ 
            var a <- true and "true" or 1 
            var a <- 1 and 2 and 3 or 4 or 4
            var a <- 1 + 2 - 2 + 3 and 3
            var a <- 1 / 2 * 3 % 4
            var a <- 1 / 2 / 2 * 3 % 4
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
    def test_277(self):
        """Simple program: int main() {} """
        input = """dynamic a
                   var e <- 3
                   var ceb = e
        """
        expect = "Error on line 3 col 27: ="
        self.assertTrue(TestParser.test(input,expect,277))
    def test_278(self):
        input = """func main (dynamic a) return 1
        """
        expect = "Error on line 1 col 11: dynamic"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_279(self):
        input = """ number a <- 4
                    number e [2] <- [1,2]
            func main(bool c)
                begin
                    number a
                    a <- 1
                    d <- a
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_280(self):
        input = """var a <- true >= "true" and 1 > 2
        """
        expect = "Error on line 1 col 35: >"
        self.assertTrue(TestParser.test(input, expect, 280))
    def test_281(self):
        input = """ func therorist(number a()[foo()[1,2+2]]) 
                begin 
                    continue
                end
            func main(number d, bool c)
                begin
                    if (a()[1,2,3] == "true") return 1
                end
        """
        expect = "Error on line 1 col 24: ("
        self.assertTrue(TestParser.test(input,expect,281))
    def test_282(self):
        input = """ func therorist(number a[1,2]) 
                begin 
                    continue
                end
            func main(number d, bool c)
                begin
                    if (a()[1,2,3] == "true") return 1
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_283(self):
        input = """ 
            var a <- a() + ++1 / 2 *3 <= 3 ... "v" >= 2
            var a <- a(1,2)[1,2,3 ... 2] + false + true
            var a <- a(z,k[2,3,"2"] ... 2)[true]
            var a <- (a ... 3) ... b and (a >= b) < b[1, b[1]]
            var a <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
            var a <- a(x,array[2])[2,3+2,true,false]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
    def test_284(self):
        input = """ func therorist(number a[1]) 
                begin 
                    continue
                    if (e < (2 < 2)) return a[b[c[foo()]]]
                end
            func main(number d, bool c)
                begin
                continue
                break
                if (a()[1,2,3] == "true") return 1
                else print(foo(123))
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_285(self):
        input = """ func therorist(number a[1]) 
                begin 
                    continue
                    if (e < (2 < 2)) return 1
                end
            func main(number d, bool c)
                begin
                    if (a()[1,2,3] == "true") return 1
                end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_286(self):
        input = """
        func main() begin 
        end
        func main() 
            begin 
                ## comment0
            end
        func main()
            ## comment1
            begin
                ## comment2
                
                ## comment3
                a <- 1 + 2 + fun()
                a[1+a] <- 1
                
                ## comment4
                a[3+4,2,4] <- 1
                
                ## comment5
            end
            ## comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
    def test_287(self):
        input = """
        func main()
            begin
            aPI()<- 3.14
            end
        """
        expect = "Error on line 4 col 17: <-"
        self.assertTrue(TestParser.test(input, expect, 287))
    def test_288(self):
        input = """ func therorist(number a[1]) 
                continue
                begin 
                    
                    if (e < (2 < 2)) return a[b[c[foo()]]]
                    a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
                    if (1<2) print()
                    else noprint(2,3,4)
                    for i until i > 10 by 1.3 * 2
                            begin
                                number a <- a + 1
                            end
                 end
                ## this is comment
        """
        expect = "Error on line 2 col 16: continue"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_289(self):
        input = """ func therorist(number a[1]) 
                begin 
                    continue
                    if (e < (2 < 2)) return a[b[c[foo()]]]
                    a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
                    if (1<2) print()
                    else noprint(2,3,4)
                    for i until i > 10 by 1.3 * 2
                            begin
                                number a <- a + 1
                            end
                 end
                ## this is comment
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_290(self):
        input = """
        func main()
            begin   
                if(1+1) api <- 1
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 1
                    ## comment2
                else api <- 1
                ## comment3
                
                if (1) api <- 1
                elif (1 ... 2)
                    ## comment1
                    
                    api <- 1
                    ## comment2
                elif (1) api <- 1
                
                if (1) api <- 1
                elif (1 ... 2) api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290)) 
    def test_291(self):
        input = """ func kaka(number a[1,5]) return 2
                ## this is comment
                ## this is comment
                func doo(number a2)
                begin        
                    a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
                    (a)[2]<- 3.14
                end
                ## this is comment
        """
        expect = "Error on line 7 col 20: ("
        self.assertTrue(TestParser.test(input,expect,291))
    def test_292(self):
        input = """
        func main()
            begin   
                if (api <- 1)
            end
        """
        expect = "Error on line 4 col 24: <-"
        self.assertTrue(TestParser.test(input, expect, 292)) 
    def test_293(self):
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
                ## comment
                
                a <- 1
            ## comment
            end
            
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293)) 
    def test_294(self):
        """Simple program: int main() {} """
        input = """func main () return (1>2)<1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_295(self):
        """Simple program: int main() {} """
        input = """func main () return 1 + 2 + 2
        func dun(bool f)
        begin
        begin
        dynamic a
        var a()[1] <- foo()
        end
        end
        """
        expect = "Error on line 6 col 13: ("
        self.assertTrue(TestParser.test(input,expect,295))
    def test_296(self):
        input = """
        func main()
            begin
            for i+1 until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 296))
    def test_297(self):
        input = """
        func main()
            begin
            for i until i >= 10 by 1 + 1
            end
        """
        expect = "Error on line 5 col 12: end"
        self.assertTrue(TestParser.test(input, expect, 297))
    def test_298(self):
        input = """func main () ##begin
        number a <- 1
        end
        
        """
        expect = "Error on line 3 col 8: end"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_299(self):
        input = """func main () return 1
        var abc <- array[foo()[a[1,foo(23)]]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_300(self):
        input = """
        func main()
            return 1 + 1
        """    
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))