import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
############## THONG
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
# func foo(number b, string c)
#     begin
#         foo(a,a)    
#     end
# func main()
#     begin
#     end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(a), Id(a)])"
#         self.assertTrue(TestChecker.test(input, expect, 402))
        
#     def test_403(self):
#         input = """
# func foo()
# func foo()
#     begin
#         return
#     end
# func foo() return
# func main()
#     begin
#     end
#         """
#         expect = """Redeclared Function: foo"""
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
# number b[1,2,3] <- [[a,d],[a,d],[a,d]]
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(b), ArrayType([1.0, 2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(d)), ArrayLit(Id(a), Id(d)), ArrayLit(Id(a), Id(d))))"
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
# func foo()
# func main()
# func main()
# begin
#     foo()
# end
#         """
#         expect = "No Function Definition: foo"
#         self.assertTrue(TestChecker.test(input, expect, 408))
        
#     def test_409(self):
#         input = """
# func foo(number a, bool b, string c) return
# func main()
# begin
#     number a
#     bool b
#     a <- foo(a, b)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(a), Id(b)])"
#         self.assertTrue(TestChecker.test(input, expect, 409))
        
#     def test_410(self):
#         input = """
# func foo(number a, bool b, string c)
# func main()
# begin
#     number a
#     bool b
#     a <- foo(a, b, c)
# end
#         """
#         expect = "No Function Definition: foo"
#         self.assertTrue(TestChecker.test(input, expect, 410))
        
#     def test_411(self):
#         input = """
# func foo(number a, bool b, string c) return a
# func main()
# begin
#     dynamic a
#     bool b
#     dynamic c
#     a <- foo(a, c, b)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(a), Id(c), Id(b)])"
#         self.assertTrue(TestChecker.test(input, expect, 411))
        
#     def test_412(self):
#         input = """
# func foo(number a[3], bool b, string c) return a
# func main()
# begin
#     number a[4]
#     bool b
#     dynamic c
#     a <- foo(a, b, c)
# end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(foo), [Id(a), Id(b), Id(c)]))"
#         self.assertTrue(TestChecker.test(input, expect, 412))
        
#     def test_413(self):
#         input = """
# func foo(number a[3], bool b, string c) return 3
# func main()
# begin
#     bool a[3]
#     bool b
#     dynamic c
#     a <- foo(a, b, c)
# end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(foo), [Id(a), Id(b), Id(c)]))"
#         self.assertTrue(TestChecker.test(input, expect, 413))
        
#     def test_414(self):
#         input = """
# func foo(number a[3], bool b, string c) return
# func main()
# begin
#     number a[3]
#     bool b
#     dynamic c
#     a <- foo(a, b, c)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(a), Id(b), Id(c)])"
#         # foo has VoidType, i dont compare type at stmt, but make condition at CallExpr
#         # from spec: For a function call <function-name>(<args>), the callee <method name> must have
#         # non-void as return type
#         self.assertTrue(TestChecker.test(input, expect, 414))
        
#     def test_415(self):
#         input = """
# func foo(number a[3], bool b, string c) return [a[1], a[2], a[3], a[4]]
# func main()
# begin
#     number a[3]
#     bool b
#     dynamic c
#     a <- foo(a, b, c)
# end
#         """
#         expect = "Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(foo), [Id(a), Id(b), Id(c)]))"
#         self.assertTrue(TestChecker.test(input, expect, 415))
        
#     def test_416(self):
#         input = """
# dynamic foo
# func foo(number a[3], bool b, string c) return b
# func main()
# begin
#     foo <- foo(foo, foo, foo)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(foo), Id(foo), Id(foo)])"
#         self.assertTrue(TestChecker.test(input, expect, 416))
        
#     def test_417(self):
#         input = """
# dynamic foo
# func foo(number a[3], bool b)
# func foo(string c) return c
# func main()
# begin
#     number a[3]
#     bool b
#     foo <- foo(a, b)
#     foo(a,b)
# end
#         """
#         expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(a), Id(b)])"
#         self.assertTrue(TestChecker.test(input, expect, 417))
    
