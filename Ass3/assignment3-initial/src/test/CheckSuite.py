import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
##############---------- PHAN THANH THONG - 2153846 ----------##############
#     def test_400(self):
#         input = """dynamic a
# number b[3] <- [true,2,a]
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(BooleanLit(True), NumLit(2.0), Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 400))
        
#     def test_401(self):
#         # a and d should be inferred by BoolType?
#         input = """dynamic a
# dynamic d
# number b[3] <- [a,true,d]
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([3.0], NumberType), None, ArrayLit(Id(a), BooleanLit(True), Id(d)))"
#         self.assertTrue(TestChecker.test(input, expect, 401))
    
#     def test_402(self):
#         input = """dynamic a
# func beou(number b, string c)
#     begin
#         beou(a,a)    
#     end
# func main()
#     begin
#     end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(beou), [Id(a), Id(a)])"
#         self.assertTrue(TestChecker.test(input, expect, 402))
        
#     def test_403(self):
#         input = """
# func beou()
# func beou()
#     begin
#         return
#     end
# func beou() return
# func main()
#     begin
#     end
#         """
#         expect = """Redeclared Function: beou"""
#         self.assertTrue(TestChecker.test(input, expect, 403))
        
#     def test_404(self):
#         input = """dynamic a
# dynamic d
# number b[3] <- [a,1,2,d]
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([3.0], NumberType), None, ArrayLit(Id(a), NumLit(1.0), NumLit(2.0), Id(d)))"
#         self.assertTrue(TestChecker.test(input, expect, 404))
        
#     def test_405(self):
#         input = """dynamic a
# dynamic d
# number b[7,7,7] <- [[a,d],[a,d],[a,d]]
# func main()
# begin
# end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(b), ArrayType([7.0, 7.0, 7.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(d)), ArrayLit(Id(a), Id(d)), ArrayLit(Id(a), Id(d))))"
#         self.assertTrue(TestChecker.test(input, expect, 405))
        
#     def test_406(self):
#         input = """dynamic a
# dynamic d
# number b[3] <- [a,a,d]
# bool c <- a
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(c), BoolType, None, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 406))
        
#     def test_407(self):
#         input = """number a
# bool d
# number b[3] <- [a,a,d]
# bool c <- a
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(Id(a), Id(a), Id(d))"
#         self.assertTrue(TestChecker.test(input, expect, 407))
    
#     def test_408(self):
#         input = """
# func beou()
# func main()
# func main()
# begin
#     beou()
# end
#         """
#         expect = "No Function Definition: beou"
#         self.assertTrue(TestChecker.test(input, expect, 408))
        
#     def test_409(self):
#         input = """
# func beou(number a, bool b, string c) return
# func main()
# begin
#     number a
#     bool b
#     a <- beou(a, b)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(a), Id(b)])"
#         self.assertTrue(TestChecker.test(input, expect, 409))
        
#     def test_410(self):
#         input = """
# func beou(number a, bool b, string c)
# func main()
# begin
#     number a
#     bool b
#     a <- beou(a, b, c)
# end
#         """
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input, expect, 410))
        
#     def test_411(self):
#         input = """
# func beou(number a, bool b, string c) return a
# func main()
# begin
#     dynamic a
#     bool b
#     dynamic c
#     a <- beou(a, c, b)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(a), Id(c), Id(b)])"
#         self.assertTrue(TestChecker.test(input, expect, 411))
        
#     def test_412(self):
#         input = """
# func beou(number a[3], bool b, string c) return a
# func main()
# begin
#     number a[4]
#     bool b
#     dynamic c
#     a <- beou(a, b, c)
# end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(beou), [Id(a), Id(b), Id(c)]))"
#         self.assertTrue(TestChecker.test(input, expect, 412))
        
#     def test_413(self):
#         input = """
# func beou(number a[3], bool b, string c) return 3
# func main()
# begin
#     bool a[3]
#     bool b
#     dynamic c
#     a <- beou(a, b, c)
# end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(beou), [Id(a), Id(b), Id(c)]))"
#         self.assertTrue(TestChecker.test(input, expect, 413))
        
#     def test_414(self):
#         input = """
# func beou(number a[3], bool b, string c) return
# func main()
# begin
#     number a[3]
#     bool b
#     dynamic c
#     a <- beou(a, b, c)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(a), Id(b), Id(c)])"
#         # beou has VoidType, i dont compare type at stmt, but make condition at CallExpr
#         # from spec: For a function call <function-name>(<args>), the callee <method name> must have
#         # non-void as return type
#         self.assertTrue(TestChecker.test(input, expect, 414))
        
#     def test_415(self):
#         input = """
# func beou(number a[3], bool b, string c) return [a[1], a[2], a[3], a[4]]
# func main()
# begin
#     number a[3]
#     bool b
#     dynamic c
#     a <- beou(a, b, c)
# end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(beou), [Id(a), Id(b), Id(c)]))"
#         self.assertTrue(TestChecker.test(input, expect, 415))
        
#     def test_416(self):
#         input = """
# dynamic beou
# func beou(number a[3], bool b, string c) return b
# func main()
# begin
#     beou <- beou(beou, beou, beou)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(beou), Id(beou), Id(beou)])"
#         self.assertTrue(TestChecker.test(input, expect, 416))
        
#     def test_417(self):
#         input = """
# dynamic beou
# func beou(number a[3], bool b)
# func beou(string c) return c
# func main()
# begin
#     number a[3]
#     bool b
#     beou <- beou(a, b)
#     beou(a,b)
# end
#         """
#         expect = "Redeclared Function: beou"
#         self.assertTrue(TestChecker.test(input, expect, 417))
    
#     def test_418(self):
#         input = """
# func beou(number a[3], bool b, string c)
# func beou(string c) return b
# func main()
# begin
#     beou <- beou(beou)
# end
#         """
#         expect = "Redeclared Function: beou"
#         self.assertTrue(TestChecker.test(input, expect, 418))
        
#     def test_419(self):
#         input = """
# dynamic a
# func beou (number b) return a
# func main()
# begin
#     beou <- beou(beou)
# end
#         """
#         expect = "Type Cannot Be Inferred: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 419))
        
#     def test_420(self):
#         input = """
# number a[3] <- [7,7,7]
# func beou (number b)
#     begin
#         a[1] <- b + a[2]
#         return a
#     end
# func main()
# begin
#     dynamic c
#     c <- a[c] + a[1,2]
#     bool d
#     c <- d
# end
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0)])"
#         #if we check size of array
#         self.assertTrue(TestChecker.test(input, expect, 420))
        
#     def test_421(self):
#         input = """
# number a[3] <- [7,7,7]
# func beou (number b)
#     begin
#         a[1] <- b + a[2]
#         dynamic c
#         c <- a[c] + beou(a[1])[1]
#         return a
#     end
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(beou), [ArrayCell(Id(a), [NumLit(1.0)])]), [NumLit(1.0)])"
#         # how to infer?
#         # or raise error (we check if ctx.arr in ArrayCell has ArrayType)
#         self.assertTrue(TestChecker.test(input, expect, 421))
        
#     def test_422(self):
#         input = """
# dynamic a
# func beou (number b)
#     begin
#         a[1] <- 1
#         return a[1,2]
#     end
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0)])"
#         # how to infer?
#         # or raise error (we check if ctx.arr in ArrayCell has ArrayType)
#         # The implicit keyword cannot be used for array type. (in spec)
#         self.assertTrue(TestChecker.test(input, expect, 422))
        
