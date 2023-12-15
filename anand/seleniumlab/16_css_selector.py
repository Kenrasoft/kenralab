from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


# Specify the path to the downloaded chromedriver.exe
driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"

driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
# Navigate to the Selectable page
driver.get("https://demoqa.com/automation-practice-form")

# Fill out the form using CSS selectors
driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys("John")
driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys("Doe")

# Select a date using the date picker
driver.find_element(By.CSS_SELECTOR, "#dateOfBirthInput").click()

# Select subjects
driver.find_element(By.CSS_SELECTOR, "#subjectsInput").send_keys("Math")
driver.find_element(By.CSS_SELECTOR, "#subjectsInput").send_keys(Keys.RETURN)

# Select hobbies

# Enter current address
driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("123 Main Street, Cityville, Country")

# Submit the form
driver.find_element(By.CSS_SELECTOR, "#submit").click()

time.sleep(5)
# Close the browser
driver.quit()


