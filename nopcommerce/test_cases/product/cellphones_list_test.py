from page_objects.product.cellphones_list_page import CellphonesListPage
from test_cases.base_test import BaseTest
import time
import re

class TestCellphonesListPage (BaseTest):
    def test_cellphones_list_navigation(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        page_title=cellphones_list_page.navigate_to_product_page()  
        time.sleep(5)
        print (page_title)
        assert page_title=="Cell phones"

    def test_cellphones_sort_AtoZ(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()
        sorted_product_names = cellphones_list_page.sort_products_AtoZ()
        assert sorted_product_names == sorted(sorted_product_names)

    def test_cellphones_sort_ZtoA(self, browser):
        cellphones_list_page = CellphonesListPage(browser)
        cellphones_list_page.navigate_to_product_page()
        sorted_product_names = cellphones_list_page.sort_products_ZtoA()
        assert sorted_product_names == sorted(sorted_product_names, reverse=True)

    def test_products_sort_price_lowtohigh(self, browser):
        cellphones_list_page = CellphonesListPage(browser)
        cellphones_list_page.navigate_to_product_page()
        sorted_product_prices = cellphones_list_page.sort_products_price_lowtohigh()
        prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
        assert prices_as_float == sorted(prices_as_float)

    def test_products_sort_price_hightolow(self, browser):
        cellphones_list_page = CellphonesListPage(browser)
        cellphones_list_page.navigate_to_product_page()
        sorted_product_prices = cellphones_list_page.sort_products_price_hightolow()
        prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
        assert prices_as_float == sorted(prices_as_float, reverse=True)

    def test_cellphones_add_item_to_cart(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()  
        cart_page_title = cellphones_list_page.add_product_to_cart()  
        print (cart_page_title)
        assert cart_page_title == "Shopping cart" 

    def test_cellphones_display_per_page_three(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()  
        count_display_per_page = cellphones_list_page.display_per_page_three()  
        print (count_display_per_page)
        assert count_display_per_page <= 3

    def test_cellphones_display_per_page_six(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()  
        count_display_per_page = cellphones_list_page.display_per_page_six()  
        print (count_display_per_page)
        assert count_display_per_page <= 6
    
    def test_cellphones_display_per_page_nine(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()  
        count_display_per_page = cellphones_list_page.display_per_page_nine()  
        print (count_display_per_page)
        assert count_display_per_page <= 9

    def test_cellphones_grid_view(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()  
        grid_view = cellphones_list_page.grid_view()
        assert "selected" in grid_view.get_attribute("class")

    def test_cellphones_list_view(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()  
        list_view = cellphones_list_page.list_view()
        assert "selected" in list_view.get_attribute("class")

    def test_cellphones_compare(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()
        compare_page_title = cellphones_list_page.compare()
        assert compare_page_title == "Compare products"

    def test_cellphones_wishlist(self, browser):
        cellphones_list_page = CellphonesListPage(browser)       
        cellphones_list_page.navigate_to_product_page()
        wishlist_page_title = cellphones_list_page.wishlist()
        assert wishlist_page_title == "Wishlist"

    