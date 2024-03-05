import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    
#     def test201(self):
#         input = """
#         var x <- 2 + -7 / 6 % -7 * 2
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 201))
#     def test202(self):
#         input = """
#         bool a <- not x + y and ("random" <= 9999) = true
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 202))
#     def test203(self):
#         input = """
#         string a <- "random" ... "string" / 2
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,203))
#     def test204(self):
#         """Simple program"""
#         input = """ number a <- 4
#                     number b[2,3] <- [[1,2,3],[4,5,6]]
#                     string b <- "xyz"
#                     string a [2] <- ["a","b"]
#                     dynamic a <- 3
#                     dynamic a
#                     var e <- 3
#                     number e [2] <- [1,2]
#         func main2(string a[3],number b[3],bool c) 
#                 begin 
#                     break
#                     a[0] <- foo(1)
#                     number d[0,3] <- foo(1)
#                     number d [0,1] <- [1,2]
#                     begin
#                         number a
#                         for i until i > 5 by 1
#                             begin
#                                 if (a = 1) a <- 2
#                                 elif (a = 3) a <- 4
#                                 else 
#                                     begin
#                                         bool j
#                                         j <- true
#                                     end
#                                 number a <- a + 1
#                                 a[b,c] <- 8
#                             end
#                     end
#                     return
#                 end
#             func main(number d, bool c)
#                 begin
#                     main2 (a,b,c)
#                     number a
#                     a <- 1
#                     d <- a
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,204))
#     def test205(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#             var i <- 0
#             for i until i >= 10 by 1
#             begin
#                 number r
#                 number s
#                 r <- 2.0
#                 number a[5]
#                 number b[5]
#                 s <- r * r * 3.14
#                 a[0] <- s
#             end
#             a[9 + fun(1)] <- x[y[2, 3]] + 4
#             number z[5] <- [1, 2, 3, 4, 5]
#             number t[2, 3] <- [[1, 2, 3], [4, 5, 6]]
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,205))
#     def test206(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,206))
#     def test207(self):
#         """Parser Test"""
#         input = """
#             func main()
#             ## a comment
#             func fen() func bug(dynamic a) ## error for sure
#         """
#         expect = "Error on line 4 col 23: func"
#         self.assertTrue(TestParser.test(input,expect,207))
#     def test208(self):
#         """Parser Test"""
#         input = """
#             func main()
#             func foo(number y[6],number x[6,9])
#             func fun(number num1, number num2)
#                 var num <- 1.1e-9
#             func main(number exp <- r + t)
#         """
#         expect = "Error on line 6 col 33: <-"
#         self.assertTrue(TestParser.test(input,expect,208))
#     def test209(self):
#         """Parser Test"""
#         input = """ func main(string a[3])
#                 begin
#                     begin
#                         number a
#                         for i until i > 5 by 1
#                             begin
#                                 if (a = 1) a <- 2
#                                 else a <- 4
#                                 number a <- a + 1
#                             end
#                     end
#                     return this
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,209))
#     def test210(self):
#         """Parser Test"""
#         input = """
#             ## a comment
#             func main() var bb <- 2.3
#         """
#         expect = "Error on line 3 col 24: var"
#         self.assertTrue(TestParser.test(input,expect,210))
#     def test211(self):
#         """Parser Test"""
#         input = """
#             func main()
#                 continue
#         """
#         expect = "Error on line 3 col 16: continue"
#         self.assertTrue(TestParser.test(input,expect,211))
#     def test212(self):
#         """Parser Test"""
#         input = """
#             ## a comment
#             func main(number a)
#                 ## a comment
#                 ## a comment

#                 begin
#                     number a
#                          for i until i > 5 by 1
#                              begin
#                                  if (a = 1) a <- 2
#                                  else a <- 4
#                                  number a <- a + 1
#                              end
#                 end

#                 ## a comment
#             func main(number a)
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,212))
#     def test213(self):
#         """Parser Test"""
#         input = """
#             number x[3] <- [0,1,2] ## This is comment
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,213))
#     def test214(self):
#         """Parser Test"""
#         input = """var x <- 9898"""
#         expect = "Error on line 1 col 13: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,214))
#     def test215(self):
#         """Parser Test"""
#         input = """func main() """
#         expect = "Error on line 1 col 12: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,215))
#     def test216(self):
#         """Parser Test"""
#         input = """ """
#         expect = "Error on line 1 col 1: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,216))
#     def test217(self):
#         """Parser Test"""
#         input = """ var x <- "a" ... "new" ... "string"
#         """
#         expect = "Error on line 1 col 24: ..."
#         self.assertTrue(TestParser.test(input,expect,217))
#     def test218(self):
#         """Parser Test"""
#         input = """
#             var variable <- false>= "string"...3 <1
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,218))
#     def test219(self):
#         """Parser Test"""
#         input = """ var xyz <- 1 / 4 * 1.2 % 4
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,219))
#     def test220(self):
#         """Parser Test"""
#         input = """
#             var troll <- 1 or 2 and 3 or 4 and 6 and 7 ## confusing
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,220))
#     def test221(self):
#         """Parser Test"""
#         input = """var troll <- 1 > 2 >= true
#         """
#         expect = "Error on line 1 col 19: >="
#         self.assertTrue(TestParser.test(input,expect,221))
#     def test222(self):
#         """Parser Test"""
#         input = """
#             var xyz <- ------12.09e-2 / not 7 * 2
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,222))
#     def test223(self):
#         """Parser Test"""
#         input = """var xyz <- --- not not not 423 or 0 and 1
#         """
#         expect = "Error on line 1 col 15: not"
#         self.assertTrue(TestParser.test(input,expect,223))
#     def test224(self):
#         """Parser Test"""
#         input = """
#             var xyz <- array[9][9][9] ## not allow this kind of array
#         """
#         expect = "Error on line 2 col 31: ["
#         self.assertTrue(TestParser.test(input,expect,224))
#     def test225(self):
#         """Parser Test"""
#         input = """dynamic [] <- arr[] ## not too
#         """
#         expect = "Error on line 1 col 8: ["
#         self.assertTrue(TestParser.test(input,expect,225))
#     def test226(self):
#         """Parser Test"""
#         input = """
#             var xyz <- foo(arr[0])
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,226))
#     def test227(self):
#         """Parser Test"""
#         input = """dynamic xyz <- foo()[] ## should have at least an expression
#         """
#         expect = "Error on line 1 col 21: ]"
#         self.assertTrue(TestParser.test(input,expect,227))
#     def test228(self):
#         """Parser Test"""
#         input = """
#             var xyz <- a(b,arr[0,1],"string", false)[a,n,2,1,true,"xyz",arr[1]]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,228))
#     def test229(self):
#         """Parser Test"""
#         input = """
#             func main() return number xyz ## bug for sure
#         """
#         expect = "Error on line 2 col 31: number"
#         self.assertTrue(TestParser.test(input,expect,229))
#     def test230(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#             x <- 1
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,230))
#     def test231(self):
#         """Parser Test"""
#         input = """
#         func main()
#         func foo() begin
#         end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,231))
#     def test232(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#             "string" <- 1 ## can't assign to an exp but should be an variable or array index
#             end
#         """
#         expect = "Error on line 4 col 12: string"
#         self.assertTrue(TestParser.test(input,expect,232))
#     def test233(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#             xyz() <- "nothing"
#             end
#         """
#         expect = "Error on line 4 col 18: <-"
#         self.assertTrue(TestParser.test(input,expect,233))
#     def test234(self):
#         """Parser Test"""
#         input = """
#         func main()
#             break ## should be block or return statement or simply newlines
#         """
#         expect = "Error on line 3 col 12: break"
#         self.assertTrue(TestParser.test(input,expect,234))
#     def test235(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#                 foo()
#                 number a
#                 xyz <- "9e+19"
#                 kt <- a
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,235))
#     def test236(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#                 if (((xyz = 0))) ## should have an statement for if 
#             end
#         """
#         expect = "Error on line 5 col 12: end"
#         self.assertTrue(TestParser.test(input,expect,236))
#     def test237(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin      
#                 continue
#                 return
#                 break
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,237))
#     def test238(self):
#         """Parser Test"""
#         input = """
#         func main()
#             for i until i >= 10 by 1 ## no for right after func declaration should have a block contains the for
#                 a <- a + 2 ## for what
#         """
#         expect = "Error on line 3 col 12: for"
#         self.assertTrue(TestParser.test(input,expect,238))
#     def test239(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#             for (i) until i >= 10 by 1 ## should be an var not an exp or subexpression - an exp with ()
#                 a <- 1
#             end
#         """
#         expect = "Error on line 4 col 16: ("
#         self.assertTrue(TestParser.test(input,expect,239))
#     def test240(self):
#         """Parser Test"""
#         input = """
#         func main()
#         func main()
        
        
#         begin
#             break
#             continue
#             for i until i >= n by 1 + 2
#                 begin
#                     break
#                     continue
#                 end
#         end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,240))
#     def test241(self):
#         """Parser Test"""
#         input = """ 
#         func main(number xyz[1,2]) begin
#                 break  
#             end
#         func _()
#             return _()[_()]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,241))
#     def test242(self):
#         """Parser Test"""
#         input = """func main()
# begin
#     if (main([5,7])) begin
#         var x <- 435
#     end
#     else begin
#         string arr[0,2,5] <- main[foo()]
#         return
#     end
#     for i until i...j <= arr[foo] by 1
#         print(i)
# end 
# """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,242))
#     def test243(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin
#             main()
#             if (foo(a-b*d+2)[0,2/2,3*4] ... false)
#             x <- 99
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,243))
#     def test244(self):
#         """Parser Test"""
#         input = """
#         func main()
#             return error
#             return main() ## this return not belong to any if, for or func

