import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

class TestAmazonFlow(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.amazon.com.tr/")

    def test_amazon_flow(self):
        home_page = HomePage(self.driver)
        search_results_page = SearchResultsPage(self.driver)
        product_page = ProductPage(self.driver)
        cart_page = CartPage(self.driver)

        self.assertTrue(home_page.is_home_page())

        home_page.search_product("samsung")

        self.assertTrue(search_results_page.has_search_results())

        search_results_page.go_to_page(2)
        self.assertEqual(search_results_page.get_current_page(), 2)

        search_results_page.click_product(3)

        self.assertTrue(product_page.is_product_page())
        product_title = product_page.get_product_title()

        product_page.add_to_cart()
        self.assertTrue(product_page.is_added_to_cart())

        product_page.go_to_cart()
        self.assertTrue(cart_page.is_cart_page())
        self.assertEqual(len(cart_page.get_cart_items()), 1)

        cart_page.delete_product()
        self.assertTrue(cart_page.is_cart_empty())

        cart_page.go_to_home()
        self.assertTrue(home_page.is_home_page())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()