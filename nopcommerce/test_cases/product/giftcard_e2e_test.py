from page_objects.product.giftcards_list_page import GiftCardListPage
from page_objects.checkout.ckstep0_shopping_cart_page import ShoppingCartPage
from page_objects.checkout.ckstep1_welcome_user_page import WelcomeUserPage
from page_objects.checkout.ckstep2_billing_address_page import BillingAddressPage
from page_objects.checkout.ckstep5_creditcard_info_page import CreditCardInfoPage
from page_objects.checkout.ckstep3_shipping_method_page import ShippingMethodPage
from page_objects.checkout.ckstep4_payment_method_page import PaymentMethodPage
from page_objects.checkout.ckstep6_order_details_page import OrderDetailsPage


class TestGiftCardE2EPage:    

    # Testcase for Jewelry E2E flow  
    def test_giftcard_e2e_checkout(self,browser):
        giftcard_page = GiftCardListPage(browser)       
        page_title=giftcard_page.navigate_to_product_page()  
        print (page_title)
        assert page_title=="Gift Cards"

        page_title=giftcard_page.add_product_to_cart()  
        print (page_title)
        assert page_title=="Shopping cart"   

     # shopping cart page
        shopping_cart = ShoppingCartPage(browser)
        page_title2=shopping_cart.shopping_cart_checkout() 
        print (page_title2)
        assert page_title2=="Welcome, Please Sign In!"
                 
        # guest checkout page
        welcome_user_page = WelcomeUserPage(browser)
        page_title3=welcome_user_page.checkout_as_guest() 
        print (page_title3)
        assert page_title3=="Checkout" 

        # billing address
        billing_address = BillingAddressPage(browser)
        page_title4=billing_address.update_billing_address()
        print (page_title4)
        assert page_title4=="Checkout"

        # selecting the shipping method
        shipping_method = ShippingMethodPage(browser)        
        shipping_method.update_shipping_method()
        # print (page_title5)
        # assert page_title5=="Checkout"
        
        # selecting the payment method
        payment_method = PaymentMethodPage(browser)
        payment_method.update_payment_method()
        # print (page_title6)
        # assert page_title6=="Checkout"

        # filling credit card information
        creditcard_info= CreditCardInfoPage(browser)
        creditcard_info.update_creditcard_info()
        # print (page_title7)
        # assert page_title7=="Checkout"

        # get order information
        order_info= OrderDetailsPage(browser)        
        order_details=order_info.update_order_details()      
        print("Order details: "+order_details)

        