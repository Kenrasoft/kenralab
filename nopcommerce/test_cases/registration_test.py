import pytest
from selenium import webdriver
from page_objects.registration_page import RegistraionPage
from test_data.registration_data import registration_data
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import random

class TestRegistraionPage:
    
    def test_registration_with_mandatory_data(self):
        # Creating driver object
        driver=webdriver.Chrome()
        # driver = webdriver.Firefox()  
        # creating registration page object   
        registration_page = RegistraionPage(driver) 
        #loading registration page 
        registration_page.navigate_to_register_page() 
        # method call to register userdata 
        registration_page.wait_for_registration_page()
        # creating random number for dynamic emailId 
        random_number = str(random.randint(1, 100000))          
        output = registration_page.register_with_userdata(registration_data["first_name"],registration_data["last_name"],random_number+registration_data["email"],registration_data["password"],registration_data["confirm_password"])
        assert output == "Your registration completed"
        print (f"User registered successfully: {output}")
        driver.quit()

    def test_registration_empty_form(self):
        driver=webdriver.Chrome()
        registration_page = RegistraionPage(driver)
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        output = registration_page.register_without_userdata()
        assert output == "First name is required."           
        print (output)        
        driver.quit() 
        
    
    def test_registration_invalid_email(self):
        driver=webdriver.Chrome()
        registration_page = RegistraionPage(driver)
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        output = registration_page.register_with_inavlid_emailid("email")
        assert output == "Wrong email"        
        print (output)
        driver.quit()

    def test_registration_invalid_password(self):
        driver=webdriver.Chrome()
        # driver=webdriver.Firefox()
        registration_page = RegistraionPage(driver)
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        output = registration_page.register_with_inavlid_password("pas")
        assert output == "must have at least 6 characters"        
        print (output)
        driver.quit()
    
    def test_register_with_mismatch_password(self):
        driver=webdriver.Chrome()
        registration_page = RegistraionPage(driver)
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        output = registration_page.register_with_mismatch_password("password123","password1234")
        assert output == "The password and confirmation password do not match."        
        print (output)
        driver.quit()

    def test_registration_with_all_the_data(self):
        # Creating driver object
        driver=webdriver.Chrome()
        # driver = webdriver.Firefox()        
        registration_page = RegistraionPage(driver)             
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        # creating random number for dynamic emailId 
        random_number = str(random.randint(1, 100000))          
        output = registration_page.register_with_user_all_data(registration_data["first_name"],registration_data["last_name"],
        registration_data["day"],registration_data["month"],registration_data["year"],random_number+registration_data["email"],
        registration_data["company_name"],registration_data["password"],registration_data["confirm_password"])
        assert output == "Your registration completed"
        print (f"User registered successfully: {output}")
        driver.quit()


    def test_ligin_with_registred_user_data(self):
        driver=webdriver.Chrome()
        # driver = webdriver.Firefox()        
        registration_page = RegistraionPage(driver)             
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()        
        # creating random number for dynamic emailId 
        random_number = str(random.randint(1, 100000))          
        output = registration_page.register_with_userdata(registration_data["first_name"],registration_data["last_name"],random_number+registration_data["email"],registration_data["password"],registration_data["confirm_password"])
        assert output == "Your registration completed"
        print (output)       
        registration_page.navigate_to_login_page() 
        output = registration_page.ligin_with_registred_user_data(random_number+registration_data["email"],registration_data["password"])
        print(output)

        driver.quit()




