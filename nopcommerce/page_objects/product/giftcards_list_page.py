from page_objects.product.product_base_page import ProductBasePage
from page_objects.product.giftcard_details_page import GiftCardDetailspage
from selenium.webdriver.common.by import By
import time

class GiftCardListPage(ProductBasePage):

    def __init__(self, driver):
        super(GiftCardListPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/gift-cards"
        self.driver.maximize_window()   
        

    def add_product_to_cart(self):
        buttons = self.driver.find_elements(*self.addtocart)
        # buttons[1].click()
        buttons[2].click()
        # for button in buttons:
        #     print(f"button: {button.text}")
        #     if(button.text == "ADD TO CART"): 
        #         button.click()
        #         break
        # time.sleep(2)  
       
        time.sleep(3)
        giftcard_page= GiftCardDetailspage(self.driver)   
        # giftcard_page.virtual_giftcard()
        giftcard_page.physical_giftcards()
        
        shoppingcart_link_element = self.driver.find_element(*self.shoppingcart_link)
        shoppingcart_link_element.click()
        time.sleep(2)
                   
        title = self.driver.find_element(*self.page_title)
        print(f"Title of cart: {title.text}")
        return title.text
    

   




