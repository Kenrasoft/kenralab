from page_objects.product.jewelry_list_page import JewelryListPage
from page_objects.checkout.ckstep0_shopping_cart_page import ShoppingCartPage
from page_objects.checkout.ckstep1_guest_checkout_page import GuestCheckoutPage
from page_objects.checkout.ckstep2_billing_address_page import BillingAddressPage
from page_objects.checkout.ckstep3_shipping_method_page import ShippingMethodPage
from page_objects.checkout.ckstep4_payment_method_page import PaymentMethodPage
from page_objects.checkout.ckstep5_creditcard_info_page import CreditCardInfoPage
import pytest

class TestCreditCardPage:
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

         # selecting the shipping method
        shipping_method = ShippingMethodPage(browser)
        shipping_method.update_shipping_method()

        # selecting the payment method
        payment_method = PaymentMethodPage(browser)
        payment_method.update_payment_method()
        
    def test_credit_card(self,browser,setup_method):
       # filling credit card information
        creditcard_info= CreditCardInfoPage(browser)
        page_title7=creditcard_info.update_credit_card_info()
        print (page_title7)
        assert page_title7=="Checkout"