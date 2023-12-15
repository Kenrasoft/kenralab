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

# Open a webpage with a file upload form
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

# Find the file input element using its name attribute (you may need to inspect the HTML to find the correct locator)
file_input = driver.find_element(By.NAME, "upfile")

# Send the file path to the file input element
file_path = "C:/test/s_logo.png"
file_input.send_keys(file_path)

# Wait for a short time to allow the file to be uploaded (adjust the time based on your system and file size)
time.sleep(2)

# Submit the form (you may need to inspect the HTML to find the correct submit button or trigger the submit in a different way)
submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit_button.click()

# Wait for a few seconds to see the result
time.sleep(5)

# Close the browser
driver.quit()



