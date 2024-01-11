from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class ProductBasePage(BasePage):

    def __init__(self, driver):
        super(ProductBasePage, self).__init__(driver) 
        self.title=(By.CSS_SELECTOR,"div[class='page-title']")
        self.addtocart = (By.CLASS_NAME, "product-box-add-to-cart-button")
        self.shoppingcart_link=(By.XPATH,"//a[normalize-space()='Shopping cart']") 
        self.click_shoppingcart=(By.XPATH, "//span[@class='cart-label']") 
        self.page_title=(By.CSS_SELECTOR,"div[class='page-title'] h1")
        self.sort_by = (By.ID, 'products-orderby')
        self.product_price = (By.CLASS_NAME, 'price.actual-price')
        self.product_title = (By.CLASS_NAME, 'product-title')
        self.prodct_name = (By.TAG_NAME, 'a')
        self.display_per_page = (By.ID, 'products-pagesize')

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
        title = self.driver.find_element(*self.page_title)
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
    
    def display_per_page_three(self):
        display_per_page = self.driver.find_element(*self.display_per_page)
        display_per_page.click()
        select = Select(display_per_page)
        select.select_by_value("3")
        time.sleep(2)
        product_elements = self.driver.find_elements(*self.product_title)
        products = [element.find_element(*self.prodct_name).text for element in product_elements]
        return len(products)
    
    def display_per_page_six(self):
        display_per_page = self.driver.find_element(*self.display_per_page)
        display_per_page.click()
        select = Select(display_per_page)
        select.select_by_value("6")
        time.sleep(2)
        product_elements = self.driver.find_elements(*self.product_title)
        products = [element.find_element(*self.prodct_name).text for element in product_elements]
        return len(products)
    
    def display_per_page_nine(self):
        display_per_page = self.driver.find_element(*self.display_per_page)
        display_per_page.click()
        select = Select(display_per_page)
        select.select_by_value("9")
        time.sleep(2)
        product_elements = self.driver.find_elements(*self.product_title)
        products = [element.find_element(*self.prodct_name).text for element in product_elements]
        return len(products)
    
    def grid_view(self):
        view_mode_div = self.driver.find_element(By.CLASS_NAME, 'product-viewmode')
        grid_view_option = view_mode_div.find_element(By.CSS_SELECTOR, 'a[data-viewmode="grid"]')
        grid_view_option.click()
        return grid_view_option
    
    def list_view(self):
        view_mode_div = self.driver.find_element(By.CLASS_NAME, 'product-viewmode')
        list_view_option = view_mode_div.find_element(By.CSS_SELECTOR, 'a[data-viewmode="list"]')
        list_view_option.click()
        time.sleep(2)
        return list_view_option
    
    def compare(self):
        # Locate and click the "Add to compare list" button
        compare_button = self.driver.find_element(By.CLASS_NAME, 'button-2.add-to-compare-list-button')
        compare_button.click()
        notification = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bar-notification.success'))
        )
        notification_link = notification.find_element(By.CSS_SELECTOR, 'a[href="/compareproducts"]')
        notification_link.click()
        title = self.driver.find_element(*self.page_title)
        return title.text
    
    def wishlist(self):
        wishlist_button = self.driver.find_element(By.CLASS_NAME, 'button-2.add-to-wishlist-button')
        wishlist_button.click()
        notification = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'bar-notification.success'))
        )
        notification_link = notification.find_element(By.CSS_SELECTOR, 'a[href="/wishlist"]')
        notification_link.click()
        title = self.driver.find_element(*self.page_title)
        return title.text


    

