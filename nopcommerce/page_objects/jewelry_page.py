from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class JewelryPage(BasePage):

    def __init__(self, driver):
        super(JewelryPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/jewelry" 
        self.title=(By.XPATH,"//h1[normalize-space()='Jewelry']")
        self.click_addtocart=(By.XPATH, "//div[@class='products-wrapper']//div[2]//div[1]//div[2]//div[3]//div[2]//button[1]")
        self.shoppingcart_title_page=(By.XPATH,"//h1[normalize-space()='Shopping cart']") 
        self.click_shoppingcart=(By.XPATH, "//span[@class='cart-label']")    
             
    def navigate_to_jewelry_page(self):               
        self.driver.get(self.url)
        self.driver.maximize_window()
        return self.driver.find_element(*self.title).text
    
    def add_item_to_cart(self):
        self.driver.find_element(*self.click_addtocart).click()
        self.driver.implicitly_wait(2)
        
        self.driver.find_element(*self.click_shoppingcart).click() 
        return self.driver.find_element(*self.shoppingcart_title_page).text
        
        

    