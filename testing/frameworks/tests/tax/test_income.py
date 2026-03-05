import sys
import unittest
from pathlib import Path
sys.path.append("../../src/tax")
from income import calculate_tax

class TestTaxCalculator(unittest.TestCase):
    
    def test_income(self):
        self.assertEqual(calculate_tax(100), 13.0)

    def test_integers_coins(self):
        self.assertEqual(calculate_tax(10.5), 1.36)

if __name__ == "__main__":
    unittest.main()