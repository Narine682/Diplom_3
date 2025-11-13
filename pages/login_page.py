from locators.locators import AuthLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, email, password):
         self.find(AuthLocators.EMAIL_INPUT).send_keys(email)
         self.find(AuthLocators.PASSWORD_INPUT).send_keys(password)
         self.click(AuthLocators.LOGIN_BUTTON_AUTH)



