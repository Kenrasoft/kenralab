from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
driver_path = "C:\\Drivers\\chromedriver\\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
# Navigate to the demoqa.com checkbox page
driver.get('https://demoqa.com/buttons')
clickBtns = driver.find_elements(By.CLASS_NAME, "btn.btn-primary")
actions = ActionChains(driver)
time.sleep(2)
actions.double_click(clickBtns[0]).perform()
time.sleep(2)
actions.context_click(clickBtns[1]).perform()
time.sleep(2)
clickBtns[2].click()
time.sleep(1)

outputDouble = driver.find_element(By.ID, "doubleClickMessage")
outputRight = driver.find_element(By.ID, "rightClickMessage") 
outputDynamic = driver.find_element(By.ID, "dynamicClickMessage")
double_message = outputDouble.text
right_message = outputRight.text
dynamic_message = outputDynamic.text


print(f"click once msg : {double_message}")
print(f"click once msg : {right_message}")
print(f"click once msg : {dynamic_message}")

time.sleep(1)

driver.quit()







