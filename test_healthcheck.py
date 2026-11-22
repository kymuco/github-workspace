"""Tests for the minimal application health check."""

import unittest

from healthcheck import check_health


class HealthCheckTests(unittest.TestCase):
    def test_successful_call(self):
        self.assertIsNotNone(check_health())

    def test_result_type(self):
        self.assertIsInstance(check_health(), dict)

    def test_status_value(self):
        self.assertEqual(check_health()["status"], "ok")


if __name__ == "__main__":
    unittest.main()
