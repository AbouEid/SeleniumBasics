import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_service = Service("Drivers/chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()


input_field = driver.find_element(By.ID, "autosuggest")

input_field.send_keys("Ind")

time.sleep(3)

dynamic_dropdown = driver.find_elements(By.CLASS_NAME, "ui-menu-item")

print([element.text for element in dynamic_dropdown])

for element in dynamic_dropdown:
    if element.text == "India":
        element.click()
        break

time.sleep(5)
