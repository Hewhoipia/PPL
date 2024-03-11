import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    
    def test1(self):
        input = """var kq <- 1 + (-1 / 2 % -3) * 1
"""
        expect = "Program([VarDecl(Id(kq), None, var, BinaryOp(+, NumLit(1.0), BinaryOp(*, BinaryOp(%, BinaryOp(/, UnaryOp(-, NumLit(1.0)), NumLit(2.0)), UnaryOp(-, NumLit(3.0))), NumLit(1.0))))])"
        self.assertTrue(TestAST.test(input, expect, 300))
        
    def test2(self):
        input = """number x
bool y
string z[3, 4]
number arr[5, 6]
bool flag[1]
string names[7, 8]
"""
        expect = "Program([VarDecl(Id(x), NumberType, None, None), VarDecl(Id(y), BoolType, None, None), VarDecl(Id(z), ArrayType([3.0, 4.0], StringType), None, None), VarDecl(Id(arr), ArrayType([5.0, 6.0], NumberType), None, None), VarDecl(Id(flag), ArrayType([1.0], BoolType), None, None), VarDecl(Id(names), ArrayType([7.0, 8.0], StringType), None, None)])"
        self.assertTrue(TestAST.test(input, expect, 301))
        
    def test3(self):
        input = """number value <- 7
bool status <- false
string text <- "modified string"
number numbers[2, 3] <- [6, 8]
bool flags[1] <- anotherFunc()
string words[4, 5] <- numbers
"""
        expect = "Program([VarDecl(Id(value), NumberType, None, NumLit(7.0)), VarDecl(Id(status), BoolType, None, BooleanLit(False)), VarDecl(Id(text), StringType, None, StringLit(modified string)), VarDecl(Id(numbers), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(NumLit(6.0), NumLit(8.0))), VarDecl(Id(flags), ArrayType([1.0], BoolType), None, CallExpr(Id(anotherFunc), [])), VarDecl(Id(words), ArrayType([4.0, 5.0], StringType), None, Id(numbers))])"
        self.assertTrue(TestAST.test(input, expect, 302))
        
    def test4(self):
        input = """number x <- 5
bool y <- false
string z <- "modified string"
number nums[2, 3] <- [7, 9]
bool flags[0] <- customFunc()
string words[4, 5] <- customFunc(2, false, [2, 4], [customFunc(), 5])
"""
        expect = "Program([VarDecl(Id(x), NumberType, None, NumLit(5.0)), VarDecl(Id(y), BoolType, None, BooleanLit(False)), VarDecl(Id(z), StringType, None, StringLit(modified string)), VarDecl(Id(nums), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(NumLit(7.0), NumLit(9.0))), VarDecl(Id(flags), ArrayType([0.0], BoolType), None, CallExpr(Id(customFunc), [])), VarDecl(Id(words), ArrayType([4.0, 5.0], StringType), None, CallExpr(Id(customFunc), [NumLit(2.0), BooleanLit(False), ArrayLit(NumLit(2.0), NumLit(4.0)), ArrayLit(CallExpr(Id(customFunc), []), NumLit(5.0))]))])"
        self.assertTrue(TestAST.test(input, expect, 303))
        
    def test5(self):
        input = """dynamic c
var d <- [1, 2, 3]
"""
        expect = "Program([VarDecl(Id(c), None, dynamic, None), VarDecl(Id(d), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))])"
        self.assertTrue(TestAST.test(input, expect, 304))
        
    def test6(self):
        input = """dynamic c
var d <- "[1, 2, 3]"
func fun()
func fun2(number a)
func fun3(bool b[1, 2])

func fun4(string c) return
func fun5()
begin
    return null
end
"""
        expect = "Program([VarDecl(Id(c), None, dynamic, None), VarDecl(Id(d), None, var, StringLit([1, 2, 3])), FuncDecl(Id(fun), [], None), FuncDecl(Id(fun2), [VarDecl(Id(a), NumberType, None, None)], None), FuncDecl(Id(fun3), [VarDecl(Id(b), ArrayType([1.0, 2.0], BoolType), None, None)], None), FuncDecl(Id(fun4), [VarDecl(Id(c), StringType, None, None)], Return()), FuncDecl(Id(fun5), [], Block([Return(Id(null))]))])"
        self.assertTrue(TestAST.test(input, expect, 305))
        
    def test7(self):
        input = """func main()
begin
    a <- 1
    b <- true
    c <- "ccc"
    d <- [1, 2, 3]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), NumLit(1.0)), AssignStmt(Id(b), BooleanLit(True)), AssignStmt(Id(c), StringLit(ccc)), AssignStmt(Id(d), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 306))
        
    def test8(self):
        input = """func main()
begin
    a <- [[1,2,3], funcall("kkk")]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), CallExpr(Id(funcall), [StringLit(kkk)])))]))])"
        self.assertTrue(TestAST.test(input, expect, 307))
        
    def test9(self):
        input = """func main()
begin
    a <- [[1,2,3], funcall("kkk")]
    a[2] <- "cell"
    a[2, cellfun()] <- [funcell(), ["str", true]]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(Id(a), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), CallExpr(Id(funcall), [StringLit(kkk)]))), AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), StringLit(cell)), AssignStmt(ArrayCell(Id(a), [NumLit(2.0), CallExpr(Id(cellfun), [])]), ArrayLit(CallExpr(Id(funcell), []), ArrayLit(StringLit(str), BooleanLit(True))))]))])"
        self.assertTrue(TestAST.test(input, expect, 308))
        
    def test10(self):
        input = """func add(number a, number b) 
begin
    return a + b
end
func sub(number a, number b) 
begin
    return a - b
end
func mul(number a, number b) 
begin
    return a * b
end
func div(number a, number b) 
begin
    if (b != 0) 
    begin
        return a / b
    end
    else 
    begin
        return 0
    end
end
number x <- add(10, 20)
number y <- sub(30, 40)
number z <- mul(x, y)
number rel <- div(z, x)
"""
        expect = "Program([FuncDecl(Id(add), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(+, Id(a), Id(b)))])), FuncDecl(Id(sub), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(-, Id(a), Id(b)))])), FuncDecl(Id(mul), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(*, Id(a), Id(b)))])), FuncDecl(Id(div), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(!=, Id(b), NumLit(0.0)), Block([Return(BinaryOp(/, Id(a), Id(b)))])), [], Block([Return(NumLit(0.0))]))])), VarDecl(Id(x), NumberType, None, CallExpr(Id(add), [NumLit(10.0), NumLit(20.0)])), VarDecl(Id(y), NumberType, None, CallExpr(Id(sub), [NumLit(30.0), NumLit(40.0)])), VarDecl(Id(z), NumberType, None, CallExpr(Id(mul), [Id(x), Id(y)])), VarDecl(Id(rel), NumberType, None, CallExpr(Id(div), [Id(z), Id(x)]))])"
        self.assertTrue(TestAST.test(input, expect, 309))
        
    def test11(self):
        input = """func main()
begin
    a[2] <- a[0 + 1, 1 - 2]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(1.0)), BinaryOp(-, NumLit(1.0), NumLit(2.0))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 310))
        
    def test12(self):
        input = """func main()
begin
    a[2] <- [a[0 + 1, b], funcall(1)]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayLit(ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(1.0)), Id(b)]), CallExpr(Id(funcall), [NumLit(1.0)])))]))])"
        self.assertTrue(TestAST.test(input, expect, 311))
        
    def test13(self):
        input = """func main()
