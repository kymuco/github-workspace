"""Unit tests for the Vector2 API."""

from dataclasses import FrozenInstanceError
import math
import unittest

from vector2 import Vector2


class Vector2Tests(unittest.TestCase):
    def assertVectorAlmostEqual(self, actual, x, y):
        self.assertIsInstance(actual, Vector2)
        self.assertAlmostEqual(actual.x, x)
        self.assertAlmostEqual(actual.y, y)

    def test_coordinates_and_negative_fractional_values(self):
        self.assertVectorAlmostEqual(Vector2(-1.25, 2.5), -1.25, 2.5)

    def test_addition(self):
        self.assertVectorAlmostEqual(Vector2(1.5, -2) + Vector2(-3, 0.25), -1.5, -1.75)

    def test_subtraction(self):
        self.assertVectorAlmostEqual(Vector2(1.5, -2) - Vector2(-3, 0.25), 4.5, -2.25)

    def test_scalar_multiplication(self):
        self.assertVectorAlmostEqual(Vector2(-2, 1.5) * -0.5, 1, -0.75)

    def test_reverse_scalar_multiplication(self):
        self.assertVectorAlmostEqual(2.5 * Vector2(-2, 1.5), -5, 3.75)

    def test_scalar_division(self):
        self.assertVectorAlmostEqual(Vector2(-3, 1.5) / 2, -1.5, 0.75)

    def test_dot_product(self):
        self.assertAlmostEqual(Vector2(1.5, -2).dot(Vector2(-4, 0.5)), -7)

    def test_length(self):
        self.assertAlmostEqual(Vector2(-3, 4).length(), 5)
        self.assertAlmostEqual(Vector2(0, 0).length(), 0)

    def test_distance(self):
        self.assertAlmostEqual(Vector2(-1, 2).distance_to(Vector2(2, -2)), 5)
        self.assertAlmostEqual(Vector2(1.5, -2).distance_to(Vector2(1.5, -2)), 0)

    def test_normalization(self):
        original = Vector2(3, -4)
        unit = original.normalized()
        self.assertVectorAlmostEqual(unit, 0.6, -0.8)
        self.assertAlmostEqual(unit.length(), 1)
        self.assertVectorAlmostEqual(original, 3, -4)

    def test_zero_vector_arithmetic(self):
        zero = Vector2(0, 0)
        self.assertVectorAlmostEqual(zero + Vector2(-2, 3), -2, 3)
        self.assertVectorAlmostEqual(zero * 5, 0, 0)
        self.assertAlmostEqual(zero.dot(Vector2(1, 2)), 0)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            Vector2(1, 2) / 0

    def test_zero_vector_cannot_be_normalized(self):
        with self.assertRaises(ValueError):
            Vector2(0, 0).normalized()

    def test_nonfinite_coordinates(self):
        for x, y in ((math.inf, 1), (-math.inf, 1), (math.nan, 1), (1, math.nan)):
            with self.subTest(x=x, y=y), self.assertRaises(ValueError):
                Vector2(x, y)

    def test_invalid_coordinate_types(self):
        for x, y in ((True, 1), (1, False), ("1", 2), (1, None), (1 + 2j, 0)):
            with self.subTest(x=x, y=y), self.assertRaises(TypeError):
                Vector2(x, y)

    def test_invalid_operand_types(self):
        v = Vector2(1, 2)
        for operation in (
            lambda: v + (1, 2),
            lambda: v - 3,
            lambda: v * "3",
            lambda: "3" * v,
            lambda: v / "3",
            lambda: v.dot((1, 2)),
            lambda: v.distance_to((1, 2)),
        ):
            with self.subTest(operation=operation), self.assertRaises(TypeError):
                operation()

    def test_nonfinite_scalars(self):
        for scalar in (math.inf, -math.inf, math.nan):
            with self.subTest(scalar=scalar):
                with self.assertRaises(ValueError):
                    Vector2(1, 2) * scalar
                with self.assertRaises(ValueError):
                    Vector2(1, 2) / scalar

    def test_immutability(self):
        original = Vector2(1, -2)
        result = original + Vector2(3, 4)
        self.assertVectorAlmostEqual(original, 1, -2)
        self.assertVectorAlmostEqual(result, 4, 2)
        with self.assertRaises(FrozenInstanceError):
            original.x = 99


if __name__ == "__main__":
    unittest.main()
