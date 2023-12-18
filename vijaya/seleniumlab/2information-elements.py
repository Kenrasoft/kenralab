from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# Specify the path to the downloaded chromedriver.exe
# driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"

# driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
driver = webdriver.Chrome()

# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")
time.sleep(5)


email_input_element = driver.find_element(By.NAME, "email_input")
print (f"Email tag: ", email_input_element.tag_name)
print (f"Email visible: ", email_input_element.is_displayed())
print (f"Email value: ", email_input_element.get_attribute("value"))



button_element = driver.find_element(By.NAME, 'button_input')
print (f"Button Enabled: ", button_element.is_enabled())

check_element = driver.find_element(By.NAME, "checkbox_input")
print (f"Checkbox selected: ", check_element.is_selected())

time.sleep(5)
# Close the browser
driver.quit()
