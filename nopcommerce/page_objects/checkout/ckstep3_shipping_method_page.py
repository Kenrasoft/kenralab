from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ShippingMethodPage(BasePage):

    def __init__(self, driver):
        super(ShippingMethodPage, self).__init__(driver)     
        self.ckeck_ground=(By.XPATH, "//input[@id='shippingoption_0']")
        self.checkout_button=(By.XPATH, "//button[@class='button-1 shipping-method-next-step-button']")
        self.payment_method_pagetitle=(By.XPATH, "//h1[normalize-space()='Checkout']")
    
    def update_shipping_method(self):
        self.driver.find_element(*self.checkout_button).click()
        return self.driver.find_element(*self.payment_method_pagetitle).text