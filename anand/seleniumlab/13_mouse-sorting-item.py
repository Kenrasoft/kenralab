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


driver.get("https://jqueryui.com/sortable/")

# Switch to the frame where the sortable elements are present
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

# Find the sortable items
sortable_items = driver.find_elements(By.CSS_SELECTOR, "#sortable li")

# Perform the sorting action by dragging and dropping items
actions = ActionChains(driver)
actions.click_and_hold(sortable_items[0]).move_to_element(sortable_items[3]).perform()

# Switch back to the main content (out of the frame)
driver.switch_to.default_content()

time.sleep(5)
# Close the browser
driver.quit()


