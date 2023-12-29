from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from test_data.jewelry_user_data import jewelry_user_data
import time

class JewelryPage(BasePage):

    def __init__(self, driver):
        super(JewelryPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/jewelry"           
        self.checkout_guest_button=(By.XPATH,"//button[normalize-space()='Checkout as Guest']")
        self.click_addtocart=(By.XPATH, "//div[@class='products-wrapper']//div[2]//div[1]//div[2]//div[3]//div[2]//button[1]")
        self.click_shoppingcart=(By.XPATH, "//span[@class='cart-label']")    
        self.click_checkagree=(By.XPATH, "//input[@id='termsofservice']")
        self.click_checkoutbutton=(By.XPATH, "//button[@id='checkout']")
        self.checkout_guest_button=(By.XPATH,"//button[normalize-space()='Checkout as Guest']")
        self.checkbox_ship_address=(By.XPATH, "//input[@id='ShipToSameAddress']")
        self.firstname_input=(By.XPATH, "//input[@id='BillingNewAddress_FirstName']")
        self.lastname_input=(By.XPATH, "//input[@id='BillingNewAddress_LastName']")
        self.email_input=(By.XPATH, "//input[@id='BillingNewAddress_Email']")
        self.company_input=(By.XPATH, "//input[@id='BillingNewAddress_Company']")
        self.country_select=(By.XPATH, "//select[@id='BillingNewAddress_CountryId']")
        self.state_select=(By.XPATH, "//select[@id='BillingNewAddress_StateProvinceId']")
        self.city_input=(By.XPATH, "//input[@id='BillingNewAddress_City']")      
        self.address_input=(By.XPATH, "//input[@id='BillingNewAddress_Address1']")
        self.zip_postalcode=(By.XPATH, "//input[@id='BillingNewAddress_ZipPostalCode']")
        self.phone_number=(By.XPATH, "//input[@id='BillingNewAddress_PhoneNumber']")
        self.fax_number=(By.XPATH, "//input[@id='BillingNewAddress_FaxNumber']")
        self.continue_button=(By.XPATH, "//button[@onclick='if (!window.__cfRLUnblockHandlers) return false; Billing.save()']")
        self.ckeck_ground=(By.XPATH, "//input[@id='shippingoption_0']")
        self.checkout_button=(By.XPATH, "//button[@class='button-1 shipping-method-next-step-button']")
        self.check_creditcardoption=(By.XPATH, "//input[@id='paymentmethod_1']")
        self.click_continue_button=(By.XPATH, "//button[@class='button-1 payment-method-next-step-button']")
        # credit information
        self.credit_card_type=(By.XPATH, "//select[@id='CreditCardType']")
        self.cardholder_name=(By.XPATH, "//input[@id='CardholderName']")
        self.cardnumber_input=(By.XPATH, "//input[@id='CardNumber']")
        self.card_expiry_date=(By.XPATH, "//select[@id='ExpireMonth']")
        self.card_expiry_year=(By.XPATH, "//select[@id='ExpireYear']")
        self.crad_code_input=(By.XPATH, "//input[@id='CardCode']")
        self.creditinfo_continue_button=(By.XPATH, "//button[@class='button-1 payment-info-next-step-button']")
        self.confirmbutton=(By.XPATH, "//button[normalize-space()='Confirm']")
        # self.click_confirm_button=(By.XPATH, "//button[normalize-space()='Confirm']")
        self.click_order_detailslink=(By.XPATH, "//a[normalize-space()='Click here for order details.']")
        # self.order_status=(By.CLASS_NAME,"order-status")



    def navigate_to_jewelry_page(self):               
        self.driver.get(self.url)
        self.driver.maximize_window()

    def jewelry_e2e_flow(self):   
        self.driver.find_element(*self.click_addtocart).click()
        self.driver.implicitly_wait(6)
        self.driver.find_element(*self.click_shoppingcart).click() 
        self.driver.find_element(*self.click_checkagree).click()
        self.driver.find_element(*self.click_checkoutbutton).click()
        self.driver.find_element(*self.checkout_guest_button).click()
        self.driver.find_element(*self.country_select).send_keys(jewelry_user_data["country"])
        self.driver.find_element(*self.firstname_input).send_keys(jewelry_user_data["first_name"])
        self.driver.find_element(*self.lastname_input).send_keys(jewelry_user_data["last_name"])
        self.driver.find_element(*self.email_input).send_keys(jewelry_user_data["email"]) 
        self.driver.find_element(*self.city_input).send_keys(jewelry_user_data["city"])        
        self.driver.find_element(*self.address_input).send_keys(jewelry_user_data["Address"])
        self.driver.find_element(*self.zip_postalcode).send_keys(jewelry_user_data["zip"])
        self.driver.find_element(*self.phone_number).send_keys(jewelry_user_data["phone_number"])
        self.driver.find_element(*self.state_select).send_keys(jewelry_user_data["state"])
        self.driver.find_element(*self.company_input).send_keys(jewelry_user_data["company"])     
        self.driver.find_element(*self.continue_button).click()
        
        # credit card information
        self.driver.find_element(*self.checkout_button).click()
        self.driver.find_element(*self.check_creditcardoption).click()
        self.driver.find_element(*self.click_continue_button).click()
        self.driver.find_element(*self.credit_card_type).send_keys("Visa")
        self.driver.find_element(*self.cardholder_name).send_keys("test card")
        self.driver.find_element(*self.cardnumber_input).send_keys("4242424242424242")
        self.driver.find_element(*self.card_expiry_date).send_keys("01")
        self.driver.find_element(*self.card_expiry_year).send_keys("2025")
        self.driver.find_element(*self.crad_code_input).send_keys("123")
        self.driver.find_element(*self.creditinfo_continue_button).click()
        self.driver.find_element(*self.confirmbutton).click()
        self.driver.find_element(*self.click_order_detailslink).click()
        

        self.driver.implicitly_wait(50)
        # time.sleep(50)


        

        # self.driver.find_element(*self.checkbox_ship_address).click()
        # self.driver.find_element(*self.click_addtocart).click()
        # self.driver.implicitly_wait(10)
       

        

    



