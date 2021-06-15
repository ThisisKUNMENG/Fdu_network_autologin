from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from tkinter import messagebox
driver = webdriver.Chrome()
driver.get('http://10.102.250.13/index.php?url=aHR0cDovL3d3dy5tc2Z0Y29ubmVjdHRlc3QuY29tL3JlZGlyZWN0')
time.sleep(1)
if driver.find_element_by_id("loginForm").is_displayed()==True :
    driver.find_element_by_id("username").send_keys("18817265295")
    option=driver.find_element_by_id("domain")
    Select(option).select_by_value("CMCC")
    driver.find_element_by_id("password").send_keys("591887")
    time.sleep(1)
    driver.find_element_by_id('login').click()
    time.sleep(3)
    driver.quit()
    messagebox.showinfo("提示","网络登录成功！")
else:
    driver.quit()
    messagebox.showinfo("提示", "网络已登录！")