begin
    a[2] <- [a[0 + 1, b], funcall(not 12)]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayLit(ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(1.0)), Id(b)]), CallExpr(Id(funcall), [UnaryOp(not, NumLit(12.0))])))]))])"
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test14(self):
        input = """func main()
begin
    number sum <- 0
    for i until 10 by 1 
    begin
        sum <- sum + i
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(sum), NumberType, None, NumLit(0.0)), For(Id(i), NumLit(10.0), NumLit(1.0), Block([AssignStmt(Id(sum), BinaryOp(+, Id(sum), Id(i)))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 313))
        
    def test15(self):
        input = """func main()
begin
    break
    continue
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Break, Continue]))])"
        self.assertTrue(TestAST.test(input, expect, 314))
        
    def test16(self):
        input = """func main()
begin
    call()
    call2(call())
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(call), []), CallStmt(Id(call2), [CallExpr(Id(call), [])])]))])"
        self.assertTrue(TestAST.test(input, expect, 315))
        
    def test17(self):
        input = """func main()
begin
    begin
    begin
    end
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Block([Block([])])]))])"
        self.assertTrue(TestAST.test(input, expect, 316))
        
    def test18(self):
        input = """func main()
begin
    for i until 10 by 1 
begin
    if (i = 5) 
    begin
        continue
    end
end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), NumLit(10.0), NumLit(1.0), Block([If((BinaryOp(=, Id(i), NumLit(5.0)), Block([Continue])), [], None)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 317))
        
    def test19(self):
        input = """func main()
begin
    if (expr(a) == "exprstr") return false
    if (a) begin
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(expr), [Id(a)]), StringLit(exprstr)), Return(BooleanLit(False))), [], None), If((Id(a), Block([])), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 318))
        
    def test20(self):
        input = """func main()
begin
    if (hth() == true)
    begin
        if (gmon() == true) return true
        elif (c) begin
            break
        end
        else
            continue
    end
    elif (d) return false
    else 
        return d
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(hth), []), BooleanLit(True)), Block([If((BinaryOp(==, CallExpr(Id(gmon), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break]))], Continue)])), [(Id(d), Return(BooleanLit(False)))], Return(Id(d)))]))])"
        self.assertTrue(TestAST.test(input, expect, 319))
        
    def test21(self):
        input = """func main()
begin
    if (hth() == true)
    begin
        if (gmon() == true) return true
        elif (c) begin
            break
        end
        else
            continue
    end
    else 
        return d
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(hth), []), BooleanLit(True)), Block([If((BinaryOp(==, CallExpr(Id(gmon), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break]))], Continue)])), [], Return(Id(d)))]))])"
        self.assertTrue(TestAST.test(input, expect, 320))
        
    def test22(self):
        input = """func main()
begin
    if (hth() == true)
    begin
        if (gmon() == true) return true
        elif (c) begin
            break
        end
        else
            continue
    end
    elif (d) return false
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(hth), []), BooleanLit(True)), Block([If((BinaryOp(==, CallExpr(Id(gmon), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break]))], Continue)])), [(Id(d), Return(BooleanLit(False)))], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 321))
        
    def test23(self):
        input = """func main()
begin
    if (hth() == true)
        if (gmon() == true) return true
        elif (c) begin
            break
        end
    elif (d) return false
    else break
    else continue
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(hth), []), BooleanLit(True)), If((BinaryOp(==, CallExpr(Id(gmon), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break])), (Id(d), Return(BooleanLit(False)))], Break)), [], Continue)]))])"
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test24(self):
        input = """func main()
begin
    if (hth() == true)
        if (gmon() == true) return true
        elif (c) begin
            break
        end
    elif (d) return false
    else break
    elif (e) return main(kts)
    else continue
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(==, CallExpr(Id(hth), []), BooleanLit(True)), If((BinaryOp(==, CallExpr(Id(gmon), []), BooleanLit(True)), Return(BooleanLit(True))), [(Id(c), Block([Break])), (Id(d), Return(BooleanLit(False)))], Break)), [(Id(e), Return(CallExpr(Id(main), [Id(kts)])))], Continue)]))])"
        self.assertTrue(TestAST.test(input, expect, 323))
        
    def test25(self):
        input = """func main()
begin
    for i until i > H() by H() - i simple()
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>, Id(i), CallExpr(Id(H), [])), BinaryOp(-, CallExpr(Id(H), []), Id(i)), CallStmt(Id(simple), []))]))])"
        self.assertTrue(TestAST.test(input, expect, 324))
        
    def test26(self):
        input = """func main()
begin
    for i until i > H() by H() - i begin
        j <- i
        if (j > 10) break
        else 
        continue
        ko()
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(>, Id(i), CallExpr(Id(H), [])), BinaryOp(-, CallExpr(Id(H), []), Id(i)), Block([AssignStmt(Id(j), Id(i)), If((BinaryOp(>, Id(j), NumLit(10.0)), Break), [], Continue), CallStmt(Id(ko), [])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 325))
        
    def test27(self):
        input = """func main()
begin
    var a <- 1 + 2/3 - not (a..."a") * 12 and (30 or true)
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, BinaryOp(and, BinaryOp(-, BinaryOp(+, NumLit(1.0), BinaryOp(/, NumLit(2.0), NumLit(3.0))), BinaryOp(*, UnaryOp(not, BinaryOp(..., Id(a), StringLit(a))), NumLit(12.0))), BinaryOp(or, NumLit(30.0), BooleanLit(True))))]))])"
        self.assertTrue(TestAST.test(input, expect, 326))
        
    def test28(self):
        input = """func main()
begin
    var a <- beo() + sys[1, 2] == -50e-12
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, BinaryOp(==, BinaryOp(+, CallExpr(Id(beo), []), ArrayCell(Id(sys), [NumLit(1.0), NumLit(2.0)])), UnaryOp(-, NumLit(5e-11))))]))])"
        self.assertTrue(TestAST.test(input, expect, 327))

    def test29(self):
        input = """func main()
begin
    for i until i + (lol / love) by love
        for j until (a[1, loveu()] != true) by i if (i == j) if (j != 0) break
        elif (j == 1) continue
        else break
        else begin
        end
        
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(+, Id(i), BinaryOp(/, Id(lol), Id(love))), Id(love), For(Id(j), BinaryOp(!=, ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(loveu), [])]), BooleanLit(True)), Id(i), If((BinaryOp(==, Id(i), Id(j)), If((BinaryOp(!=, Id(j), NumLit(0.0)), Break), [(BinaryOp(==, Id(j), NumLit(1.0)), Continue)], Break)), [], Block([]))))]))])"
        self.assertTrue(TestAST.test(input, expect, 328))
        
    def test30(self):
        input = """func main()
begin
    for i until i + (lol / love) by love
        if (love != i) 
        for j until (a[1, loveu()] != true) by i if (i == j) if (j != 0) break
        elif (j == 1) continue
        else break
        else begin
        end

end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(+, Id(i), BinaryOp(/, Id(lol), Id(love))), Id(love), If((BinaryOp(!=, Id(love), Id(i)), For(Id(j), BinaryOp(!=, ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(loveu), [])]), BooleanLit(True)), Id(i), If((BinaryOp(==, Id(i), Id(j)), If((BinaryOp(!=, Id(j), NumLit(0.0)), Break), [(BinaryOp(==, Id(j), NumLit(1.0)), Continue)], Break)), [], Block([])))), [], None))]))])"
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test31(self):
        input = """number a[2, 2] <- [[1, 2], [3, 4]]
        """
        expect = """Program([VarDecl(Id(a), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0))))])"""
        
        self.assertTrue(TestAST.test(input, expect, 330))
        
    def test32 (self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- x1...(x2-x1)

end
"""
        expect = """Program([FuncDecl(Id(main), [VarDecl(Id(args), ArrayType([4.0], NumberType), None, None)], Block([VarDecl(Id(x1), StringType, None, ArrayCell(Id(args), [NumLit(0.0)])), VarDecl(Id(x2), StringType, None, ArrayCell(Id(args), [NumLit(1.0)])), AssignStmt(Id(x3), BinaryOp(..., Id(x1), BinaryOp(-, Id(x2), Id(x1))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test33(self):
        input = """func main()
