import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_400(self):
        input = """dynamic a
number b[3] <- [TRUE,2,a]
func main()
begin
end
        """
        expect = "Type Mismatch In Expression: [TRUE,2,a]"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_401(self):
        # a and d should be inferred by BoolType?
        input = """dynamic a
dynamic d
number b[3] <- [a,TRUE,d]
func main()
begin
end
        """
        expect = "Type Mismatch In Statement: number b[3] <- [a,TRUE,d]"
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_402(self):
        input = """dynamic a
func foo(number b, string c)
    begin
        foo(a,a)    
    end
func main()
    begin
    end
        """
        expect = "Type Mismatch In Statement: foo(a,a)"
        self.assertTrue(TestChecker.test(input, expect, 402))
        
    def test_403(self):
        input = """
func foo()
func foo()
    begin
        return
    end
func foo()
    return
func main()
    begin
    end
        """
        expect = """Redeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 403))
        
    def test_404(self):
        input = """dynamic a
dynamic d
number b[3] <- [a,1,2,d]
func main()
begin
end
        """
        expect = "Type Mismatch In Statement: number b[3] <- [a,1,2,d]"
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_405(self):
        input = """dynamic a
dynamic d
number b[1,2,3] <- [[a],[a,d],[d]]
func main()
begin
end
        """
        expect = "Type Mismatch In Statement: number b[1,2,3] <- [[a],[a,d],[d]]"
        self.assertTrue(TestChecker.test(input, expect, 405))
        
    def test_406(self):
        input = """dynamic a
dynamic d
number b[1,2,3] <- [[a],[a,d],[d,d,d]]
bool c <- a
func main()
begin
end
        """
        expect = "Type Mismatch In Statement: bool c <- a"
        self.assertTrue(TestChecker.test(input, expect, 406))
        
    def test_407(self):
        input = """number a
bool d
number b[1,2,3] <- [[a],[a,a],[d,d,d]]
bool c <- a
func main()
begin
end
        """
        expect = "Type Mismatch In Expression: [[a],[a,a],[d,d,d]]"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_408(self):
        input = """
func foo()
func main()
func main()
begin
end
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
        
    def test_409(self):
        input = """
func foo(number a, bool b, string c) return
func main()
begin
    number a
    bool b
    a = foo(a, b)
end
        """
        expect = "Type Mismatch In Expression: foo(a, b)"
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test_410(self):
        input = """
func foo(number a, bool b, string c)
func main()
begin
    number a
    bool b
    a = foo(a, b, c)
end
        """
        expect = "No Function Definition: foo"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_411(self):
        input = """
func foo(number a, bool b, string c) return
func main()
begin
    dynamic a
    bool b
    dynamic c
    a = foo(a, c, b)
end
        """
        expect = "Type Mismatch In Expression: foo(a, c, b)"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    def test_412(self):
        input = """
func foo(number a[3], bool b, string c) return
func main()
begin
    number a[4]
    bool b
    dynamic c
    a = foo(a, b, c)
end
        """
        expect = "Type Mismatch In Expression: foo(a, b, c)"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test_413(self):
        input = """
func foo(number a[3], bool b, string c) return
func main()
begin
    bool a[3]
    bool b
    dynamic c
    a = foo(a, b, c)
end
        """
        expect = "Type Mismatch In Expression: foo(a, b, c)"
        self.assertTrue(TestChecker.test(input, expect, 413))
        
    def test_414(self):
        input = """
func foo(number a[3], bool b, string c) return
func main()
begin
    number a[3]
    bool b
    dynamic c
    a = foo(a, b, c)
end
        """
        expect = "Type Mismatch In Expression: foo(a, b, c)"
        # foo has VoidType, i dont compare type at stmt, but make condition at CallExpr
        # from spec: For a function call <function-name>(<args>), the callee <method name> must have
        # non-void as return type
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test_415(self):
        input = """
func foo(number a[3], bool b, string c) return b
func main()
begin
    number a[3]
    bool b
    dynamic c
    a = foo(a, b, c)
end
        """
        expect = "Type Mismatch In Statement: a = foo(a, b, c)"
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    def test_416(self):
        input = """
dynamic foo
func foo(number a[3], bool b, string c) return b
func main()
begin
    foo=foo(foo, foo, foo)
end
        """
        expect = "Type Mismatch In Expression: foo(foo, foo, foo)"
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_417(self):
        input = """
func foo()
func foo(number a[3], bool b, string c)
func foo(string c) return b
func main()
begin
    foo=foo(foo, foo, foo)
end
        """
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_418(self):
        input = """
func foo(number a[3], bool b, string c)
func foo(string c) return b
func main()
begin
    foo=foo(foo)
end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 418))
        
    def test_419(self):
        input = """
dynamic a
func foo (number b) return a
func main()
begin
    foo=foo(foo)
end
        """
        expect = "Type Cannot Be Inferred: return a"
        self.assertTrue(TestChecker.test(input, expect, 419))
        
    def test_420(self):
        input = """
number a[3] <- [1,2,3]
func foo (number b)
    begin
        a[1] <- b + a[2]
        return a
    end
func main()
begin
    dynamic c
    foo(a[1])[1] = a[c] + a[1,2]
end
        """
        expect = "Type Mismatch In Expression: a[1,2]"
        #if we check size of array?
        self.assertTrue(TestChecker.test(input, expect, 420))
        
    def test_421(self):
        input = """
number a[3] <- [1,2,3]
func foo (number b)
    begin
        a[1] <- b + a[2]
        dynamic c
        foo(a[1])[1] = a[c] + a[2]
        return a
    end
func main()
begin
end
        """
        expect = "Type Mismatch In Expression: foo(a[1])[1]"
        # how to infer?
        # or raise error (we check if ctx.arr in ArrayCell is ArrayType)
        self.assertTrue(TestChecker.test(input, expect, 421))
