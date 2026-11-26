import unittest

from time_utils import hours_to_minutes, minutes_to_seconds


class TimeUtilsTests(unittest.TestCase):
    def test_hours_to_minutes(self):
        self.assertEqual(hours_to_minutes(2), 120)

    def test_minutes_to_seconds(self):
        self.assertEqual(minutes_to_seconds(3), 180)

    def test_zero_and_fractional_values(self):
        self.assertEqual(hours_to_minutes(0), 0)
        self.assertEqual(minutes_to_seconds(0), 0)
        self.assertAlmostEqual(hours_to_minutes(1.25), 75.0)
        self.assertAlmostEqual(minutes_to_seconds(0.125), 7.5)


if __name__ == "__main__":
    unittest.main()