begin
    var a <- "simp"
    if (a <= 3.14 and not (a > 0)) begin
        print("hell")
        if (a = a and APondabeat()) print("true")
        elif (true = true)
            print("true")
        else APondabeat()
        
    end
    elif (a = 1) 
        print("luv")
    elif (a = 2) print("diu")
    else 
        print("somuch")
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, StringLit(simp)), If((BinaryOp(<=, Id(a), BinaryOp(and, NumLit(3.14), UnaryOp(not, BinaryOp(>, Id(a), NumLit(0.0))))), Block([CallStmt(Id(print), [StringLit(hell)]), If((BinaryOp(=, Id(a), BinaryOp(and, Id(a), CallExpr(Id(APondabeat), []))), CallStmt(Id(print), [StringLit(true)])), [(BinaryOp(=, BooleanLit(True), BooleanLit(True)), CallStmt(Id(print), [StringLit(true)]))], CallStmt(Id(APondabeat), []))])), [(BinaryOp(=, Id(a), NumLit(1.0)), CallStmt(Id(print), [StringLit(luv)])), (BinaryOp(=, Id(a), NumLit(2.0)), CallStmt(Id(print), [StringLit(diu)]))], CallStmt(Id(print), [StringLit(somuch)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 332))
        
    def test34(self):
        input = """func main(number args[4])
begin
    string x1 <- args[0]
    string x2 <- args[1]
    x3 <- beo(x1 / x3 / x4 * 2 + not (x1 +- x2))

end
"""
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(args), ArrayType([4.0], NumberType), None, None)], Block([VarDecl(Id(x1), StringType, None, ArrayCell(Id(args), [NumLit(0.0)])), VarDecl(Id(x2), StringType, None, ArrayCell(Id(args), [NumLit(1.0)])), AssignStmt(Id(x3), CallExpr(Id(beo), [BinaryOp(+, BinaryOp(*, BinaryOp(/, BinaryOp(/, Id(x1), Id(x3)), Id(x4)), NumLit(2.0)), UnaryOp(not, BinaryOp(+, Id(x1), UnaryOp(-, Id(x2)))))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 333))
        
    def test35(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (beo(y) - x > (2 <= 3))
    print(x)
    ## else if (unu(x) - y == true) print(y) else return false

end
"""
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(args), ArrayType([4.0], NumberType), None, None)], Block([VarDecl(Id(x), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))), VarDecl(Id(y), None, dynamic, Id(x)), If((BinaryOp(>, BinaryOp(-, CallExpr(Id(beo), [Id(y)]), Id(x)), BinaryOp(<=, NumLit(2.0), NumLit(3.0))), CallStmt(Id(print), [Id(x)])), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 334))
        
    def test36(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (beo(y) - x > (2 <= 3))
    print(x)
    else if (unu(x) - y == true) print(y)
    else return false

end
"""
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(args), ArrayType([4.0], NumberType), None, None)], Block([VarDecl(Id(x), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))), VarDecl(Id(y), None, dynamic, Id(x)), If((BinaryOp(>, BinaryOp(-, CallExpr(Id(beo), [Id(y)]), Id(x)), BinaryOp(<=, NumLit(2.0), NumLit(3.0))), CallStmt(Id(print), [Id(x)])), [], If((BinaryOp(==, BinaryOp(-, CallExpr(Id(unu), [Id(x)]), Id(y)), BooleanLit(True)), CallStmt(Id(print), [Id(y)])), [], Return(BooleanLit(False))))]))])"
        self.assertTrue(TestAST.test(input, expect, 335))
        
    def test37(self):
        input = """func main(number args[4])
begin
    var x <- [1,2,3,4]
    dynamic y <- x
    if (beo(y) - x > (2 <= 3))
    print(x)
    else if (unu(x) - y == true) print(y)
    else for i until true by main() begin
        for j until i > 10 by 1 break
    end

end
"""
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(args), ArrayType([4.0], NumberType), None, None)], Block([VarDecl(Id(x), None, var, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))), VarDecl(Id(y), None, dynamic, Id(x)), If((BinaryOp(>, BinaryOp(-, CallExpr(Id(beo), [Id(y)]), Id(x)), BinaryOp(<=, NumLit(2.0), NumLit(3.0))), CallStmt(Id(print), [Id(x)])), [], If((BinaryOp(==, BinaryOp(-, CallExpr(Id(unu), [Id(x)]), Id(y)), BooleanLit(True)), CallStmt(Id(print), [Id(y)])), [], For(Id(i), BooleanLit(True), CallExpr(Id(main), []), Block([For(Id(j), BinaryOp(>, Id(i), NumLit(10.0)), NumLit(1.0), Break)]))))]))])"
        self.assertTrue(TestAST.test(input, expect, 336))
        
    def test38(self):
        input = """func add(number a, number b) 
begin
    return a + b
end
func main()
begin
    number kq <- add(10 + 20, 30 * 40)
end
"""
        expect = "Program([FuncDecl(Id(add), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(+, Id(a), Id(b)))])), FuncDecl(Id(main), [], Block([VarDecl(Id(kq), NumberType, None, CallExpr(Id(add), [BinaryOp(+, NumLit(10.0), NumLit(20.0)), BinaryOp(*, NumLit(30.0), NumLit(40.0))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 337))
        
    def test39(self):
        input = """func inlist(number arr[3]) 
begin
    ## print array
end
func main()
begin
    number arr[3] <- [1 + 2, 3 * 4, 5 / 6]
    inlist(arr)
end
"""
        expect = "Program([FuncDecl(Id(inlist), [VarDecl(Id(arr), ArrayType([3.0], NumberType), None, None)], Block([])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(BinaryOp(+, NumLit(1.0), NumLit(2.0)), BinaryOp(*, NumLit(3.0), NumLit(4.0)), BinaryOp(/, NumLit(5.0), NumLit(6.0)))), CallStmt(Id(inlist), [Id(arr)])]))])"
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test40(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[beo()]
        return
    end
    for i until i < arr[beo] by 1
        print(i)
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((CallExpr(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))]), Block([VarDecl(Id(x), None, var, NumLit(2.0))])), [], Block([VarDecl(Id(arr), ArrayType([1.0, 2.0, 3.0], StringType), None, ArrayCell(Id(main), [CallExpr(Id(beo), [])])), Return()])), For(Id(i), BinaryOp(<, Id(i), ArrayCell(Id(arr), [Id(beo)])), NumLit(1.0), CallStmt(Id(print), [Id(i)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 339))
        
    def test41(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[beo()]
        return
    end
    for i until i...j <= arr[beo] by 1
        print(i)
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((CallExpr(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))]), Block([VarDecl(Id(x), None, var, NumLit(2.0))])), [], Block([VarDecl(Id(arr), ArrayType([1.0, 2.0, 3.0], StringType), None, ArrayCell(Id(main), [CallExpr(Id(beo), [])])), Return()])), For(Id(i), BinaryOp(..., Id(i), BinaryOp(<=, Id(j), ArrayCell(Id(arr), [Id(beo)]))), NumLit(1.0), CallStmt(Id(print), [Id(i)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 340))
        
    def test42(self):
        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[beo()]
        return
    end
    for i until i...(j <= arr[beo<1]) by 1
        print(i)
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((CallExpr(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))]), Block([VarDecl(Id(x), None, var, NumLit(2.0))])), [], Block([VarDecl(Id(arr), ArrayType([1.0, 2.0, 3.0], StringType), None, ArrayCell(Id(main), [CallExpr(Id(beo), [])])), Return()])), For(Id(i), BinaryOp(..., Id(i), BinaryOp(<=, Id(j), ArrayCell(Id(arr), [BinaryOp(<, Id(beo), NumLit(1.0))]))), NumLit(1.0), CallStmt(Id(print), [Id(i)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 341))
        
    def test43(self):
        input = """func main()
begin
    string str <- "t dep trai"..."la do"
    if (not len(str) > 10)
    print("ong co noi t")
    else print("de lai")
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(str), StringType, None, BinaryOp(..., StringLit(t dep trai), StringLit(la do))), If((BinaryOp(>, UnaryOp(not, CallExpr(Id(len), [Id(str)])), NumLit(10.0)), CallStmt(Id(print), [StringLit(ong co noi t)])), [], CallStmt(Id(print), [StringLit(de lai)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 342))
        
    def test44(self):
        input = """func main()
begin
    string str <- "t dep trai"..."la do"
    if (not len(str) and str..."bonus" > 10)
    print("ong co noi t")
    else print("de lai")
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(str), StringType, None, BinaryOp(..., StringLit(t dep trai), StringLit(la do))), If((BinaryOp(..., BinaryOp(and, UnaryOp(not, CallExpr(Id(len), [Id(str)])), Id(str)), BinaryOp(>, StringLit(bonus), NumLit(10.0))), CallStmt(Id(print), [StringLit(ong co noi t)])), [], CallStmt(Id(print), [StringLit(de lai)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 343))
        
    def test45(self):
        input = """func main() begin
    if (ngu) if (simp) print("dai gai")
    else print("hao han")
    else ngu <- not true
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((Id(ngu), If((Id(simp), CallStmt(Id(print), [StringLit(dai gai)])), [], CallStmt(Id(print), [StringLit(hao han)]))), [], AssignStmt(Id(ngu), UnaryOp(not, BooleanLit(True))))]))])"
        self.assertTrue(TestAST.test(input, expect, 344))
        
    def test46(self):
        input = """func main(number abc[1,2]) begin
  break  
end
func kenchana()
begin
if (main[1] == "906090")
return
end
"""
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(abc), ArrayType([1.0, 2.0], NumberType), None, None)], Block([Break])), FuncDecl(Id(kenchana), [], Block([If((BinaryOp(==, ArrayCell(Id(main), [NumLit(1.0)]), StringLit(906090)), Return()), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 345))
        
    def test47(self):
        input = """func main(number abc[1,2]) begin
  break  
end
func _()
 return _()[_()]
"""
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(abc), ArrayType([1.0, 2.0], NumberType), None, None)], Block([Break])), FuncDecl(Id(_), [], Return(ArrayCell(CallExpr(Id(_), []), [CallExpr(Id(_), [])])))])"
        self.assertTrue(TestAST.test(input, expect, 346))
        
    def test48(self):
        input = """func add(number a, number b) 
    begin
        return a + b
    end
func cpxF(number a, number b) 
    begin
        number arr[3] <- [1, 2, 3]
        number kq <- add(arr[0], arr[1]) * arr[2]
    end
"""
        expect = "Program([FuncDecl(Id(add), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(+, Id(a), Id(b)))])), FuncDecl(Id(cpxF), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(kq), NumberType, None, BinaryOp(*, CallExpr(Id(add), [ArrayCell(Id(arr), [NumLit(0.0)]), ArrayCell(Id(arr), [NumLit(1.0)])]), ArrayCell(Id(arr), [NumLit(2.0)])))]))])"
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test49(self):
        input = """func main()
begin
    number a <- (1 + 2 - 3 / 4 % 5) <= not ((-"bangkieu" * ((2)...(3.2))) != (beo() == unu()))
    number b[1,2]
    a <- b[beo((1 + 2.2)... "unu"), (a + b) <= ((c / d) != 2)]
    a <- beo()[1, 2, 3]
end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, BinaryOp(<=, BinaryOp(-, BinaryOp(+, NumLit(1.0), NumLit(2.0)), BinaryOp(%, BinaryOp(/, NumLit(3.0), NumLit(4.0)), NumLit(5.0))), UnaryOp(not, BinaryOp(!=, BinaryOp(*, UnaryOp(-, StringLit(bangkieu)), BinaryOp(..., NumLit(2.0), NumLit(3.2))), BinaryOp(==, CallExpr(Id(beo), []), CallExpr(Id(unu), [])))))), VarDecl(Id(b), ArrayType([1.0, 2.0], NumberType), None, None), AssignStmt(Id(a), ArrayCell(Id(b), [CallExpr(Id(beo), [BinaryOp(..., BinaryOp(+, NumLit(1.0), NumLit(2.2)), StringLit(unu))]), BinaryOp(<=, BinaryOp(+, Id(a), Id(b)), BinaryOp(!=, BinaryOp(/, Id(c), Id(d)), NumLit(2.0)))])), AssignStmt(Id(a), ArrayCell(CallExpr(Id(beo), []), [NumLit(1.0), NumLit(2.0), NumLit(3.0)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 348))
        
    def test50(self):
        input = """var x <- 1.2e12
func main()
begin
    number a
    a[1, main()] <- 1 + beo()
end
        """
        expect = "Program([VarDecl(Id(x), None, var, NumLit(1200000000000.0)), FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, None), AssignStmt(ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(main), [])]), BinaryOp(+, NumLit(1.0), CallExpr(Id(beo), [])))]))])"
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test51(self):
        input = """var x <- 1.2e12
func main()
begin
    bool x
    string c <- bangkieu
    dynamic a
    a[1, main()] <- 1 + beo()
    bool y[1, 2, 3] <- [a = c, b - beo(), "bye bye"]
end
        """
        expect = "Program([VarDecl(Id(x), None, var, NumLit(1200000000000.0)), FuncDecl(Id(main), [], Block([VarDecl(Id(x), BoolType, None, None), VarDecl(Id(c), StringType, None, Id(bangkieu)), VarDecl(Id(a), None, dynamic, None), AssignStmt(ArrayCell(Id(a), [NumLit(1.0), CallExpr(Id(main), [])]), BinaryOp(+, NumLit(1.0), CallExpr(Id(beo), []))), VarDecl(Id(y), ArrayType([1.0, 2.0, 3.0], BoolType), None, ArrayLit(BinaryOp(=, Id(a), Id(c)), BinaryOp(-, Id(b), CallExpr(Id(beo), [])), StringLit(bye bye)))]))])"
        self.assertTrue(TestAST.test(input, expect, 350))
        
    def test52(self):
        input = """func main()
begin
    var a <- "simp"
    for i until not (simp + 4 > beo(i) / unu(i)) by print("simp")
    begin
        print("hell")
        break
    end
    break
end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, StringLit(simp)), For(Id(i), UnaryOp(not, BinaryOp(>, BinaryOp(+, Id(simp), NumLit(4.0)), BinaryOp(/, CallExpr(Id(beo), [Id(i)]), CallExpr(Id(unu), [Id(i)])))), CallExpr(Id(print), [StringLit(simp)]), Block([CallStmt(Id(print), [StringLit(hell)]), Break])), Break]))])"
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test52(self):
        input = """func main()
begin
    var a <- "simp"
    for i until not (simp + 4 > beo(i) / unu(i)) by print("simp")...print("simp2") 
    begin
        if (a = 1) continue
        else begin
            for j until j < main() by -1 begin
                simp[beo(i), j] <- [i, j]
            end
        end
        
    end
    return
end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, StringLit(simp)), For(Id(i), UnaryOp(not, BinaryOp(>, BinaryOp(+, Id(simp), NumLit(4.0)), BinaryOp(/, CallExpr(Id(beo), [Id(i)]), CallExpr(Id(unu), [Id(i)])))), BinaryOp(..., CallExpr(Id(print), [StringLit(simp)]), CallExpr(Id(print), [StringLit(simp2)])), Block([If((BinaryOp(=, Id(a), NumLit(1.0)), Continue), [], Block([For(Id(j), BinaryOp(<, Id(j), CallExpr(Id(main), [])), UnaryOp(-, NumLit(1.0)), Block([AssignStmt(ArrayCell(Id(simp), [CallExpr(Id(beo), [Id(i)]), Id(j)]), ArrayLit(Id(i), Id(j)))]))]))])), Return()]))])"
        self.assertTrue(TestAST.test(input, expect, 351))
        
    def test53(self):
        input = """func main()
begin
    var a <- "simp"
    for i until not (simp + 4 > beo(i) / unu(i)) by print("simp")...print("simp2") 
    begin
        nyc()
        nym(print("hj"))
        nymcuanym(simp, 1 + not true, nyc(), buontinh()[1, beo()], array[a], 2 < 10)
    end
    return
end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), None, var, StringLit(simp)), For(Id(i), UnaryOp(not, BinaryOp(>, BinaryOp(+, Id(simp), NumLit(4.0)), BinaryOp(/, CallExpr(Id(beo), [Id(i)]), CallExpr(Id(unu), [Id(i)])))), BinaryOp(..., CallExpr(Id(print), [StringLit(simp)]), CallExpr(Id(print), [StringLit(simp2)])), Block([CallStmt(Id(nyc), []), CallStmt(Id(nym), [CallExpr(Id(print), [StringLit(hj)])]), CallStmt(Id(nymcuanym), [Id(simp), BinaryOp(+, NumLit(1.0), UnaryOp(not, BooleanLit(True))), CallExpr(Id(nyc), []), ArrayCell(CallExpr(Id(buontinh), []), [NumLit(1.0), CallExpr(Id(beo), [])]), ArrayCell(Id(array), [Id(a)]), BinaryOp(<, NumLit(2.0), NumLit(10.0))])])), Return()]))])"
        self.assertTrue(TestAST.test(input, expect, 352))
        
    def test54(self):
        input = """func conmobanggia(number a)

