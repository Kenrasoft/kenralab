from page_objects.checkout.ckstep1_welcome_user_page import WelcomeUserPage
from test_cases.base_test import BaseTest
from utils.pre_reqs import pre_req_welcome_user
from test_data.product.product_data import product_type

import pytest

class TestGuestCheckoutPage:

    @pytest.fixture
    def setup(self,browser, product_type):
       pre_req_welcome_user(browser, product_type) 
                   
    @pytest.mark.parametrize("product_type", product_type) 
    def test_welcome_guest_page(self,browser,setup, product_type):
        welcome_user_page = WelcomeUserPage(browser)
        page_title = welcome_user_page.checkout_as_guest() 
        print (page_title)
        assert page_title == "Checkout"