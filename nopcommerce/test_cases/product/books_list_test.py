from page_objects.product.books_list_page import BooksListPage
from test_cases.base_test import BaseTest
import time
import re

class TestBooksListPage (BaseTest):

    # Testcase for booksPage
    def test_books_list_navigation(self, browser):
        list_page = BooksListPage(browser)       
        page_title= list_page.navigate_to_product_page()  
        time.sleep(5)
        print (page_title)
        assert page_title=="Books"

    def test_books_add_item_to_cart(self, browser):
        list_page = BooksListPage(browser)       
        list_page.navigate_to_product_page()  
        cart_page_title = list_page.add_product_to_cart()  
        print (cart_page_title)
        assert cart_page_title == "Shopping cart"
    
    def test_books_sort_AtoZ(self, browser):
        books_list_page = BooksListPage(browser)       
        books_list_page.navigate_to_product_page()
        sorted_product_names = books_list_page.sort_products_AtoZ()
        assert sorted_product_names == sorted(sorted_product_names)

    def test_books_sort_ZtoA(self, browser):
        books_list_page = BooksListPage(browser)
        books_list_page.navigate_to_product_page()
        sorted_product_names = books_list_page.sort_products_ZtoA()
        assert sorted_product_names == sorted(sorted_product_names, reverse=True)

    def test_products_sort_price_lowtohigh(self, browser):
        books_list_page = BooksListPage(browser)
        books_list_page.navigate_to_product_page()
        sorted_product_prices = books_list_page.sort_products_price_lowtohigh()
        prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
        assert prices_as_float == sorted(prices_as_float)

    def test_products_sort_price_hightolow(self, browser):
        books_list_page = BooksListPage(browser)
        books_list_page.navigate_to_product_page()
        sorted_product_prices = books_list_page.sort_products_price_hightolow()
        prices_as_float = [float(re.sub(r'[^\d.]', '', price)) for price in sorted_product_prices]
        assert prices_as_float == sorted(prices_as_float, reverse=True)
    


