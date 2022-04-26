from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path="C:/Users/INY/chromedriver_win32/chromedriver")
s = Service("C:/Users/INY/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=s)
url = "http://newtours.demoaut.com/"
driver.get(url)

print(driver.title)
print(driver.current_url)
print(driver.page_source)

driver.close()

'''driver = webdriver.Firefox(executable_path="C:/Users/INY/C:/Users/INY/geckodriver-v0.30.0-win64/geckodriver")
url = "http://newtours.demoaut.com/"
driver.get(url)
print(driver.title)


driver.close()'''