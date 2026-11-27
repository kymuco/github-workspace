"""Diagnostic unittest suite with one intentionally failing assertion."""

import unittest

from diagnostic_demo import add


class DiagnosticDemoTests(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-4, 1), -3)

    def test_intentional_failure(self):
        self.assertEqual(add(2, 3), 6)


if __name__ == "__main__":
    unittest.main()
