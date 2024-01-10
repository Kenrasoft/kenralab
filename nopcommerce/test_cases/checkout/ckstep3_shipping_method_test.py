from page_objects.checkout.ckstep3_shipping_method_page import ShippingMethodPage
from test_data.product.product_data import product_type
from utils.pre_reqs import pre_req_shipping_method
from utils.pre_reqs import pre_req_billing_address

import pytest

class TestShippingMethodPage:
    @pytest.fixture
    def setup(self, browser, product_type):
        pre_req_shipping_method(browser, product_type) 

    @pytest.mark.parametrize("product_type", product_type)   
    def test_shipping_method(self, browser, setup, product_type):
        shipping_method = ShippingMethodPage(browser)
        shipping_method.update_shipping_method()
        
