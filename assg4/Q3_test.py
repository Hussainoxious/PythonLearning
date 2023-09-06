import unittest
from Q3 import validate_number

class TestPhoneNumberValidation(unittest.TestCase):
    def test_valid_numbers(self):
        valid_numbers = [
            "(123)456-7890",
            "(123) 456-7890",
            "123-456-7890",
            "(123)456-7890",
        ]
        for phone_number in valid_numbers:
            self.assertTrue(validate_number(phone_number))

    def test_invalid_numbers(self):
        invalid_numbers = [
            "1234567890",
            "(123)-456-7890",
            "123 456-7890",
        ]
        for phone_number in invalid_numbers:
            self.assertFalse(validate_number(phone_number))

if __name__ == '__main__':
    unittest.main()
