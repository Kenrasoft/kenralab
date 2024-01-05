from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from test_data.jewelry_user_data import jewelry_user_data


class BillingAddressPage(BasePage):

    def __init__(self, driver):
        super(BillingAddressPage, self).__init__(driver)   
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
        self.shipping_method_pagetitle=(By.XPATH, "//h1[normalize-space()='Checkout']")

    def update_billing_address(self):
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
        return self.driver.find_element(*self.shipping_method_pagetitle).text
        