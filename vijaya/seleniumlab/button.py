from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


driver_path = "C:\\Drivers\\chromedriver\\chromedriver.exe"



def doubleclick_button():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get('https://demoqa.com/buttons')
    driver.maximize_window()
    doubleclick_button = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
    actions = ActionChains(driver)
    actions.double_click(doubleclick_button).perform()
    displaytext= "You have done a double click"
    actualmessage= driver.find_element(By.XPATH,"//p[@id='doubleClickMessage']").text
    print ("actual message:"+actualmessage)
    assert actualmessage == displaytext
    time.sleep(8)
    driver.quit()

def right_clickbutton():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get('https://demoqa.com/buttons')
    driver.maximize_window()
    right_clickbutton= driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
    actions = ActionChains(driver)
    actions.context_click(right_clickbutton).perform()
    displaytext= "You have done a right click"
    actualmessage= driver.find_element(By.XPATH,"//p[@id='rightClickMessage']").text
    print ("actual message:"+actualmessage)
    assert actualmessage == displaytext

    time.sleep(8)
    driver.quit()

def click_button():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get('https://demoqa.com/buttons')
    driver.maximize_window()
    click_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Click Me'])[1]")
    click_button.click()
    displaytext= "You have done a dynamic click"
    actualmessage= driver.find_element(By.XPATH,"//p[@id='dynamicClickMessage']").text
    print ("actual message:"+actualmessage)
    assert actualmessage == displaytext
    time.sleep(8)
    driver.quit()




click_button()
# doubleclick_button()
# right_clickbutton()


