import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

@pytest.fixture
def chrome_browser():
    driver_path = "../configuration/chromedriver.exe"
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    return driver

@pytest.fixture
def browser(chrome_browser):
    driver = chrome_browser
    yield driver
    driver.quit()

    
