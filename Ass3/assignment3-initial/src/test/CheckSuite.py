import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    def test_400(self):
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 400))
        
    def test_401(self):
        input = """number b
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 401))
