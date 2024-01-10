from page_objects.product.product_base_page import ProductBasePage

class CellphonesListPage(ProductBasePage):
    def __init__(self, driver):
        super(CellphonesListPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/cell-phones"
        

