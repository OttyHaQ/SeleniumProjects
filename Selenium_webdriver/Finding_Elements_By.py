

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.keys import Keys
import pdb

driver = webdriver.Chrome()
Url = 'http://demostore.supersqa.com'
driver.get(Url)
time.sleep(3)

#------- By.ID--------------#

cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()
time.sleep(3)

driver.back()               # to previous page
time.sleep(3)
driver.forward()            # opposite of the above
time.sleep(3)
driver.quit()

driver.get('http://demostore.supersqa.com/my-account')
'''user_Name = driver.find_element(By.ID, 'username')
user_Name.send_keys('myusername')
time.sleep(3)
driver.quit()'''

#--------By.CSS_Selector-------#

my_acct = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
my_acct.click()

#--------By.XPATH-------#

sample_page = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[5]/a')
sample_page.click()

#------By.NAME--------#

my_acct = driver.find_element(By.NAME, 'Name')

#-----By.CLASS_NAME-----#

my_acct = driver.find_element(By.CLASS_NAME, 'Class_Name')

#-----By.TAG_NAME-------#

my_acct = driver.find_element(By.TAG_NAME, 'Tag_Name')

#-----By.LINK_TEXT-------#

my_acct = driver.find_element(By.LINK_TEXT, 'Link_text')

#------By.PARTIAL_LINK_TEXT-----#

my_acct = driver.find_element(By.PARTIAL_LINK_TEXT, 'Partial_link_text')

# driver.find_element finds one or the first one it sees
# driver.find_elements finds all with the attribute

