import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def browser():
    driver_path = "C:\\Users\\anand\\Selenium\\chromedriver.exe"
    driver = webdriver.Chrome(service=ChromeService(executable_path=driver_path))
    yield driver
    driver.quit()

def test_login_with_valid_credentials(browser):
    
    login_page = LoginPage(browser)
    login_page.navigate_to_login_page()
    login_page.wait_for_login_page()
    output = login_page.login_with_credentials("Tuser777", "TestUser@777")
    
    assert output == "TUser777"
    print (f"User Logged in successfully: {output}")