#     def test_423(self):
#         input = """
# var a <- 3
# func beou (number b)
#     return a
# func main()
# begin
#     beou(a)
# end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(beou), [Id(a)])"
#         self.assertTrue(TestChecker.test(input, expect, 423))
        
#     def test_424(self):
#         input = """
# dynamic b
# dynamic c
# dynamic d
# func main()
# begin
#     number a[3] <- [b,c,d]
#     bool f <- d
# end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(f), BoolType, None, Id(d))"
#         # infer b c d to number
#         self.assertTrue(TestChecker.test(input, expect, 424))

#     def test_425(self):
#         input = """number a
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 425))
#     def test_426(self):
#         input = """
#         func boo()
#         func main() begin
#             boo()
#         end
#         """
#         expect = "No Function Definition: boo"
#         self.assertTrue(TestChecker.test(input, expect, 426))
        
#     def test_427(self):
#         input = """
#         func beou() begin
#             return 1
#         end
#         func main() begin
#             beou()
#         end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(beou), [])"
#         self.assertTrue(TestChecker.test(input, expect, 427))
#     def test_428(self):
#         input = """
#         func main() begin
            
#             dynamic b
#             dynamic a 
#             number x[1, 2] <- [[1,b]]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 428))
#     def test_429(self):
#         input = """
#         func main() begin
            
#             dynamic b
#             dynamic a <- [b]
#             number x[1, 2] <- [[1,b]]
#         end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, ArrayLit(Id(b)))"
#         self.assertTrue(TestChecker.test(input, expect, 429))
#     def test_430(self):
#         input = """
#         func main() begin
#             number x[1, 2] <- [[1,2]]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 430))
#     def test_431(self):
#         input = """
#         func main() begin
#         dynamic b
#             number x[2, 2] <- [[1,2], [b, b]]
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 431))
#     def test_432(self):
#         input = """
#         func main() begin
#         end
#         func beou(number x)
#         func beou(number x, number y) begin
#         end
#         """
#         expect = "Redeclared Function: beou"
#         self.assertTrue(TestChecker.test(input, expect, 432))
#     def test_433(self):
#         input = """
#         func main() begin
#         number a <- a
#         end
#         func beou(number x, number y)
#         func beou(number z, number x) begin
#         end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 433))
#     def test_434(self):
#         input = """
#         func main() begin
#         end
#         func beou(number x, number x) begin
#         end
#         """
#         expect = "Redeclared Parameter: x"
#         self.assertTrue(TestChecker.test(input, expect, 434))

#     def test_435(self):
#         input = """
# func main()
# begin
#     var x <- [[[[1, 6]], [3, 4, 8]], [[2, 4, 1], [9, 40, 11]]]

# end
# """
#         myret_ = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(6.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(8.0)))"
#         self.assertTrue(TestChecker.test(input, myret_, 435))
#     def test_436(self):
#         input = """
# func main()
# begin
#     number a[2, 2] <- [[6, 8], [6, 8]]
#     number b[2] <- a[0]
#     writeNumber(b[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 436))
#     def test_437(self):
#         input = """
#         func main()
# begin 
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[3,3] <- [a,b]
#     a <- [7,7,7]
#     b <- [8,8,8]
#     c <- [9,9,9]
#     writeNumber(a[0] + b[0] + c[0])
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([3.0, 3.0], NumberType), None, ArrayLit(Id(a), Id(b)))"
#         self.assertTrue(TestChecker.test(input, expect, 437))
#     def test_438(self):
#         input = """
# func beou(number a[3,3]) return 1
#         func main()
# begin 
#     dynamic a
#     dynamic b
#     dynamic c
#     number x <- beou([a,b,c])
#     a <- [7,7,7]
#     b <- [8,8,8]
#     c <- [9,9,9]
#     writeNumber(a[0] + b[0] + c[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 438))
#     def test_439(self):
#         input = """
#         func main()
# begin 
#     dynamic a
#     dynamic b
#     dynamic c
#     dynamic d <- [a,b,c]
# end
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(d), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
#         self.assertTrue(TestChecker.test(input, expect, 439))
#     def test_440(self):
#         input = """
#             dynamic a
#             dynamic x
#             dynamic y
#             func beou(number a,string b) return
#             func main() begin
#                 number a <- beou(x,y)
#                 number x
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(x), Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 440))
    
#     def test_441(self):
#         input = """
#         func main()
# begin 
#     dynamic a
#     dynamic b
#     dynamic c
#     number x[3,3]
#     x <- [a,b,c]
#     a <- [7,7,7]
#     b <- [8,8,8]
#     c <- [9,9,9]
#     writeNumber(a[0] + b[0] + c[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 441))
        
#     def test_442(self):
#         input = """
# func beou(number a[3,3]) return
#         func main()
# begin 
#     dynamic a
#     dynamic b
#     dynamic c
#     beou([a,b,c])
#     a <- [7,7,7]
#     b <- [8,8,8]
#     c <- [9,9,9]
#     writeNumber(a[0] + b[0] + c[0])
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 442))
        
#     def test_443(self):
#         input = """
# func beou()
# func main()
#     begin
#         number x[3,3] <- beou()
#     end
# dynamic a
# dynamic b
# dynamic c
# func beou() return [a,b,c]
# func beou1() begin
#     a <- [7,7,7]
#     b <- [8,8,8]
#     c <- [9,9,9]
# end
# """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 443))

#     def test_444(self):
#         input = """
#             number a
#             number a
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 444))

#     def test_445(self):
#         input = """
#             number a
#             func beounu(number a,string a)
#         """
#         expect = "Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input, expect, 445))

#     def test_446(self):
#         input = """
#             func beounu()
#             func beounu()
#         """
#         expect = "Redeclared Function: beounu"
#         self.assertTrue(TestChecker.test(input, expect, 446))

#     def test_447(self):
#         input = """
#             func beounu() return
#             func beounu() return
#         """
#         expect = "Redeclared Function: beounu"
#         self.assertTrue(TestChecker.test(input, expect, 447))

#     def test_448(self):
#         input = """
#             func beounu() return
#             func beounu() 
#         """
#         expect = "Redeclared Function: beounu"
#         self.assertTrue(TestChecker.test(input, expect, 448))

#     def test_449(self):
#         input = """
#             func beounu(number a,string b) 
#             func beounu(string a,number b) 
#         """
#         expect = "Redeclared Function: beounu"
#         self.assertTrue(TestChecker.test(input, expect, 449))

#     def test_450(self):
#         input = """
#             func beounu(number a,string b) 
#             func beounu(number a,string b) 
#         """
#         expect = "Redeclared Function: beounu"
#         self.assertTrue(TestChecker.test(input, expect, 450))

#     def test_451(self):
#         input = """
#             func beounu(number a,string b) 
#             func beounu(number a,string b) begin
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 451))

#     def test_452(self):
#         input = """
#             number a
#             func beounu(number a,string a)
#                 begin
#                     number a
#                 end
#         """
#         expect = "Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input, expect, 452))

#     def test_453(self):
#         input = """
#             number a
#             func beounu(number a,string b)
#                 begin
#                     c <- a
#                 end
#         """
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input, expect, 453))

#     def test_454(self):
#         input = """
#             number a
#             number b
#             var c <- d
#         """
#         expect = "Undeclared Identifier: d"
#         self.assertTrue(TestChecker.test(input, expect, 454))