begin
    if (a = 0) return 1 + a /3
    return conmobanggia(a-1)
end
func main()
begin
    if (conmobanggia()) begin
        writeString("What's good" + 1.23e-12)
    end
end
"""
        expect = "Program([FuncDecl(Id(conmobanggia), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(=, Id(a), NumLit(0.0)), Return(BinaryOp(+, NumLit(1.0), BinaryOp(/, Id(a), NumLit(3.0))))), [], None), Return(CallExpr(Id(conmobanggia), [BinaryOp(-, Id(a), NumLit(1.0))]))])), FuncDecl(Id(main), [], Block([If((CallExpr(Id(conmobanggia), []), Block([CallStmt(Id(writeString), [BinaryOp(+, StringLit(What's good), NumLit(1.23e-12))])])), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 353))
        
    def test55(self):
        input = """func conmobanggia(number a)

begin
    if (a = 0) return 1 + a /3
    return conmobanggia(a-1)
end

number a <- 16 / conmobanggia(a)

func main()
begin
    for i until conmobanggia(i) != "a"...a by conmobanggia(a)
    begin
        writeString(i)
    end
end
"""
        expect = "Program([FuncDecl(Id(conmobanggia), [VarDecl(Id(a), NumberType, None, None)], Block([If((BinaryOp(=, Id(a), NumLit(0.0)), Return(BinaryOp(+, NumLit(1.0), BinaryOp(/, Id(a), NumLit(3.0))))), [], None), Return(CallExpr(Id(conmobanggia), [BinaryOp(-, Id(a), NumLit(1.0))]))])), VarDecl(Id(a), NumberType, None, BinaryOp(/, NumLit(16.0), CallExpr(Id(conmobanggia), [Id(a)]))), FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(..., BinaryOp(!=, CallExpr(Id(conmobanggia), [Id(i)]), StringLit(a)), Id(a)), CallExpr(Id(conmobanggia), [Id(a)]), Block([CallStmt(Id(writeString), [Id(i)])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 354))
        
    def test56(self):
        input = """func conmobanggia(number a, string arr[1, 2])

