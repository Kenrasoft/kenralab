from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class OrderDetailsPage(BasePage):

    def __init__(self, driver):
        super(OrderDetailsPage, self).__init__(driver)       
                     
        # order confirmation page
        self.click_order_detailslink=(By.XPATH, "//a[normalize-space()='Click here for order details.']")
        # order information page
        self.order_status=(By.XPATH, "//li[@class='order-status']")       
        self.order_amount=(By.XPATH, "//li[@class='order-total']")   

    def update_order_details(self):
        # order status page and this is the final page
        self.driver.find_element(*self.click_order_detailslink).click()
        self.driver.implicitly_wait(5)
        order_status=self.driver.find_element(*self.order_status).text   
        order_amount=self.driver.find_element(*self.order_amount).text      
        return order_status+ " " +order_amount
