import unittest

from feedback_demo import multiply


class FeedbackDemoTests(unittest.TestCase):
    def test_positive_small(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_positive_large(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_negative(self):
        self.assertEqual(multiply(-2, 3), -6)


if __name__ == "__main__":
    unittest.main()
