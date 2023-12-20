from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
driver_path = "C:\\Drivers\\chromedriver\\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
# URL - https://demoqa.com/automation-practice-form
# Fill out the valid data in all required fields
# When I click the "Submit" button, the form should be submitted successfully, and a confirmation message should be displayed

def fill_form_data():
    driver.get('https://demoqa.com/automation-practice-form')
    driver.maximize_window()
    driver.find_element(By.XPATH,"//input[@id='firstName']").send_keys("Jase")
    driver.find_element(By.XPATH,"//input[@id='lastName']").send_keys("smith")
    driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys("smith@gmail.com")
    driver.find_element(By.XPATH,"//label[normalize-space()='Male']").click()
    driver.find_element(By.XPATH,"//input[@id='userNumber']").send_keys("123654789")
    # driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']").send_keys("25 Dec 2019")
    # driver.find_element(By.XPATH,"//div[@class='subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3']").send_keys("subject")
    driver.find_element(By.CSS_SELECTOR,"#submit").click()


    time.sleep(3)
    driver.quit()
fill_form_data()