import pytest
from selenium import webdriver
from page_objects.registration_page import RegistraionPage
from test_data.registration_data import registration_data
from selenium.webdriver.common.by import By
import time
import random

class TestRegistraionPage:
    
    def test_registration_with_mandatory_data(self):
        driver=webdriver.Chrome()
        # driver = webdriver.Firefox()
        registration_page = RegistraionPage(driver)
        registration_page.navigate_to_register_page()
        registration_page.wait_for_registration_page()
        random_number = str(random.randint(1, 100000))  
        output = registration_page.register_with_userdata(registration_data["first_name"],registration_data["last_name"],random_number+registration_data["email"],registration_data["password"],registration_data["confirm_password"])
        assert output == "Your registration completed"
        print (f"User registered successfully: {output}")