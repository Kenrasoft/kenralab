from page_objects.jewelry_page import JewelryPage

class TestJewelPage:

    # Testcase for jewelryPage
    def test_jewelry_page(self,browser):
        jewelry_page = JewelryPage(browser)       
        page_title=jewelry_page.navigate_to_jewelry_page()  
        print (page_title)
        assert page_title=="Jewelry"

        page_title=jewelry_page.add_item_to_cart()  
        print (page_title)
        assert page_title=="Shopping cart" 

    

       
