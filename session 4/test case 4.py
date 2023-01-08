#test case 4.1
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('http://localhost:80')
browser.get("https://money.rediff.com/gainers/bse/daily/groupa")
browser.maximize_window()
#______________________________self______________________________
#textmsg=browser.find_element(By.XPATH,"//a[normalize-space()='Astra Microwave']//self::a").text
#print(textmsg)
#______________________________parent____________________________
#textmsg=browser.find_element(By.XPATH,"//a[normalize-space()='Astra Microwave']/parent::td").text
#print(textmsg)
#_____________________________child______________________________
#textmsg=browser.find_element(By.XPATH,"//a[normalize-space()='Astra Microwave']/ancestor::tr/child::td").text
#print(textmsg)

#childs=browser.find_elements(By.XPATH,"//a[normalize-space()='Astra Microwave']/ancestor::tr/child::td")
#print(len(childs))
#browser.close()
#_______________________________ancestor__________________________
#textmsg=browser.find_element(By.XPATH,"//a[normalize-space()='Astra Microwave']/ancestor::tr").text
#print(textmsg)
#___________________________descendant____________________________
#descendents=browser.find_elements(By.XPATH,"//a[normalize-space()='Astra Microwave']/ancestor::tr/descendant::*")
#print(len(descendents))
#___________________________following_____________________________
#followings=browser.find_elements(By.XPATH,"//a[normalize-space()='Astra Microwave']/ancestor::tr/following::*")
#print(len(followings))
#_________________________following-sibling_______________________
#followingsiblings=browser.find_elements(By.XPATH,"//a[normalize-space()='Astra Microwave']/ancestor::tr/following-sibling::*")
#print(len(followingsiblings))
#---------------------------preceding-----------------------------
#precedings=browser.find_elements(By.XPATH,"//a[normalize-space()='Astra Microwave']/ancestor::tr/preceding::*")
#print(len(precedings))
#_______________________preceding-sibling_________________________
precedingsiblings=browser.find_elements(By.XPATH,"//a[normalize-space()='Astra Microwave']/ancestor::tr/preceding-sibling::*")
print(len(precedingsiblings))
time.sleep(10.0)
