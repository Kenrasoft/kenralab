from page_objects.product.jewelry_list_page import JewelryListPage
from page_objects.product.books_list_page import BooksListPage
from page_objects.checkout.ckstep0_shopping_cart_page import ShoppingCartPage
from page_objects.checkout.ckstep1_welcome_user_page import WelcomeUserPage
from page_objects.checkout.ckstep2_billing_address_page import BillingAddressPage
from page_objects.checkout.ckstep3_shipping_method_page import ShippingMethodPage
from page_objects.checkout.ckstep4_payment_method_page import PaymentMethodPage
from page_objects.checkout.ckstep5_creditcard_info_page import CreditCardInfoPage


def pre_req_shopping_cart(browser, product_type):
    list_page = None
    if(product_type == "jewelry"):
        list_page = JewelryListPage(browser)
    elif(product_type == "books"):
        list_page = BooksListPage(browser)
    
    if(list_page):
        list_page.navigate_to_product_page()              
        list_page.add_product_to_cart() 

def pre_req_welcome_user(browser, product_type):
    pre_req_shopping_cart(browser, product_type)
    shopping_cart = ShoppingCartPage(browser)
    shopping_cart.shopping_cart_checkout() 

def pre_req_billing_address(browser, product_type):
    pre_req_welcome_user(browser, product_type)
    welcome_user_page = WelcomeUserPage(browser)
    welcome_user_page.checkout_as_guest()

def pre_req_shipping_method(browser, product_type):
    pre_req_billing_address(browser, product_type)
    billing_address_page = BillingAddressPage(browser)
    billing_address_page.update_billing_address()

def pre_req_payment_method(browser, product_type):
    pre_req_shipping_method(browser, product_type)
    shipping_method_page = ShippingMethodPage(browser)
    shipping_method_page.update_shipping_method()

def pre_req_creditcard_info(browser, product_type):
    pre_req_payment_method(browser, product_type)
    payment_method = PaymentMethodPage(browser)
    payment_method.update_payment_method()
