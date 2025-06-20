import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_subtraction(self):
        """Test the subtract method with various scenarios."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-4, -6), 2)
        self.assertEqual(self.calc.subtract(7, 0), 7)

    def test_multiplication(self):
        """Test the multiply method with various numbers."""
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-1, 6), -6)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(-2, -4), 8)

    def test_division(self):
        """Test the divide method with normal and edge cases."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-8, 2), -4)
        self.assertEqual(self.calc.divide(0, 5), 0)

        # Division by zero should raise an error
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_division_type_errors(self):
        """Test the divide method with invalid input types."""
        with self.assertRaises(TypeError):
            self.calc.divide("10", 2)

        with self.assertRaises(TypeError):
            self.calc.divide(None, 2)

        with self.assertRaises(TypeError):
            self.calc.divide(2, "0")

if __name__ == '__main__':
    unittest.main()