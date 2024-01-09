from page_objects.product.jewelry_list_page import JewelryListPage
from page_objects.product.books_list_page import BooksListPage
from page_objects.checkout.ckstep0_shopping_cart_page import ShoppingCartPage
from test_cases.base_test import BaseTest
from test_data.product.product_data import product_type

import pytest
import time

class TestShoppingCartPage (BaseTest):

    @pytest.fixture
    def setup(self,browser, product_type):
        
        self.list_page = None
        if(product_type == "jewelry"):
            self.list_page = JewelryListPage(browser)
        elif(product_type == "books"):
            self.list_page = BooksListPage(browser)
        
        if(self.list_page):
            self.list_page.navigate_to_product_page()              
            self.list_page.add_product_to_cart() 

    @pytest.mark.parametrize("product_type", product_type)                        
    def test_shopping_cart(self,browser,setup, product_type):
        if(self.list_page):
            shopping_cart = ShoppingCartPage(browser)
            page_title = shopping_cart.shopping_cart_checkout()
            time.sleep(5) 
            print (page_title)
            assert page_title=="Welcome, Please Sign In!"

               




       