#         """
#         expect = "Error on line 4 col 12: return"
#         self.assertTrue(TestParser.test(input,expect,244))
#     def test245(self):
#         """Parser Test"""
#         input = """
#         func main() func() ## no identifiers allowed to be same as the keywords
#         """
#         expect = "Error on line 2 col 20: func"
#         self.assertTrue(TestParser.test(input,expect,245))
#     def test246(self):
#         """Parser Test"""
#         input = """
#         var a <- continue ## no expression allowed to be same as the keywords
#         """
#         expect = "Error on line 2 col 17: continue"
#         self.assertTrue(TestParser.test(input,expect,246))
#     def test247(self):
#         """Parser Test"""
#         input = """ ## a confusing from first look testcase :v
#         func main()
#             begin
#                 begin
#                     begin
#                     end
#                     begin
#                     end
#                 end
#                 begin
#                 return false
#                 end             
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,247))
#     def test248(self):
#         """Parser Test"""
#         input = """func main(number args[99])
# begin
#     string a <- args[0]
#     string b <- args[1]
#     c = a..b ## the token is for sure error for the concat operator

# end
# """
#         expect = "."
#         self.assertTrue(TestParser.test(input,expect,248))
#     def test249(self):
#         """Parser Test"""
#         input = """
#         ## from spec
#         func areDivisors(number num1, number num2)
#             return (a % num2 = 0 ... num2 % num1 = 0)
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,249))
#     def test250(self):
#         """Parser Test"""
#         input = """
#             func isPrime(number x)
#             number y <- 123
#             string a[2] <- ["1",str(y)]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,250))
#     def test251(self):
#         """Parser Test"""
#         input = """var x
#         ## not let uninitialized in var word declarations
#         """
#         expect = """Error on line 1 col 5: 
# """
#         self.assertTrue(TestParser.test(input,expect,251))
#     def test252(self):
#         """Parser Test"""
#         input = """func main () number x[2] <- [1, 2]
#         """
#         expect = "Error on line 1 col 13: number"
#         self.assertTrue(TestParser.test(input,expect,252))
#     def test253(self):
#         """Parser Test"""
#         input = """ ## no statements allowed in global scope
#                     begin
#                         number a <- 1
#                     end
#         """
#         expect = "Error on line 2 col 20: begin"
#         self.assertTrue(TestParser.test(input,expect,253))
#     def test254(self):
#         """Parser Test"""
#         input = """func main () return 1 < 0 < false ## relational operations in Zcode is none associative
#         """
#         expect = "Error on line 1 col 26: <"
#         self.assertTrue(TestParser.test(input,expect,254))
#     def test255(self):
#         """Parser Test"""
#         input = """
#         func isPrime(number x)
#         func main()
#             begin
#                 number x <- readNumber()
#                 if (isPrime(x)) printString("Yes")
#                 else printString("No")
#             end
            
            
            
#         func isPrime(number x)
#             begin
#                 if (x <= 1) return false
#                 else return isPrime(x)
#                 var i <- 2
#                 for i until i > x / 2 by 1
#                     begin
#                         if (x % i = 0) return false
#                     end
#                 return true
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,255))
#     def test256(self):
#         """Parser Test"""
#         input = """func main (float a) return 

#         """
#         expect = "Error on line 1 col 11: float"
#         self.assertTrue(TestParser.test(input,expect,256))
#     def test257(self):
#         """Parser Test"""
#         input = """func main () return a[3 + foo(2)] <- a[b[2, 3]] + 4
#         """
#         expect = "Error on line 1 col 34: <-"
#         self.assertTrue(TestParser.test(input,expect,257))
#     def test258(self):
#         """Parser Test"""
#         input = """func main () var xyz <-123 >="string"...99>false
#         """
#         expect = "Error on line 1 col 13: var"
#         self.assertTrue(TestParser.test(input,expect,258))
#     def test259(self):
#         """Parser Test"""
#         input = """func main () return run(true)
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,259))
#     def test260(self):
#         """Parser Test"""
#         input = """dynamic a <- 3 + 1
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,260))
#     def test261(self):
#         """Parser Test"""
#         input = """number fun(x,y) <- 999
#         """
#         expect = "Error on line 1 col 10: ("
#         self.assertTrue(TestParser.test(input,expect,261))
#     def test262(self):
#         """Parser Test"""
#         input = """func main () 
#                     begin
#                     if (x[foo()[0,false]] == "ok") return true
#                     end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,262))
#     def test263(self):
#         """Parser Test"""
#         input = """func main () return 1
#         dynamic xyz <- arr[0,1,arr[arr[(false) and 1]],arr[9]]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,263))
#     def test264(self):
#         """Parser Test"""
#         input = """func main(number args[10])
# begin
#     var x <- [0,1,2]
#     dynamic y <- x
#     if (fun(k) - l = (5 <= 1))
#     print(x)
#     else if (bar(x) - y == true) print(y) else return false

# end
# """
#         expect = "Error on line 7 col 42: else"
#         self.assertTrue(TestParser.test(input,expect,264))
#     def test265(self):
#         """Parser Test"""
#         input = """func foo(number a(), string b)
#                     begin
#                         var i <- 0
#                         for i until i >= 5 by 1
#                         begin
#                             a[i] <- i * i + 5
#                         end
#                         return -1
#                     end
#         """
#         expect = "Error on line 1 col 17: ("
#         self.assertTrue(TestParser.test(input,expect,265))
#     def test266(self):
#         """Parser Test"""
#         input = """func foo(bool k, string l)
#                     begin
#                         begin
#                             dynamic y
#                             var x <- "a" ... "b"
#                         end
#                         return false
#                         begin
#                         end
#                     end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,266))
#     def test267(self):
#         """Parser Test"""
#         input = """func foo(number a, string b)
#                     begin
#                         begin
#                             dynamic a <- a() % 100 
#                             var b <- "26" ... "7"
#                             main(l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
#                             break
#                         end
#                         return true
#                     end"""
#         expect = "Error on line 10 col 23: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,267))
#     def test268(self):
#         """Parser Test"""
#         input = """
#         func Divisors()
#             return (str(num1) ... str(num2))
#         func main()
#             begin
#                 var num1 <- a()[0,1]
#                 var num2 <- b()[foo(a[2]),n]
#             end
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,268))
#     def test269(self):
#         """Parser Test"""
#         input = """
#         func Divisors()
#             return (str(num1) ... str(num2))
#         func main()
#             begin
#                 var num1 <- a()[1,2,3]
#                 var num2()[1,2] <- b()[foo(a[2]),n]
#             end
#             """
#         expect = "Error on line 7 col 24: ("
#         self.assertTrue(TestParser.test(input,expect,269))
#     def test270(self):
#         """Parser Test"""
#         input = """
#         func main () return false
#         func isPrime(number x)
#             begin
#             var i <- 0
#             for i until (i / x / 2) by 1
#             begin
#             func foo() return true
#             end
#         """
#         expect = "Error on line 8 col 12: func"
#         self.assertTrue(TestParser.test(input,expect,270))
#     def test271(self):
#         """Parser Test"""
#         input = """func main () return
#         if xyz == "true" return
#         """
#         expect = "Error on line 2 col 8: if"
#         self.assertTrue(TestParser.test(input,expect,271))
#     def test272(self):
#         """Parser Test"""
#         input = """func main () return 
#         begin
#         end
#         """
#         expect = "Error on line 2 col 8: begin"
#         self.assertTrue(TestParser.test(input,expect,272))
#     def test273(self):
#         """Parser Test"""
#         input = """func main () return"""
#         expect = "Error on line 1 col 19: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,273))
#     def test274(self):
#         """Parser Test"""
#         input = """func main (dynamic x <- 1) 
#         return 1
#         """
#         expect = "Error on line 1 col 11: dynamic"
#         self.assertTrue(TestParser.test(input,expect,274))
#     def test275(self):
#         """Parser Test"""
#         input = """func main () return 1
#         begin
#         var i <- 0
#         for i until i >= 10 by 1
#         print(i)
#         end
#         """
#         expect = "Error on line 2 col 8: begin"
#         self.assertTrue(TestParser.test(input,expect,275))
#     def test276(self):
#         """Parser Test"""
#         input = """func main () return 0
#         func foo(number x)
#         if (true) xyz <- 1
#         else xyz <- 1   
#         """
#         expect = "Error on line 3 col 8: if"
#         self.assertTrue(TestParser.test(input,expect,276))
#     def test277(self):
#         """Parser Test"""
#         input = """dynamic m <- 2
#                    var t <- "string"
#                    var k = 1231e12
#         """
#         expect = "Error on line 3 col 25: ="
#         self.assertTrue(TestParser.test(input,expect,277))
#     def test278(self):
#         """Parser Test"""
#         input = """ number a <- 4
#                     number b[2,3] <- [[1,2,3],[4,5,6]]
#                     var e [2] <- [1,2]
#             func main(number d)
#                 begin
#                     a <- 1
#                     d <- a
#                 end
#         """
#         expect = "Error on line 3 col 26: ["
#         self.assertTrue(TestParser.test(input,expect,278))
#     def test279(self):
#         """Parser Test"""
#         input = """ number x <- 4
#                     number arr [2] <- [0, n]
#             func main(bool k, string l)
#                 begin
#                     number a
#                     a <- 1
#                     d <- a
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,279))
#     def test280(self):
#         """Parser Test"""
#         input = """ func foo(number a[1,2]) 
#                 begin 
#                     continue
#                 end
#             func main(number d, bool c)
#                 begin
#                     if (a()[1,2,3] == "true") return 1
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,280))
#     def test281(self):
#         """Parser Test"""
#         input = """ func foo(number x()[foo()[1,2+2]]) 
#                 begin 
#                     continue
#                 end
#             func main(number d, bool k, string l)
#                 begin
#                     if (a()[0] == "true") return 1
#                 end
#         """
#         expect = "Error on line 1 col 18: ("
#         self.assertTrue(TestParser.test(input,expect,281))
#     def test282(self):
#         """Parser Test"""
#         input = """ func foo(number a[2,5]) 
#                 begin 
#                     continue
#                     if (l < 12 < false) return 1
#                 end
#             func main(number d, bool k, string l)
#                 begin
#                     if (a()[1,2,3] == "true") return 1
#                 end
#         """
#         expect = "Error on line 4 col 31: <"
#         self.assertTrue(TestParser.test(input,expect,282))
#     def test283(self):
#         """Parser Test"""
#         input = """ func foo(number x[10]) 
#                 begin 
#                     continue
#                     if ((l < 12) < false) return 1
#                 end
#             func main(number d, bool k, string l)
#                 begin
#                     if (a()[1,2,3] == "true") return 1
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,283))
#     def test284(self):
#         """Parser Test"""
#         input = """ func foo(number x[10]) 
#                 begin 
#                     continue
#                     if ((l < 12) < false) return a[b[c[foo()]]]
#                 end
#             func main(number d, bool k, string l)
#                 begin
#                 continue
#                 break
#                 if (a()[1,2,3] == "true") return 1
#                 else print(foo(123))
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,284))
#     def test285(self):
#         """Parser Test"""
#         input = """ func foo(number x[10]) 
#                 begin 
#                     continue
#                     if ((l < 12) < false) return a[b[c[foo()]]]
#                     foo(0,1) <- a(2)[1,2] 
#                 end
#             func main(number d, bool k, string l)
#                 begin
#                 continue
#                 break
#                 if (a()[1,2,3] == "true") return 1
#                 else print(foo(123))
#                 end
#         """
#         expect = "Error on line 5 col 29: <-"
#         self.assertTrue(TestParser.test(input,expect,285))
#     def test286(self):
#         """Parser Test"""
#         input = """ func foo(number x[10]) 
#                 begin 
#                     continue
#                     if ((l < 12) < false) return a[b[c[foo()]]]
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                 end
#                 ## this is comment
#             func main(number d, bool k, string l)
#                 begin
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,286))
#     def test287(self):
#         """Parser Test"""
#         input = """ func foo(number x[10]) 
#                 begin 
#                     continue
#                     if ((l < 12) < false) return a[b[c[foo()]]]
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                     if (1<2) print()
#                     else noprint(2,3,4)
#                     for i until i-1 > 9 by 2 * 3 % 4
#                             begin
#                                 number a <- a * 4
#                             end
#                  end
#                 ## this is comment
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,287))
#     def test288(self):
#         """Parser Test"""
#         input = """ func foo(number x[10]) 
#                 continue
#                 begin 
                    
