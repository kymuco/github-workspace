"""Tests for string_utils.reverse_text."""

import unittest

from string_utils import reverse_text


class ReverseTextTests(unittest.TestCase):
    def test_regular_text(self):
        self.assertEqual(reverse_text("hello"), "olleh")

    def test_empty_text(self):
        self.assertEqual(reverse_text(""), "")

    def test_empty_text_type_and_length(self):
        result = reverse_text("")
        self.assertIsInstance(result, str)
        self.assertEqual(len(result), 0)

    def test_unicode_text(self):
        self.assertEqual(reverse_text("привет"), "тевирп")


if __name__ == "__main__":
    unittest.main()