#     def test_418(self):
#         input = """
# func foo(number a[3], bool b, string c)
# func foo(string c) return b
# func main()
# begin
#     foo <- foo(foo)
# end
#         """
#         expect = "Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input, expect, 418))
        
#     def test_419(self):
#         input = """
# dynamic a
# func foo (number b) return a
# func main()
# begin
#     foo <- foo(foo)
# end
#         """
#         expect = "Type Cannot Be Inferred: Return(Id(a))"
#         self.assertTrue(TestChecker.test(input, expect, 419))
        
#     def test_420(self):
#         input = """
# number a[3] <- [1,2,3]
# func foo (number b)
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
# number a[3] <- [1,2,3]
# func foo (number b)
#     begin
#         a[1] <- b + a[2]
#         dynamic c
#         c <- a[c] + foo(a[1])[1]
#         return a
#     end
# func main()
# begin
# end
#         """
#         expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(foo), [ArrayCell(Id(a), [NumLit(1.0)])]), [NumLit(1.0)])"
#         # how to infer?
#         # or raise error (we check if ctx.arr in ArrayCell has ArrayType)
#         self.assertTrue(TestChecker.test(input, expect, 421))
        
#     def test_422(self):
#         input = """
# dynamic a
# func foo (number b)
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
# func foo (number b)
#     return a
# func main()
# begin
#     foo(a)
# end
#         """
#         expect = "Type Mismatch In Statement: CallStmt(Id(foo), [Id(a)])"
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


############# TIN

    def test1(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
    def test2(self):
        input = """
        func foo()
        func main() begin
            foo()
        end
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 401))
        
    def test3(self):
        input = """
        func foo() begin
            return 1
        end
        func main() begin
            foo()
        end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test4(self):
        input = """
        func main() begin
            
            dynamic b
            dynamic a 
            number x[1, 2] <- [[1,b]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test5(self):
        input = """
        func main() begin
            
            dynamic b
            dynamic a <- [b]
            number x[1, 2] <- [[1,b]]
        end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, dynamic, ArrayLit(Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test6(self):
        input = """
        func main() begin
            number x[1, 2] <- [[1,2]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test7(self):
        input = """
        func main() begin
        dynamic b
            number x[2, 2] <- [[1,2], [b, b]]
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test8(self):
        input = """
        func main() begin
        end
        func foo(number x)
        func foo(number x, number y) begin
        end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test9(self):
        input = """
        func main() begin
        number a <- a
        end
        func foo(number x, number y)
        func foo(number z, number x) begin
        end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test10(self):
        input = """
        func main() begin
        end
        func foo(number x, number x) begin
        end
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test11(self):
        input = """
func main()
begin
    var x <- [[[[1, 2]], [3, 4, 5]], [[6, 7, 8], [9, 10, 11]]]

end
"""
        myret_ = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0))), ArrayLit(NumLit(3.0), NumLit(4.0), NumLit(5.0)))"
        self.assertTrue(TestChecker.test(input, myret_, 410))
    def test12(self):
        input = """
func main()
begin
    number a[2, 2] <- [[1, 2], [3, 4]]
    number b[2] <- a[0]
    writeNumber(b[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test13(self):
        input = """
        func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    number x[3,3] <- [a,b]
    a <- [1,2,3]
    b <- [4,5,6]
    c <- [7,8,9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), ArrayType([3.0, 3.0], NumberType), None, ArrayLit(Id(a), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test14(self):
        input = """
        func main()
begin 
    dynamic a
    dynamic b
    dynamic c
    number x[3,3] <- [a,b, c]
    a <- [1,2,3]
    b <- [4,5,6]
    c <- [7,8,9]
    writeNumber(a[0] + b[0] + c[0])
end
"""
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 413))
    def test15(self):
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
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test16(self):
        input = """
            dynamic a
            dynamic x
            dynamic y
            func foo(number a,string b) return
            func main() begin
                number a <- foo(x,y)
                number x
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x), Id(y)])"
        self.assertTrue(TestChecker.test(input, expect, 415))