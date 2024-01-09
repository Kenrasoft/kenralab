from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
import time

class ShippingMethodPage(BasePage):

    def __init__(self, driver):
        super(ShippingMethodPage, self).__init__(driver)     
        self.ground_shipping = (By.ID, "shippingoption_0")
        self.continue_button = (By.XPATH, "//button[@class='button-1 shipping-method-next-step-button']")

    
    def update_shipping_method(self):
        #self.driver.find_element(*self.ground_shipping)
        time.sleep(5)
        self.driver.find_element(*self.continue_button).click()
