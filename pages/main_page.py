from locators.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):
    def go_to_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_TAB)
    def go_to_orders_feed(self):
        self.click(MainPageLocators.ORDERS_FEED_TAB)
    def open_ingredient(self, ingredient_locator, timeout=20):
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(ingredient_locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(ingredient_locator)).click()
    def close_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.INGREDIENT_MODAL_CLOSE)).click()
        self.click(MainPageLocators.INGREDIENT_MODAL_CLOSE)
    def get_ingredient_counter(self, ingredient_element):
        try:
            counter = ingredient_element.find_element(*MainPageLocators.INGREDIENT_COUNTER_RELATIVE)
            return counter.text or "0"
        except:
            return "0"
    def drag_to_constructor(self, ingredient_element):
        target = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_DROP_AREA))
        ActionChains(self.driver).drag_and_drop(ingredient_element, target).perform()





