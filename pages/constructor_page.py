from selenium.webdriver.common.by import By
from pages.modal import Modal
from locators.locators import INGREDIENT, INGREDIENT_COUNTER

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.modal = Modal(driver)

    def open_ingredient(self):
        self.driver.find_element(*INGREDIENT).click()

    def get_ingredient_counter(self):
        return int(self.driver.find_element(*INGREDIENT_COUNTER).text)
