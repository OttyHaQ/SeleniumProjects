

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# Example 1: Placeholder
search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
place_holder = search_field.get_attribute('placeholder')
if place_holder != "search products...":
    raise Exception("Place holder for search field is not as expected. Actual: {}". format(place_holder))
else:
    print("PASS")

# Example 2: (See which tab is selected)

