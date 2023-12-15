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
driver.get("https://demoqa.com/checkbox")

# Find the file input element using its name attribute (you may need to inspect the HTML to find the correct locator)
checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-home']//span[@class='rct-checkbox']//*[name()='svg']")

checkbox.click()

# Wait for a few seconds to see the result
time.sleep(5)

# Close the browser
driver.quit()