#                     if ((l < 12) < false) return a[b[c[foo()]]]
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                     if (1<2) print()
#                     else noprint(2,3,4)
#                     for i until i-1 > 9 by 2 * 3 % 4
#                             begin
#                                 number a <- a * 4
#                             end
#                  end
#                 ## this is comment
#         """
#         expect = "Error on line 2 col 16: continue"
#         self.assertTrue(TestParser.test(input,expect,288))
#     def test289(self):
#         """Parser Test"""
#         input = """ func foo(number a[1,3,4]) 
#                 return 2
#                 func doo(dynamic a)
#                 begin        
#                     if ((l < 12) < false) return a[b[c[foo()]]]
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                     if (1<2) print()
#                     else noprint(2,3,4)
#                     for i until i-1 > 9 by 2 * 3 % 4
#                             begin
#                                 number a <- a * 4
#                             end
#                  end
#                 ## this is comment
#         """
#         expect = "Error on line 3 col 25: dynamic"
#         self.assertTrue(TestParser.test(input,expect,289))
#     def test290(self):
#         """Parser Test"""
#         input = """ func foo(number a[1,3]) return 2
#                 ## this is comment
#                 ## this is comment
#                 func foo(var a <- 2)
#                 begin        
#                     x[345,k(999)[1,2,3]] <- a(12)[0] 
#                 end
#                 ## this is comment
#         """
#         expect = "Error on line 4 col 25: var"
#         self.assertTrue(TestParser.test(input,expect,290))
#     def test291(self):
#         """Parser Test"""
#         input = """ func foo(number a[1,5]) return 2
#                 ## this is comment
#                 ## this is comment
#                 func foo(number x)
#                 begin        
#                     x[345,k(999)[1,2,3]] <- a(12)[0]
#                     (a)[2]<- 3.14
#                 end
#                 ## this is comment
#         """
#         expect = "Error on line 7 col 20: ("
#         self.assertTrue(TestParser.test(input,expect,291))
#     def test292(self):
#         """Parser Test"""
#         input = """
#         func main()
#             begin   
#                 if(foo()[1,2,3] = 1) xyz[2] <- 1
#                 ## comment0
                
#                 if(1<2) 
#                     ## comment1
                    
#                     napi <- 1
#                     ## comment2
#                 else solute()
#                 ## comment3
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,292))
#     def test293(self):
#         """Parser Test"""
#         input = """func main () return 9<8>true
#         """
#         expect = "Error on line 1 col 23: >"
#         self.assertTrue(TestParser.test(input,expect,293))
#     def test294(self):
#         """Parser Test"""
#         input = """func main () return (true>false)<10
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,294))
#     def test295(self):
#         """Parser Test"""
#         input = """func main () return true
#         func dun(bool f)
#             begin
#                 begin
#                     dynamic a <- "lhs of assign should be a variable not function call"
#         var a() <- foo()
#                 end
#             end
#         """
#         expect = "Error on line 6 col 13: ("
#         self.assertTrue(TestParser.test(input,expect,295))
#     def test296(self):
#         """Parser Test"""
#         input = """ 
#             var xyz <- false > "1istrue" + 99e10 / 2
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,296))
#     def test297(self):
#         """Parser Test"""
#         input = """func main () return 1
#         var xyz <- array[foo()[a[1,foo(23)]]]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,297))
#     def test298(self):
#         """Parser Test"""
#         input = """func main () ##begin
#         number x <- "end is the error"
#         end
        
#         """
#         expect = "Error on line 3 col 8: end"
#         self.assertTrue(TestParser.test(input,expect,298))
#     def test299(self):
#         """Parser Test"""
#         input = """func main () dynamic x
#         """
#         expect = "Error on line 1 col 13: dynamic"
#         self.assertTrue(TestParser.test(input,expect,299))
#     def test300(self):
#         """Parser Test"""
#         input = """func main () 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,300))


######### Kien
#     def test_201(self):
#         """Simple program: int main() {} """
#         input = """func main () return a[b[2, 3]] + 4
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,201))
#     def test_202(self):
#         input = """
#             func main(string a)
#                 begin
#                     break ## this is the comment
#                 end
#             func main(dynamic a)
#         """
#         expect = "Error on line 6 col 22: dynamic"
#         self.assertTrue(TestParser.test(input, expect, 202))
#     def test_203(self):
#         """Simple program"""
#         input = """
#         func areDivisors(number num1, number num2)
#             return ((num1 % num2 = 0) or (num2 % num1 = 0))

#         func main()
#             begin
#             var num1 <- readNumber()
#             var num2 <- readNumber()

#             if (areDivisors(num1, num2)) writeString("Yes")
#             else writeString("No")
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,203))
#     def test_204(self):
#         """Simple program"""
#         input = """
#         func isPrime(number x)

