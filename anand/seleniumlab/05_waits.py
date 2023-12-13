from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Specify the path to the downloaded chromedriver.exe
driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"

driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))

driver.implicitly_wait(10)
driver.get("http://127.0.0.1:5500/formSubmit.html")



p_element = driver.find_element(By.ID, "pId")
u_element = driver.find_element(By.ID, "uId")
s_element = driver.find_element(By.ID, "sId")

u_element.send_keys("Anand")

# Find the submit button and wait for it to be clickable
s_element = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.ID, "sId")))


s_element.click()

print("Element P:" + p_element.text)

time.sleep(5)

driver.quit()
