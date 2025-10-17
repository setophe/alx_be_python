"""import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(SimpleCalculator.add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(SimpleCalculator.subtract(1, 2), -1)

    def test_division(self):
        self.assertEqual(SimpleCalculator.divide(4, 2), 2)
        self.assertEqual(SimpleCalculator.divide(4, 0),)

    def test_multiplication(self):
        self.assertEqual(SimpleCalculator.multiply(4, 2), 8)"""

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(-5, 5), -10)
        self.assertEqual(self.calc.subtract(10.5, 2.5), 8.0)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(-4, -5), 20)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(5, -1), -5)
        self.assertEqual(self.calc.divide(-8, -2), 4)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_division_by_zero(self):
        """Test that dividing by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

if __name__ == '__main__':
    unittest.main()