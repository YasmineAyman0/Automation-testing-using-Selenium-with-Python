# test case 9.2 dynamic web tables
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
browser.maximize_window()
time.sleep(5)
# Login
browser.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
browser.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
browser.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(6)
# Admin--->user management--->users
browser.find_element(By.XPATH, "//li[1]//a[1]//span[1]").click()
time.sleep(3)
browser.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
browser.find_element(By.XPATH, "//a[@role='menuitem']").click()
time.sleep(8)

# ________________________________________________________
browser.close()
