import unittest

from diagnostic_demo import add


class DiagnosticDemoTests(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_and_positive_numbers(self):
        self.assertEqual(add(-2, 3), 1)

    def test_intentional_failure(self):
        self.assertEqual(add(2,3),6)


if __name__ == "__main__":
    unittest.main()
