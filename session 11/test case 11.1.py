# test case 11.1 mouse actions
import time
from selenium.webdriver import ActionChains
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
admin = browser.find_element(By.XPATH, "//li[1]//a[1]//span[1]")
time.sleep(6)
usermanagement = browser.find_element(By.XPATH, "//span[normalize-space()='User Management']")
users = browser.find_element(By.XPATH, "//a[@role='menuitem']")
time.sleep(4)

# Mouse hover
act = ActionChains(browser)
act.move_to_element(admin).move_to_element(usermanagement).move_to_element(users).click().perform()
