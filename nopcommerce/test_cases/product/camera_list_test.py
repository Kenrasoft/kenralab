from page_objects.product.camera_list_page import CameraListPage
from test_cases.base_test import BaseTest
import time
import re

class TestCameraListPage (BaseTest):
    # def test_camera_list_navigation(self, browser):
    #     camera_list_page = CameraListPage(browser)       
    #     page_title=camera_list_page.navigate_to_product_page()  
    #     time.sleep(5)
    #     print (page_title)
    #     assert page_title=="Camera & photo"

    # def test_camera_sort_AtoZ(self, browser):
    #     camera_list_page = CameraListPage(browser)       
    #     camera_list_page.navigate_to_product_page()
    #     sorted_product_names = camera_list_page.sort_products_AtoZ()
    #     assert sorted_product_names == sorted(sorted_product_names)

    # def test_camera_sort_ZtoA(self, browser):
    #     camera_list_page = CameraListPage(browser)
    #     camera_list_page.navigate_to_product_page()
    #     sorted_product_names = camera_list_page.sort_products_ZtoA()
    #     assert sorted_product_names == sorted(sorted_product_names, reverse=True)

    # def test_products_sort_price_lowtohigh(self, browser):
    #     camera_list_page = CameraListPage(browser)
    #     camera_list_page.navigate_to_product_page()
    #     sorted_product_prices = camera_list_page.sort_products_price_lowtohigh()
    #     prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
    #     assert prices_as_float == sorted(prices_as_float)

    # def test_products_sort_price_hightolow(self, browser):
    #     camera_list_page = CameraListPage(browser)
    #     camera_list_page.navigate_to_product_page()
    #     sorted_product_prices = camera_list_page.sort_products_price_hightolow()
    #     prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
    #     assert prices_as_float == sorted(prices_as_float, reverse=True)

    # def test_camera_add_item_to_cart(self, browser):
    #     camera_list_page = CameraListPage(browser)       
    #     camera_list_page.navigate_to_product_page()  
    #     cart_page_title = camera_list_page.add_product_to_cart()  
    #     print (cart_page_title)
    #     assert cart_page_title == "Shopping cart" 

    def test_camera_display_per_page_three(self, browser):
        camera_list_page = CameraListPage(browser)       
        camera_list_page.navigate_to_product_page()  
        count_display_per_page = camera_list_page.display_per_page_three()  
        print (count_display_per_page)
        assert count_display_per_page <= 3

    def test_camera_display_per_page_six(self, browser):
        camera_list_page = CameraListPage(browser)       
        camera_list_page.navigate_to_product_page()  
        count_display_per_page = camera_list_page.display_per_page_six()  
        print (count_display_per_page)
        assert count_display_per_page <= 6
    
    def test_camera_display_per_page_nine(self, browser):
        camera_list_page = CameraListPage(browser)       
        camera_list_page.navigate_to_product_page()  
        count_display_per_page = camera_list_page.display_per_page_nine()  
        print (count_display_per_page)
        assert count_display_per_page <= 9
