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
driver.get("https://jqueryui.com/selectable/")

# Switch to the iframe containing the Selectable demo
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))

# Simulate holding down the Ctrl key
webdriver.ActionChains(driver).key_down(Keys.CONTROL).perform()

# Click on the items you want to select
items_to_select = driver.find_elements(By.CSS_SELECTOR, "#selectable li")
items_to_select[0].click()
items_to_select[2].click()
items_to_select[4].click()


#for item in items_to_select:
#    item.click()

# Release the Ctrl key
webdriver.ActionChains(driver).key_up(Keys.CONTROL).perform()


time.sleep(5)
# Close the browser
driver.quit()


