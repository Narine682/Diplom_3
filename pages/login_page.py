from locators.locators import AuthLocators, MainPageLocators
from pages.base_page import BasePage
class LoginPage(BasePage):

    def open_login_form(self):
         self.click(MainPageLocators.LOGIN_BUTTON)
    def login(self, email, password):
         self.open_login_form()

         email_field = self.find(AuthLocators.EMAIL_INPUT)
         email_field.send_keys(email)

         password_field = self.find(AuthLocators.PASSWORD_INPUT)
         password_field.send_keys(password)

         self.click(AuthLocators.LOGIN_BUTTON_AUTH)



