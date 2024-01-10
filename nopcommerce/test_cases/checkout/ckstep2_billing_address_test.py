from page_objects.checkout.ckstep2_billing_address_page import BillingAddressPage
from utils.pre_reqs import pre_req_welcome_user
from test_data.product.product_data import product_type
from utils.pre_reqs import pre_req_billing_address

import pytest

class TestBillingAddressPage:
    @pytest.fixture
    def setup(self,browser, product_type):
        pre_req_billing_address(browser, product_type) 
        
    
    @pytest.mark.parametrize("product_type", product_type) 
    def test_billing_address(self, browser, setup, product_type):
        billing_address = BillingAddressPage(browser)
        page_title = billing_address.update_billing_address()
        print (page_title)
        assert page_title == "Checkout"