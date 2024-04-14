import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_400(self):
        input = """dynamic a
number b[3] <- [TRUE,2,a]
func main()
begin
    return
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
    return
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
        return
    end
        """
        expect = "Type Mismatch In Statement: foo(a,a)"
        self.assertTrue(TestChecker.test(input, expect, 401))
