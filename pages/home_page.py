from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")
    AMAZON_LOGO = (By.ID, "nav-logo-sprites")

    def is_home_page(self):
        return self.is_element_visible(self.AMAZON_LOGO)

    def search_product(self, product_name):
        self.send_keys(self.SEARCH_BOX, product_name)
        self.click_element(self.SEARCH_BUTTON)