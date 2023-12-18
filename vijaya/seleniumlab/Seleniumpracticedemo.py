import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(4)
driver.find_element(By.NAME, 'username').send_keys("Admin")
driver.find_element(By.NAME, 'password').send_keys("admin123")
driver.find_element(By.NAME, 'Login').click()
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()

act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")
          
#driver.close()
          