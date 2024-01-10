from page_objects.product.product_base_page import ProductBasePage

class CameraListPage(ProductBasePage):
    def __init__(self, driver):
        super(CameraListPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/camera-photo"
        

