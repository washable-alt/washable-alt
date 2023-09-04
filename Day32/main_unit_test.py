import os

from dotenv import load_dotenv
import unittest

class main(unittest.TestCase):
    
    load_dotenv()
    email_sender = os.getenv("EMAIL_SENDER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_receiver = os.getenv("EMAIL_RECEIVER")

    def test_email_sender_equals_true(self):
        self.assertTrue(os.getenv("EMAIL_SENDER").lower(), "Insert sender email address here")

    def test_email_password_equals_true(self):
        self.assertEqual;(os.getenv("EMAIL_PASSWORD").lower(), "Insert gmail app password")

    def test_email_receiver_equals_true(self):
        self.assertEqual(os.getenv("EMAIL_RECEIVER").lower(), "Insert receiver email address here")
    


if __name__ == "__main__":
    try:
        unittest.main()
    except AssertionError as e:
        print(e)
