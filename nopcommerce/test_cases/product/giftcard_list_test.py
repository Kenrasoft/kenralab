from page_objects.product.giftcards_list_page import GiftCardListPage
from test_cases.base_test import BaseTest
import time
import re

class TestGiftCardListPage (BaseTest):

    # Testcase for jewelryPage
    def test_giftcard_list_navigation(self, browser):
        giftcard_list_page = GiftCardListPage(browser)       
        page_title=giftcard_list_page.navigate_to_product_page()  
        time.sleep(2)
        print (page_title)
        assert page_title=="Gift Cards"

    def test_giftcard_sort_AtoZ(self, browser):
        giftcard_list_page = GiftCardListPage(browser)       
        giftcard_list_page.navigate_to_product_page()
        sorted_product_names = giftcard_list_page.sort_products_AtoZ()
        print(sorted_product_names)
        assert sorted_product_names == sorted(sorted_product_names)

    def test_giftcard_sort_ZtoA(self, browser):
        giftcard_list_page = GiftCardListPage(browser)
        giftcard_list_page.navigate_to_product_page()
        sorted_product_names = giftcard_list_page.sort_products_ZtoA()
        print(sorted_product_names)
        assert sorted_product_names == sorted(sorted_product_names, reverse=True)

    def test_giftcard_sort_price_lowtohigh(self, browser):
        giftcard_list_page = GiftCardListPage(browser)
        giftcard_list_page.navigate_to_product_page()
        sorted_product_prices = giftcard_list_page.sort_products_price_lowtohigh()
        prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
        print(prices_as_float)
        assert prices_as_float == sorted(prices_as_float)

    def test_giftcard_sort_price_hightolow(self, browser):
        giftcard_list_page = GiftCardListPage(browser)
        giftcard_list_page.navigate_to_product_page()
        sorted_product_prices = giftcard_list_page.sort_products_price_hightolow()
        prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
        print(prices_as_float)
        assert prices_as_float == sorted(prices_as_float, reverse=True)


    # def test_giftcard_add_virtual_item_to_cart(self, browser):
    #     giftcard_list_page = GiftCardListPage(browser)       
    #     giftcard_list_page.navigate_to_product_page()  
    #     cart_page_title = giftcard_list_page.add_product_to_cart()

    #     time.sleep(2)  
    #     print (cart_page_title)
    #     assert cart_page_title == "Shopping cart" 

    def test_giftcard_add_physical_item_to_cart(self, browser):
        giftcard_list_page = GiftCardListPage(browser)       
        giftcard_list_page.navigate_to_product_page()  
        cart_page_title = giftcard_list_page.add_product_to_cart()

        time.sleep(2)  
        print (cart_page_title)
        assert cart_page_title == "Shopping cart" 

    
    
