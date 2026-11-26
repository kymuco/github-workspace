import math
import unittest

from geometry import circle_area, rectangle_area


class GeometryTests(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3), 9 * math.pi)
        self.assertEqual(circle_area(0), 0)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(4, 5), 20)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(4, 0), 0)

    def test_negative_dimensions(self):
        with self.assertRaises(ValueError):
            circle_area(-1)
        with self.assertRaises(ValueError):
            rectangle_area(-1, 2)
        with self.assertRaises(ValueError):
            rectangle_area(2, -1)


if __name__ == "__main__":
    unittest.main()