#     def test_455(self):
#         input = """
#             number a
#             number b
#             func main() begin
#                 c <- d
#             end
#         """
#         expect = "Undeclared Identifier: c"
#         self.assertTrue(TestChecker.test(input, expect, 455))

#     def test_456(self):
#         input = """
#             number a
#             number b
#             func beounu(number a,string b) begin
#             end
#             func main() begin
#                 beounu1()
#             end
#         """
#         expect = "Undeclared Function: beounu1"
#         self.assertTrue(TestChecker.test(input, expect, 456))

#     def test_457(self):
#         input = """
#             number a[2,3]
#             number c
#             func beounu() begin
#                 c[1,2]<-5
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(c), [NumLit(1.0), NumLit(2.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 457))

#     def test_458(self):
#         input = """
#             number a[2,3]
#             number c
#             func beounu() begin
#                 c["1","2"]<-5
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(c), [StringLit(1), StringLit(2)])"
#         self.assertTrue(TestChecker.test(input, expect, 458))

#     def test_459(self):
#         input = """
#             number a[2,3]
#             number c
#             func beounu() begin
#                 a["1","2"]<-5
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1), StringLit(2)])"
#         self.assertTrue(TestChecker.test(input, expect, 459))

#     def test_460(self):
#         input = """
#             number a[2,3]
#             number c
#             func beounu() begin
#                 a[2,3]<-5
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 460))

#     def test_461(self):
#         input = """
#             number a[2,3]
#             number c
#             func beounu() begin
#                 a[2,3]<-"5"
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(2.0), NumLit(3.0)]), StringLit(5))"
#         self.assertTrue(TestChecker.test(input, expect, 461))

#     def test_462(self):
#         input = """
#             number a
#             string b
#             func beounu() begin
#                 number c <- a + b
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 462))

#     def test_463(self):
#         input = """
#             bool a
#             bool b
#             func beounu() begin
#                 number c <- a + b
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 463))

#     def test_464(self):
#         input = """
#             bool a
#             bool b
#             func beounu() begin
#                 number c <- -a
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: UnaryOp(-, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 464))

#     def test_465(self):
#         input = """
#             number a
#             bool b
#             func beounu() begin
#                 number c <- -a
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect,465))

#     def test_466(self):
#         input = """
#             number a
#             bool b
#             func beounu() begin
#                 number c <- -a
#             end
#             func beounu1() begin
#                 b <- beounu()
#             end
#             func main() return
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beounu), [])"
#         self.assertTrue(TestChecker.test(input, expect, 466))

#     def test_467(self):
#         input = """
#             number a
#             bool b
#             func beounu() begin
#                 number c <- -a
#                 return true
#             end
#             func beounu1() begin
#                 b <- beounu()
#             end
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 467))

#     def test_468(self):
#         input = """
#             number a
#             func beounu() return
#             func main() begin
#                 number b <- a
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 468))

#     def test_469(self):
#         input = """
#             dynamic a
#             func beounu() return
#             func main() begin
#                 var b <- a
#             end
#         """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 469))

#     def test_470(self):
#         input = """
#             var a<-5
#             func beounu() return
#             func main() begin
#                 var b <- a
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 470))

#     def test_471(self):
#         input = """
#             dynamic a
#             func beounu() return
#             func main() begin
#                 var b <- a and (a>b)
#             end
#         """
#         expect = "Type Mismatch In Expression: BinaryOp(>, Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 471))

#     def test_472(self):
#         input = """
#             dynamic a
#             func beounu() return
#             func main() begin
#                 var b <- a and true
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 472))

#     def test_473(self):
#         input = """
#             dynamic a
#             func beounu() return
#             func main() begin
#                 var y <- a+beounu(x)
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beounu), [Id(x)])"
#         self.assertTrue(TestChecker.test(input, expect, 473))

#     def test_474(self):
#         input = """
#             dynamic a
#             func beounu(number a) return
#             func main() begin
#                 var y <- a+beounu(x)
#             end
#         """
#         expect = "Undeclared Identifier: x"
#         self.assertTrue(TestChecker.test(input, expect, 474))

#     def test_475(self):
#         input = """
#             dynamic a
#             dynamic x
#             func beounu(number a) return
#             func main() begin
#                 var y <- a+beounu(x)
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beounu), [Id(x)])"
#         self.assertTrue(TestChecker.test(input, expect, 475))

#     def test_476(self):
#         input = """
#             dynamic a
#             dynamic x
#             func beounu(number a) return a
#             func main() begin
#                 var y <- a+beounu(x)
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 476))

#     def test_477(self):
#         input = """
#             dynamic a
#             dynamic x
#             func beounu(number a) return a
#             func main() begin
#                 beounu(x,y)
#             end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(beounu), [Id(x), Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 477))

#     def test_478(self):
#         input = """
#             dynamic a
#             dynamic x
#             dynamic y
#             func beounu(number a,string b) return 
#             func main() begin
#                 beounu(x,y)
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 478))

#     def test_479(self):
#         input = """
#             dynamic a
#             dynamic x
#             dynamic y
#             func beounu(number a,string b) return
#             func main() begin
#                 number a <- beounu(x,y)
#             end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(beounu), [Id(x), Id(y)])"
#         self.assertTrue(TestChecker.test(input, expect, 479))

#     def test_480(self):
#         input = """
#             dynamic a
#             dynamic b
#             func main() begin
#                 a <- b
#             end
#         """
#         expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
#         self.assertTrue(TestChecker.test(input, expect, 480))

#     def test_481(self):
#         input = """
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 481))

#     def test_482(self):
#         input = """
#             func main()
#             func main() begin
#                 number main
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 482))

#     def test_483(self):
#         input = """
#             func main(number a) begin
#             end
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 483))

#     def test_484(self):
#         input = """
#             func main() return 1   
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 484))

#     def test_485(self):
#         input = """
#             number emiu
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 485))

#     def test_486(self):
#         input = """
#             func babiboo(number a)
#             func babiboo(number a) return     

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 486))

#     def test_487(self):
#         input = """
#             func babiboo(number a) return   

#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 487))

#     def test_488(self):
#         input = """
#             func babiboo(number a) 

#             func main() return
#         """
#         expect = "No Function Definition: babiboo"
#         self.assertTrue(TestChecker.test(input, expect, 488))
        
#     def test_489(self):
#         input = """
#             number a
#             string a 
            
#             func main() return
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 489))

#     def test_490(self):
#         input = """
#             func a()
#             number a
            
#             func main() return
#         """
#         expect = "No Function Definition: a"
#         self.assertTrue(TestChecker.test(input, expect, 490))

#     def test_491(self):
#         input = """
#             func babiboo() return
#             func babiboo()
            
#             func main() return
#         """
#         expect = "Redeclared Function: babiboo"
#         self.assertTrue(TestChecker.test(input, expect, 491))

#     def test_492(self):
#         input = """
#             func babiboo()
#             func babiboo()
            
#             func main() return
#         """
#         expect = "Redeclared Function: babiboo"
#         self.assertTrue(TestChecker.test(input, expect, 492))

#     def test_493(self):
#         input = """
#             func babiboo() return
#             func babiboo() return
            
#             func main() return
#         """
#         expect = "Redeclared Function: babiboo"
#         self.assertTrue(TestChecker.test(input, expect, 493))

#     def test_494(self):
#         input = """
#             number babiboo
#             func babiboo() return
            
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 494))

#     def test_495(self):
#         input = """
#             number a
#             func emiu() return
#             func main()begin
#                 number a
#                 number c
#                 string emiu
#                 begin
#                     number c
#                     string emiu
#                 end
#             end
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 495))

