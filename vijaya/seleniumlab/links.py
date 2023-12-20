from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
driver_path = "C:\\Drivers\\chromedriver\\chromedriver.exe"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))

def click_link():
    driver.get('https://demoqa.com/links')
    driver.maximize_window()
    linkclick=driver.find_element(By.XPATH,"//a[@id='simpleLink']")
    linkclick.click()
    time.sleep(3)
    title=driver.title
    print ("title:" + title)
    assert title == "DEMOQA"
    driver.quit()

# Given I navigate to the https://demoqa.com/links page, When I click a link with an invalid URL, Then an appropriate error page or message should be displayed.
def click_invalid_url():
    driver.get('https://demoqa.com/links')
    driver.maximize_window()
    driver.find_element(By.XPATH,"//a[@id='invalid-url']").click()
    time.sleep(2)
    expectedvalue= "Link has responded with staus 404 and status text Not Found"
    actualvalue= driver.find_element(By.XPATH," //p[@id='linkResponse']").text
    print ("actual value:"+actualvalue)
    assert actualvalue == expectedvalue
    driver.quit()

#Given I navigate to the https://demoqa.com/links page, When I click a link that triggers a file download, Then the file download should be initiated.
def file_download():
    driver.get('https://demoqa.com/upload-download')
    driver.maximize_window()
    driver.find_element(By.XPATH,"//a[@id='downloadButton']").click()
    time.sleep(5)
    driver.quit()
# Given I navigate to the https://demoqa.com/links page, When I click a link with a broken URL, Then an appropriate error page or message should be displayed.
def click_broken_url():
    driver.get('https://demoqa.com/broken')
    driver.maximize_window()
    driver.find_element(By.XPATH,"//a[normalize-space()='Click Here for Broken Link']").click()
    time.sleep(5)
    expectederrormessage="This page returned a 500 status code."
    errormessage=driver.find_element(By.XPATH,"//p[contains(text(),'This page returned a 500 status code.')]").text
    print("errormessage:" +errormessage)
    assert expectederrormessage in errormessage

    driver.quit()

# click_link()
# click_invalid_url()
# file_download()  
click_broken_url()













# Given I navigate to the https://demoqa.com/links page, When I click a link with a valid URL, Then I should be redirected to the expected destination.