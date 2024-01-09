import pytest
from selenium import webdriver
from page_objects.user.login_page import LoginPage
from test_cases.base_test import BaseTest
from test_data.user.login_data import valid_login_data
from test_data.user.login_data import invalid_login_data
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class TestLoginPage(BaseTest) :
    
    @pytest.fixture
    def setup(self, browser, login_data):
        print("Parameters")
        user = login_data["username"]
        print(f"{user}")


    @pytest.mark.parametrize("login_data", valid_login_data)
    def test_login_with_valid_credentials(self, browser, setup, login_data):
        
        login_page = LoginPage(browser)
        login_page.navigate_to_login_page()
        login_page.wait_for_login_page()
        
        output = login_page.login_with_credentials(login_data["username"], login_data["password"])
        
        assert output == login_data["username"]
        print (f"User Logged in successfully: {output}")

    @pytest.mark.parametrize("login_data", invalid_login_data)
    def test_login_with_invalid_credentials(self, browser, setup, login_data):
        
        login_page = LoginPage(browser)
        login_page.navigate_to_login_page()
        login_page.wait_for_login_page()
        
        output = login_page.login_with_invalid_credentials(login_data["username"], login_data["password"])
        
        assert output == "Invalid username or password!"
        user = login_data["username"]
        print (f"Invalid credentials for the User : {user}")


