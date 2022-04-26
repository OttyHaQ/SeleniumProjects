

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
url = 'http://demostore.supersqa.com'
driver.implicitly_wait(5)

driver.get(url)

def my_Acct():
    my_Account = driver.find_element(By.LINK_TEXT, 'My account')
    my_Account.click()

def user_reg():
    email = driver.find_element(By.ID, 'reg_email')
    email.send_keys('gvcijhl@supersqa.com')

    passwd = driver.find_element(By.ID, 'reg_password')
    passwd.send_keys('Jklmnpass1254.')

    time.sleep(3)

    register = driver.find_element(By.XPATH, "//*[@id='customer_login']/div[2]/form/p[3]/button")
    register.click()

def log_out():
    driver.find_element(By.XPATH, '//*[@id="post-9"]/div/div/nav/ul/li[6]/a').click()

my_Acct()
user_reg()
log_out()

print("TEST PASSED")

driver.quit()