#     def test_496(self):
#         input = """
#             number a
#             func emiu() return
#             func main()begin
#                 number a
#                 string a
#             end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 496))

#     def test_497(self):
#         input = """
#             number a
#             func emiu() return
#             func main()begin
#                 number a
#                 begin
#                     number a
#                 end
#                 string a
#             end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 497))

#     def test_498(self):
#         input = """
#             number a
#             func emiu() return
#             func main()begin
#                 number a
#                 begin
#                     number a
#                     string a
#                 end
                
#             end
#         """
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 498))

#     def test_499(self):
#         input = """
#             number a
#             func emiu(number a, number emiu, number c)
#             begin
#                 string c
#             end
            
#             func main() return
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 499))
        
#     def test_500(self):
#         input = """
#     number a
#     func bolero() return false
#     func bolero2(number c)
#     func main() begin
#         a <- bolero2(2)
#         a()
#     end
#     func bolero2(number c) begin
#         bool b <- bolero()
#         return c
#     end
#         """
#         expect = "Undeclared Function: a"
#         self.assertTrue(TestChecker.test(input, expect, 500))

################################# Quan (Moi update)
    def test1(self):
        input = """func test()
    func test() begin
    end
    func main() begin
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test2(self):
        input = """func test() begin
    end
    func test()
    func main() begin
    end
        """
        expect = "Redeclared Function: test"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test3(self):
        input = """func test()
    func main() begin
    end
    func test() begin
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test4(self):
        input = """func test()
    func main() begin
    end
    func test()
        """
        expect = "Redeclared Function: test"
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test5(self):
        input = """func test()
    func test() begin
    end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test6(self):
        input = """func test()
    func test() begin
    end
    func main(number a) begin
    end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test7(self):
        input = """func test(number a, string b)
    func test(number a, string b) begin
    end
    func main() begin
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test8(self):
        input = """func test(number a, string b)
    func test(number c, string d) begin
    end
    func main() begin
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test9(self):
        input = """func test(number a, string a)
    func test(number c, string d) begin
    end
    func main() begin
    end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test10(self):
        input = """
    func main() begin
        number a <- 1
        a <- "bruh"
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(bruh))"
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test11(self):
        input = """
    func main() begin
        number a <- 1
        number a <- 1
    end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test12(self):
        input = """
    func main() begin
        var a <- 1
        a <- 10.99
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test13(self):
        input = """
    func main() begin
        var a <- 1
        a <- true
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test14(self):
        input = """
    func main() begin
        dynamic a
        a <- 1000
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test15(self):
        input = """
    func main() begin
        dynamic a
        a <- 1000
        a <- "hello"
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test16(self):
        input = """
    dynamic a
    func main() begin
        a <- 1000
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    def test17(self):
        input = """
    func main() begin
        dynamic a
        var b <- a
    end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 416))
    
    def test18(self):
        input = """
    func main() begin
        dynamic a
        dynamic b
        b <- a
    end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(b), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test19(self):
        input = """
    func main() begin
        dynamic a
        dynamic b <- a
    end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, dynamic, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test20(self):
        input = """
    func main() begin
        number a <- a
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test21(self):
        input = """
    number a
    string b
    bool c
    func main() begin
        a <- 123
        b <- "hello"
        c <- true
        string a <- "another a"
        dynamic b <- a
        var c <- a
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test22(self):
        input = """
    number a
    string b
    bool c
    func main() begin
        a <- 123
        b <- "hello"
        c <- true
        string a <- "another a"
        dynamic b <- a
        var c <- a
        a <- 456
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(456.0))"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test23(self):
        input = """
    number a
    string b
    bool c
    func main() begin
        a <- 123
        b <- "hello"
        c <- true
        string a <- "another a"
        var c <- a
        b <- c
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test24(self):
        input = """
    func test() begin
    end
    func main() begin
        test()
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test25(self):
        input = """
    func test(number a, bool b) begin
    end
    func main() begin
        test(1, true)
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 424))
    
    def test26(self):
        input = """
    func test(number a, bool b) begin
    end
    func main() begin
        test("wrong", true)
    end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(test), [StringLit(wrong), BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test27(self):
        input = """
    func test(number a, bool b) return true
    func main() begin
        bool b <- test(1, true)
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test28(self):
        input = """
    func test(number a, bool b) return true
    func main() begin
        number b <- test(1, true)
    end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, None, CallExpr(Id(test), [NumLit(1.0), BooleanLit(True)]))"
        self.assertTrue(TestChecker.test(input, expect, 427))
        
    def test29(self):
        input = """
    func test(number a, bool b) return true
    func main() begin
        test(1, true)
    end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(test), [NumLit(1.0), BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test30(self):
        input = """
    func test(number a, bool b) return true
    func main() begin
        dynamic a
        bool b <- test(1, a)
        a <- true
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test31(self):
        input = """
    func test(number a, bool b) return true
    func main() begin
        dynamic a
        bool b <- test(1, a)
        a <- 123
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), NumLit(123.0))"
        self.assertTrue(TestChecker.test(input, expect, 430))
        
    def test32(self):
        input = """
    func test(number a, bool b) return true
    func main() begin
        bool b <- test(1, test(2, false))
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test33(self):
        input = """
    func test(number a, bool b)
    func main() begin
        bool b <- test(1, test(2, false))
    end
        """
        expect = "No Function Definition: test"
        self.assertTrue(TestChecker.test(input, expect, 432))
        
    def test34(self):
        input = """
    func test(number a, bool b)
    func main() begin
        string b <- test(1, test(2, false))
    end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), StringType, None, CallExpr(Id(test), [NumLit(1.0), CallExpr(Id(test), [NumLit(2.0), BooleanLit(False)])]))"
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test35(self):
        input = """
    func test(number a, bool b)
    func main() begin
        bool b <- test(1, test(2, false))
    end
    func test(number c, bool d) return 1.23
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.23))"
        self.assertTrue(TestChecker.test(input, expect, 434))
        
    def test36(self):
        input = """
    func test(number a, bool b)
    func main() begin
        bool b <- test(1, test(2, false))
    end
    func test(number c, bool d) return true
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test37(self):
        input = """
    func test(number a, bool b)
    func main() begin
        test(1, true)
    end
    func test(number a, bool b) begin
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test38(self):
        input = """
    func test(number a, bool b)
    func main() begin
        test(1, true)
    end
    func test(number a, bool b) return 1
        """
        expect = "Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 437))
        
    def test39(self):
        input = """
    func main() begin
        var a <- a
    end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 438))
        
    def test40(self):
        input = """
    number a <- 1
    func main() begin
        var a <- a
    end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 439))
        
    def test41(self):
        input = """
    number a <- 1
    func main() begin
        number a <- a
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test42(self):
        input = """
    func main() begin
        writeNumber(1)
        writeString("hello")
        writeBool(true)
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test43(self):
        input = """
    func main() begin
        writeNumber()
    end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(writeNumber), [])"
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test44(self):
        input = """
    func writeNumber(number a)
    func main() begin
        writeNumber(1)
    end
        """
        expect = "Redeclared Function: writeNumber"
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test45(self):
        input = """
    func main() begin
        string s <- readString()
        number n <- readNumber()
        bool b <- readBool()
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test46(self):
        input = """
    func main() begin
        string s <- readString()
        number n <- readNumber()
        readBool()
    end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(readBool), [])"
        self.assertTrue(TestChecker.test(input, expect, 445))
        
    def test47(self):
        input = """
    func readString() return "hello"
    func main() begin
        string s <- readString()
        number n <- readNumber()
        bool b <- readBool()
    end
        """
        expect = "Redeclared Function: readString"
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test48(self):
        input = """
    func main() begin
        number a <- writeNumber(1)
    end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(writeNumber), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test49(self):
        input = """
    func main() begin
        string s <- readString(1)
        number n <- readNumber()
        bool b <- readBool()
    end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(readString), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test50(self):
        input = """
    number a
    func main() begin
        string a <- readString()
    end
    func test() begin
        a <- 1
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test51(self):
        input = """
    number a
    func main() begin
        string a <- readString()
    end
    func test() begin
        a <- "Hello, World!"
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(Hello, World!))"
        self.assertTrue(TestChecker.test(input, expect, 450))
        
    def test52(self):
        input = """
    func test() begin
        return 1
        return "true"
    end
    func main() begin
        number a <- test()
    end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(true))"
        self.assertTrue(TestChecker.test(input, expect, 451))
        
    def test53(self):
        input = """
    func test() begin
        return 1
        return 3.14
    end
    func main() begin
        number a <- test()
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test54(self):
        input = """
    number a
    func test() return false
    func test2(number c)
    func main() begin
        a <- test2(2)
    end
    func test2(number c) begin
        bool b <- test()
        return c
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test55(self):
        input = """
    number a
    func test() return false
    func test2(number c)
    func main() begin
        a <- test2(2)
    end
    func test2(number c) begin
        bool b <- test()
        return b
    end
        """
        expect = "Type Mismatch In Statement: Return(Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test56(self):
        input = """
    number a
    func test() return false
    func test2(number c)
    func main() begin
        a <- test2(2)
        c <- a
    end
    func test2(number c) begin
        bool b <- test()
        return c
    end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test57(self):
        input = """
    number a
    func test() return false
    func test2(number c)
    func main() begin
        a <- test2(2)
        a()
    end
    func test2(number c) begin
        bool b <- test()
        return c
    end
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test58(self):
        input = """
    number a
    func test(number b) return false
    func test2(number c)
    func main() begin
        a <- test2(2)
        a <- b
    end
    func test2(number c) begin
        bool b <- test()
        return c
    end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 457))
        
    def test59(self):
        input = """
    dynamic a
    func getA(number x)
    func test2(number c)
    func main() begin
        dynamic x
        test2(getA(x))
    end
    func getA(number x) return a
    func test2(number c) begin
        writeNumber(c)
        return
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test60(self):
        input = """
    dynamic a
    func getA(number x)
    func test2(number c)
    func test3()
    func main() begin
        dynamic x
        test2(getA(x))
    end
    func getA(number x) return test3()
    func test2(number c) begin
        writeNumber(c)
        return
    end
    func test3() return 3.14
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 459))
        
    def test61(self):
        input = """
    dynamic a
    func getA(number x)
    func test2(number c)
    func test3()
    func main() begin
        dynamic x
        test2(getA(x))
    end
    func getA(number x) return test3()
    func test2(number c) begin
        writeNumber(c)
        return
    end
    func test3() return false
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 460))
        
    def test62(self):
        input = """
    func main() begin
        number a
        bool b <- true
        if (b)
            a <- 1
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 461))
        
    def test63(self):
        input = """
    func main() begin
        number a
        bool b <- true
        if (a)
            a <- 1
        else
            a <- 2
    end
        """
        expect = "Type Mismatch In Statement: If((Id(a), AssignStmt(Id(a), NumLit(1.0))), [], AssignStmt(Id(a), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test64(self):
        input = """
    func main() begin
        number a
        bool b <- true
        bool c <- false
        if (b) begin
            string a <- "hello"
        end
        elif (b) begin
            a <- 1
        end
        else
            a <- 2
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 463))
        
    def test65(self):
        input = """
    func main() begin
        number a
        bool b <- true
        if (b) begin
            string a <- "hello"
        end
        else begin
            a <- "error"
        end
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), StringLit(error))"
        self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test66(self):
        input = """
    func main() begin
        number a
        bool b <- true
        dynamic c
        dynamic d
        if (c) begin
            string a <- "hello"
            c <- false
        end
        elif (d) d <- false
        c <- d
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 465))
        
    def test67(self):
        input = """
    func main() begin
        bool a <- true
        bool b <- false
        if (a and b) begin
            a <- false
        end
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 466))
        
    def test68(self):
        input = """
    func main() begin
        bool a <- true
        bool b <- false
        number c
        if (a or b) begin
            c <- 1 + 2 / 3
        end
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))
        
    def test69(self):
        input = """
    func main() begin
        bool a <- true
        bool b <- false
        number c
        dynamic d
        if (c = d) begin
            d <- 1
        end
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))
        
    def test70(self):
        input = """
    func main() begin
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        if ((a = b) and (a < b) or (a > b) or (a <=b) or (a >= b) or (a != b)) begin
            b <- a
            a <- b
        end
        elif ((c and d) or (c or d)) c <- d
        elif ((e..."zcode") == f) f <- "sucks"
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test71(self):
        input = """
    number a <- 10
    bool b <- true
    func test(number e) begin
        return e + 1
    end
    func main() begin
        number c <- test(a)
        if ((c > a) and b) return
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))
        
    def test72(self):
        input = """
    number a <- 10
    dynamic b
    func main() begin
        number i
        for i until b by 1 begin
            writeNumber(i)
            if (i > 5) break
        end
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    def test73(self):
        input = """
    bool a <- true
    var b <- a or b
    func main() begin
        number i
        for i until b by 1 begin
            writeNumber(i)
            if (i > 5) continue
        end
        break
    end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 472))
        
    def test74(self):
        input = """
    bool a <- true
    var b <- a or b
    func main() begin
        number i
        for i until b by 1 begin
            var j <- i
            for j until a by j + 1
            begin
                if (j > 5) continue
            end
            if (i > 5) break
        end
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 473))
        
    def test75(self):
        input = """
    number a[1, 2]
    func main() begin
        a[1, 1] <- 1
        a[2, 1] <- 2
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 474))
        
    def test76(self):
        input = """
    number a[1, 2]
    func main() begin
        number a
        a[1] <- 1
    end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test77(self):
        input = """
    number a[1, 2]
    func main() begin
        a[1 + 1, 0] <- 1
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))
        
    def test78(self):
        input = """
    number a[1, 2]
    func main() begin
        dynamic b
        a[1 + 1, b] <- 1
        b <- false
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
    def test79(self):
        input = """
    func main() begin
        bool a[2, 3] <- [[true, true, true], [false, false, false]]
        a[1] <- [true, true, false]
        a[1] <- true
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 478))
        
    def test80(self):
        input = """
    func main() begin
        number a[5] <- [1,2,3,4,5,6]
    end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0)))"
        self.assertTrue(TestChecker.test(input, expect, 479))
    
    def test81(self):
        input = """
    func main() begin
        number a[5] <- [1,true,3,4,5]
    end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), BooleanLit(True), NumLit(3.0), NumLit(4.0), NumLit(5.0))"
        self.assertTrue(TestChecker.test(input, expect, 480))
        
    def test82(self):
        input = """
    func main() begin
        dynamic a
        number b[5] <- [1, 2, 3, a, 5]
        a <- false
        
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 481))
        
    def test83(self):
        input = """
    func main() begin
        dynamic a
        number b[2, 5] <- [[1, 2, 3, 4, 5], a]
        a <- [1, 2, 3, 4, 5]
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))
        
    def test84(self):
        input = """
    func main() begin
        dynamic a
        number b[2, 5] <- [[1, 2, 3, 4, 5], a]
        a <- [1, 2, 3, 4]
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 483))
        
    def test85(self):
        input = """
    func main() begin
        dynamic a
        number b[2, 4] <- [[1, 2, 3, 4]]
    end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([2.0, 4.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))))"
        self.assertTrue(TestChecker.test(input, expect, 484))
        
    def test86(self):
        input = """
    func main() begin
        dynamic a
        number b[2, 4] <- [[1, 2, 3, 4, 5], [1, 2, 3, 4]]
    end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)))"
        self.assertTrue(TestChecker.test(input, expect, 485))
        
    def test87(self):
        input = """
    func main() begin
        number a
        if (true) number a
    end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 486))
    
    def test88(self):
        input = """
    func main() begin
        dynamic a
        number b[2, 5] <- [[1, 2, 3, 4, 5], a]
        b[1] <- [1, 2, 3, 4, 5, 6]
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(b), [NumLit(1.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0), NumLit(6.0)))"
        self.assertTrue(TestChecker.test(input, expect, 487))
        
    def test89(self):
        input = """
    func main() begin
        dynamic a
        number b[3, 3, 3] <- [[[1,2,3],[4,5,6],[7,8,9]] , [[1,2,3],[4,5,6],[7,8,9]] , [[1,2,3],[4,5,6],[7,8,9]]]
        
        var c <- b[1]
        c <- [[1,2,3],[4,5,6],[7,8,9]]
        
        var d <- b[1, 2]
        d <- [41, 51, 61]
        
        number e <- b[1,2,3]
        e <- 3.14
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    def test90(self):
        input = """
    func main() begin
        dynamic a
        number b[3, 3, 3] <- [[[1,2,3],[4,5,6],[7,8,9]] , [[1,2,3],[4,5,6],[7,8,9]] , [[1,2,3],[4,5,6],[7,8,9]]]
        
        var c <- b[1]
        c <- [[1,2,3],[4,5,6],[7,8,9]]
        
        number d <- b[1, 2]
    end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(d), NumberType, None, ArrayCell(Id(b), [NumLit(1.0), NumLit(2.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 489))
        
    def test91(self):
        input = """
    func main() begin
        dynamic a
        dynamic b
        a <- [b, 2, 3]
        b <- 3.14
        a <- [6,7,8]
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 490))
        
    def test92(self):
        input = """
    func main() begin
        dynamic a <- [a, 2, 3]
    end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), None, dynamic, ArrayLit(Id(a), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 491))
        
    def test93(self):
        input = """
    func main() begin
        dynamic x
        x[1, 2] <- [1,2,3]
    end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(ArrayCell(Id(x), [NumLit(1.0), NumLit(2.0)]), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 492))
        
    def test94(self):
        input = """
    func main() begin
        dynamic x
        number a[2,2] <- [[x,1], [4,4]]
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 493))
        
    def test95(self):
        input = """
    func main() begin
        dynamic x
        dynamic y
        number a[2,2] <- [[x,x], [4,4]]
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))
        
    def test96(self):
        input = """
    func main() begin
        dynamic x
        dynamic y
        number a[2,2] <- [[x,x], [y,4]]
        y <- 3.14
        x <- 10
        x <- true
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 495))
        
    def test97(self):
        input = """
    func main() begin
        dynamic x
        dynamic y
        number a[2,2] <- [[x,x], [y,4]]
        y <- 3.14
        x <- 10
        x <- true
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 496))
        
    def test97(self):
        input = """
    func main() begin
        dynamic x
        dynamic y
        var a <- [[x,x], [y,4]]
        y <- 3.14
        x <- 10
        x <- true
    end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 496))
        
    def test98(self):
        input = """
    func main() begin
        dynamic x
        dynamic y
        var a <- [[x,x], [y,y]]
    end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, ArrayLit(ArrayLit(Id(x), Id(x)), ArrayLit(Id(y), Id(y))))"
        self.assertTrue(TestChecker.test(input, expect, 497))
        
    def test99(self):
        input = """
    func foo()
    func main() begin
        dynamic x
        number a[2,2] <- [[foo(),x], [4,4]]
        x <- 1000
        number c <- x + foo()
    end
            
    func foo() return 123
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 498))
        
    def test100(self):
        input = """
    string a <- "final"
    func supercomplextest123(number a, bool b, string c)
    func main() begin
        var a <- 1
        dynamic b <- a
        number m
        dynamic n
        var c <- [[123, 456], [m, n]]
        dynamic q <- c[1,1]
        n <- 101112
        dynamic s
        for a until b < c[0, 1] by m begin
            if (a >= b / 20 + 1) begin
                number c <- b
                for c until a * 20 < q by c * supercomplextest123(c, s == "uper", s) begin
                    writeNumber(c)
                    continue
                end
            end
            elif (b != a) continue
            else begin
                c[1] <- [a, b]
                return
            end
        end
    end
    func supercomplextest123(number e, bool f, string g)
    begin
        writeString(a)
        if (((a..."test") == "finaltest") and not f) return 1
        return e
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
        
    def test101(self):
        input = """
    func foo(number a[3, 4])
    func main() begin
        dynamic a
        number b <- foo(a)
        a <- [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    end
            
    func foo(number a[3, 4]) return 123
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 500))
        
    def test102(self):
        input = """
    func foo(number a[3, 4])
    func main() begin
        dynamic a
        foo(a)
        a <- [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    end
            
    func foo(number a[3, 4]) return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 501))
        
    def test103(self):
        input = """
    func foo(number a[3, 4]) begin
        dynamic gg
        if (a[1,1] > 0) return a[1]
        elif (a[1, 1] = 0) return gg
        else begin
            gg <- [1, 2, 3, 4]
            return gg
        end
    end
    func main() begin
        dynamic a
        var b <- foo(a)
        b <- a[3]
    end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 502))
    
    def test104(self):
        input = """
    func foo(number a[3, 4])
    func main() begin
        dynamic a
        foo(a)
        a <- [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    end
            
    func foo(number a[3, 5]) return
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 503))
    def test_424(self):
        input = """
