from selenium.webdriver.common.by import By
from locators.locators import CONSTRUCTOR_TAB, ORDERS_FEED_TAB

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_constructor(self):
        self.driver.find_element(*CONSTRUCTOR_TAB).click()

    def go_to_orders_feed(self):
        self.driver.find_element(*ORDERS_FEED_TAB).click()




