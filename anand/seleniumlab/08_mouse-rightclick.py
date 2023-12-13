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

driver.get("http://demo.guru99.com/test/simple_context_menu.html")

box = driver.find_element(By.XPATH, '//span[text()="right click me"]')
action = ActionChains(driver)
action.context_click(box).perform()

time.sleep(5)
# Close the browser
driver.quit()

