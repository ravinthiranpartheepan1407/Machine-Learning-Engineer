import unittest
import main
import smtplib

class Email_Test(unittest.TestCase):
    obj_email = main.email
    obj_message = main.message
    obj_content = main.content
    def test_email_message(self, obj_email, obj_message, obj_content):
        try:
            self.assertIs(obj_email is str)
            self.assertIs(obj_message is str)
            self.assertIs(obj_content is str)
        except:
            raise ValueError("Please Enter the required fields")
    def test_email_connection(self):
        smtplib.SMTP_PORT = 587
        try:
            self.assertEqual(smtplib.SMTP_PORT, 587)
        except:
            raise smtplib.SMTPServerDisconnected("Sever connected on some other unkown port")

unittest.main()
    

