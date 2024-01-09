from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ProductBasePage(BasePage):


    def __init__(self, driver):
        super(ProductBasePage, self).__init__(driver) 
        self.title=(By.CSS_SELECTOR,"div[class='page-title']")
        self.addtocart = (By.CLASS_NAME, "product-box-add-to-cart-button")
        self.shoppingcart_link=(By.XPATH,"//a[normalize-space()='Shopping cart']") 
        self.click_shoppingcart=(By.XPATH, "//span[@class='cart-label']") 
        self.shopping_cart_title=(By.CSS_SELECTOR,"div[class='page-title'] h1")

    def navigate_to_product_page(self):               
        self.driver.get(self.url)
        return self.driver.find_element(*self.title).text
    
    def add_product_to_cart(self):
        buttons = self.driver.find_elements(*self.addtocart)
        for button in buttons:
            print(f"button: {button.text}")
            if(button.text == "ADD TO CART"): 
                button.click()
                break

        time.sleep(5)
        shoppingcart_link_element = self.driver.find_element(*self.shoppingcart_link)
        shoppingcart_link_element.click()
        time.sleep(5)
        title = self.driver.find_element(*self.shopping_cart_title)
        print(f"Title of cart: {title.text}")
        return title.text
