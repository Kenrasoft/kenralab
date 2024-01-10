
from page_objects.product.jewelrylist_sort_page import JewelryListPages

class TestJewelryListPage:

    def test_jewelry_list_actions(self,browser):
        jewelry_list = JewelryListPages(browser)       
        jewelry_list.navigate_to_jewelry_page()       
        page_title=jewelry_list.jewelry_list_actions()
        assert page_title=="nopCommerce demo store. Jewelry"

    def test_jewelry_sort_ascending_order(self,browser):
        ascending_list= ['40', '41', '42']
        jewelry_list = JewelryListPages(browser)       
        jewelry_list.navigate_to_jewelry_page()       
        product_ids=jewelry_list.jewelry_list_sort_ascending()
        print(product_ids)
        assert product_ids==ascending_list

    def test_jewelry_sort_descending_order(self,browser):
        descending_list= ['42', '41', '40']
        jewelry_list = JewelryListPages(browser)       
        jewelry_list.navigate_to_jewelry_page()       
        product_ids=jewelry_list.jewelry_list_sort_descending()
        print(product_ids)
        assert product_ids==descending_list

    def test_jewelry_prices_lowtohigh(self,browser):
        lowtohigh_list= ['$30.00 per 1 day(s)', '$360.00', '$2,100.00']
        jewelry_list = JewelryListPages(browser)       
        jewelry_list.navigate_to_jewelry_page()       
        product_prices=jewelry_list.jewelry_price_lowtohigh()      
        assert product_prices==lowtohigh_list

    def test_jewelry_prices_hightolow(self,browser):
        hightolow_list= ['$2,100.00', '$360.00', '$30.00 per 1 day(s)']
        jewelry_list = JewelryListPages(browser)       
        jewelry_list.navigate_to_jewelry_page()       
        product_prices=jewelry_list.jewelry_price_hightolow()        
        assert product_prices==hightolow_list
       
       
        
        