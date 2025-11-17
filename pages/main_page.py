import allure
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
    def open_ingredient(self, ingredient_locator):
        element = self.wait_for_visible(ingredient_locator)
        self.scroll_into_view(element)
        self.wait_for_clickable(ingredient_locator).click()
        self.wait_for_visible(MainPageLocators.MODAL_WINDOW)

    def close_ingredient_modal(self):
        try:
            self.wait_for_clickable(MainPageLocators.INGREDIENT_MODAL_CLOSE).click()
        except TimeoutException:
            raise AttributeError("Крестик модального окна не найден")

        self.wait_for_visible(MainPageLocators.MODAL_WINDOW)

    def is_ingredient_modal_opened(self):
         return self.is_visible(MainPageLocators.MODAL_WINDOW)

    def is_ingredient_model_closed(self):
        return self.wait_for_not_visible(MainPageLocators.MODAL_WINDOW, timeout=15)

    def get_ingredient_counter(self, ingredient_element):
        try:
            counter = ingredient_element.find_element(*MainPageLocators.INGREDIENT_COUNTER_RELATIVE)
            return counter.text or "0"
        except :
            return "0"
    def drag_to_constructor(self, ingredient_element):
        target = self.find(MainPageLocators.CONSTRUCTOR_DROP_AREA)
        ActionChains(self.driver).drag_and_drop(ingredient_element, target).perform()

    def click_place_an_order_safe(self):
        self.wait_for_clickable(MainPageLocators.ORDER_BUTTON).click()

    def create_order_and_get_number(self):
        bun = self.find(MainPageLocators.INGREDIENT_BUN)
        self.drag_to_constructor(bun)
        self.click_place_an_order_safe()
        order_number_element = self.wait_for_visible(MainPageLocators.ORDER_NUMBER)
        order_number = order_number_element.text
        self.close_ingredient_modal()
        return order_number


