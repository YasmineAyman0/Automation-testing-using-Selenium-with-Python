#test case 3.1
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://www.facebook.com")
#browser.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/div[1]/div[4]/div[1]/div/div/a[1]').click()
browser.maximize_window()
time.sleep(90)