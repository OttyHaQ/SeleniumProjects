from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestOrangeHRM():

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homPageTitle(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        assert self.driver.title == "OrangeHRM"

    def test_login(self, setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        assert  self.driver.title == "OrangeHRM"

# To generate html report, parce the command "pytest -v -s --html=directory\report.html --self-contained-html  test_pytest_html_report.py"