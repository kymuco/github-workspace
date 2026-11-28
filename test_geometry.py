"""Unit tests for the geometry module."""

import math
import unittest

from geometry import Circle, Rectangle, Triangle


class CircleTests(unittest.TestCase):
    def test_area_and_perimeter(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), 4 * math.pi)
        self.assertAlmostEqual(circle.perimeter(), 4 * math.pi)

    def test_fractional_radius(self):
        circle = Circle(0.5)
        self.assertAlmostEqual(circle.area(), 0.25 * math.pi)
        self.assertAlmostEqual(circle.perimeter(), math.pi)

    def test_invalid_radius(self):
        for radius in (0, -1, float("inf"), -float("inf"), float("nan"), True, "2", None):
            with self.subTest(radius=radius), self.assertRaises(ValueError):
                Circle(radius)


class RectangleTests(unittest.TestCase):
    def test_area_and_perimeter(self):
        rectangle = Rectangle(3, 4)
        self.assertAlmostEqual(rectangle.area(), 12)
        self.assertAlmostEqual(rectangle.perimeter(), 14)

    def test_fractional_dimensions(self):
        rectangle = Rectangle(1.5, 2.25)
        self.assertAlmostEqual(rectangle.area(), 3.375)
        self.assertAlmostEqual(rectangle.perimeter(), 7.5)

    def test_invalid_dimensions(self):
        invalid = (
            (0, 2), (2, 0), (-1, 2), (2, -1),
            (float("inf"), 2), (2, float("nan")), (True, 2),
        )
        for width, height in invalid:
            with self.subTest(width=width, height=height), self.assertRaises(ValueError):
                Rectangle(width, height)


class TriangleTests(unittest.TestCase):
    def test_area_and_perimeter(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)
        self.assertAlmostEqual(triangle.perimeter(), 12)

    def test_fractional_sides(self):
        triangle = Triangle(1.5, 2, 2.5)
        self.assertAlmostEqual(triangle.area(), 1.5)
        self.assertAlmostEqual(triangle.perimeter(), 6)

    def test_equilateral_triangle(self):
        triangle = Triangle(2, 2, 2)
        self.assertAlmostEqual(triangle.area(), math.sqrt(3))
        self.assertAlmostEqual(triangle.perimeter(), 6)

    def test_impossible_triangles(self):
        for sides in ((1, 2, 3), (1, 1, 3), (2, 3, 5), (1, 2, 4)):
            with self.subTest(sides=sides), self.assertRaises(ValueError):
                Triangle(*sides)

    def test_invalid_sides(self):
        invalid = (
            (0, 3, 4), (-1, 3, 4), (3, 4, float("inf")),
            (float("nan"), 4, 5), (True, 4, 5), ("3", 4, 5),
        )
        for sides in invalid:
            with self.subTest(sides=sides), self.assertRaises(ValueError):
                Triangle(*sides)


if __name__ == "__main__":
    unittest.main()
