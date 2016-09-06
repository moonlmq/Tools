from selenium import webdriver
import time,os
from selenium.webdriver.common.keys import Keys

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"]=chromedriver
b = webdriver.Chrome(chromedriver)

b.get("http://.com/")
time.sleep(3)
b.find_element_by_id("CCM_LoginMain1_tbName").clear
time.sleep(1)
b.find_element_by_id("CCM_LoginMain1_tbName").focus()
b.find_element_by_id("CCM_LoginMain1_tbName").send_keys("")
time.sleep(1)
b.find_element_by_id("CCM_LoginMain1_tbPass").clear
time.sleep(1)
b.find_element_by_id("CCM_LoginMain1_tbPass").send_keys("")
b.find_element_by_id("CCM_LoginMain1_ImageButtonlogin1").click()
# time.sleep(2)
# elem= b.find_element_by_id("IB2").click()
# time.sleep(5)
# b.close()

# b.get("http://www.baidu.com/")

# time.sleep(1)

# b.find_element_by_id("kw").clear

# time.sleep(1)

# b.find_element_by_id("kw").send_keys("hello")