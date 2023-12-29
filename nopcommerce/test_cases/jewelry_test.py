from page_objects.jewelry_page import JewelryPage
import pytest
import time


class TestJewelPage:

    def test_jewelry_e2e_checkout(self,browser):
        jewelry_page = JewelryPage(browser)       
        jewelry_page.navigate_to_jewelry_page()         
        jewelry_page.jewelry_e2e_flow()


       