begin
    if (a = 0) return 1 + a /3
    return conmobanggia(a-1)
end

number a <- 16 / conmobanggia(a)

func main()
begin
    for i until conmobanggia(i) != "a"...a by conmobanggia(a)
    begin
        if (i == conmobanggia(a) and not ("a" + true > 1)) writeString("bangkieu")
        elif (i + 1 > 2) return 1
        else
        return 10
    end
end
"""
        expect = "Program([FuncDecl(Id(conmobanggia), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(arr), ArrayType([1.0, 2.0], StringType), None, None)], Block([If((BinaryOp(=, Id(a), NumLit(0.0)), Return(BinaryOp(+, NumLit(1.0), BinaryOp(/, Id(a), NumLit(3.0))))), [], None), Return(CallExpr(Id(conmobanggia), [BinaryOp(-, Id(a), NumLit(1.0))]))])), VarDecl(Id(a), NumberType, None, BinaryOp(/, NumLit(16.0), CallExpr(Id(conmobanggia), [Id(a)]))), FuncDecl(Id(main), [], Block([For(Id(i), BinaryOp(..., BinaryOp(!=, CallExpr(Id(conmobanggia), [Id(i)]), StringLit(a)), Id(a)), CallExpr(Id(conmobanggia), [Id(a)]), Block([If((BinaryOp(==, Id(i), BinaryOp(and, CallExpr(Id(conmobanggia), [Id(a)]), UnaryOp(not, BinaryOp(>, BinaryOp(+, StringLit(a), BooleanLit(True)), NumLit(1.0))))), CallStmt(Id(writeString), [StringLit(bangkieu)])), [(BinaryOp(>, BinaryOp(+, Id(i), NumLit(1.0)), NumLit(2.0)), Return(NumLit(1.0)))], Return(NumLit(10.0)))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 355))
        
    def test57(self):
        input = """func main()
