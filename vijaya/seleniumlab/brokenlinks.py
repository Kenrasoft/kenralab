from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
driver_path = "C:\\Drivers\\chromedriver\\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
# Given I navigate to the https://demoqa.com/broken page, When I scan the page for broken links, Then all broken links should be identified and logged.

def broken_links():
    driver.get('https://demoqa.com/broken')
    driver.maximize_window()
    brokenlinks=driver.find_elements(By.XPATH,"//p[contains(text(), 'Broken ')]")
    for brokenlink in brokenlinks:
        print("brokenlinks:"+brokenlink.text)
    time.sleep(5)
    driver.quit()
# Given I navigate to the https://demoqa.com/broken page, When I click each link on the page, 
# Then the status of the links should be checked, And any broken links should be identified and logged.
def click_links():
    driver.get('https://demoqa.com/broken')
    driver.maximize_window()
    driver.find_element(By.XPATH,"//a[normalize-space()='Click Here for Broken Link']").click()
    time.sleep(5)
    expectederrormessage="This page returned a 500 status code."
    errormessage=driver.find_element(By.XPATH,"//p[contains(text(),'This page returned a 500 status code.')]").text
    print("errormessage:" +errormessage)
    assert expectederrormessage in errormessage

    driver.quit()



# broken_links()
click_links()

