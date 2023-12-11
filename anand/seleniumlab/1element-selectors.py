from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Specify the path to the downloaded chromedriver.exe
driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"

driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))

driver.get("https://demoqa.com/text-box")

user_element = driver.find_element(By.ID, "userName-label")

print (f"UserName label: ", user_element.text)

# Close the browser
driver.quit()
