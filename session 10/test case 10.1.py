# test case 10.1 date picker (select day , month and year from date picker)
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://jqueryui.com/datepicker/")
browser.maximize_window()
time.sleep(5)
browser.switch_to.frame(0)
# browser.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("06/01/2023")    #mm/dd/yyyy
year = "2023"
month = "January"
day = "2"
browser.find_element(By.XPATH, "//input[@id='datepicker']").click()
# select month and year
while True:
    mon = browser.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = browser.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yr == year:
        break;
    else:
        browser.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  # Next arrow
time.sleep(5)
# select day
dates = browser.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tbody/tr/td")

for ele in dates:
    if ele.text == day:
        ele.click()
        break
