from locators.locators import FeedPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class FeedPage(BasePage):
    def get_total_count(self):
        el = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(FeedPageLocators.TOTAL_COUNTER)
        )
        return int(el.text)

    def wait_for_total_count_increase(self, previous_count):
        WebDriverWait(self.driver, 60).until(
            lambda d: int(self.driver.find_element(*FeedPageLocators.TOTAL_COUNTER).text) > previous_count
        )


    def get_today_count(self):
        el = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(FeedPageLocators.TODAY_COUNTER)
        )
        return int(el.text)

    def wait_for_today_count_increase(self, previous_count):
        WebDriverWait(self.driver, 60).until(
            lambda d: int(self.driver.find_element(*FeedPageLocators.TODAY_COUNTER).text) > previous_count
        )


    def get_orders_in_progress_numbers(self):
        numbers = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDERS_IN_PROGRESS)
        )
        return [n.text.strip() for n in numbers if n.text.strip()]

    def wait_for_order_in_progress(self, order_number):
        WebDriverWait(self.driver, 60).until(
            lambda d: order_number in self.get_orders_in_progress_numbers()
        )


        