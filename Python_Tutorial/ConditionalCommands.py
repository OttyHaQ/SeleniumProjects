from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("C:/Users/INY/chromedriver_win32/chromedriver")
driver = webdriver.Chrome(service=s)

url = "https://www.renmoney.com/"
driver.get(url)

driver.find_element(By.XPATH, "//*[@id='Header']/div[1]/div[1]/div[2]/a[1]").click()

email=driver.find_element(By.NAME, "email")
email.send_keys("akpanudootobong@gmail.com")

driver.find_element(By.XPATH, "/html/body/app-root/app-auth/div/div/app-login/div/button").click()

password=driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("Nsisong03.")
driver.find_element(By.NAME, "submit").click()


'''print(pwd.is_displayed())
print(pwd.is_enabled)

user_name.send_keys("mercury")
pwd.send_keys("mercury")

driver.find_element(By.NAME, "login").click()

round_trip=driver.find_element(By.CSS_SELECTOR, "input[value=roundtrip]")

print("Round trip button selection status: ", round_trip.is_selected())

one_way_trip=driver.find_element(By.CSS_SELECTOR, "input[value=oneway]")

print("Oneway trip button selection status: ", one_way_trip.is_selected())'''
