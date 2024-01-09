from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from test_data.checkout.credit_card_data import credit_card_info
import time

class CreditCardInfoPage(BasePage):

    def __init__(self, driver):
        super(CreditCardInfoPage, self).__init__(driver)          
        self.credit_card_type=(By.XPATH, "//select[@id='CreditCardType']")
        self.cardholder_name=(By.XPATH, "//input[@id='CardholderName']")
        self.cardnumber_input=(By.XPATH, "//input[@id='CardNumber']")
        self.card_expiry_date=(By.XPATH, "//select[@id='ExpireMonth']")
        self.card_expiry_year=(By.XPATH, "//select[@id='ExpireYear']")
        self.crad_code_input=(By.XPATH, "//input[@id='CardCode']")
        self.continue_button=(By.XPATH, "//button[@class='button-1 payment-info-next-step-button']")
        self.confirm_button=(By.XPATH, "//button[@class='button-1 confirm-order-next-step-button']")
        self.order_info_page_title=(By.XPATH,"//h1[normalize-space()='Checkout']")

    def update_creditcard_info(self):
        time.sleep(5)
        self.driver.find_element(*self.credit_card_type).send_keys(credit_card_info["card_type"])
        self.driver.find_element(*self.cardholder_name).send_keys(credit_card_info["cardholder_name"])
        self.driver.find_element(*self.cardnumber_input).send_keys(credit_card_info["card_number"])
        self.driver.find_element(*self.card_expiry_date).send_keys(credit_card_info["expiration_month"])
        self.driver.find_element(*self.card_expiry_year).send_keys(credit_card_info["expiration_year"])
        self.driver.find_element(*self.crad_code_input).send_keys(credit_card_info["card_code"])
        self.driver.find_element(*self.continue_button).click()
        time.sleep(5)
        self.driver.find_element(*self.confirm_button).click()
        time.sleep(5)
        #return self.driver.find_element(*self.order_info_page_title).text