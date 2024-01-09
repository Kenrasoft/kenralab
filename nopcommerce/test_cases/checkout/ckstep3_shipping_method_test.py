from page_objects.product.jewelry_list_page import JewelryListPage
from page_objects.checkout.ckstep0_shopping_cart_page import ShoppingCartPage
from page_objects.checkout.ckstep1_guest_checkout_page import GuestCheckoutPage
from page_objects.checkout.ckstep2_billing_address_page import BillingAddressPage
from page_objects.checkout.ckstep3_shipping_method_page import ShippingMethodPage
import pytest

class TestShippingMethodPage:
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
        guestcheckout_page = GuestCheckoutPage(browser)
        guestcheckout_page.guest_checkout_page() 

        # billing address
        billing_address = BillingAddressPage(browser)
        billing_address.update_billing_address()
       
    def test_shipping_method(self,browser,setup_method):
         # selecting the shipping method
        shipping_method = ShippingMethodPage(browser)
        page_title5=shipping_method.update_shipping_method()
        print (page_title5)
        assert page_title5=="Checkout"
        