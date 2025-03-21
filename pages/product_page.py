from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
import time

class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_CONFIRMATION = (By.CSS_SELECTOR, "#NATC_SMART_WAGON_CONF_MSG_SUCCESS, .a-size-medium-plus.a-color-base.sw-atc-text")
    PRODUCT_TITLE = (By.ID, "productTitle")
    GO_TO_CART = (By.CSS_SELECTOR, "#nav-cart, #sw-gtc")

    def is_product_page(self):
        return self.is_element_visible(self.PRODUCT_TITLE)

    def get_product_title(self):
        return self.find_element(self.PRODUCT_TITLE).text

    def add_to_cart(self):
        try:
            time.sleep(2)
            self.click_element(self.ADD_TO_CART_BUTTON)
        except TimeoutException:
            try:
                alt_add_button = (By.NAME, "submit.add-to-cart")
                self.click_element(alt_add_button)
            except TimeoutException:
                self.driver.execute_script(
                    "document.querySelector('#add-to-cart-button, input[name=\"submit.add-to-cart\"]').click()"
                )
        time.sleep(2)

    def is_added_to_cart(self):
        return self.is_element_visible(self.CART_CONFIRMATION)

    def go_to_cart(self):
        try:
            self.click_element(self.GO_TO_CART)
        except TimeoutException:
            self.driver.get("https://www.amazon.com.tr/gp/cart/view.html")