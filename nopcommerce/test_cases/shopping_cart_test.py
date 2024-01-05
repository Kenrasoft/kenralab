from page_objects.jewelry_page import JewelryPage
from page_objects.billing_address_page import BillingAddressPage
from page_objects.creditcard_info_page import CreditCardInfoPage
from page_objects.addtocart_page import AddToCartPage
from page_objects.shipping_method_page import ShippingMethodPage
from page_objects.payment_method_page import PaymentMethodPage
from page_objects.order_details_page import OrderDetailsPage
from page_objects.shopping_cart_page import ShoppingCartPage
from page_objects.guest_checkout_page import GuestCheckoutPage
import pytest

class TestShoppingCartPage:
    @pytest.fixture
    def setup_method(self,browser):
        jewelry_page = JewelryPage(browser)       
        jewelry_page.navigate_to_jewelry_page()              
        # adding item to the cart 
        jewelry_page.add_item_to_cart() 
                            
        # shopping cart page
    def test_shopping_cart(self,browser,setup_method):
        shopping_cart = ShoppingCartPage(browser)
        page_title2=shopping_cart.shopping_cart_checkout() 
        print (page_title2)
        assert page_title2=="Welcome, Please Sign In!"

        

               




       
