from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your WebDriver executable (e.g., chromedriver.exe for Chrome)
driver_path = "C:\\Drivers\\chromedriver\\chromedriver.exe"
def get_cell_data():
    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    # Navigate to the demoqa.com checkbox page
    driver.get('https://demoqa.com/webtables')
    time.sleep(3)
    celldata= driver.find_element(By.XPATH,"//div[contains(text(), 'Cierra')]").text
    print(celldata)
    assert celldata ==  "Cierra"
    driver.quit()

# Given I navigate to the https://demoqa.com/webtables page, When I edit the data in a cell in the table, And I save the changes, Then the updated data should be reflected in the table.
def edit_data_in_cell():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get("https://demoqa.com/webtables")
    # Click on the "Edit" button for the first entry
    # edit_button = driver.find_element(By.XPATH, "//span[@id='edit-record-1']//*[name()='svg']//*[name()='path' and contains(@d,'M880 836H1')]")
    edit_button = driver.find_element(By.XPATH, "(//*[name()='path'])[54]")     
    edit_button.click()
    # Modify the "Age" value
    driver.find_element(By.XPATH, "//input[@id='firstName']").clear()
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Ram")

    # # Click the "Submit" button
    driver.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()
    
    # # Verify that the entry is updated in the table
    celldata= driver.find_element(By.XPATH,"//div[contains(text(), 'Ram')]").text
    print("updated_Name:"+ celldata)
    assert "Ram" in celldata
    driver.close()  
# Given I navigate to the https://demoqa.com/webtables page, When I add a new row to the table with valid data, Then the new row should be appended to the table.
def add_row_in_table():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get("https://demoqa.com/webtables")
    add_button = driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']")     
    add_button.click()
    driver.find_element(By.XPATH, "//input[@id='firstName']").send_keys("Ram")
    driver.find_element(By.XPATH, "//input[@id='lastName']").send_keys("Jai")
    driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("ram@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='age']").send_keys("18")
    driver.find_element(By.XPATH, "//input[@id='salary']").send_keys("100000")
    driver.find_element(By.XPATH, "//input[@id='department']").send_keys("Technology")

    driver.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()
    # # Verify that the new row in the table
    name= driver.find_element(By.XPATH,"//div[contains(text(), 'Ram')]").text
    age= driver.find_element(By.XPATH,"//div[contains(text(), '18')]").text
    
    print("updated_Name:"+ name)
    print("updated_age:"+ age)

    assert "Ram" in name
    assert "18" in age

    driver.close() 

# Given I navigate to the https://demoqa.com/webtables page, 
# When I add a new row to the table with invalid data, Then an appropriate validation message should be displayed. 
def invalid_row():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get("https://demoqa.com/webtables")
    add_button = driver.find_element(By.XPATH, "//button[@id='addNewRecordButton']")     
    add_button.click()

    driver.find_element(By.XPATH, "(//button[normalize-space()='Submit'])[1]").click()
    time.sleep(5)

#  Given I navigate to the https://demoqa.com/webtables page, When I delete a row from the table, Then the row should be removed from the table.
def delete_row():
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    driver.get("https://demoqa.com/webtables")
    delete_button=driver.find_element(By.XPATH,"//span[@id='delete-record-3']//*[name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]")

    # delete_button=driver.find_element(By.XPATH, "//*[name()='path'])[59]")

    delete_button.click()
    time.sleep(5)

get_cell_data()
# edit_data_in_cell()
# add_row_in_table()
# invalid_row()
# delete_row()



