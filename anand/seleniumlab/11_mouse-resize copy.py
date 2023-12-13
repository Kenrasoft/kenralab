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

driver.get("https://jqueryui.com/resizable/")

# Switch to the frame where the resizable element is present
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

# Find the resizable element
resizable_handle = driver.find_element(By.CSS_SELECTOR, ".ui-resizable-handle")

# Perform the resizable action by dragging the handle
actions = ActionChains(driver)
actions.click_and_hold(resizable_handle).move_by_offset(100, 100).release().perform()

# Switch back to the main content (out of the frame)
driver.switch_to.default_content()

time.sleep(5)
# Close the browser
driver.quit()



