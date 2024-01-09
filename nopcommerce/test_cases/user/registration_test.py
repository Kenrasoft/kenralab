import pytest
from selenium import webdriver
from page_objects.user.registration_page import RegistraionPage
from test_data.user.registration_data import registration_data,registration_data_invalid
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time
import random


class TestRegistraionPage:
    
    def test_registration_with_mandatory_data(self,browser):
        # creating registration page object   
        registration_page = RegistraionPage(browser) 
        #loading registration page 
        registration_page.navigate_to_register_page() 
        # method call to register userdata 
        registration_page.wait_for_registration_page()
        # creating random number for dynamic emailId 
        random_number = str(random.randint(1, 100000)) 
        print(random_number+registration_data["email"])         
        output = registration_page.register_with_userdata(registration_data["first_name"],registration_data["last_name"],random_number+registration_data["email"],registration_data["password"],registration_data["confirm_password"])
        assert output == "Your registration completed"
        print (f"User registered successfully: {output}")
       

    def test_registration_empty_form(self,browser):        
        registration_page = RegistraionPage(browser)
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        output = registration_page.register_without_userdata()
        assert output == "First name is required."           
        print (output)        
        
    
    def test_registration_invalid_email(self,browser):        
        registration_page = RegistraionPage(browser)
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        output = registration_page.register_with_inavlid_emailid(registration_data_invalid["email"])
        assert output == "Wrong email"        
        print (output)
        

    def test_registration_invalid_password(self,browser):       
        registration_page = RegistraionPage(browser)
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        output = registration_page.register_with_inavlid_password(registration_data_invalid["password"])
        assert output == "must have at least 6 characters"        
        print (output)
        
    
    def test_register_with_mismatch_password(self,browser):        
        registration_page = RegistraionPage(browser)
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        output = registration_page.register_with_mismatch_password(registration_data_invalid["password"],registration_data_invalid["confirm_password"])
        assert output == "The password and confirmation password do not match."        
        print (output)
        
    def test_registration_with_all_the_data(self,browser):            
        registration_page = RegistraionPage(browser)             
        registration_page.navigate_to_register_page()  
        registration_page.wait_for_registration_page()
        # creating random number for dynamic emailId 
        random_number = str(random.randint(1, 100000))  
        print (random_number+registration_data["email"])       
        output = registration_page.register_with_user_all_data(registration_data["first_name"],registration_data["last_name"],
        registration_data["day"],registration_data["month"],registration_data["year"],random_number+registration_data["email"],
        registration_data["company_name"],registration_data["password"],registration_data["confirm_password"])
        assert output == "Your registration completed"
        print (f"User registered successfully: {output}")
        


    def test_ligin_with_registred_user_data(self,browser):           
        registration_page = RegistraionPage(browser)             
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

        




