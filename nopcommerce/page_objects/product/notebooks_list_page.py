from page_objects.product.product_base_page import ProductBasePage

class NotebooksListPage(ProductBasePage):
    def __init__(self, driver):
        super(NotebooksListPage, self).__init__(driver)          
        self.url="https://demo.nopcommerce.com/notebooks"