#         func main()
#             begin
#                 number x <- readNumber()
#                 if (isPrime(x)) printString("Yes")
#                 else printString("No")
#             end
#         func isPrime(number x)
#             begin
#                 if (x <= 1) return false
#                 var i <- 2
#                 for i until i > x / 2 by 1
#                 begin
#                     if (x % i = 0) return false
#                 end
#                 return true
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,204))
#     def test_205(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             var i <- 0
#             for i until i >= 10 by 1
#             begin
#                 number r
#                 number s
#                 r <- 2.0
#                 number a[5]
#                 number b[5]
#                 s <- r * r * 3.14
#                 a[0] <- s
#             end
#             a[3 + foo(2)] <- a[b[2, 3]] + 4
#             number a[5] <- [1, 2, 3, 4, 5]
#             number b[2, 3] <- [[1, 2, 3], [4, 5, 6]]
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,205))
#     def test_206(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             var i <- 0
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,206))
#     def test_207(self):
#         """Simple program: int main() {} """
#         input = """
#             func main()
#             ## see ya
#             func fen() func therorist(dynamic a) ## see ya
#         """
#         expect = "Error on line 4 col 23: func"
#         self.assertTrue(TestParser.test(input,expect,207))
#     def test_208(self):
#         """Simple program: int main() {} """
#         input = """
#             func main()
#             func therorist(number a[5],number x[5,3])
#             func therorist(number num1, number num2)
#                 var xinchao <- 1.3e-3
#             func main(number xe <- b + 3)
#         """
#         expect = "Error on line 6 col 32: <-"
#         self.assertTrue(TestParser.test(input,expect,208))
#     def test_209(self):
#         """Simple program: int main() {} """
#         input = """ func main(string a[3])
#                 begin
#                     begin
#                         number a
#                         for i until i > 5 by 1
#                             begin
#                                 if (a = 1) a <- 2
#                                 else a <- 4
#                                 number a <- a + 1
#                             end
#                     end
#                     return this
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,209))
#     def test_210(self):
#         """Simple program: int main() {} """
#         input = """
#             ##This is comment
#             func main() var bb <- 2.3
#         """
#         expect = "Error on line 3 col 24: var"
#         self.assertTrue(TestParser.test(input,expect,210))
#     def test_211(self):
#         """Simple program: int main() {} """
#         input = """
#             func main()
#                 continue
#         """
#         expect = "Error on line 3 col 16: continue"
#         self.assertTrue(TestParser.test(input,expect,211))
#     def test_212(self):
#         """Simple program: int main() {} """
#         input = """
#             ##This is comment
#             func main(number a)
#                 ##This is comment
#                 ##This is comment

#                 begin
#                     number a
#                          for i until i > 5 by 1
#                              begin
#                                  if (a = 1) a <- 2
#                                  else a <- 4
#                                  number a <- a + 1
#                              end
#                 end

#                 ##This is comment
#             func main(number a)
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,212))
#     def test_213(self):
#         """Simple program: int main() {} """
#         input = """
#             number a[2] <- [1,2] ## This is comment
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,213))
#     def test_214(self):
#         """Simple program: int main() {} """
#         input = """var b <- 21"""
#         expect = "Error on line 1 col 11: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,214))
#     def test_215(self):
#         """Simple program: int main() {} """
#         input = """func main() """
#         expect = "Error on line 1 col 12: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,215))
#     def test_216(self):
#         """Simple program: int main() {} """
#         input = """ var ac <- "xin" ... "chao"
# """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,216))
#     def test_217(self):
#         """Simple program: int main() {} """
#         input = """ var ac <- "xin" ... "12" ... "chao"
#         """
#         expect = "Error on line 1 col 26: ..."
#         self.assertTrue(TestParser.test(input,expect,217))
#     def test_218(self):
#         """Simple program: int main() {} """
#         input = """
#             var thismy <- false >= "this" ... 1 > 2
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,218))
#     def test_219(self):
#         """Simple program: int main() {} """
#         input = """ var abc <- 1 / 4 * 1.2 % 4
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,219))
#     def test_220(self):
#         """Simple program: int main() {} """
#         input = """
#             var abc <- 4 and 4 and 4 or 4 or 4
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,220))
#     def test_221(self):
#         """Simple program: int main() {} """
#         input = """var abc <- 1 > 2 >= true
#         """
#         expect = "Error on line 1 col 17: >="
#         self.assertTrue(TestParser.test(input,expect,221))
#     def test_222(self):
#         """Simple program: int main() {} """
#         input = """
#             var abc <- ---1.3e-10 * not 7
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,222))
#     def test_223(self):
#         """Simple program: int main() {} """
#         input = """var abc <- --- not not not 5.3
#         """
#         expect = "Error on line 1 col 15: not"
#         self.assertTrue(TestParser.test(input,expect,223))
#     def test_224(self):
#         """Simple program: int main() {} """
#         input = """
#             var abc <- array[1][1][2]
#         """
#         expect = "Error on line 2 col 31: ["
#         self.assertTrue(TestParser.test(input,expect,224))
#     def test_225(self):
#         """Simple program: int main() {} """
#         input = """dynamic [] <- a[]
#         """
#         expect = "Error on line 1 col 8: ["
#         self.assertTrue(TestParser.test(input,expect,225))
#     def test_226(self):
#         """Simple program: int main() {} """
#         input = """
#             var abc <- a(ab[1])
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,226))
#     def test_227(self):
#         """Simple program: int main() {} """
#         input = """dynamic abc <- foo()[]
#         """
#         expect = "Error on line 1 col 21: ]"
#         self.assertTrue(TestParser.test(input,expect,227))
#     def test_228(self):
#         """Simple program: int main() {} """
#         input = """
#             var abc <- a(b,arr[2,2,3,4,5,6])[2,3.3e-12+2,true]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,228))
#     def test_229(self):
#         """Simple program: int main() {} """
#         input = """
#             func main() return number a
#         """
#         expect = "Error on line 2 col 31: number"
#         self.assertTrue(TestParser.test(input,expect,229))
#     def test_230(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             abc <- 3.14e-122
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,230))
#     def test_231(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#         func threat() begin
#         end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,231))
#     def test_232(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             "abc" <- 1
#             end
#         """
#         expect = "Error on line 4 col 12: abc"
#         self.assertTrue(TestParser.test(input,expect,232))
#     def test_233(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             abc() <- "xinchao"
#             end
#         """
#         expect = "Error on line 4 col 18: <-"
#         self.assertTrue(TestParser.test(input,expect,233))
#     def test_234(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             break
#         """
#         expect = "Error on line 3 col 12: break"
#         self.assertTrue(TestParser.test(input,expect,234))
#     def test_235(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#                 foo()
#                 number a
#                 abc <- 1.4e-1
#                 dc <- a
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,235))
#     def test_236(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#                 if (((abc = 1)))
#             end
#         """
#         expect = "Error on line 5 col 12: end"
#         self.assertTrue(TestParser.test(input,expect,236))
#     def test_237(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             break
#             continue
#             end

#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,237))
#     def test_238(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             for i until i >= 10 by 1
#                 a <- 1
#         """
#         expect = "Error on line 3 col 12: for"
#         self.assertTrue(TestParser.test(input,expect,238))
#     def test_239(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             for (i) until i >= 10 by 1
#                 a <- 1
#             end
#         """
#         expect = "Error on line 4 col 16: ("
#         self.assertTrue(TestParser.test(input,expect,239))
#     def test_240(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#         func main()
#         func main()
#         func main()
#         func main()
#         begin
#             break
#             continue
#             for i until i >= 10 by 1.2e-14 + 2.3
#                 begin
#                     break
#                     continue
#                 end
#         end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,240))
#     def test_241(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             if (a = 1)
#             end
#         """
#         expect = "Error on line 5 col 12: end"
#         self.assertTrue(TestParser.test(input,expect,241))
#     def test_242(self):
#         """Simple program: int main() {} """
#         input = """
#         number a 
#         func main()
#             return 1 + 1
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,242))
#     def test_243(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#             main()
#             if (f(a-b)[1,2-2,3*4] < 1)
#             a <- 3
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,243))
#     def test_244(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             return 3
#             return main()

#         """
#         expect = "Error on line 4 col 12: return"
#         self.assertTrue(TestParser.test(input,expect,244))
#     def test_245(self):
#         """Simple program: int main() {} """
#         input = """
#         func main() func()
#         """
#         expect = "Error on line 2 col 20: func"
#         self.assertTrue(TestParser.test(input,expect,245))
#     def test_246(self):
#         """Simple program: int main() {} """
#         input = """
#         var a <- break
#         """
#         expect = "Error on line 2 col 17: break"
#         self.assertTrue(TestParser.test(input,expect,246))
#     def test_247(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin
#                 begin
#                     begin
#                     end
#                     begin
#                     end
#                 end
#                 begin
#                 return true
#                 end             
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,247))
#     def test_248(self):
#         """Simple program: int main() {} """
#         input = """var abc <- 3.14e-314
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,248))
#     def test_249(self):
#         """Simple program: int main() {} """
#         input = """
#         func areDivisors(number num1, number num2)
#             return (a % num2 = 0 ... num2 % num1 = 0)
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,249))
#     def test_250(self):
#         """Simple program: int main() {} """
#         input = """
#             func isPrime(number x)
#             number b <- 234
#             string a[2] <- ["a","b"]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,250))
#     def test_251(self):
#         """Simple program: int main() {} """
#         input = """dynamic a
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,251))
#     def test_252(self):
#         """Simple program: int main() {} """
#         input = """func main () number a[5] <- [1, 2, 3, 4, 5]
#         """
#         expect = "Error on line 1 col 13: number"
#         self.assertTrue(TestParser.test(input,expect,252))
#     def test_253(self):
#         """Simple program: int main() {} """
#         input = """
#                     begin
#                         number a <- 1
#                     end
#         """
#         expect = "Error on line 2 col 20: begin"
#         self.assertTrue(TestParser.test(input,expect,253))
#     def test_254(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1 < 1 < 2
#         """
#         expect = "Error on line 1 col 26: <"
#         self.assertTrue(TestParser.test(input,expect,254))
#     def test_255(self):
#         """Simple program: int main() {} """
#         input = """
#          func main()
#              begin
#              if (f(a-b)[1,2-2,3*4] < 1)
#              end
#          """
#         expect = "Error on line 5 col 13: end"
#         self.assertTrue(TestParser.test(input,expect,255))
#     def test_256(self):
#         """Simple program: int main() {} """
#         input = """func main (num a) return 

