import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from portfolio import Portfolio

class TestPortfolio(unittest.TestCase):
    
    def setUp(self):
        """Run before each test - creates fresh portfolio"""
        self.portfolio = Portfolio()  # Default 66000
        self.customPortfolio = Portfolio(100000)  # Custom amount
    
    # Test 1: Initialization
    def test_default_initial_cash(self):
        """Test portfolio starts with default cash"""
        self.assertEqual(self.portfolio.getCashBalance(), 66001)

if __name__ == '__main__':
    unittest.main()        