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

driver.get("https://www.google.com/")

# Locate the search input field
search_input = driver.find_element(By.NAME, "q")

# Type "Selenium" using key down and key up events
search_input.send_keys(Keys.SHIFT, "selenium")  # Holding down the Shift key
search_input.send_keys(Keys.ENTER)  # Simulating pressing Enter

# Pause for a moment to observe the result
driver.implicitly_wait(5)

time.sleep(15)
# Close the browser
driver.quit()

