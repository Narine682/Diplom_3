from locators.locators import AuthLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, email, password):
         email_field = self.find(AuthLocators.EMAIL_INPUT)
         email_field.click()
         email_field.send_keys(email)

         password_field = self.find(AuthLocators.PASSWORD_INPUT)
         password_field.click()
         password_field.send_keys(password)

         self.click(AuthLocators.LOGIN_BUTTON_AUTH)



