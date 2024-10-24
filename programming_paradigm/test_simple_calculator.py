import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(7, 3), 10)
        self.assertEqual(self.calc.add(9, -2), 7)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(-4, 3), -7)
        self.assertEqual(self.calc.subtract(10, -3), 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.subtract(-2, 3), -6)
        self.assertEqual(self.calc.subtract(8, -3), 5)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertEqual(self.calc.subtract(10, 5), 2)
        self.assertEqual(self.calc.subtract(25, 5), 5)