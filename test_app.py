import unittest

from app import add_numbers, get_greeting


class TestApplication(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -3), -8)

    def test_add_zero(self):
        self.assertEqual(add_numbers(10, 0), 10)

    def test_greeting(self):
        self.assertEqual(
            get_greeting("DevOps"),
            "Hello, DevOps! Welcome to the CI/CD application."
        )


if __name__ == "__main__":
    unittest.main()