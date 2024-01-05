from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage



class PaymentMethodPage(BasePage):

    def __init__(self, driver):
        super(PaymentMethodPage, self).__init__(driver)     
        self.check_creditcardoption=(By.XPATH, "//input[@id='paymentmethod_1']")
        self.click_continue_button=(By.XPATH, "//button[@class='button-1 payment-method-next-step-button']")
        self.payment_info_pagetitle=(By.XPATH, "//h1[normalize-space()='Checkout']")


    def update_payment_method(self):
        self.driver.find_element(*self.check_creditcardoption).click()
        self.driver.find_element(*self.click_continue_button).click()
        return self.driver.find_element(*self.payment_info_pagetitle).text
        