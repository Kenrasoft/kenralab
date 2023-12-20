from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#  When I check a checkbox, Then the checkbox should be selected.


def select_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    time.sleep(10)
    driver.find_element(By.ID,"item-1").click()
    time.sleep(6)
    driver.find_element(By.ID,"tree-node").click()
    time.sleep(6)
    driver.find_element(By.ID,"tree-node-home").click()
    time.sleep(5)

# When I uncheck a checked checkbox, Then the checkbox should be deselected.
def deselect_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    time.sleep(3)
    # driver.find_element(By.ID,"item-1").click()
    # time.sleep(2)
    driver.find_element(By.ID,"tree-node-home").click()
    time.sleep(5)
    driver.find_element(By.ID,"tree-node-home").unclick()
    time.sleep(4)


# When I check multiple checkboxes, Then all selected checkboxes should remain selected.
def select_checkboxes():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.ID,"item-1").click()
    time.sleep(2)
    driver.find_element(By.ID,"tree-node-home").click()
    time.sleep(5)
    driver.find_element(By.ID,"tree-node-desktop").click()
    time.sleep(5)
    driver.find_element(By.ID,"tree-node-documents").click()
    time.sleep(5)
    driver.find_element(By.ID,"tree-node-downloads").click()
    time.sleep(5)

# When I uncheck all selected checkboxes, Then no checkbox should remain selected.
def uncheck_checkbox():
    driver=webdriver.Chrome()
    driver.get("https://demoqa.com/checkbox")
    driver.maximize_window()
    time.sleep(3)
    driver.find_element(By.ID,"item-1").click()
    time.sleep(2)
    driver.find_element(By.ID,"tree-node-home").uncheck()
    time.sleep(5)
    driver.find_element(By.ID,"tree-node-desktop").uncheck()
    time.sleep(5)
    driver.find_element(By.ID,"tree-node-documents").uncheck()
    time.sleep(5)
    driver.find_element(By.ID,"tree-node-downloads").uncheck()
    time.sleep(5)



select_checkbox()
deselect_checkbox()
select_checkboxes()
uncheck_checkbox()



