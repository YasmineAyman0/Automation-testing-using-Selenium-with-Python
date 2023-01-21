# test case 13.1 select element from bootstrap dropdown list
import time
import public as public
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

browser = webdriver.Chrome()
browser.implicitly_wait(6)
browser.get('http://localhost:80')
browser.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
browser.maximize_window()
browser.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
countrieslist = browser.find_element(By.XPATH, "//span[@class='select2-dropdown select2-dropdown--below']//li").click()
print(len(countrieslist))

for country in countrieslist:
    if country.text == "Egypt":
        country.click()
        break

time.sleep(5)
browser.close()