dynamic b
dynamic c
dynamic d
func main()
begin
    number a[3] <- [b,c,d]
    number f <- d
end
        """
        expect = ""
        # infer b c d to number
        self.assertTrue(TestChecker.test(input, expect, 424))
    def test_1(self):
        input = """
        dynamic x
        number a[2,2] <- [x,[x,x]]
        func main() return
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(x), ArrayLit(Id(x), Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 504))
    def test_uninfer_or_mismatch_13(self):
        input = """
            func main()
            begin
                number a[2,3] <- [[1,2,3],[4,5,6]]
                a <- [[1,2,3,4],[4,5,6]]
            end

        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(4.0), NumLit(5.0), NumLit(6.0)))"
        self.assertTrue(TestChecker.test(input, expect, 523))
    def testsomething(self):
        input = """
        func trong(number a[1])
                        return a[1]
                    var abc <- false > "1" + 2
                    """
        expect = "Type Mismatch In Expression: BinaryOp(>, BooleanLit(False), BinaryOp(+, StringLit(1), NumLit(2.0)))"
        self.assertTrue(TestChecker.test(input, expect, 1910))
        
        
######################################################


class CheckerSuite(unittest.TestCase):
##############---------- PHAN THANH THONG - 2153846 ----------##############
    def test_400(self):
        input = """dynamic a
