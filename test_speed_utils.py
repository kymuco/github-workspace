import unittest

from speed_utils import kmh_to_ms, ms_to_kmh


class SpeedUtilsTests(unittest.TestCase):
    def test_kmh_to_ms(self):
        self.assertAlmostEqual(kmh_to_ms(36), 10)

    def test_ms_to_kmh(self):
        self.assertAlmostEqual(ms_to_kmh(10), 36)

    def test_zero_and_fractional_values(self):
        self.assertAlmostEqual(kmh_to_ms(0), 0)
        self.assertAlmostEqual(ms_to_kmh(0), 0)
        self.assertAlmostEqual(kmh_to_ms(5.4), 1.5)
        self.assertAlmostEqual(ms_to_kmh(1.25), 4.5)


if __name__ == "__main__":
    unittest.main()
