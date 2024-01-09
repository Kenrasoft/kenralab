from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import time

class RegistraionPage(BasePage):

    def __init__(self, driver):
        super(RegistraionPage, self).__init__(driver)   
        self.url = "https://demo.nopcommerce.com/register?returnUrl=%2Fcustomer%2Finfo"
        self.login_url="https://demo.nopcommerce.com/login?returnurl=%2Fregisterresult%2F1"
        self.gender_male=(By.XPATH, "//input[@id='gender-male']")
        self.gender_female=(By.XPATH, "//input[@id='gender-female']")
        self.firstname_input = (By.XPATH, "//input[@id='FirstName']")
        self.lastname_input = (By.XPATH, "//input[@id='LastName']")
        self.date_of_birth_day=(By.XPATH, "//select[@name='DateOfBirthDay']")
        self.date_of_birth_month=(By.XPATH, "//select[@name='DateOfBirthMonth']")
        self.date_of_birth_year=(By.XPATH, "//select[@name='DateOfBirthYear']")
        self.email_input = (By.XPATH, "//input[@id='Email']")        
        self.company_input = (By.XPATH, "//input[@id='Company']")
        self.newsletter_input = (By.XPATH, "//input[@id='Newsletter']")
        self.password_input = (By.XPATH, "//input[@id='Password']")
        self.confirmpassword_input = (By.XPATH, "//input[@id='ConfirmPassword']")
        self.register_button = (By.XPATH, "//button[@id='register-button']")
        self.registraion_output =(By.XPATH, "//div[@class='result']")                
        self.firstname_error =(By.XPATH, "//span[@id='FirstName-error']")
        self.email_error =(By.XPATH, "//span[@id='Email-error']")
        self.password_error=(By.XPATH,"//li[normalize-space()='must have at least 6 characters']")
        self.confirmpassword_error=(By.XPATH,"//span[@id='ConfirmPassword-error']")   
        self.email_login=(By.XPATH,"//input[@id='Email']")
        self.password_login=(By.XPATH,"//input[@id='Password']")
        self.login_button=(By.XPATH,"//button[normalize-space()='Log in']")
        self.logout_button=(By.XPATH,"(//a[normalize-space()='Log out'])[1]")
               

    def navigate_to_register_page(self):               
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def navigate_to_login_page(self):
        self.driver.get(self.login_url)
        self.driver.maximize_window()

    def register_with_userdata(self,firstname,lastname,email,password,confirmpassword):        
        self.driver.find_element(*self.firstname_input).send_keys(firstname)
        self.driver.find_element(*self.lastname_input).send_keys(lastname)        
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirmpassword_input).send_keys(confirmpassword)
        self.driver.find_element(*self.register_button).click()

        self.driver.implicitly_wait(3)
        registration_output_element = self.driver.find_element(*self.registraion_output)
        return registration_output_element.text
    

    def register_without_userdata(self):        
        self.driver.find_element(*self.register_button).click()
        self.driver.implicitly_wait(3)
        firstname_error_element = self.driver.find_element(*self.firstname_error)
        return firstname_error_element.text
    
    def register_with_inavlid_emailid(self,email):  
        self.driver.find_element(*self.email_input).send_keys(email)     
        self.driver.find_element(*self.register_button).click()
        self.driver.implicitly_wait(3)
        email_error_element = self.driver.find_element(*self.email_error)
        return email_error_element.text
    
    def register_with_inavlid_password(self,password):  
        self.driver.find_element(*self.password_input).send_keys(password)     
        self.driver.find_element(*self.register_button).click()
        self.driver.implicitly_wait(3)
        password_error_element = self.driver.find_element(*self.password_error)
        return password_error_element.text
    
    def register_with_mismatch_password(self,password,confirmpassword):  
        self.driver.find_element(*self.password_input).send_keys(password) 
        self.driver.find_element(*self.confirmpassword_input).send_keys(confirmpassword)     
        self.driver.find_element(*self.register_button).click()
        self.driver.implicitly_wait(3)
        mismatchpassword_password_error_element = self.driver.find_element(*self.confirmpassword_error)
        return mismatchpassword_password_error_element.text
    
    def register_with_user_all_data(self,firstname,lastname,day,month,year,email,company_name,password,confirmpassword):  
        self.driver.find_element(*self.gender_male).click()
        # self.driver.find_element(*self.gender_female).click()        
        self.driver.find_element(*self.firstname_input).send_keys(firstname)
        self.driver.find_element(*self.lastname_input).send_keys(lastname) 
        self.driver.find_element(*self.date_of_birth_day).send_keys(day) 
        self.driver.find_element(*self.date_of_birth_month).send_keys(month)
        self.driver.find_element(*self.date_of_birth_year).send_keys(year)     
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.company_input).send_keys(company_name)
        self.driver.find_element(*self.newsletter_input).click()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirmpassword_input).send_keys(confirmpassword)        
        self.driver.find_element(*self.register_button).click()

        self.driver.implicitly_wait(3)
        registration_output_element = self.driver.find_element(*self.registraion_output)
        return registration_output_element.text
    
    def ligin_with_registred_user_data(self,email,password):    
        self.driver.find_element(*self.email_login).send_keys(email)
        self.driver.find_element(*self.password_login).send_keys(password)        
        self.driver.find_element(*self.login_button).click()  
        self.driver.implicitly_wait(3)  
        return "Login successful"
        

    def wait_for_registration_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.firstname_input)
        )
