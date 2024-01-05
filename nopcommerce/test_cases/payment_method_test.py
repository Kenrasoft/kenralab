from page_objects.guest_checkout_page import GuestCheckoutPage
from page_objects.jewelry_page import JewelryPage
from page_objects.shopping_cart_page import ShoppingCartPage
from page_objects.billing_address_page import BillingAddressPage
from page_objects.shipping_method_page import ShippingMethodPage
from page_objects.payment_method_page import PaymentMethodPage
import pytest

class TestPaymentMethodPage:
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

        # billing address
        billing_address = BillingAddressPage(browser)
        billing_address.update_billing_address()

         # selecting the shipping method
        shipping_method = ShippingMethodPage(browser)
        shipping_method.update_shipping_method()
        
    def test_payment_method(self,browser,setup_method):
        # selecting the payment method
        payment_method = PaymentMethodPage(browser)
        page_title6=payment_method.update_payment_method()
        print (page_title6)
        assert page_title6=="Checkout"
        