from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

class ProductBasePage(BasePage):


    def __init__(self, driver):
        super(ProductBasePage, self).__init__(driver) 
        self.title=(By.CSS_SELECTOR,"div[class='page-title']")
        self.addtocart = (By.CLASS_NAME, "product-box-add-to-cart-button")
        self.shoppingcart_link=(By.XPATH,"//a[normalize-space()='Shopping cart']") 
        self.click_shoppingcart=(By.XPATH, "//span[@class='cart-label']") 
        self.shopping_cart_title=(By.CSS_SELECTOR,"div[class='page-title'] h1")
        self.sort_by = (By.ID, 'products-orderby')
        self.product_price = (By.CLASS_NAME, 'price.actual-price')
        self.product_title = (By.CLASS_NAME, 'product-title')
        self.prodct_name = (By.TAG_NAME, 'a')

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
    
    def sort_products_AtoZ(self):
        sort_by = self.driver.find_element(*self.sort_by)
        sort_by.click()
        select = Select(sort_by)
        select.select_by_value('5')
        time.sleep(2)
        product_elements = self.driver.find_elements(*self.product_title)
        sorted_product_AtoZ = [element.find_element(*self.prodct_name).text for element in product_elements]
        return sorted_product_AtoZ
    
    def sort_products_ZtoA(self):
        sort_by = self.driver.find_element(*self.sort_by)
        sort_by.click()
        select = Select(sort_by)
        select.select_by_value('6')
        time.sleep(2)
        product_elements = self.driver.find_elements(*self.product_title)
        sorted_product_ZtoA = [element.find_element(*self.prodct_name).text for element in product_elements]
        return sorted_product_ZtoA

    def sort_products_price_lowtohigh(self):
        sort_by = self.driver.find_element(*self.sort_by)
        sort_by.click()
        select = Select(sort_by)
        select.select_by_value('10')
        time.sleep(2)
        product_elements = self.driver.find_elements(*self.product_price)
        sorted_product_prices = [element.text for element in product_elements]
        return sorted_product_prices
    
    def sort_products_price_hightolow(self):
        sort_by = self.driver.find_element(*self.sort_by)
        sort_by.click()
        select = Select(sort_by)
        select.select_by_value('11')
        time.sleep(2)
        product_elements = self.driver.find_elements(*self.product_price)
        sorted_product_prices = [element.text for element in product_elements]
        return sorted_product_prices
