from page_objects.checkout.ckstep5_creditcard_info_page import CreditCardInfoPage
from test_data.product.product_data import product_type
from utils.pre_reqs import pre_req_creditcard_info
from utils.pre_reqs import pre_req_payment_method
import pytest


class TestCreditCardPage:
    @pytest.fixture
    def setup(self, browser, product_type):
        pre_req_creditcard_info(browser, product_type)
        
        
    @pytest.mark.parametrize("product_type", product_type)     
    def test_credit_card(self, browser, setup, product_type):
        creditcard_info= CreditCardInfoPage(browser)
        page_title = creditcard_info.update_creditcard_info()
        #assert page_title == "Checkout"