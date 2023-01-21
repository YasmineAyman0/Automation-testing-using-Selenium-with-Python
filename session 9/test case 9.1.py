# test case 9.1 static web tables
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://testautomationpractice.blogspot.com/")
browser.maximize_window()

# 1)count number of rows and columns
time.sleep(6)
noOfrows = len(browser.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
noOfcolumns = len(browser.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))
time.sleep(6)
# print(noOfrows)  #7
# print(noOfcolumns)  #4

# 2)Read specific row & column data
data = browser.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

# 3)Read all the rows and columns data
# print("Print all the rows and columns data")
# for r in range(2,noOfrows+1):
#   for c in range(1,noOfcolumns+1):
#      data=browser.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#     print(data,end='                   ')
#    print()

# 4)Read specific rows and columns based on a condition (print book names whose auther is mukesh and its price)
# print("Print Mukesh book names and price ")
# for r in range(2,noOfrows+1):
#   authername=browser.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
#  if authername=="Mukesh":
#     booknames=browser.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
#    price=browser.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
#   print(authername,"          ",booknames,"           ",price)

browser.close()