begin
    bool bangkieu <- true
    number arr[3, 4] <- beo(arr[5, 6])
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(bangkieu), BoolType, None, BooleanLit(True)), VarDecl(Id(arr), ArrayType([3.0, 4.0], NumberType), None, CallExpr(Id(beo), [ArrayCell(Id(arr), [NumLit(5.0), NumLit(6.0)])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 356))
        
    def test58(self):
        input = """func main()
begin
    var bangkieu <- true
    number arr[3, 4] <- beo(arr[5, 6])
    if (arr) ## comment
    begin
        beo()
    end
    else arr <- beo(arr[beo(arr)])
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(bangkieu), None, var, BooleanLit(True)), VarDecl(Id(arr), ArrayType([3.0, 4.0], NumberType), None, CallExpr(Id(beo), [ArrayCell(Id(arr), [NumLit(5.0), NumLit(6.0)])])), If((Id(arr), Block([CallStmt(Id(beo), [])])), [], AssignStmt(Id(arr), CallExpr(Id(beo), [ArrayCell(Id(arr), [CallExpr(Id(beo), [Id(arr)])])])))]))])"
        self.assertTrue(TestAST.test(input, expect, 357))
        
    def test59(self):
        input = """func main()
## begin
##     var bangkieu <- true
##    number arr[3, 4] <- beo(arr[5, 6])
##    if (arr) ## comment
##    begin
##        beo()
##    end
##   else arr <- beo(arr[beo(arr)])
## end
"""
        expect = "Program([FuncDecl(Id(main), [], None)])"
        self.assertTrue(TestAST.test(input, expect, 358))
        
    def test60(self):
        input = """func main(number args[4])
begin
    if (beo(y) / x + 3 >= (2 <= 3)) main(x, y, 2, 3)
end
"""
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(args), ArrayType([4.0], NumberType), None, None)], Block([If((BinaryOp(>=, BinaryOp(+, BinaryOp(/, CallExpr(Id(beo), [Id(y)]), Id(x)), NumLit(3.0)), BinaryOp(<=, NumLit(2.0), NumLit(3.0))), CallStmt(Id(main), [Id(x), Id(y), NumLit(2.0), NumLit(3.0)])), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 359))
        
    def test61(self):
        input = """func main(number args[4])
begin
    if (beo(y) / x + 3 >= (2 <= 3)) main(x, y, 2, 3)
    else if (false) if (true) main <- main - 1
    else return true
    else return
end
"""
        expect = "Program([FuncDecl(Id(main), [VarDecl(Id(args), ArrayType([4.0], NumberType), None, None)], Block([If((BinaryOp(>=, BinaryOp(+, BinaryOp(/, CallExpr(Id(beo), [Id(y)]), Id(x)), NumLit(3.0)), BinaryOp(<=, NumLit(2.0), NumLit(3.0))), CallStmt(Id(main), [Id(x), Id(y), NumLit(2.0), NumLit(3.0)])), [], If((BooleanLit(False), If((BooleanLit(True), AssignStmt(Id(main), BinaryOp(-, Id(main), NumLit(1.0)))), [], Return(BooleanLit(True)))), [], Return()))]))])"
        self.assertTrue(TestAST.test(input, expect, 360))
        
    def test62(self):
        input = """func main()
func main()
begin
end
"""
        expect = "Program([FuncDecl(Id(main), [], None), FuncDecl(Id(main), [], Block([]))])"
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test63(self):
        input = """func main()
begin
    begin
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Block([])]))])"
        self.assertTrue(TestAST.test(input, expect, 362))
        
    def test64(self):
        input = """func main()
begin
    number a[1, 2] <- [1, 2]
    a[a[a[2]]] <- [a[a[a[1]]]]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), ArrayType([1.0, 2.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0))), AssignStmt(ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [NumLit(2.0)])])]), ArrayLit(ArrayCell(Id(a), [ArrayCell(Id(a), [ArrayCell(Id(a), [NumLit(1.0)])])])))]))])"
        self.assertTrue(TestAST.test(input, expect, 363))
        
    def test65(self):
        input = """func main()
begin
    number a <- 10
    number b <- 20
    number c <- a + b
    return c
end
    """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(10.0)), VarDecl(Id(b), NumberType, None, NumLit(20.0)), VarDecl(Id(c), NumberType, None, BinaryOp(+, Id(a), Id(b))), Return(Id(c))]))])"
        self.assertTrue(TestAST.test(input, expect, 364))

    def test66(self):
        input = """func main()
begin
    string name <- "MrDam"
    number age <- 90
    bool laudaitinhai <- true
    return name + " is " + age + " years old. chu nhan ca khuc " + laudaitinhai
end
    """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(name), StringType, None, StringLit(MrDam)), VarDecl(Id(age), NumberType, None, NumLit(90.0)), VarDecl(Id(laudaitinhai), BoolType, None, BooleanLit(True)), Return(BinaryOp(+, BinaryOp(+, BinaryOp(+, BinaryOp(+, Id(name), StringLit( is )), Id(age)), StringLit( years old. chu nhan ca khuc )), Id(laudaitinhai)))]))])"
        self.assertTrue(TestAST.test(input, expect, 365))
        
    def test67(self):
        input = """func main()
begin
    number a <- 5
    number b <- 10
    if (a > b) 
        return "a is greater than b"
    else if (a < b )
        return "a is less than b"
    else
        return "a is equal to b"
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(5.0)), VarDecl(Id(b), NumberType, None, NumLit(10.0)), If((BinaryOp(>, Id(a), Id(b)), Return(StringLit(a is greater than b))), [], If((BinaryOp(<, Id(a), Id(b)), Return(StringLit(a is less than b))), [], Return(StringLit(a is equal to b))))]))])"
        self.assertTrue(TestAST.test(input, expect, 366))
        
    def test68(self):
        input = """number x <- 10
number y <- 20
number z <- x + y
func add(number a, number b) 
begin
    return a + b
end
func main()
begin
    number kq <- add(x, y)
end
"""
        expect = "Program([VarDecl(Id(x), NumberType, None, NumLit(10.0)), VarDecl(Id(y), NumberType, None, NumLit(20.0)), VarDecl(Id(z), NumberType, None, BinaryOp(+, Id(x), Id(y))), FuncDecl(Id(add), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(+, Id(a), Id(b)))])), FuncDecl(Id(main), [], Block([VarDecl(Id(kq), NumberType, None, CallExpr(Id(add), [Id(x), Id(y)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 367))
        
    def test69(self):
        input = """func main()
begin
    bool kq <- ((10 + 20) < (30 * 40)) and ((50 / 60) >= (70 - 80))
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(kq), BoolType, None, BinaryOp(and, BinaryOp(<, BinaryOp(+, NumLit(10.0), NumLit(20.0)), BinaryOp(*, NumLit(30.0), NumLit(40.0))), BinaryOp(>=, BinaryOp(/, NumLit(50.0), NumLit(60.0)), BinaryOp(-, NumLit(70.0), NumLit(80.0)))))]))])"
        self.assertTrue(TestAST.test(input, expect, 368))
        
    def test70(self):
        input = """func main()
begin
    number kq <- -10 + not true
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(kq), NumberType, None, BinaryOp(+, UnaryOp(-, NumLit(10.0)), UnaryOp(not, BooleanLit(True))))]))])"
        self.assertTrue(TestAST.test(input, expect, 369))
        
    def test71(self):
        input = """func main()
begin
    number kq <- (10 + 20) * (30 - 40) / (50 % 60)
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(kq), NumberType, None, BinaryOp(/, BinaryOp(*, BinaryOp(+, NumLit(10.0), NumLit(20.0)), BinaryOp(-, NumLit(30.0), NumLit(40.0))), BinaryOp(%, NumLit(50.0), NumLit(60.0))))]))])"
        self.assertTrue(TestAST.test(input, expect, 370))
        
    def test72(self):
        input = """func main()
begin
    if (10 + 20 < 30) 
    begin
        number x <- 40
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, BinaryOp(+, NumLit(10.0), NumLit(20.0)), NumLit(30.0)), Block([VarDecl(Id(x), NumberType, None, NumLit(40.0))])), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 371))
        
    def test73(self):
        input = """func main()
begin
    if (10 + 20 < 30) 
    begin
        number x <- 40
    end
    else 
    begin
        number y <- 50
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, BinaryOp(+, NumLit(10.0), NumLit(20.0)), NumLit(30.0)), Block([VarDecl(Id(x), NumberType, None, NumLit(40.0))])), [], Block([VarDecl(Id(y), NumberType, None, NumLit(50.0))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 372))
        
    def test74(self):
        input = """func main()
