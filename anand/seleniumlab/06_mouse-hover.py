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

driver.get("http://the-internet.herokuapp.com/hovers")

user1 = driver.find_element(By.XPATH, '//div[@class="figure"][3]')

print(user1)

action = ActionChains(driver)
action.move_to_element(user1).perform()

time.sleep(15)
# Close the browser
driver.quit()
