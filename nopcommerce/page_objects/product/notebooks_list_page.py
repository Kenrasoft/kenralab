from selenium.webdriver.common.by import By
from page_objects.product.product_base_page import ProductBasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class NotebooksListPage(ProductBasePage):
    def __init__(self, driver):
        super(NotebooksListPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/notebooks"