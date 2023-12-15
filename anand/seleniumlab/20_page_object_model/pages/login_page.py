# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By




class LoginPage:
    def __init__(self, driver):
        
        self.driver = driver
        self.url = "https://demoqa.com/login"
        self.username_input = (By.ID, "userName")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login")

    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def login_with_credentials(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

        self.driver.implicitly_wait(3)
        user_output_element = self.driver.find_element(By.ID, "userName-value")
        return user_output_element.text

    def wait_for_login_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
