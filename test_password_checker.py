import unittest
from PasswordChecker import check_password


class PasswordCheckerTesting(unittest.TestCase):

    def test_correct_passwords(self):
        self.assertTrue(check_password("HelloWorld123!"))

    def test_short_passwords(self):
        self.assertFalse(check_password("Hello12!"))

    def test_no_uppercases(self):
        self.assertFalse(check_password("helloworld123!"))

    def test_no_numbers(self):
        self.assertFalse(check_password("HelloWorld!"))

    def test_no_special_characters(self):
        self.assertFalse(check_password("HelloWorld123"))


if __name__ == "__main__":
    unittest.main()


