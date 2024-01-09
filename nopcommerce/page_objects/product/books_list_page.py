from page_objects.product.product_base_page import ProductBasePage
from selenium.webdriver.common.by import By
import time

class BooksListPage(ProductBasePage):

    def __init__(self, driver):
        super(BooksListPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/books"
    
