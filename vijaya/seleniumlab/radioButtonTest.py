from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
driver_path = "C:\\Drivers\\chromedriver\\chromedriver.exe"

chrome_options = Options()

# driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)

def check_radiobutton():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)
    driver.get('https://demoqa.com/radio-button')
    driver.maximize_window()
    radioYes = driver.find_element(By.ID, "yesRadio")
    # radioImp = driver.find_element(By.ID, "impressiveRadio")
    radioButtons = driver.find_elements(By.CLASS_NAME, "custom-control-label")
    radioButtons[0].click()
    print (f"Radio button 1 is selected: {radioYes.is_selected()}")
    time.sleep(4)
    driver.quit()

def switch_radiobutton():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)
    driver.get('https://demoqa.com/radio-button')
    driver.maximize_window()
    radioYes = driver.find_element(By.ID, "yesRadio")
    radioImp = driver.find_element(By.ID, "impressiveRadio")
    radioButtons = driver.find_elements(By.CLASS_NAME, "custom-control-label")
    radioButtons[0].click()
    print (f"Radio button 1 is selected: {radioYes.is_selected()}")
    time.sleep(2)
    radioButtons[1].click()
    print (f"Radio button 2 is selected: {radioImp.is_selected()}")
    print (f"Radio button 1 is selected: {radioYes.is_selected()}")
    time.sleep(4)
    driver.quit()

def doublecheck_radiobutton():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)
    driver.get('https://demoqa.com/radio-button')
    driver.maximize_window()
    radioYes = driver.find_element(By.ID, "yesRadio")
    # radioImp = driver.find_element(By.ID, "impressiveRadio")
    radioButtons = driver.find_elements(By.CLASS_NAME, "custom-control-label")
    radioButtons[0].click()
    print (f"Radio button 1 is selected: {radioYes.is_selected()}")
    time.sleep(2)
    radioButtons[0].click()
    print (f"Radio button 1 is selected: {radioYes.is_selected()}")
    time.sleep(4)
    driver.quit()

def checkdisabled_radiobutton():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path), options=chrome_options)
    driver.get('https://demoqa.com/radio-button')
    driver.maximize_window()
    noRadio = driver.find_element(By.ID, "noRadio")
    # radioImp = driver.find_element(By.ID, "impressiveRadio")
    radioButtons = driver.find_elements(By.CLASS_NAME, "custom-control-label")
    radioButtons[2].click()
    print (f"Radio button 3 is selected: {noRadio.is_selected()}")
    time.sleep(4)
    driver.quit()

check_radiobutton()
switch_radiobutton()
doublecheck_radiobutton()
checkdisabled_radiobutton()

    