#test case 1
from selenium import webdriver
# driver = webdriver.Chrome('/path/to/chromedriver')
# driver=webdriver.Chrome("E:\Interviews\Automation\python\1\session1\chromedriver_win32\chromedriver.exe")
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://admin-demo.nopcommerce.com/login")
# browser.find_element_by_id("Email").send_keys("admin@yourstore.com")
# browser.find_element_by_id("Password").send_keys("admin")
#browser.find_element_by_class_name("buttons").click()
browser.find_element(By.CLASS_NAME,"buttons").click()
act = browser.title
browser.close()
exp = "Dashboard / nopCommerce administration"
if act==exp:
    print("test is passed")
else:
    print("test is failed")
   # browser.close()