begin
    if (10 + 20 < 30) 
    begin
        number x <- 40
    end
    elif (50 - 60 > 70) 
    begin
        number y <- 80
    end
    else 
    begin
        number z <- 90
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((BinaryOp(<, BinaryOp(+, NumLit(10.0), NumLit(20.0)), NumLit(30.0)), Block([VarDecl(Id(x), NumberType, None, NumLit(40.0))])), [(BinaryOp(>, BinaryOp(-, NumLit(50.0), NumLit(60.0)), NumLit(70.0)), Block([VarDecl(Id(y), NumberType, None, NumLit(80.0))]))], Block([VarDecl(Id(z), NumberType, None, NumLit(90.0))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 373))
        
    def test75(self):
        input = """func main()
begin
    a[2] <- [a[0 + 1, b], funcall("1"...(not 12))]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayLit(ArrayCell(Id(a), [BinaryOp(+, NumLit(0.0), NumLit(1.0)), Id(b)]), CallExpr(Id(funcall), [BinaryOp(..., StringLit(1), UnaryOp(not, NumLit(12.0)))])))]))])"
        self.assertTrue(TestAST.test(input, expect, 374))
        
    def test76(self):
        input = """func main()
begin
    for i until 10 by 1 
    begin
        if (i = 5) 
        begin
            break
        end
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([For(Id(i), NumLit(10.0), NumLit(1.0), Block([If((BinaryOp(=, Id(i), NumLit(5.0)), Block([Break])), [], None)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 375))
        
    def test77(self):
        input = """func main()
begin
    begin
    begin
        a <- 3
        call()
        return
    end
    end
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([Block([Block([AssignStmt(Id(a), NumLit(3.0)), CallStmt(Id(call), []), Return()])])]))])"
        self.assertTrue(TestAST.test(input, expect, 376))
        
    def test78(self):
        input = """func dieubong() 
begin
    return 10 + 20
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([Return(BinaryOp(+, NumLit(10.0), NumLit(20.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 377))
        
    def test79(self):
        input = """func dieubong() 
begin
    number a <- 10
    number b <- 20
    number c <- a + b
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([VarDecl(Id(a), NumberType, None, NumLit(10.0)), VarDecl(Id(b), NumberType, None, NumLit(20.0)), VarDecl(Id(c), NumberType, None, BinaryOp(+, Id(a), Id(b)))]))])"
        self.assertTrue(TestAST.test(input, expect, 378))
        
    def test80(self):
        input = """func dieubong() 
begin
    bool kq <- true and false or not true
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([VarDecl(Id(kq), BoolType, None, BinaryOp(or, BinaryOp(and, BooleanLit(True), BooleanLit(False)), UnaryOp(not, BooleanLit(True))))]))])"
        self.assertTrue(TestAST.test(input, expect, 379))
        
    def test81(self):
        input = """func dieubong() 
begin
    string s <- ("oi hoi" ... " ") ... "dieu bong"
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([VarDecl(Id(s), StringType, None, BinaryOp(..., BinaryOp(..., StringLit(oi hoi), StringLit( )), StringLit(dieu bong)))]))])"
        self.assertTrue(TestAST.test(input, expect, 380))
        
    def test82(self):
        input = """func dieubong() 
begin
    number n <- 123 + 456
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([VarDecl(Id(n), NumberType, None, BinaryOp(+, NumLit(123.0), NumLit(456.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 381))
        
    def test83(self):
        input = """func dieubong() 
begin
    number arr[3] <- [1, 2, 3]
    number ngta <- arr[0] + 10
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(ngta), NumberType, None, BinaryOp(+, ArrayCell(Id(arr), [NumLit(0.0)]), NumLit(10.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 382))
        
    def test84(self):
        input = """func dieubong() 
begin
    number arr[3] <- [1, 2, 3]
    arr[0] <- 10 + 20
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), AssignStmt(ArrayCell(Id(arr), [NumLit(0.0)]), BinaryOp(+, NumLit(10.0), NumLit(20.0)))]))])"
        self.assertTrue(TestAST.test(input, expect, 383))
        
    def test85(self):
        input = """func inlist(number arr[3]) 
begin
    ## print array
end
func main()
begin
    number arr[3] <- [1, 2, 3]
    inlist(arr)
end
"""
        expect = "Program([FuncDecl(Id(inlist), [VarDecl(Id(arr), ArrayType([3.0], NumberType), None, None)], Block([])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), CallStmt(Id(inlist), [Id(arr)])]))])"
        self.assertTrue(TestAST.test(input, expect, 384))
        
    def test86(self):
        input = """func main()
begin
    main([1,2,3,4])
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([CallStmt(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))])]))])"
        self.assertTrue(TestAST.test(input, expect, 385))
        
    def test87(self):
        input = """func dieubong() 
begin
    return 10
end
func main()
begin
    number arr[3] <- [dieubong(), dieubong(), dieubong()]
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([Return(NumLit(10.0))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(CallExpr(Id(dieubong), []), CallExpr(Id(dieubong), []), CallExpr(Id(dieubong), [])))]))])"
        self.assertTrue(TestAST.test(input, expect, 386))
     
    def test88(self):
        input = """func add(number a, number b) 
begin
    return a + b
end
func main()
begin
    number sum <- 0
    for i until 10 by 1 
    begin
        sum <- add(sum, i)
    end
end
"""
        expect = "Program([FuncDecl(Id(add), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(+, Id(a), Id(b)))])), FuncDecl(Id(main), [], Block([VarDecl(Id(sum), NumberType, None, NumLit(0.0)), For(Id(i), NumLit(10.0), NumLit(1.0), Block([AssignStmt(Id(sum), CallExpr(Id(add), [Id(sum), Id(i)]))]))]))])"
        self.assertTrue(TestAST.test(input, expect, 387))
        
    def test89(self):
        input = """func add(number a, number b) 
begin
    return a + b
end
func dieubong() 
begin
    return add(10, 20)
end
"""
        expect = "Program([FuncDecl(Id(add), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(+, Id(a), Id(b)))])), FuncDecl(Id(dieubong), [], Block([Return(CallExpr(Id(add), [NumLit(10.0), NumLit(20.0)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 388))
    
    def test90(self):
        input = """func dieubong() 
begin
    return 10
end
func main() 
begin
    number arr[3] <- [dieubong(), dieubong(), dieubong()]
    number ngta <- arr[dieubong()]
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([Return(NumLit(10.0))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(CallExpr(Id(dieubong), []), CallExpr(Id(dieubong), []), CallExpr(Id(dieubong), []))), VarDecl(Id(ngta), NumberType, None, ArrayCell(Id(arr), [CallExpr(Id(dieubong), [])]))]))])"
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test91(self):
        input = """func dieubong() 
begin
    return 10
end
func main() 
begin
    number arr[3] <- [1, 2, 3]
    arr[dieubong()] <- 10
end
"""
        expect = "Program([FuncDecl(Id(dieubong), [], Block([Return(NumLit(10.0))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), AssignStmt(ArrayCell(Id(arr), [CallExpr(Id(dieubong), [])]), NumLit(10.0))]))])"
        self.assertTrue(TestAST.test(input, expect, 390))
        
    def test92(self):

        input = """func main()
begin
    if (main([1,2,3,4])) begin
        var x <- 2
    end
    else begin
        string arr[1,2,3] <- main[beo()]
        return
    end
end 
"""
        expect = "Program([FuncDecl(Id(main), [], Block([If((CallExpr(Id(main), [ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0))]), Block([VarDecl(Id(x), None, var, NumLit(2.0))])), [], Block([VarDecl(Id(arr), ArrayType([1.0, 2.0, 3.0], StringType), None, ArrayCell(Id(main), [CallExpr(Id(beo), [])])), Return()]))]))])"
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test93(self):
        input = """func main()
begin
    number x <- 10
    number y <- 20
    number z <- x + y
    number arr[3] <- [1, 2, 3]
    number sum <- arr[0] + arr[1] + arr[2]
    number kq <- add(x, y)
