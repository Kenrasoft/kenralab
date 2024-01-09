from page_objects.product.product_base_page import ProductBasePage
from selenium.webdriver.common.by import By
import time

class JewelryListPage(ProductBasePage):

    def __init__(self, driver):
        super(JewelryListPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/jewelry"
        self.rent_page_title=(By.CSS_SELECTOR,"div[class='product-name'] h1")
    
    def rent_product(self):
        buttons = self.driver.find_elements(*self.addtocart)
        for button in buttons:
            print(f"button: {button.text}")
            if(button.text == "RENT"): 
                button.click()
                break

        time.sleep(5)
        title = self.driver.find_element(*self.rent_page_title)
        print(f"Rent page title: {title.text}")
        return title.text

    