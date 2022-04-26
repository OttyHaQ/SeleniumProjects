import unittest

class SignupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("This is signup by email")
        self.assertTrue(True)

    def test_signupbyFacebook(self):
        print("This is Signup by Facebook")
        self.assertTrue(True)

    def test_signupbyTwitter(self):
        print("This is Signup by twitter")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()