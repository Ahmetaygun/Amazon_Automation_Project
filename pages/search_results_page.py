from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage
import time

class SearchResultsPage(BasePage):
    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    PAGINATION_BUTTONS = (By.CSS_SELECTOR, ".s-pagination-item")
    PAGE_NUMBER = (By.CSS_SELECTOR, ".s-pagination-selected")
    COOKIE_ACCEPT_BUTTON = (By.CSS_SELECTOR, "#sp-cc-accept")
    
    def handle_cookie_consent(self):
        try:
            cookie_button = self.driver.find_element(*self.COOKIE_ACCEPT_BUTTON)
            if cookie_button.is_displayed():
                cookie_button.click()
                time.sleep(1)
        except:
            pass

    def click_product(self, index):
        self.handle_cookie_consent()
        time.sleep(1)
        
        products = self.find_elements(self.SEARCH_RESULTS)
        product = products[index - 1]
        
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", product)
        time.sleep(1)
        
        try:
            product.click()
        except ElementClickInterceptedException:
            try:
                product_link = product.find_element(By.CSS_SELECTOR, "h2 a, .a-link-normal")
                self.driver.execute_script("arguments[0].click();", product_link)
            except:
                self.driver.execute_script("arguments[0].click();", product)
        
        time.sleep(2)

    def go_to_page(self, page_number):
        time.sleep(2)
        try:
            self.driver.execute_script("window.scrollTo({top: document.body.scrollHeight, behavior: 'smooth'});")
            time.sleep(1)
            
            page_button = self.driver.find_element(By.CSS_SELECTOR, f".s-pagination-button[aria-label='{page_number} sayfasına git']")
            
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", page_button)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", page_button)
            time.sleep(2)
            
        except Exception as e:
            try:
                pagination_buttons = self.find_elements(self.PAGINATION_BUTTONS)
                for button in pagination_buttons:
                    if button.text.strip() == str(page_number):
                        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
                        time.sleep(1)
                        self.driver.execute_script("arguments[0].click();", button)
                        time.sleep(2)
                        break
            except Exception:
                current_url = self.driver.current_url
                if "page=" in current_url:
                    new_url = current_url.replace(f"page={page_number-1}", f"page={page_number}")
                else:
                    new_url = current_url + f"&page={page_number}"
                self.driver.get(new_url)
                time.sleep(2)

    def has_search_results(self):
        results = self.find_elements(self.SEARCH_RESULTS)
        return len(results) > 0

    def get_current_page(self):
        try:
            return int(self.find_element(self.PAGE_NUMBER).text)
        except TimeoutException:
            current_page = self.driver.execute_script(
                "return document.querySelector('.s-pagination-selected').textContent.trim()"
            )
            return int(current_page)