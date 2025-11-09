from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import INGREDIENT_MODAL, MODAL_CLOSE_BUTTON

class Modal:
    def __init__(self, driver):
        self.driver = driver

    def is_open(self):
        return self.driver.find_element(*INGREDIENT_MODAL).is_displayed*()
    def close(self):
        self.driver.find_element(*MODAL_CLOSE_BUTTON).click()


        