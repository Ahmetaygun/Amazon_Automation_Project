from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
import time

class CartPage(BasePage):
    CART_TITLE = (By.CSS_SELECTOR, ".sc-cart-header")
    DELETE_BUTTON = (By.CSS_SELECTOR, "input[data-action='delete'], .sc-action-delete")
    EMPTY_CART_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Sepetiniz boş')]")
    CART_ITEMS = (By.CSS_SELECTOR, ".sc-list-item-content")
    HOME_LINK = (By.ID, "nav-logo-sprites")

    def is_cart_page(self):
        return self.is_element_visible(self.CART_TITLE)

    def delete_product(self):
        try:
            time.sleep(2)
            delete_buttons = self.driver.find_elements(By.CSS_SELECTOR,
                "input[data-action='delete'], .sc-action-delete, input[value='Sil']")
            
            for button in delete_buttons:
                if button.is_displayed():
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
                    time.sleep(1)
                    self.driver.execute_script("arguments[0].click();", button)
                    time.sleep(2)
            
            time.sleep(3)
        except Exception:
            self.driver.execute_script("""
                const deleteButtons = document.querySelectorAll('input[data-action="delete"], .sc-action-delete, input[value="Sil"]');
                deleteButtons.forEach(button => button.click());
            """)
            time.sleep(3)

    def is_cart_empty(self):
        time.sleep(3)
        try:
            empty_messages = self.driver.find_elements(By.XPATH,
                "//*[contains(text(), 'Sepetiniz boş') or contains(text(), 'Amazon sepetiniz boş')]")
            
            if any(msg.is_displayed() for msg in empty_messages):
                return True
            
            return len(self.driver.find_elements(*self.CART_ITEMS)) == 0
            
        except Exception:
            return self.driver.execute_script("""
                return !document.querySelector('.sc-list-item-content') || 
                       document.documentElement.textContent.includes('Sepetiniz boş');
            """)

    def get_cart_items(self):
        return self.find_elements(self.CART_ITEMS)

    def go_to_home(self):
        self.click_element(self.HOME_LINK)