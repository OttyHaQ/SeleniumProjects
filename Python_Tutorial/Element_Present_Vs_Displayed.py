
# checking if element is present

driver.find_element(By.ID, 'site-header-cart')


# checking if element is displayed

if my element.is_displayed:
    element.click()
else:
    raise Exception("Element not displayed")

