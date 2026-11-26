import unittest

from distance import kilometers_to_meters, meters_to_kilometers


class DistanceTests(unittest.TestCase):
    def test_kilometers_to_meters(self):
        self.assertEqual(kilometers_to_meters(5), 5000)

    def test_meters_to_kilometers(self):
        self.assertEqual(meters_to_kilometers(2500), 2.5)

    def test_zero_and_fractional_values(self):
        self.assertEqual(kilometers_to_meters(0), 0)
        self.assertEqual(meters_to_kilometers(0), 0)
        self.assertAlmostEqual(kilometers_to_meters(1.2345), 1234.5)
        self.assertAlmostEqual(meters_to_kilometers(12.5), 0.0125)


if __name__ == "__main__":
    unittest.main()
