from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
import time

s = Service("C:/Users/INY/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=s)
url1 = "http://demo.automationtesting.in/Windows.html"
url2 = "http://newtours.demoaut.com/"
driver.get(url1)
print(driver.title)

time.sleep(3)

driver.get(url2)
print(driver.title)

time.sleep(3)

driver.back()
print(driver.title)

time.sleep(3)

driver.forward()
print(driver.title)

time.sleep(5)

driver.quit()