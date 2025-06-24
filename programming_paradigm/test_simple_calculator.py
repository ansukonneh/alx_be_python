import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a new calculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test addition of two numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtraction(self):
        """Test subtraction of two numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(-5, 5), -10)

    def test_multiplication(self):
        """Test multiplication of two numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_division(self):
        """Test division of two numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(-9, 3), -3.0)
        self.assertEqual(self.calc.divide(-6, -2), 3.0)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero should return None
        self.assertEqual(self.calc.divide(0, 5), 0.0)

if __name__ == '__main__':
    unittest.main()
