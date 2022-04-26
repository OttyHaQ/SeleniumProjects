
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
Url = 'http://demostore.supersqa.com'
driver.get(Url)

#-----Implicit wait----#
# Makes driver wait for elements to load before find items.(race condition)
# Set only once

driver.implicitly_wait(10)          # implicit wait

my_image = driver.find_element(By.ID, 'the slow image')
my_image.click()


#-----Explicit wait-----#
# Need to set it anytime we need it

from selenium.webdriver.support.ui import webDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = webDriverWait(driver, 10)
my_image = wait.until(EC.visibility_of_element_located((By.ID, 'the slow image')))

# EC = Expected condition (there are a lot)

print("image found")

'''!!! Never mix implicit with explicit wait !!!'''