#         """
#         expect = "Error on line 1 col 11: num"
#         self.assertTrue(TestParser.test(input,expect,256))
#     def test_257(self):
#         """Simple program: int main() {} """
#         input = """func main () return a[3 + foo(2)] <- a[b[2, 3]] + 4
#         """
#         expect = "Error on line 1 col 34: <-"
#         self.assertTrue(TestParser.test(input,expect,257))
#     def test_258(self):
#         """Simple program: int main() {} """
#         input = """func main () var abc <- true >= "false" ... 1 > 2
#         """
#         expect = "Error on line 1 col 13: var"
#         self.assertTrue(TestParser.test(input,expect,258))
#     def test_259(self):
#         """Simple program: int main() {} """
#         input = """func main () return foo(2.3e-10)
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,259))
#     def test_260(self):
#         """Simple program: int main() {} """
#         input = """dynamic a <- 3 + 1
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,260))
#     def test_261(self):
#         """Simple program: int main() {} """
#         input = """number foo(b,c) <- 8
#         """
#         expect = "Error on line 1 col 10: ("
#         self.assertTrue(TestParser.test(input,expect,261))
#     def test_262(self):
#         """Simple program: int main() {} """
#         input = """func main () 
#                     begin
#                     if (a[foo()[1,2]] = 1) return 1
#                     end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,262))
#     def test_263(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1
#         dynamic abc <- arr[1,2,arr[arr[(1.3e-10*2.2) and 1]],arr[2]]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,263))
#     def test_264(self):
#         """Simple program: int main() {} """
#         input = """func foo(number a[5], string b)
#                     begin
#                         var i <- 0
#                         for i until i >= 5 by 1
#                         begin
#                             a[i] <- i * i + 5
#                         end
#                         return -1
#                     end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,264))
#     def test_265(self):
#         """Simple program: int main() {} """
#         input = """func foo(number a(), string b)
#                     begin
#                         var i <- 0
#                         for i until i >= 5 by 1
#                         begin
#                             a[i] <- i * i + 5
#                         end
#                         return -1
#                     end
#         """
#         expect = "Error on line 1 col 17: ("
#         self.assertTrue(TestParser.test(input,expect,265))
#     def test_266(self):
#         """Simple program: int main() {} """
#         input = """func foo(number a, string b)
#                     begin
#                         begin
#                             dynamic a <- a() + 1 / 2 *3 
#                             var b <- "anpah" ... "beta"
#                         end
#                         return -1
#                     end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,266))
#     def test_267(self):
#         """Simple program: int main() {} """
#         input = """func foo(number a, string b)
#                     begin
#                         begin
#                             dynamic a <- a() + 1 / 2 *3 
#                             var b <- "anpah" ... "beta"
#                             main([1,2,3], 1+2, a, c ... e)
#                             break
#                         end
#                         return -1
#                     end"""
#         expect = "Error on line 10 col 23: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,267))
#     def test_268(self):
#         """Simple program: int main() {} """
#         input = """
#         func Divisors()
#             return (num1 ... num2)
#         func main()
#             begin
#                 var num1 <- a()[1,2,3]
#                 var num2 <- b()[2,3,foo(a[2])]
#             end
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,268))
#     def test_269(self):
#         """Simple program: int main() {} """
#         input = """
#         func Divisors()
#             return (num1 ... num2)
#         func main()
#             begin
#                 var num1 <- a()[1,2,3]
#                 var num2()[1,2] <- b()[2,3,foo(a[2])]
#             end
#             """
#         expect = "Error on line 7 col 24: ("
#         self.assertTrue(TestParser.test(input,expect,269))
#     def test_270(self):
#         """Simple program: int main() {} """
#         input = """
#         func main () return 1
#         func isPrime(number x)
#             begin
#             var i <- 2
#             for i until i > x / 2 by 1
#             begin
#             func abc()
#             end
#         """
#         expect = "Error on line 8 col 12: func"
#         self.assertTrue(TestParser.test(input,expect,270))
#     def test_271(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1
#         if abc == "true" return false
#         """
#         expect = "Error on line 2 col 8: if"
#         self.assertTrue(TestParser.test(input,expect,271))
#     def test_272(self):
#         """Simple program: int main() {} """
#         input = """func main () return 
#         begin
#         end
#         """
#         expect = "Error on line 2 col 8: begin"
#         self.assertTrue(TestParser.test(input,expect,272))
#     def test_273(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1"""
#         expect = "Error on line 1 col 21: <EOF>"
#         self.assertTrue(TestParser.test(input,expect,273))
#     def test_274(self):
#         """Simple program: int main() {} """
#         input = """func main (dynamic a) return 1
#         """
#         expect = "Error on line 1 col 11: dynamic"
#         self.assertTrue(TestParser.test(input,expect,274))
#     def test_275(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1
#         begin
#         var i <- 0
#         for i until i >= 10 by 1
#         writeNumbe(i)
#         end
#         """
#         expect = "Error on line 2 col 8: begin"
#         self.assertTrue(TestParser.test(input,expect,275))
#     def test_276(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1
#         func cera(number a)
#         if (1) abc <- 1
#         else abc <- 1   
#         """
#         expect = "Error on line 3 col 8: if"
#         self.assertTrue(TestParser.test(input,expect,276))
#     def test_277(self):
#         """Simple program: int main() {} """
#         input = """dynamic a
#                    var e <- 3
#                    var ceb = e
#         """
#         expect = "Error on line 3 col 27: ="
#         self.assertTrue(TestParser.test(input,expect,277))
#     def test_278(self):
#         """Simple program: int main() {} """
#         input = """ number a <- 4
#                     number b[2,3] <- [[1,2,3],[4,5,6]]
#                     var e [2] <- [1,2]
#             func main(number d)
#                 begin
#                     a <- 1
#                     d <- a
#                 end
#         """
#         expect = "Error on line 3 col 26: ["
#         self.assertTrue(TestParser.test(input,expect,278))
#     def test_279(self):
#         """Simple program: int main() {} """
#         input = """ number a <- 4
#                     number e [2] <- [1,2]
#             func main(bool c)
#                 begin
#                     number a
#                     a <- 1
#                     d <- a
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,279))
#     def test_280(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1,2]) 
#                 begin 
#                     continue
#                 end
#             func main(number d, bool c)
#                 begin
#                     if (a()[1,2,3] == "true") return 1
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,280))
#     def test_281(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a()[foo()[1,2+2]]) 
#                 begin 
#                     continue
#                 end
#             func main(number d, bool c)
#                 begin
#                     if (a()[1,2,3] == "true") return 1
#                 end
#         """
#         expect = "Error on line 1 col 24: ("
#         self.assertTrue(TestParser.test(input,expect,281))
#     def test_282(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[2,5]) 
#                 begin 
#                     continue
#                     if (e < 2 < 2) return 1
#                 end
#             func main(number d, bool c)
#                 begin
#                     if (a()[1,2,3] == "true") return 1
#                 end
#         """
#         expect = "Error on line 4 col 30: <"
#         self.assertTrue(TestParser.test(input,expect,282))
#     def test_283(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1]) 
#                 begin 
#                     continue
#                     if (e < (2 < 2)) return 1
#                 end
#             func main(number d, bool c)
#                 begin
#                     if (a()[1,2,3] == "true") return 1
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,283))
#     def test_284(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1]) 
#                 begin 
#                     continue
#                     if (e < (2 < 2)) return a[b[c[foo()]]]
#                 end
#             func main(number d, bool c)
#                 begin
#                 continue
#                 break
#                 if (a()[1,2,3] == "true") return 1
#                 else print(foo(123))
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,284))
#     def test_285(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1]) 
#                 begin 
#                     continue
#                     if (e < (2 < 2)) return a[b[c[foo()]]]
#                     a(2,3) <- a(2)[1,2] 
#                 end
#             func main(number d, bool c)
#                 begin
#                 continue
#                 break
#                 if (a()[1,2,3] == "true") return 1
#                 else print(foo(123))
#                 end
#         """
#         expect = "Error on line 5 col 27: <-"
#         self.assertTrue(TestParser.test(input,expect,285))
#     def test_286(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1]) 
#                 begin 
#                     continue
#                     if (e < (2 < 2)) return a[b[c[foo()]]]
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                 end
#                 ## this is comment
#             func main(number d, bool c)
#                 begin
#                 end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,286))
#     def test_287(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1]) 
#                 begin 
#                     continue
#                     if (e < (2 < 2)) return a[b[c[foo()]]]
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                     if (1<2) print()
#                     else noprint(2,3,4)
#                     for i until i > 10 by 1.3 * 2
#                             begin
#                                 number a <- a + 1
#                             end
#                  end
#                 ## this is comment
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,287))
#     def test_288(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1]) 
#                 continue
#                 begin 
                    
