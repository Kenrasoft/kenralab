from page_objects.product.jewelry_list_page import JewelryListPage
from page_objects.checkout.ckstep2_billing_address_page import BillingAddressPage
from page_objects.checkout.ckstep5_creditcard_info_page import CreditCardInfoPage
from page_objects.checkout.ckstep3_shipping_method_page import ShippingMethodPage
from page_objects.checkout.ckstep4_payment_method_page import PaymentMethodPage
from page_objects.checkout.ckstep6_order_details_page import OrderDetailsPage
from page_objects.checkout.ckstep0_shopping_cart_page import ShoppingCartPage
from page_objects.checkout.ckstep1_guest_checkout_page import GuestCheckoutPage

class TestJewelE2EPage:    

    # Testcase for Jewelry E2E flow  
    def test_jewelry_e2e_checkout(self,browser):
        jewelry_page = JewelryListPage(browser)       
        page_title=jewelry_page.navigate_to_product_page()  
        print (page_title)
        assert page_title=="Jewelry"

        page_title=jewelry_page.add_product_to_cart()  
        print (page_title)
        assert page_title=="Shopping cart"                
        
        # shopping cart page
        shopping_cart = ShoppingCartPage(browser)
        page_title2=shopping_cart.shopping_cart_checkout() 
        print (page_title2)
        assert page_title2=="Welcome, Please Sign In!"

        # guest checkout page
        guestcheckout_page = GuestCheckoutPage(browser)
        page_title3=guestcheckout_page.guest_checkout_page() 
        print (page_title3)
        assert page_title3=="Checkout"
                
        # billing address
        billing_address = BillingAddressPage(browser)
        page_title4=billing_address.update_billing_address()
        print (page_title4)
        assert page_title4=="Checkout"
        
        # selecting the shipping method
        shipping_method = ShippingMethodPage(browser)
        page_title5=shipping_method.update_shipping_method()
        print (page_title5)
        assert page_title5=="Checkout"

        # selecting the payment method
        payment_method = PaymentMethodPage(browser)
        page_title6=payment_method.update_payment_method()
        print (page_title6)
        assert page_title6=="Checkout"
        
        
        # filling credit card information
        creditcard_info= CreditCardInfoPage(browser)
        page_title7=creditcard_info.update_credit_card_info()
        print (page_title7)
        assert page_title7=="Checkout"


        # get order information
        order_info= OrderDetailsPage(browser)        
        order_details=order_info.update_order_details()      
        print("Order details: "+order_details)

        




       
