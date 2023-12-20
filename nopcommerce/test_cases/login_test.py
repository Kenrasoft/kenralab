import pytest
from selenium import webdriver
from page_objects.login_page import LoginPage
from test_data.login_data import login_data
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class TestLoginPage:
    
    def test_login_with_valid_credentials(self, browser):
        
        login_page = LoginPage(browser)
        login_page.navigate_to_login_page()
        login_page.wait_for_login_page()
        
        output = login_page.login_with_credentials(login_data["username"], login_data["password"])
        
        assert output == login_data["username"]
        print (f"User Logged in successfully: {output}")