number b[3] <- [true,2,a]
func main()
begin
end
        """
        expect = "Type Mismatch In Expression: ArrayLit(BooleanLit(True), NumLit(2.0), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_401(self):
        # a and d should be inferred by BoolType?
        input = """dynamic a
dynamic d
number b[3] <- [a,true,d]
func main()
begin
end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([3.0], NumberType), None, ArrayLit(Id(a), BooleanLit(True), Id(d)))"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_402(self):
        input = """dynamic a
func beou(number b, string c)
    begin
        beou(a,a)    
    end
func main()
    begin
    end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(beou), [Id(a), Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_403(self):
        input = """
func beou()
func beou()
    begin
        return
    end
func beou() return
func main()
    begin
    end
        """
        expect = """Redeclared Function: beou"""
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test_404(self):
        input = """dynamic a
dynamic d
number b[3] <- [a,1,2,d]
func main()
begin
end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([3.0], NumberType), None, ArrayLit(Id(a), NumLit(1.0), NumLit(2.0), Id(d)))"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_405(self):
        input = """dynamic a
dynamic d
number b[7,7,7] <- [[a,d],[a,d],[a,d]]
func main()
begin
end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), ArrayType([7.0, 7.0, 7.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(d)), ArrayLit(Id(a), Id(d)), ArrayLit(Id(a), Id(d))))"
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test_406(self):
        input = """dynamic a
