from page_objects.product.jewelry_list_page import JewelryListPage
from page_objects.checkout.ckstep0_shopping_cart_page import ShoppingCartPage
from page_objects.checkout.ckstep1_guest_checkout_page import GuestCheckoutPage

import pytest

class TestGuestCheckoutPage (TestShoppingCartPage):
    @pytest.fixture
    def setup_method(self,browser):
        jewelry_page = JewelryListPage(browser)       
        jewelry_page.navigate_to_product_page()  
        
        # adding item to the cart 
        jewelry_page.add_item_to_cart()  
             
        # shopping cart page
        shopping_cart = ShoppingCartPage(browser)
        shopping_cart.shopping_cart_checkout() 
               
        # guest checkout page
    def test_guest_checkout_page(self,browser,setup_method):
        guestcheckout_page = GuestCheckoutPage(browser)
        page_title3=guestcheckout_page.guest_checkout_page() 
        print (page_title3)
        assert page_title3=="Checkout"