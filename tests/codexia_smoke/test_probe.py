import unittest


class SmokeProbe(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(2 + 2, 4)
