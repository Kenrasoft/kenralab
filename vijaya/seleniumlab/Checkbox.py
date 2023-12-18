from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
driver_path = "C:\\Drivers\\chromedriver\\chromedriver.exe"

# Create a new instance of the Chrome driver
# driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))


# Navigate to the demoqa.com checkbox page
def check_checkbox():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get('https://demoqa.com/checkbox')
    driver.maximize_window()
    homeCB = driver.find_element(By.ID, "tree-node-home")
    checkboxes = driver.find_elements(By.CLASS_NAME, "rct-checkbox")
    toggle = driver.find_element(By.CLASS_NAME, "rct-collapse.rct-collapse-btn")
    toggle.click()
    time.sleep(4)
    desktopCB = driver.find_element(By.ID, "tree-node-desktop")
    checkboxes[0].click()
    print(f"Checkbox is selected : {desktopCB.is_selected()}");
    time.sleep(2)
    driver.quit()


def uncheck_checkbox():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get('https://demoqa.com/checkbox')
    driver.maximize_window()
    homeCB = driver.find_element(By.ID, "tree-node-home")
    checkboxes = driver.find_elements(By.CLASS_NAME, "rct-checkbox")
    toggle = driver.find_element(By.CLASS_NAME, "rct-collapse.rct-collapse-btn")
    toggle.click()
    time.sleep(4)
    desktopCB = driver.find_element(By.ID, "tree-node-desktop")
    checkboxes[0].click()
    time.sleep(3)
    print(f"Checkbox is selected : {desktopCB.is_selected()}");
    checkboxes[0].click()
    print(f"Checkbox is selected : {desktopCB.is_selected()}");
    time.sleep(2)
    driver.quit()

check_checkbox()
uncheck_checkbox()