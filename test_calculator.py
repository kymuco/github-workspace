"""Unit tests for the calculator module."""

import unittest

from calculator import add, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-4, -6), -10)

    def test_add_zero(self):
        self.assertEqual(add(-4, 0), -4)

    def test_add_fractions(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_subtract_positive(self):
        self.assertEqual(subtract(8, 3), 5)

    def test_subtract_negative(self):
        self.assertEqual(subtract(-8, -3), -5)

    def test_subtract_zero(self):
        self.assertEqual(subtract(0, 5), -5)

    def test_subtract_fractions(self):
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)

    def test_multiply_positive(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-4, 5), -20)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, -5), 0)

    def test_multiply_fractions(self):
        self.assertAlmostEqual(multiply(0.2, 0.3), 0.06)

    def test_divide_positive(self):
        self.assertEqual(divide(12, 4), 3)

    def test_divide_negative_numerator(self):
        self.assertEqual(divide(-12, 4), -3)

    def test_divide_negative_denominator(self):
        self.assertEqual(divide(12, -4), -3)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 4), 0)

    def test_divide_fractions(self):
        self.assertAlmostEqual(divide(0.3, 0.1), 3)

    def test_divide_by_integer_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_divide_by_float_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0.0)

    def test_divide_by_negative_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, -0.0)

    def test_zero_divided_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)


if __name__ == "__main__":
    unittest.main()