dynamic d
number b[3] <- [a,a,d]
bool c <- a
func main()
begin
end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(c), BoolType, None, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test_407(self):
        input = """number a
bool d
number b[3] <- [a,a,d]
bool c <- a
func main()
begin
end
        """
        expect = "Type Mismatch In Expression: ArrayLit(Id(a), Id(a), Id(d))"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_408(self):
        input = """
func beou()
func main()
func main()
begin
    beou()
end
        """
        expect = "No Function Definition: beou"
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_409(self):
        input = """
func beou(number a, bool b, string c) return
func main()
begin
    number a
    bool b
    a <- beou(a, b)
end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(a), Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test_410(self):
        input = """
func beou(number a, bool b, string c)
func main()
begin
    number a
    bool b
    a <- beou(a, b, c)
end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_411(self):
        input = """
func beou(number a, bool b, string c) return a
func main()
begin
    dynamic a
    bool b
    dynamic c
    a <- beou(a, c, b)
end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(a), Id(c), Id(b)])"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test_412(self):
        input = """
func beou(number a[3], bool b, string c) return a
func main()
begin
    number a[4]
    bool b
    dynamic c
    a <- beou(a, b, c)
end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(beou), [Id(a), Id(b), Id(c)]))"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test_413(self):
        input = """
func beou(number a[3], bool b, string c) return 3
func main()
begin
    bool a[3]
    bool b
    dynamic c
    a <- beou(a, b, c)
end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(beou), [Id(a), Id(b), Id(c)]))"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test_414(self):
        input = """
func beou(number a[3], bool b, string c) return
func main()
begin
    number a[3]
    bool b
    dynamic c
    a <- beou(a, b, c)
end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(a), Id(b), Id(c)])"
        # beou has VoidType, i dont compare type at stmt, but make condition at CallExpr
        # from spec: For a function call <function-name>(<args>), the callee <method name> must have
        # non-void as return type
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test_415(self):
        input = """
func beou(number a[3], bool b, string c) return [a[1], a[2], a[3], a[4]]
func main()
begin
    number a[3]
    bool b
    dynamic c
    a <- beou(a, b, c)
end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(beou), [Id(a), Id(b), Id(c)]))"
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    def test_416(self):
        input = """
dynamic beou
func beou(number a[3], bool b, string c) return b
func main()
begin
    beou <- beou(beou, beou, beou)
end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(beou), Id(beou), Id(beou)])"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_417(self):
        input = """
dynamic beou
func beou(number a[3], bool b)
func beou(string c) return c
func main()
begin
    number a[3]
    bool b
    beou <- beou(a, b)
    beou(a,b)
end
        """
        expect = "Redeclared Function: beou"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_418(self):
        input = """
func beou(number a[3], bool b, string c)
func beou(string c) return b
func main()
begin
    beou <- beou(beou)
end
        """
        expect = "Redeclared Function: beou"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_419(self):
        input = """
dynamic a
func beou (number b) return a
func main()
begin
    beou <- beou(beou)
end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_420(self):
        input = """
number a[3] <- [7,7,7]
func beou (number b)
    begin
        a[1] <- b + a[2]
        return a
    end
func main()
begin
    dynamic c
    c <- a[c] + a[1,2]
    bool d
    c <- d
end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0)])"
        #if we check size of array
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_421(self):
        input = """
number a[3] <- [7,7,7]
func beou (number b)
    begin
        a[1] <- b + a[2]
        dynamic c
        c <- a[c] + beou(a[1])[1]
        return a
    end
func main()
begin
end
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(beou), [ArrayCell(Id(a), [NumLit(1.0)])]), [NumLit(1.0)])"
        # how to infer?
        # or raise error (we check if ctx.arr in ArrayCell has ArrayType)
        self.assertTrue(TestChecker.test(input, expect, 421))
        
    def test_422(self):
        input = """
dynamic a
func beou (number b)
    begin
        a[1] <- 1
        return a[1,2]
    end
func main()
begin
end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0)])"
        # how to infer?
        # or raise error (we check if ctx.arr in ArrayCell has ArrayType)
        # The implicit keyword cannot be used for array type. (in spec)
        self.assertTrue(TestChecker.test(input, expect, 422))
        
    def test_423(self):
        input = """
var a <- 3
func beou (number b)
    return a
func main()
begin
    beou(a)
end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(beou), [Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 423))
        
    def test_424(self):
        input = """
dynamic b
dynamic c
dynamic d
func main()
begin
    number a[3] <- [b,c,d]
    bool f <- d
