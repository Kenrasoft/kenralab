from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# Given I navigate to the https://demoqa.com/text-box page, When I enter a valid full name in the "Full Name" text box, 
# And I enter a valid current address in the "Current Address" text box, 
# And I don't enter the email, And I submit the form, Then You should see the error for the email.
def testcase1():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(3)
    userNameElement = driver.find_element(By.ID,"userName")
    userNameElement.send_keys("Vijaya")
    time.sleep(1)
    currentAddressElement=driver.find_element(By.ID,"currentAddress")
    currentAddressElement.send_keys("11026 Morro Bay Ln")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()

    userEmailElement=driver.find_element(By.ID,"userEmail")
    emailId = userEmailElement.get_attribute('value') 
    if not emailId:
        userEmailElement.send_keys("Please enter your email address")
    time.sleep(5)
    # driver.quit()
    testcase1()

# Given I navigate to the https://demoqa.com/text-box page, When I enter an valid full name in the "Full Name" text box,
# And I enter a valid current address in the "Current Address" text box, 
# And I submit the form, Then an appropriate validation message should be displayed.
def testcase2():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(3)
    userNameElement = driver.find_element(By.ID,"userName")
    userNameElement.send_keys("Vijaya")
    time.sleep(1)
    currentAddressElement=driver.find_element(By.ID,"currentAddress")
    currentAddressElement.send_keys("11026 Morro Bay Ln ")
    time.sleep(1)
    driver.find_element(By.ID,"submit").click()
    userEmailElement=driver.find_element(By.ID,"userEmail")
    emailId = userEmailElement.get_attribute('value') 
    if not emailId:
        userEmailElement.send_keys("Please enter your email address")
    time.sleep(5)
    # driver.quit()
    testcase2()

# Given I navigate to the https://demoqa.com/text-box page, When I enter a valid full name in the "Full Name" text box, 
# And I enter a valid current address in the "Current Address" text box,
# And I clear the "Full Name" text box, And I submit the form, Then an appropriate validation message should be displayed.
def testcase3():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    driver.maximize_window()
    time.sleep(3)
    userNameElement = driver.find_element(By.ID,"userName")
    userNameElement.send_keys("Vijaya")
    time.sleep(1)
    currentAddressElement=driver.find_element(By.ID,"currentAddress")
    currentAddressElement.send_keys("11026 Morro Bay Ln")
    time.sleep(1)
    userNameElement = driver.find_element(By.ID,"userName")
    userNameElement.clear()
    driver.find_element(By.ID,"submit").click()
    fullName = userNameElement.get_attribute('value') 
    if not fullName:
        userNameElement.send_keys("Please enter your Name")
    time.sleep(5)
    # driver.quit()
    testcase3()
    



