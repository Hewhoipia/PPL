import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
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