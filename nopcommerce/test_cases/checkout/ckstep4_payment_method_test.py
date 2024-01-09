from page_objects.checkout.ckstep4_payment_method_page import PaymentMethodPage
from test_data.product.product_data import product_type
from utils.pre_reqs import pre_req_payment_method


import pytest


class TestPaymentMethodPage:
    @pytest.fixture
    def setup(self, browser, product_type):
        pre_req_payment_method(browser, product_type)

    @pytest.mark.parametrize("product_type", product_type)     
    def test_payment_method(self, browser, setup, product_type):
        
        payment_method = PaymentMethodPage(browser)
        page_title = payment_method.update_payment_method()
        #print (page_title6)
        #assert page_title6=="Checkout"
        