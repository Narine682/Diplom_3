from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import EMAIL_INPUT, PASSWORD_INPUT, LOGIN_BUTTON, ACCOUNT_HEADER
from utils.constants import TEST_EMAIL, TEST_PASSWORD

class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    def login(self, email=TEST_EMAIL, password=TEST_PASSWORD):
         WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(EMAIL_INPUT)
         ).send_keys(email)
         self.driver.find_element(*EMAIL_INPUT).send_keys(email)
         self.driver.find_element(*PASSWORD_INPUT).send_keys(password)
         self.driver.find_element(*LOGIN_BUTTON).click()