end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(f), BoolType, None, Id(d))"
        # infer b c d to number
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test_426(self):
        input = """
        func boo()
        func main() begin
            boo()
        end
        """
        expect = "No Function Definition: boo"
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    def test_427(self):
        input = """
        func beou() begin
            return 1
        end
        func main() begin
            beou()
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(beou), [])"
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_428(self):
        input = """
        func main() begin
            
            dynamic b
            dynamic a 
            number x[1, 2] <- [[1,b]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test_429(self):
        input = """
        func main() begin
            
            dynamic b
            dynamic a <- [b]
            number x[1, 2] <- [[1,b]]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, ArrayLit(Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test_430(self):
        input = """
        func main() begin
            number x[1, 2] <- [[1,2]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_431(self):
        input = """
        func main() begin
        dynamic b
            number x[2, 2] <- [[1,2], [b, b]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test_432(self):
        input = """
        func main() begin
        end
        func beou(number x)
        func beou(number x, number y) begin
        end
        """
        expect = "Redeclared Function: beou"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_433(self):
        input = """
        func main() begin
        number a <- a
        end
        func beou(number x, number y)
        func beou(number z, number x) begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_434(self):
        input = """
        func main() begin
        end
        func beou(number x, number x) begin
        end
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
func main()
begin
    var x <- [[[[1, 6]], [3, 4, 8]], [[2, 4, 1], [9, 40, 11]]]

end
"""
        myret_ = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(6.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(8.0)))"
        self.assertTrue(TestChecker.test(input, myret_, 435))
    def test_436(self):
        input = """
func main()
begin
    number a[2, 2] <- [[6, 8], [6, 8]]
    number b[2] <- a[0]
    writeNumber(b[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 436))
    def test_437(self):
        input = """
        func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    number x[3,3] <- [a,b]
    a <- [7,7,7]
    b <- [8,8,8]
    c <- [9,9,9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([3.0, 3.0], NumberType), None, ArrayLit(Id(a), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_438(self):
        input = """
func beou(number a[3,3]) return 1
        func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    number x <- beou([a,b,c])
    a <- [7,7,7]
    b <- [8,8,8]
    c <- [9,9,9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_439(self):
        input = """
        func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    dynamic d <- [a,b,c]
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(d), None, dynamic, ArrayLit(Id(a), Id(b), Id(c)))"
        self.assertTrue(TestChecker.test(input, expect, 439))
    def test_440(self):
        input = """
            dynamic a
            dynamic x
            dynamic y
            func beou(number a,string b) return
            func main() begin
                number a <- beou(x,y)
                number x
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beou), [Id(x), Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 440))
    
    def test_441(self):
        input = """
        func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    number x[3,3]
    x <- [a,b,c]
    a <- [7,7,7]
    b <- [8,8,8]
    c <- [9,9,9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test_442(self):
        input = """
func beou(number a[3,3]) return
        func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    beou([a,b,c])
    a <- [7,7,7]
    b <- [8,8,8]
    c <- [9,9,9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))
        
    def test_443(self):
        input = """
func beou()
func main()
    begin
        number x[3,3] <- beou()
    end
dynamic a
dynamic b
dynamic c
func beou() return [a,b,c]
func beou1() begin
    a <- [7,7,7]
    b <- [8,8,8]
    c <- [9,9,9]
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        input = """
            number a
            number a
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        input = """
            number a
            func beounu(number a,string a)
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        input = """
            func beounu()
            func beounu()
        """
        expect = "Redeclared Function: beounu"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        input = """
            func beounu() return
            func beounu() return
        """
        expect = "Redeclared Function: beounu"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        input = """
            func beounu() return
            func beounu() 
        """
        expect = "Redeclared Function: beounu"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
            func beounu(number a,string b) 
            func beounu(string a,number b) 
        """
        expect = "Redeclared Function: beounu"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
            func beounu(number a,string b) 
            func beounu(number a,string b) 
        """
        expect = "Redeclared Function: beounu"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
            func beounu(number a,string b) 
            func beounu(number a,string b) begin
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
            number a
            func beounu(number a,string a)
                begin
                    number a
                end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """
            number a
            func beounu(number a,string b)
                begin
                    c <- a
                end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        input = """
            number a
            number b
            var c <- d
        """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        input = """
            number a
            number b
            func main() begin
                c <- d
            end
        """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        input = """
            number a
            number b
            func beounu(number a,string b) begin
            end
            func main() begin
                beounu1()
            end
        """
        expect = "Undeclared Function: beounu1"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """
            number a[2,3]
            number c
            func beounu() begin
                c[1,2]<-5
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        input = """
            number a[2,3]
            number c
            func beounu() begin
                c["1","2"]<-5
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(c), [StringLit(1), StringLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        input = """
            number a[2,3]
            number c
            func beounu() begin
                a["1","2"]<-5
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(1), StringLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        input = """
            number a[2,3]
            number c
            func beounu() begin
                a[2,3]<-5
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        input = """
            number a[2,3]
            number c
            func beounu() begin
                a[2,3]<-"5"
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(2.0), NumLit(3.0)]), StringLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        input = """
            number a
            string b
            func beounu() begin
                number c <- a + b
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        input = """
            bool a
            bool b
            func beounu() begin
                number c <- a + b
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        input = """
            bool a
            bool b
            func beounu() begin
                number c <- -a
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: UnaryOp(-, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        input = """
            number a
            bool b
            func beounu() begin
                number c <- -a
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect,465))

    def test_466(self):
        input = """
            number a
            bool b
            func beounu() begin
                number c <- -a
            end
            func beounu1() begin
                b <- beounu()
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beounu), [])"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        input = """
            number a
            bool b
            func beounu() begin
                number c <- -a
                return true
            end
            func beounu1() begin
                b <- beounu()
            end
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        input = """
            number a
            func beounu() return
            func main() begin
                number b <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        input = """
            dynamic a
            func beounu() return
            func main() begin
                var b <- a
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        input = """
            var a<-5
            func beounu() return
            func main() begin
                var b <- a
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        input = """
            dynamic a
            func beounu() return
            func main() begin
                var b <- a and (a>b)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(>, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """
            dynamic a
            func beounu() return
            func main() begin
                var b <- a and true
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        input = """
            dynamic a
            func beounu() return
            func main() begin
                var y <- a+beounu(x)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beounu), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        input = """
            dynamic a
            func beounu(number a) return
            func main() begin
                var y <- a+beounu(x)
            end
        """
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        input = """
            dynamic a
            dynamic x
            func beounu(number a) return
            func main() begin
                var y <- a+beounu(x)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beounu), [Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        input = """
            dynamic a
            dynamic x
            func beounu(number a) return a
            func main() begin
                var y <- a+beounu(x)
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """
            dynamic a
            dynamic x
            func beounu(number a) return a
            func main() begin
                beounu(x,y)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(beounu), [Id(x), Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = """
            dynamic a
            dynamic x
            dynamic y
            func beounu(number a,string b) return 
            func main() begin
                beounu(x,y)
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
            dynamic a
            dynamic x
            dynamic y
            func beounu(number a,string b) return
            func main() begin
                number a <- beounu(x,y)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(beounu), [Id(x), Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
            dynamic a
            dynamic b
            func main() begin
                a <- b
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = """
            func main()
            func main() begin
                number main
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = """
            func main(number a) begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """
            func main() return 1   
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """
            number emiu
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """
            func babiboo(number a)
            func babiboo(number a) return     

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """
            func babiboo(number a) return   

            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = """
            func babiboo(number a) 

            func main() return
        """
        expect = "No Function Definition: babiboo"
        self.assertTrue(TestChecker.test(input, expect, 488))
        
    def test_489(self):
        input = """
            number a
            string a 
            
            func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """
            func a()
            number a
            
            func main() return
        """
        expect = "No Function Definition: a"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
            func babiboo() return
            func babiboo()
            
            func main() return
        """
        expect = "Redeclared Function: babiboo"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """
            func babiboo()
            func babiboo()
            
            func main() return
        """
        expect = "Redeclared Function: babiboo"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_493(self):
        input = """
            func babiboo() return
            func babiboo() return
            
            func main() return
        """
        expect = "Redeclared Function: babiboo"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
            number babiboo
            func babiboo() return
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
            number a
            func emiu() return
            func main()begin
                number a
                number c
                string emiu
                begin
                    number c
                    string emiu
                end
            end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
            number a
            func emiu() return
            func main()begin
                number a
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """
            number a
            func emiu() return
            func main()begin
                number a
                begin
                    number a
                end
                string a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
            number a
            func emiu() return
            func main()begin
                number a
                begin
                    number a
                    string a
                end
                
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
            number a
            func emiu(number a, number emiu, number c)
            begin
                string c
            end
            
            func main() return
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))
        
    def test_500(self):
        input = """
    number a
    func bolero() return false
    func bolero2(number c)
    func main() begin
        a <- bolero2(2)
        a()
    end
    func bolero2(number c) begin
        bool b <- bolero()
        return c
    end
        """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 500))