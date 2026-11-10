import unittest
from PasswordChecker import check_password


class PasswordCheckerTesting(unittest.TestCase):

    def test_correct_passwords(self):
        self.assertTrue(check_password("SecurePass123!"))

    def test_short_passwords(self):
        self.assertFalse(check_password("Hello12!"))

    def test_no_uppercases(self):
        self.assertFalse(check_password("securepass123!"))

    def test_no_numbers(self):
        self.assertFalse(check_password("SecurePassword!"))

    def test_no_special_characters(self):
        self.assertFalse(check_password("SecurePass123"))

    def test_no_lowercase(self):
        self.assertFalse(check_password("SECUREPASS123!"))


if __name__ == "__main__":
    unittest.main()


