#differences between find_element() and find_elements()
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://admin-demo.nopcommerce.com/admin/")
browser.maximize_window()
#_________________________find_element()_______________________________
element=browser.find_element(By.XPATH,"//input[@placeholder='Search']")
element.send_keys("Apple MacBook")
time.sleep(5)