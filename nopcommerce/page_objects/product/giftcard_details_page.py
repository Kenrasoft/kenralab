from page_objects.product.product_base_page import ProductBasePage
from test_data.user.giftcard_user_data import giftcard_userdata
from test_data.user.giftcard_user_data import physical_giftcard
from selenium.webdriver.common.by import By
import time

class GiftCardDetailspage(ProductBasePage):

    def __init__(self, driver):
        super(GiftCardDetailspage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/gift-cards"

        # # Virtual Giftcard page
        # self.recipientname=(By.ID,"giftcard_43_RecipientName")
        # self.recipientemail=(By.ID,"giftcard_43_RecipientEmail")
        # self.yourname=(By.ID,"giftcard_43_SenderName")
        # self.youremail=(By.ID,"giftcard_43_SenderEmail")
        # self.message_virtual=(By.ID,"giftcard_43_Message")
        # # self.message=(By.XPATH,"//textarea[@id='giftcard_43_Message']")
        # self.productquantity=(By.ID,"product_enteredQuantity_43")
        # self.addproducttocart=(By.ID,"add-to-cart-button-43")

        # Physical Giftcard page

        # self.product_title=(By.CLASS_NAME,"product-name")#//h1[normalize-space()='$50 Physical Gift Card']        
        # self.recipients_name=(By.CLASS_NAME,"recipient-name")        
        # self.your_name=(By.ID,"giftcard_44_SenderName")        
        # self.message_physical=(By.ID,"giftcard_44_Message")        
        # self.addtocart_button=(By.ID,"add-to-cart-button-44")
        
        self.product_title=(By.CLASS_NAME,"product-name")#////h1[normalize-space()='$100 Physical Gift Card']
        self.recipients_name=(By.ID,"giftcard_45_RecipientName")
        self.your_name=(By.ID,"giftcard_45_SenderName")
        self.message_physical=(By.ID,"giftcard_45_Message")
        self.addtocart_button=(By.ID,"add-to-cart-button-45")
        
    # def virtual_giftcard(self):
    #     self.driver.find_element(*self.recipientname).send_keys(giftcard_userdata["recipient_name"])              
    #     self.driver.find_element(*self.recipientemail).send_keys(giftcard_userdata["recipient_email"])       
    #     self.driver.find_element(*self.yourname).send_keys(giftcard_userdata["your_name"])      
    #     self.driver.find_element(*self.youremail).send_keys(giftcard_userdata["your_email"])        
    #     self.driver.find_element(*self.message_virtual).send_keys(giftcard_userdata["message"])      
    #     self.driver.find_element(*self.addproducttocart).click()

    def physical_giftcards(self):
        # self.find_element(*self.product_title).text
        self.driver.find_element(*self.recipients_name).send_keys(physical_giftcard["recipients_name"])
        self.driver.find_element(*self.your_name).send_keys(physical_giftcard["your_name"])
        self.driver.find_element(*self.message_physical).send_keys(physical_giftcard["message"])
        time.sleep(5)
        print("before physical buttons clicked")
        self.driver.find_element(*self.addtocart_button).click()
        print("after physical buttons clicked")

    







