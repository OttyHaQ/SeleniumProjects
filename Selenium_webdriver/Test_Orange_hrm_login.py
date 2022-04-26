from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HtmlTestRunner

class OrangeHrmTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title does not match")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        userName = self.driver.find_element(By.NAME, "txtUsername")
        password = self.driver.find_element(By.NAME, "txtPassword")
        submit = self.driver.find_element(By.NAME, "Submit")
        userName.send_keys("Admin")
        password.send_keys("admin123")
        submit.click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title does not match")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\INY\\SeleniumProjects\\generating_HTML_report\\Reports'))

# run python Test_Orange_hrm_login.py in the terminal to generate html report