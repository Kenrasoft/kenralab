from page_objects.guest_checkout_page import GuestCheckoutPage
from page_objects.jewelry_page import JewelryPage
from page_objects.shopping_cart_page import ShoppingCartPage
from page_objects.billing_address_page import BillingAddressPage
import pytest

class TestBillingAddressPage:
    @pytest.fixture
    def setup_method(self,browser):
        jewelry_page = JewelryPage(browser)       
        jewelry_page.navigate_to_jewelry_page()  
        
        # adding item to the cart 
        jewelry_page.add_item_to_cart() 

        # shopping cart page
        shopping_cart = ShoppingCartPage(browser)
        shopping_cart.shopping_cart_checkout() 
        
        # guest checkout page
        guestcheckout_page = GuestCheckoutPage(browser)
        guestcheckout_page.guest_checkout_page() 
       
    def test_billing_address(self, browser,setup_method):
        # billing address
        billing_address = BillingAddressPage(browser)
        page_title4=billing_address.update_billing_address()
        print (page_title4)
        assert page_title4=="Checkout"