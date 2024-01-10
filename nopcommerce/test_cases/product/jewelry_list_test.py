from page_objects.product.jewelry_list_page import JewelryListPage
from test_cases.base_test import BaseTest
import time
import re

class TestJewelListPage (BaseTest):

    # Testcase for jewelryPage
    def test_jewelry_list_navigation(self, browser):
        jewelry_list_page = JewelryListPage(browser)       
        page_title=jewelry_list_page.navigate_to_product_page()  
        time.sleep(5)
        print (page_title)
        assert page_title=="Jewelry"

    def test_jewelry_add_item_to_cart(self, browser):
        jewelry_list_page = JewelryListPage(browser)       
        jewelry_list_page.navigate_to_product_page()  
        cart_page_title = jewelry_list_page.add_product_to_cart()  
        print (cart_page_title)
        assert cart_page_title == "Shopping cart" 
    
    def test_jewelry_rent_item(self, browser):
        jewelry_list_page = JewelryListPage(browser)       
        jewelry_list_page.navigate_to_product_page()  
        rent_page_title = jewelry_list_page.rent_product() 
        print (rent_page_title) 
        assert "rental" in rent_page_title
    
    def test_jewelry_sort_AtoZ(self, browser):
        jewelry_list_page = JewelryListPage(browser)       
        jewelry_list_page.navigate_to_product_page()
        sorted_product_names = jewelry_list_page.sort_products_AtoZ()
        assert sorted_product_names == sorted(sorted_product_names)

    def test_jewelry_sort_ZtoA(self, browser):
        jewelry_list_page = JewelryListPage(browser)
        jewelry_list_page.navigate_to_product_page()
        sorted_product_names = jewelry_list_page.sort_products_ZtoA()
        assert sorted_product_names == sorted(sorted_product_names, reverse=True)

    def test_products_sort_price_lowtohigh(self, browser):
        jewelry_list_page = JewelryListPage(browser)
        jewelry_list_page.navigate_to_product_page()
        sorted_product_prices = jewelry_list_page.sort_products_price_lowtohigh()
        prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
        assert prices_as_float == sorted(prices_as_float)

    def test_products_sort_price_hightolow(self, browser):
        jewelry_list_page = JewelryListPage(browser)
        jewelry_list_page.navigate_to_product_page()
        sorted_product_prices = jewelry_list_page.sort_products_price_hightolow()
        prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
        assert prices_as_float == sorted(prices_as_float, reverse=True)


