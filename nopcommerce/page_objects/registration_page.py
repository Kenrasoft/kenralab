from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage

class RegistraionPage(BasePage):

    def __init__(self, driver):
        super(RegistraionPage, self).__init__(driver)        
        self.url = "https://demo.nopcommerce.com/register?returnUrl=%2Fcustomer%2Finfo"
        self.firstname_input = (By.XPATH, "//input[@id='FirstName']")
        self.lastname_input = (By.XPATH, "//input[@id='LastName']")
        self.email_input = (By.XPATH, "//input[@id='Email']")
        self.password_input = (By.XPATH, "//input[@id='Password']")
        self.confirmpassword_input = (By.XPATH, "//input[@id='ConfirmPassword']")
        self.register_button = (By.XPATH, "//button[@id='register-button']")
        self.registraion_output =(By.XPATH, "//div[@class='result']")
        

    def navigate_to_register_page(self):        
        self.driver.get(self.url)

    def register_with_userdata(self, firstname,lastname,email,password,confirmpassword):
        self.driver.find_element(*self.firstname_input).send_keys(firstname)
        self.driver.find_element(*self.lastname_input).send_keys(lastname)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.confirmpassword_input).send_keys(confirmpassword)
        self.driver.find_element(*self.register_button).click()

        self.driver.implicitly_wait(3)
        registration_output_element = self.driver.find_element(*self.registraion_output)
        return registration_output_element.text

    def wait_for_registration_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.firstname_input)
        )
