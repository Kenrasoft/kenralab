import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"

driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))

url = "https://demoqa.com/login"

driver.get(url)

user_element = driver.find_element(By.ID, "userName")
pass_element = driver.find_element(By.ID, "password")
login_element = driver.find_element(By.ID, "login")

user_element.send_keys("Tuser777")
pass_element.send_keys("TestUser@777")
login_element.click()
driver.implicitly_wait(3)

user_output_element = driver.find_element(By.ID, "userName-value")
assert user_output_element.text == "TUser777"
print (f"User Logged in successfully: {user_output_element.text}")

time.sleep(5)

