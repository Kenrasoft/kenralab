from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Specify the path to the downloaded chromedriver.exe
driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"

# Create a new instance of the Chrome driver using ChromeService
# Create ChromeOptions object
chrome_options = Options()

# Enable headless mode
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--enable-logging")
# chrome_options.add_argument("--v=1")

driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)

driver.get("https://www.selenium.dev/selenium/web/inputs.html")


radio_elements = driver.find_elements(By.NAME, "radio_input")
i = 0

for radio_element in radio_elements:
    i = i+1
    print (f"Radio button {i} selected: {radio_element.is_selected()}")

radio_elements[1].click()
print (f"Radio button 2 is clicked: {radio_elements[1].is_selected()}")
print (f"Radio button 1 is selected: {radio_elements[0].is_selected()}")

driver.quit()
