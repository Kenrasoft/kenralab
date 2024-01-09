from page_objects.product.product_base_page import ProductBasePage
from selenium.webdriver.common.by import By

class JewelryPage(ProductBasePage):

    def __init__(self, driver):
        super(JewelryPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/jewelry"
        self.title=(By.XPATH,"//h1[normalize-space()='Jewelry']")
        self.addtocart=(By.XPATH, "//div[@class='products-wrapper']//div[2]//div[1]//div[2]//div[3]//div[2]//button[1]")
        #self.addtocart=(By.XPATH, "//button[@class='button-2 product-box-add-to-cart-button']")
        
        self.shoppingcart_title_page=(By.XPATH,"//a[normalize-space()='Shopping cart']") 
        self.click_shoppingcart=(By.XPATH, "//span[@class='cart-label']")    
    

    