#                     if (e < (2 < 2)) return a[b[c[foo()]]]
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                     if (1<2) print()
#                     else noprint(2,3,4)
#                     for i until i > 10 by 1.3 * 2
#                             begin
#                                 number a <- a + 1
#                             end
#                  end
#                 ## this is comment
#         """
#         expect = "Error on line 2 col 16: continue"
#         self.assertTrue(TestParser.test(input,expect,288))
#     def test_289(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1,3,4]) 
#                 return 2
#                 func doo(dynamic a)
#                 begin        
#                     if (e < (2 < 2)) return a[b[c[foo()]]]
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                     if (1<2) print()
#                     else noprint(2,3,4)
#                     for i until i > 10 by 1.3 * 2
#                             begin
#                                 number a <- a + 1
#                             end
#                  end
#                 ## this is comment
#         """
#         expect = "Error on line 3 col 25: dynamic"
#         self.assertTrue(TestParser.test(input,expect,289))
#     def test_290(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1,3]) return 2
#                 ## this is comment
#                 ## this is comment
#                 func doo(var a <- 2)
#                 begin        
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                 end
#                 ## this is comment
#         """
#         expect = "Error on line 4 col 25: var"
#         self.assertTrue(TestParser.test(input,expect,290))
#     def test_291(self):
#         """Simple program: int main() {} """
#         input = """ func therorist(number a[1,5]) return 2
#                 ## this is comment
#                 ## this is comment
#                 func doo(number a2)
#                 begin        
#                     a[123,foo(23)[1,2,3]] <- a(2)[1,2] 
#                     (a)[2]<- 3.14
#                 end
#                 ## this is comment
#         """
#         expect = "Error on line 7 col 20: ("
#         self.assertTrue(TestParser.test(input,expect,291))
#     def test_292(self):
#         """Simple program: int main() {} """
#         input = """
#         func main()
#             begin   
#                 if(foo()[1,2,3] = 1) abc[2] <- 1
#                 ## comment0
                
#                 if(1<2) 
#                     ## comment1
                    
#                     napi <- 1
#                     ## comment2
#                 else solute()
#                 ## comment3
#             end
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,292))
#     def test_293(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1<2>1
#         """
#         expect = "Error on line 1 col 23: >"
#         self.assertTrue(TestParser.test(input,expect,293))
#     def test_294(self):
#         """Simple program: int main() {} """
#         input = """func main () return (1>2)<1
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,294))
#     def test_295(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1 + 2 + 2
#         func dun(bool f)
#         begin
#         begin
#         dynamic a
#         var a()[1] <- foo()
#         end
#         end
#         """
#         expect = "Error on line 6 col 13: ("
#         self.assertTrue(TestParser.test(input,expect,295))
#     def test_296(self):
#         """Simple program: int main() {} """
#         input = """ 
#             var abc <- false > "1" + 2
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,296))
#     def test_297(self):
#         """Simple program: int main() {} """
#         input = """func main () return 1
#         var abc <- array[foo()[a[1,foo(23)]]]
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,297))
#     def test_298(self):
#         """Simple program: int main() {} """
#         input = """func main () ##begin
#         number a <- 1
#         end
        
#         """
#         expect = "Error on line 3 col 8: end"
#         self.assertTrue(TestParser.test(input,expect,298))
#     def test_299(self):
#         """Simple program: int main() {} """
#         input = """func main () dynamic c <- 1
#         """
#         expect = "Error on line 1 col 13: dynamic"
#         self.assertTrue(TestParser.test(input,expect,299))
#     def test_300(self):
#         """Simple program: int main() {} """
#         input = """func main () 
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,300))
        
########### Quan

    def test1(self):
        input = """
        var a <- 1 + -1 / 2 % -3 * 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    def test2(self):
        input = """
        string a <- "random" ... "string" / 2
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    def test3(self):
        input = """
        bool a <- not x + y and ("random string" <= 123) = true
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test4(self):
        input = """
        func main()
        begin
            number a
            number b[1,2]
            a <- b["language" / 2 + true, ("hello"..."world") and not -"successful"]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))
    def test5(self):
        input = """
        func main()
        begin
            number a <- (1 + 2 - 3 / 4 % 5) <= not ((-"bruh" * ((2)...(3.2))) != (foo() == bar()))
            number b[1,2]
            a <- b[foo((1 + 2.2)... "bar"), (a + b) <= ((c / d) != 2)]
            a <- foo()[1, 2, 3]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))
    def test6(self):
        input = """
        bool a <- not x + y and "random string" <= 123 = true
        """
        expect = "Error on line 2 col 55: ="
        self.assertTrue(TestParser.test(input, expect, 205))
    def test7(self):
        input = """
        func main()
        begin
            number a
            number b[1,2]
            a <- (1 + 2 + foo())["language" / 2 + true, ("hello"..."world") and not -"successful"]
        end
        """
        expect = "Error on line 6 col 32: ["
        self.assertTrue(TestParser.test(input, expect, 206))
    def test8(self):
        input = """
        func main()
        begin
            number a
            number b[1,2]
            a <- b[foo((1 + 2.2)... "bar"), (a + b) <= ((c / d) != 2)]
            a <- foo()[1, 2, 3][1, 2, 3]
        end
        """
        expect = "Error on line 7 col 31: ["
        self.assertTrue(TestParser.test(input, expect, 207))
    def test9(self):
        input = """
        func main()
        begin
            a[3 + foo(2)] <- (a[b[2, 3]] + 4)()[1]
        end
        """
        expect = "Error on line 4 col 45: ("
        self.assertTrue(TestParser.test(input, expect, 208))
    def test10(self):
        input = """
        func main()
        begin
            number a
            number b[1,2]
            a <- b["language" / 2 + true, ("hello"..."world") not -"successful"]
        end
        """
        expect = "Error on line 6 col 62: not"
        self.assertTrue(TestParser.test(input, expect, 209))
    
    def test11(self):
        input = """
        var x <- 1.2e12
        func main()
        begin
            number a
            a[1, main()] <- 1 + foo()
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))
    def test12(self):
        input = """
        var x <- 1.2e12
        func main()
        begin
            bool x
            string c <- bruh
            dynamic a
            a[1, main()] <- 1 + foo()
            bool y[1, 2, 3] <- [a = c, b - foo(), "bye bye"]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))
    def test13(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            if (a <= 3.14 and not (a > 0)) print("hehe")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))      
    def test14(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            if (a <= 3.14 and not (a > 0)) 
            print("hehe")
            elif (a = 1) print("haha")
            else print("hoho")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))
    def test15(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            if (a <= 3.14 and not (a > 0)) begin
                print("hehe")
                if (a = a and QuanDepTrai()) print("true")
                elif (true = true)
                    print("true")
                else QuanDepTrai()
                
            end
            elif (a = 1) 
                print("haha")
            elif (a = 2) print("hoho")
            else 
                print("huhu")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))  
    def test16(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            if (a <= 3.14 and not (a > 0)) 
            begin
            
            
                return true
                
            end
            elif (a = 1) begin 
                print("haha")
            end
            elif (a = 2) print("hoho")
            else 
                print("huhu")
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))
    def test17(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            for i until lmao + 4 > foo(i) / bar(i) by 1 print("hehe")
            
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))
    def test18(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            for i until not (lmao + 4 > foo(i) / bar(i)) by print("lmao")
            begin
                print("hehe")
                break
            end
            break
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))
    def test19(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            for i until not (lmao + 4 > foo(i) / bar(i)) by print("lmao")...print("lmao2") 
            begin
                if (a = 1) continue
                else begin
                    for j until j < main() by -1 begin
                        lmao[foo(i), j] <- [i, j]
                    end
                end
                
            end
            return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    def test20(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            for i until not (lmao + 4 > foo(i) / bar(i)) by print("lmao")...print("lmao2") 
            begin
                func1()
                func2(print("hj"))
                func3(lmao, 1 + not true, func1(), func4()[1, foo()], array[a], 2 < 10)
            end
            return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test21(self):
        input = """
        func main()
        begin
            number a
            bool b
            string c
            var d
            dynamic e
            number array[1]
        end
        """
        expect = """Error on line 7 col 17: 
