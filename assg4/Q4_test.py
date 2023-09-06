import unittest
from Q4 import validate_email

class TestValidateEmail(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "nsommer@wooster.edu",
            "n.sommer@cs.wooster.edu",
            "yippee_skippy@yee-haw.wheeeee",
            "fun-times@Taylor.hall.wooster.edu",
        ]
        for email in valid_emails:
            self.assertTrue(validate_email(email))

    def test_invalid_emails(self):
        invalid_emails = [
            "n@sommer@wooster.edu",
            "n sommer@wooster.edu",
            "nsommer@wooster..edu",
            "nsommer@wooster.edu-org",
        ]
        for email in invalid_emails:
            self.assertFalse(validate_email(email))

if __name__ == '__main__':
    unittest.main()