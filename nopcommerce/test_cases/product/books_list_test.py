from page_objects.product.books_list_page import BooksListPage
from test_cases.base_test import BaseTest
import time


class TestBooksListPage (BaseTest):

    # Testcase for jewelryPage
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
    


