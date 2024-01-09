from page_objects.product.jewelry_list_page import JewelryListPage
from page_objects.product.books_list_page import BooksListPage
from page_objects.checkout.ckstep0_shopping_cart_page import ShoppingCartPage
from test_cases.base_test import BaseTest
from test_data.product.product_data import product_type
from utils.pre_reqs import pre_req_shopping_cart

import pytest
import time

class TestShoppingCartPage (BaseTest):

    @pytest.fixture
    def setup(self,browser, product_type):
        pre_req_shopping_cart(browser, product_type)


    @pytest.mark.parametrize("product_type", product_type)                        
    def test_shopping_cart(self,browser,setup, product_type):
        shopping_cart = ShoppingCartPage(browser)
        page_title = shopping_cart.shopping_cart_checkout()
        time.sleep(5) 
        print (page_title)
        assert page_title=="Welcome, Please Sign In!"

               




       