"""
        self.assertTrue(TestParser.test(input, expect, 220))
    def test22(self):
        input = """
        func main()
        begin
            number a
            bool b
            string c
            var d <- 1 + 1
            dynamic e
            number array[foo()]
        end
        """
        expect = "Error on line 9 col 25: foo"
        self.assertTrue(TestParser.test(input, expect, 221))
    def test23(self):
        input = """
        func main()
        begin
            number a
            bool b
            string c
            var d <- 1 + 1
            dynamic e
            var array[1, 2]
        end
        """
        expect = "Error on line 9 col 21: ["
        self.assertTrue(TestParser.test(input, expect, 222))
    def test24(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            if (a <= 3.14 and not (a > 0)) 
                print("hehe")
                if (a = a and QuanDepTrai()) print("true")
                elif (true = true)
                    print("true")
                else QuanDepTrai()  
            
            elif (a = 1) 
                print("haha")
            elif (a = 2) print("hoho")
            else 
                print("huhu")
        end
        """
        expect = "Error on line 12 col 12: elif"
        self.assertTrue(TestParser.test(input, expect, 223))
    def test25(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            if (a <= 3.14 and not (a > 0)) begin
                print("hehe")
                if (a = a and QuanDepTrai()) print("true")
                elif (true = true)
                    print("true")
                else QuanDepTrai()
                
            end elif (a = 1) 
                print("haha")
            elif (a = 2) print("hoho")
            else print("huhu")
        end
        """
        expect = "Error on line 12 col 16: elif"
        self.assertTrue(TestParser.test(input, expect, 224))
    def test26(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            for foo() until lmao + 4 > foo(i) / bar(i) by 1 print("hehe")
            
        end
        """
        expect = "Error on line 5 col 19: ("
        self.assertTrue(TestParser.test(input, expect, 225))
    def test27(self):
        input = """
        func main()
        begin
            var a <- "lmao"
            for i until abc() by i <- i + 1 print("lmao")

            break
        end
        """
        expect = "Error on line 5 col 35: <-"
        self.assertTrue(TestParser.test(input, expect, 226))
    def test28(self):
        input = """
        func main()
        begin
            foo() + 2
        end
        """
        expect = "Error on line 4 col 18: +"
        self.assertTrue(TestParser.test(input, expect, 227))
    def test29(self):
        input = """
        func main()
        begin
            foo() <- 3 + 2
        end
        """
        expect = "Error on line 4 col 18: <-"
        self.assertTrue(TestParser.test(input, expect, 228))
    def test30(self):
        input = """
        func main()
        begin
            number arr[] <- [1, 2, lol()]
        end
        """
        expect = "Error on line 4 col 23: ]"
        self.assertTrue(TestParser.test(input, expect, 229))
        
    def test31(self):
        input = """
        func lmao()
            break
        func main() ## main function
        
        begin
            var a <- "lmao"
            for i until not (lmao + 4 > foo(i) / bar(i)) by print("lmao") ## hjhj
            
            ## block 
            begin
                print("hehe")
                break
            end
            break
        end
        """
        expect = "Error on line 3 col 12: break"
        self.assertTrue(TestParser.test(input, expect, 230))  
    def test32(self):
        input = """
        func lmao() 
            ## break
            
        var x <- 2
        number glob
        glob <- 8
        
        func main() ## main function
        
        begin
            var a <- "lmao"
            for i until not (lmao + 4 > foo(i) / bar(i)) by print("lmao") ## hjhj
            
            ## block 
            begin
                print("hehe")
                break
            end
            break
        end
        
        """
        expect = "Error on line 7 col 8: glob"
        self.assertTrue(TestParser.test(input, expect, 231))
    def test33(self):
        input = """
        func lmao() 
            ## break
            
        func lol(number a, bool b)
        func QuanDepTrai() return true
        
        func loi        (dynamic a)
        
        func main() ## main function
        
        begin
            var a <- "lmao"
            for i until not (lmao + 4 > foo(i) / bar(i)) by print("lmao") ## hjhj
            
            ## block 
            begin
                print("hehe")
                break
            end
            break
        end
        
        """
        expect = "Error on line 8 col 25: dynamic"
        self.assertTrue(TestParser.test(input, expect, 232))
    def test34(self):
        input = """
        func lmao() 
            ## break
            
        func lol(number a, bool b)
        func QuanDepTrai() return true
        
        func loi (foo())
        
        func main() ## main function
        
        begin
            var a <- "lmao"
            for i until not (lmao + 4 > foo(i) / bar(i)) by print("lmao") ## hjhj
            
        end
        
        """
        expect = "Error on line 8 col 18: foo"
        self.assertTrue(TestParser.test(input, expect, 233))
    def test35(self):
        input = """
        func lmao() 
            ## break
            
        func lol(number a, bool b)
        func QuanDepTrai() return true
        
        func loi (number a[1, 2], string s[1, foo()])
        
        func main() ## main function
        
        begin
            break
        end
        
        """
        expect = "Error on line 8 col 46: foo"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test36(self):
        input = """func random(int a)
func main()
begin
    if (random()) print("false")
end
"""
        expect = "Error on line 1 col 12: int"
        self.assertTrue(TestParser.test(input, expect, 235))
        

    def test37(self):
        input = """func random(number a) return
func main()
begin
    if (random()) begin
        writeString("What's good" + 1.23e-12)
    end
end"""
        expect = "Error on line 7 col 3: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 236))
        

    def test38(self):
        input = """func random(number a)

begin
    if (a = 0) return 1 + a /3
    return random(a-1)
end
func main()
begin
    if (random()) begin
        writeString("What's good" + 1.23e-12)
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        

    def test39(self):
        input = """func random(number a)

begin
    if (a = 0) return 1 + a /3
    return random(a-1)
end

number a <- 16 / random(a)

func main()
begin
    for i until random(i) != "a"...a by random(a)
    begin
        writeString(i)
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        
    def test40(self):
        input = """func random(number a)

begin
    if (a = 0) return 1 + a /3
    return random(a-1)
end

number a <- 16 / random(a)

func main()
begin
    for i until random(i) != "a"...a by random(a)
    begin
        if (i == random(a) and not ("a" + true > 1)) writeString("bruh")
        elif i + 1 > 2 return
    end
end
"""
        expect = "Error on line 15 col 13: i"
        self.assertTrue(TestParser.test(input, expect, 239))
        


    def test41(self):
        input = """func random(number a)

begin
    if (a = 0) return 1 + a /3
    return random(a-1)
end

number a <- 16 / random(a)

func main()
begin
    for i until random(i) != "a"...a by random(a)
    begin
        if (i == random(a) and not ("a" + true > 1)) writeString("bruh")
        elif (i + 1 > 2) return 1 else
        return 10
    end
end
"""
        expect = "Error on line 15 col 34: else"
        self.assertTrue(TestParser.test(input, expect, 240))
        

    def test42(self):
        input = """func random(number a <- 6)

begin
    if (a = 0) return 1 + a /3
    return random(a-1)
end

number a <- 16 / random(a)

func main()
begin
    for i until random(i) != "a"...a by random(a)
    begin
        if (i == random(a) and not ("a" + true > 1)) writeString("bruh")
        elif (i + 1 > 2) return 1
        else
        return 10
    end
end
"""
        expect = "Error on line 1 col 21: <-"
        self.assertTrue(TestParser.test(input, expect, 241))
        

    def test43(self):
        input = """func random(number a, arr[1, 2])

begin
    if (a = 0) return 1 + a /3
    return random(a-1)
end

number a <- 16 / random(a)

func main()
begin
    for i until random(i) != "a"...a by random(a)
    begin
        if (i == random(a) and not ("a" + true > 1)) writeString("bruh")
        elif (i + 1 > 2) return 1
        else
        return 10
    end
end
"""
        expect = "Error on line 1 col 22: arr"
        self.assertTrue(TestParser.test(input, expect, 242))
        

    def test44(self):
        input = """func random(number a, string arr[1, 2])

begin
    if (a = 0) return 1 + a /3
    return random(a-1)
end

number a <- 16 / random(a)

func main()
begin
    for i until random(i) != "a"...a by random(a)
    begin
        if (i == random(a) and not ("a" + true > 1)) writeString("bruh")
        elif (i + 1 > 2) return 1
        else
        return 10
    end
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        

    def test45(self):
        input = """number a <- 3
bool arr[1, 2, 3]

func main()
    arr[1, 1, 1] <- arr[2,2,2]
"""
        expect = "Error on line 5 col 4: arr"
        self.assertTrue(TestParser.test(input, expect, 244))
    
    def test46(self):
        input = """if (x < 3) return true
"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 245))
        

    def test47(self):
        input = """func main()
begin
    boolean bruh <- true
    number arr[3, 4] <- foo(arr[5, 6])
end
"""
        expect = "Error on line 3 col 12: bruh"
        self.assertTrue(TestParser.test(input, expect, 246))
        

    def test48(self):
        input = """func main()
begin
    bool bruh <- true
    number arr[3, 4] <- foo(arr[5, 6])
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))
        

    def test49(self):
        input = """func main()
begin
    var bruh <- true
    number arr[3, 4] <- foo(arr[5, 6])
    if (arr) ## comment
    begin
        foo()
    end
    else arr <- foo(arr[foo(arr)])
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
        

    def test50(self):
        input = """func main()
begin
    var bruh <- true
    number arr[3, 4] <- foo(arr[5, 6])
    if (arr) ## comment
    begin
        foo()
    end
    else arr <- foo(arr[foo(arr)])()[1]
end
"""
        expect = "Error on line 9 col 34: ("
        self.assertTrue(TestParser.test(input, expect, 249))
        

    def test51(self):
        input = """func main()
begin
    var bruh <- true
    number arr[3, 4] <- foo(arr[5, 6])
    if (arr) ## comment
    begin
        foo()
    end
    else arr <- foo(arr[foo(arr)])[1]
    for (i + 1) until i by i
end
"""
        expect = "Error on line 10 col 8: ("
        self.assertTrue(TestParser.test(input, expect, 250))
          

    def test52(self):
        input = """func main()
begin
    var bruh <- true
    number arr[3, 4] <- foo(arr[5, 6])
    if (arr) ## comment
    begin
        foo()
    end
    elif (arr != foo(arr[foo(arr)])[1])
    for i until i ##by i
        increment(i *- 2)
    else return 
end
"""
        expect = """Error on line 10 col 24: 
"""
        self.assertTrue(TestParser.test(input, expect, 251))
        

    def test53(self):
        input = """func main()
begin
    var bruh <- true
    number arr[3, 4] <- foo(arr[5, 6])
    if (arr) ## comment
    begin
        foo()
    end
    elif (arr != foo(arr[foo(arr)])[1])
    for i by 2
        increment(i *- 2*i)
    else return 
end
"""
        expect = "Error on line 10 col 10: by"
        self.assertTrue(TestParser.test(input, expect, 252))
        
        

    def test54(self):
        input = """func main()
begin
    return break
end
"""
        expect = "Error on line 3 col 11: break"
        self.assertTrue(TestParser.test(input, expect, 253))
        

    def test55(self):
        input = """func main()
begin
    return main - 1
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))
        

    def test56(self):
        input = """func main(number args[])
begin
    return 0
end
"""
        expect = "Error on line 1 col 22: ]"
        self.assertTrue(TestParser.test(input, expect, 255))
        

    def test57(self):
        input = """func main(number args[4])
begin
    string x1 = args[0]
    string x2 = args[1]

end
"""
        expect = "Error on line 3 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 256))
        

    def test58(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 = x1..x2

end
"""
        expect = "."
        self.assertTrue(TestParser.test(input, expect, 257))
        

    def test59(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 = x1...(x2-x1)

end
"""
        expect = "Error on line 5 col 7: ="
        self.assertTrue(TestParser.test(input, expect, 258))
        

    def test60(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- x1...(x2-x1)

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))
        

    def test61(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- x1...x2-x1

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
        

    def test61(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- x1...x2...x1

end
"""
        expect = "Error on line 5 col 17: ..."
        self.assertTrue(TestParser.test(input, expect, 260))
        

    def test62(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- x1 / x3 / x4 * 2 + not (x1 +- bool)

end
"""
        expect = "Error on line 5 col 40: bool"
        self.assertTrue(TestParser.test(input, expect, 261))
        

    def test63(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- (x1 / x3 / x4 * 2 + not (x1 +- x2))()

end
"""
        expect = "Error on line 5 col 45: ("
        self.assertTrue(TestParser.test(input, expect, 262))
        

    def test64(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- foo(x1 / x3 / x4 * 2 + not (x1 +- x2))()

end
"""
        expect = "Error on line 5 col 48: ("
        self.assertTrue(TestParser.test(input, expect, 263))
        

    def test65(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- foo(x1 / x3 / x4 * 2 + not (x1 +- x2))

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 264))
        

    def test66(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,]

end
"""
        expect = "Error on line 3 col 20: ]"
        self.assertTrue(TestParser.test(input, expect, 265))

    def test67(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic <- x
    ## if (foo(y) - x > (2 > 3))
    ##print(x)
    ## else if (bar(x) - y == true) print(y) else return false

end
"""
        expect = "Error on line 4 col 12: <-"
        self.assertTrue(TestParser.test(input, expect, 266))
        

    def test68(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (foo(y) - x > 2 > 3)
    print(x)
    ## else if (bar(x) - y == true) print(y) else return false

end
"""
        expect = "Error on line 5 col 23: >"
        self.assertTrue(TestParser.test(input, expect, 267))
        

    def test69(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (foo(y) - x > (2 <= 3))
    print(x)
    ## else if (bar(x) - y == true) print(y) else return false

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
        

    def test70(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (foo(y) - x > (2 <= 3))
    print(x)
    else if (bar(x) - y == true) print(y) else return false

end
"""
        expect = "Error on line 7 col 42: else"
        self.assertTrue(TestParser.test(input, expect, 269))
        

    def test71(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (foo(y) - x > (2 <= 3))
    print(x)
    else if (bar(x) - y == true) print(y)
    else return false

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 270))
        

    def test72(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (foo(y) - x > (2 <= 3))
    print(x)
    else if (bar(x) - y == true) print(y)
    else for i until true by main() begin
    end

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
        

    def test73(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (foo(y) - x > (2 <= 3))
    print(x)
    else if (bar(x) - y == true) print(y)
    else for i until true by main() begin
        for j until i > 10 by 1
    end

end
"""
        expect = "Error on line 10 col 4: end"
        self.assertTrue(TestParser.test(input, expect, 272))
        

    def test74(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (foo(y) - x > (2 <= 3))
    print(x)
    else if (bar(x) - y == true) print(y)
    else for i until true by main() begin
        for j until i > 10 by 1 break
    end

end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 273))
        

    def test75(self):
        input = """function main()
begin
end """
        expect = "Error on line 1 col 0: function"
        self.assertTrue(TestParser.test(input, expect, 274))
        

    def test76(self):
        input = """func main()
begin
    func function()
    begin
        return
    end
end 
"""
        expect = "Error on line 3 col 4: func"
        self.assertTrue(TestParser.test(input, expect, 275))
        

    def test77(self):
        input = """func main()
begin
    main(x <- 1)
end 
"""
        expect = "Error on line 3 col 11: <-"
        self.assertTrue(TestParser.test(input, expect, 276))
        

    def test78(self):
        input = """func main()
begin
    main([1,2,3,4])
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))
        

    def test79(self):
        input = """func main()
begin
    if (main([1,2,3,4]))
    else return
end 
"""
        expect = "Error on line 4 col 4: else"
        self.assertTrue(TestParser.test(input, expect, 278))
        
        

    def test80(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x < 2
    end
    else begin 
    
    end
end 
"""
        expect = "Error on line 4 col 14: <"
        self.assertTrue(TestParser.test(input, expect, 279))
        

    def test81(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    else begin 
    return
    end
end 
"""
        expect = "Error on line 5 col 4: else"
        self.assertTrue(TestParser.test(input, expect, 280))
        

    def test82(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        var arr[1,2,3] <- main[foo()]
        return
    end
end 
"""
        expect = "Error on line 7 col 15: ["
        self.assertTrue(TestParser.test(input, expect, 281))
        

    def test83(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        void arr[1,2,3] <- main[foo()]
        return
    end
end 
"""
        expect = "Error on line 7 col 13: arr"
        self.assertTrue(TestParser.test(input, expect, 282))
        

    def test84(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[foo()]
        return
    end
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))
        

    def test85(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[foo()]
        return
    end
    for i == 0 until i < 5 by 1
        print(i)
end 
"""
        expect = "Error on line 10 col 10: =="
        self.assertTrue(TestParser.test(input, expect, 284))
        

    def test86(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[foo()]
        return
    end
    for arr[0] until i < 5 by 1
        print(i)
end 
"""
        expect = "Error on line 10 col 11: ["
        self.assertTrue(TestParser.test(input, expect, 285))
        

    def test87(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[foo()]
        return
    end
    for i until i < arr[foo] by 1
        print(i)
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))
        

    def test88(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[foo()]
        return
    end
    for i until i...j <= arr[foo] by 1
        print(i)
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))
        

    def test89(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[foo()]
        return
    end
    for i until i...(j <= arr[foo<1]) by 1
        print(i)
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))
        

        

    def test90(self):
        input = """func main()
begin
    string str <- "HelloWorld"..."!"
    if (not len(str) > 10)
    print("long string")
    else print("short string")
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))
        

    def test91(self):
        input = """func main()
begin
    string str <- "HelloWorld"..."!"
    if (not len(str) and str..."bonus" > 10)
    print("long string")
    else print("short string")
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))
        

    def test92(self):
        input = """func main()
begin
    string str <- "HelloWorld"..."!"
    if (not len(str) and (str..."bonus" > 10))
    print("long string")
    else print("short string")
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))
        

    def test93(self):
        input = """func main() begin
    if (failed) if (chained) print("nuh uh")
    else print("")
    else failed <- not true
end 
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))
        

    def test94(self):
        input = """func main(number [1,2]) begin
    
end 
"""
        expect = "Error on line 1 col 17: ["
        self.assertTrue(TestParser.test(input, expect, 293))
        

    def test95(self):
        input = """func main(number abc[1,2]) begin
  break  
end 
if (main[1] == "95")
return
"""
        expect = "Error on line 4 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 294))
        

    def test96(self):
        input = """func main(number abc[1,2]) begin
  break  
end
func chinsau()
if (main[1] == "95")
return
"""
        expect = "Error on line 5 col 0: if"
        self.assertTrue(TestParser.test(input, expect, 295))
        

    def test97(self):
        input = """func main(number abc[1,2]) begin
  break  
end
func chinbay()
begin
if (main[1] == "95")
return
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))
        

    def test98(self):
        input = """func main(number abc[1,2]) begin
  break  
end
func _()
 return _()[_()]
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))
        

    def test99(self):
        input = """func main()
begin
    if (main() <- 2) return main <- 2
end
"""
        expect = "Error on line 3 col 15: <-"
        self.assertTrue(TestParser.test(input, expect, 298))


    def test100(self):
        input = """func final()
begin
    if (final() < 2) return final()[1] != not 2
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))