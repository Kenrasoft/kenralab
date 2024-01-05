from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import time



class ShoppingCartPage(BasePage):

    def __init__(self, driver):
        super(ShoppingCartPage, self).__init__(driver)
       
        # self.checkout_guest_button=(By.XPATH,"//button[normalize-space()='Checkout as Guest']")
        self.welcome_signin_page=(By.XPATH,"//h1[normalize-space()='Welcome, Please Sign In!']")
        self.click_checkagree=(By.XPATH, "//input[@id='termsofservice']")
        self.click_checkoutbutton=(By.XPATH, "//button[@id='checkout']")
    
    def shopping_cart_checkout(self):
        self.driver.find_element(*self.click_checkagree).click()
        self.driver.find_element(*self.click_checkoutbutton).click()
        return self.driver.find_element(*self.welcome_signin_page).text
    