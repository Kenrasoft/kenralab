from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from test_data.checkout.user_payment_data import billing_data


class BillingAddressPage(BasePage):

    def __init__(self, driver):
        super(BillingAddressPage, self).__init__(driver)   
        
        self.firstname = (By.ID, "BillingNewAddress_FirstName")
        self.lastname =(By.ID, "BillingNewAddress_LastName")
        self.email_input = (By.ID, "BillingNewAddress_Email")
        self.company_input=(By.ID, "BillingNewAddress_Company")
        self.country_select=(By.ID, "BillingNewAddress_CountryId")
        self.state_select=(By.ID, "BillingNewAddress_StateProvinceId")
        self.city_input=(By.ID, "BillingNewAddress_City")      
        self.address_input=(By.ID, "BillingNewAddress_Address1")
        self.zip_postalcode=(By.ID, "BillingNewAddress_ZipPostalCode")
        self.phone_number=(By.ID, "BillingNewAddress_PhoneNumber")
        self.fax_number=(By.ID, "BillingNewAddress_FaxNumber")
        self.continue_button=(By.NAME, "save")
        self.shipping_method_pagetitle=(By.CSS_SELECTOR, "div[class='page-title'] h1")

    def update_billing_address(self):
        self.driver.find_element(*self.firstname).send_keys(billing_data["first_name"])
        self.driver.find_element(*self.lastname).send_keys(billing_data["last_name"])
        self.driver.find_element(*self.country_select).send_keys(billing_data["country"])
        self.driver.find_element(*self.email_input).send_keys(billing_data["email"]) 
        self.driver.find_element(*self.city_input).send_keys(billing_data["city"])        
        self.driver.find_element(*self.address_input).send_keys(billing_data["Address"])
        self.driver.find_element(*self.zip_postalcode).send_keys(billing_data["zip"])
        self.driver.find_element(*self.phone_number).send_keys(billing_data["phone_number"])
        self.driver.find_element(*self.state_select).send_keys(billing_data["state"])
        self.driver.find_element(*self.company_input).send_keys(billing_data["company"])     
        self.driver.find_element(*self.continue_button).click()

        shipping_page_title_element = self.driver.find_element(*self.shipping_method_pagetitle)
        print(shipping_page_title_element.text)
        return shipping_page_title_element.text
        
        