end
func add(number a, number b) 
    begin
        return a + b
    end
    """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, NumLit(10.0)), VarDecl(Id(y), NumberType, None, NumLit(20.0)), VarDecl(Id(z), NumberType, None, BinaryOp(+, Id(x), Id(y))), VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), VarDecl(Id(sum), NumberType, None, BinaryOp(+, BinaryOp(+, ArrayCell(Id(arr), [NumLit(0.0)]), ArrayCell(Id(arr), [NumLit(1.0)])), ArrayCell(Id(arr), [NumLit(2.0)]))), VarDecl(Id(kq), NumberType, None, CallExpr(Id(add), [Id(x), Id(y)]))])), FuncDecl(Id(add), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([Return(BinaryOp(+, Id(a), Id(b)))]))])"
        self.assertTrue(TestAST.test(input, expect, 392))
        
    def test94(self):
        input = """func main()
begin
    number x <- 10 * 20 / 30 % 40 - 50 + 60
    number arr[3] <- [1 + 2 * 3, 4 / 5 - 6, 7 % 8 + 9]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(x), NumberType, None, BinaryOp(+, BinaryOp(-, BinaryOp(%, BinaryOp(/, BinaryOp(*, NumLit(10.0), NumLit(20.0)), NumLit(30.0)), NumLit(40.0)), NumLit(50.0)), NumLit(60.0))), VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(BinaryOp(+, NumLit(1.0), BinaryOp(*, NumLit(2.0), NumLit(3.0))), BinaryOp(-, BinaryOp(/, NumLit(4.0), NumLit(5.0)), NumLit(6.0)), BinaryOp(+, BinaryOp(%, NumLit(7.0), NumLit(8.0)), NumLit(9.0))))]))])"
        self.assertTrue(TestAST.test(input, expect, 393))
        
    def test95(self):
        input = """func cal(number a, number b) 
begin
    if (a > b) 
    begin
        return a - b
    end
    elif (a < b) 
    begin
        return b - a
    end
    else 
    begin
        return a * b
    end
end
func main()
begin
    number kq <- cal(10, 20)
end
"""
        expect = "Program([FuncDecl(Id(cal), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), Block([Return(BinaryOp(-, Id(a), Id(b)))])), [(BinaryOp(<, Id(a), Id(b)), Block([Return(BinaryOp(-, Id(b), Id(a)))]))], Block([Return(BinaryOp(*, Id(a), Id(b)))]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(kq), NumberType, None, CallExpr(Id(cal), [NumLit(10.0), NumLit(20.0)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 394))
        
    def test96(self):
        input = """func pcsarr(number arr[3]) 
    begin
        for i until 3 by 1 
        begin
            arr[i] <- arr[i] * 2
        end
    end
func main()
begin
    number arr[3] <- [1, 2, 3]
    pcsarr(arr)
end
"""
        expect = "Program([FuncDecl(Id(pcsarr), [VarDecl(Id(arr), ArrayType([3.0], NumberType), None, None)], Block([For(Id(i), NumLit(3.0), NumLit(1.0), Block([AssignStmt(ArrayCell(Id(arr), [Id(i)]), BinaryOp(*, ArrayCell(Id(arr), [Id(i)]), NumLit(2.0)))]))])), FuncDecl(Id(main), [], Block([VarDecl(Id(arr), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0))), CallStmt(Id(pcsarr), [Id(arr)])]))])"
        self.assertTrue(TestAST.test(input, expect, 395))
        
    def test97(self):
        input = """func cpxF(number a, number b) 
func main()
begin
    number kq <- cpxF(10, 5)
end
func cpxF(number a, number b) 
    begin
        if (a > b) 
        begin
            for i until a by 1 
            begin
                if (i % 2 = 0) 
                begin
                    a <- a - i
                end
            end
        end
        return a
    end
"""
        expect = "Program([FuncDecl(Id(cpxF), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], None), FuncDecl(Id(main), [], Block([VarDecl(Id(kq), NumberType, None, CallExpr(Id(cpxF), [NumLit(10.0), NumLit(5.0)]))])), FuncDecl(Id(cpxF), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None)], Block([If((BinaryOp(>, Id(a), Id(b)), Block([For(Id(i), Id(a), NumLit(1.0), Block([If((BinaryOp(=, BinaryOp(%, Id(i), NumLit(2.0)), NumLit(0.0)), Block([AssignStmt(Id(a), BinaryOp(-, Id(a), Id(i)))])), [], None)]))])), [], None), Return(Id(a))]))])"
        self.assertTrue(TestAST.test(input, expect, 396))
        
    def test98(self):
        input = """func nyc()
begin
    if (nyc() < 2) return nyc()[1] != not 2
end
"""
        expect = "Program([FuncDecl(Id(nyc), [], Block([If((BinaryOp(<, CallExpr(Id(nyc), []), NumLit(2.0)), Return(BinaryOp(!=, ArrayCell(CallExpr(Id(nyc), []), [NumLit(1.0)]), UnaryOp(not, NumLit(2.0))))), [], None)]))])"
        self.assertTrue(TestAST.test(input, expect, 397))
        
    def test99(self):
        input = """number x <- 10
number y <- 20
number z <- x * y / 2 + 3 - 4 % 5
number arr[5] <- [1, 2, 3, 4, 5]
number sum <- arr[0] + arr[1] * arr[2] - arr[3] / arr[4]
func cal(number a, number b, number c) 
begin
    return a * b / c + a - b % c
end

func main()
begin
    number kq <- cal(x, y, z)
    number finalkq <- kq + sum * arr[2]
end
"""
        expect = "Program([VarDecl(Id(x), NumberType, None, NumLit(10.0)), VarDecl(Id(y), NumberType, None, NumLit(20.0)), VarDecl(Id(z), NumberType, None, BinaryOp(-, BinaryOp(+, BinaryOp(/, BinaryOp(*, Id(x), Id(y)), NumLit(2.0)), NumLit(3.0)), BinaryOp(%, NumLit(4.0), NumLit(5.0)))), VarDecl(Id(arr), ArrayType([5.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0), NumLit(5.0))), VarDecl(Id(sum), NumberType, None, BinaryOp(-, BinaryOp(+, ArrayCell(Id(arr), [NumLit(0.0)]), BinaryOp(*, ArrayCell(Id(arr), [NumLit(1.0)]), ArrayCell(Id(arr), [NumLit(2.0)]))), BinaryOp(/, ArrayCell(Id(arr), [NumLit(3.0)]), ArrayCell(Id(arr), [NumLit(4.0)])))), FuncDecl(Id(cal), [VarDecl(Id(a), NumberType, None, None), VarDecl(Id(b), NumberType, None, None), VarDecl(Id(c), NumberType, None, None)], Block([Return(BinaryOp(-, BinaryOp(+, BinaryOp(/, BinaryOp(*, Id(a), Id(b)), Id(c)), Id(a)), BinaryOp(%, Id(b), Id(c))))])), FuncDecl(Id(main), [], Block([VarDecl(Id(kq), NumberType, None, CallExpr(Id(cal), [Id(x), Id(y), Id(z)])), VarDecl(Id(finalkq), NumberType, None, BinaryOp(+, Id(kq), BinaryOp(*, Id(sum), ArrayCell(Id(arr), [NumLit(2.0)]))))]))])"
        self.assertTrue(TestAST.test(input, expect, 398))
        
    def test100(self):
        input = """func main()
begin
    a[2] <- a[0]
end
"""
        expect = "Program([FuncDecl(Id(main), [], Block([AssignStmt(ArrayCell(Id(a), [NumLit(2.0)]), ArrayCell(Id(a), [NumLit(0.0)]))]))])"
        self.assertTrue(TestAST.test(input, expect, 399))
        