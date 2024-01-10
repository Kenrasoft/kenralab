from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

import time

class JewelryListPages(BasePage):

    def __init__(self, driver):
        super(JewelryListPages, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/jewelry"          
        self.sort_by=(By.XPATH,"//select[@id='products-orderby']")
        self.ascending=(By.XPATH,"//option[@value='5']")
        self.descending=(By.XPATH,"//option[@value='6']")
        self.lowtohigh=(By.XPATH,"//option[@value='10']")
        self.hightolow=(By.XPATH,"//option[@value='11']")
        self.createdon=(By.XPATH,"//option[@value='15']")
        self.display=(By.XPATH,"//select[@id='products-pagesize']")         
        self.perpage_option1=(By.XPATH,"//option[@value='3']")
        self.perpage_option2=(By.XPATH,"//select[@id='products-pagesize']/option[text()='6']")
        self.perpage_option3=(By.XPATH,"//option[@value='9']")
        self.item_perpage=(By.XPATH,"//a[normalize-space()='List']")
        self.product_items=(By.CSS_SELECTOR,'.item-grid .product-item')
        # self.product_items=(By.XPATH,"//*[contains(@class, 'item-grid')]//*[contains(@class, 'product-item')]")

        # self.product_prices=(By.CSS_SELECTOR,'.item-grid .price actual-price')
        self.product_prices = (By.XPATH,"//div[@class='add-info']//span[@class='price actual-price']")
        
             
    def navigate_to_jewelry_page(self):               
        self.driver.get(self.url)
        self.driver.maximize_window()

    def jewelry_list_actions(self):               
        
        self.driver.find_element(*self.ascending).click()
        time.sleep(2)
        self.driver.find_element(*self.descending).click()
        time.sleep(2)
        self.driver.find_element(*self.lowtohigh).click()
        time.sleep(2)
        self.driver.find_element(*self.hightolow).click()
        time.sleep(2)
        self.driver.find_element(*self.createdon).click()
        time.sleep(2)
        self.driver.find_element(*self.display).click()
        time.sleep(2)
        self.driver.find_element(*self.perpage_option1).click()
        time.sleep(2)
        self.driver.find_element(*self.perpage_option2).click()
        time.sleep(2)
        self.driver.find_element(*self.perpage_option3).click()
        time.sleep(2)
        self.driver.find_element(*self.item_perpage).click()
        time.sleep(2)    

        page_title = self.driver.title
        # print("Page Title:", page_title)
        return page_title
    
    def jewelry_list_sort_ascending(self):
        self.driver.find_element(*self.ascending).click()
        time.sleep(2)
        # Find all elements with class 'product-item' within the 'item-grid'
        product_items = self.driver.find_elements(*self.product_items)
        # Extract 'data-productid' values from each element
        product_ids = [item.get_attribute('data-productid') for item in product_items]
        return product_ids
    
    def jewelry_list_sort_descending(self):
        self.driver.find_element(*self.descending).click()
        time.sleep(2)
        # Find all elements with class 'product-item' within the 'item-grid'
        product_items = self.driver.find_elements(*self.product_items)
        # Extract 'data-productid' values from each element
        product_ids = [item.get_attribute('data-productid') for item in product_items]
        return product_ids

    def jewelry_price_lowtohigh(self):
        self.driver.find_element(*self.lowtohigh).click()
        time.sleep(2)
        # Find all elements with class 'product-prices' within the 'item-grid'
        product_prices = self.driver.find_elements(*self.product_prices)        
        # Extract and print each price value
        product_priceindollars = [item.text for item in product_prices]        
        print(product_priceindollars)
        return product_priceindollars
    
    def jewelry_price_hightolow(self):
        self.driver.find_element(*self.hightolow).click()
        time.sleep(2)
        # Find all elements with class 'product-prices' within the 'item-grid'
        product_prices = self.driver.find_elements(*self.product_prices)
        # Extract and print each price value
        product_priceindollars = [item.text for item in product_prices]
        print(product_priceindollars)
        return product_priceindollars
