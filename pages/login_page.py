from locators.locators import AuthLocators, MainPageLocators
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Открыть форму входа")
    def open_login_form(self):
        try:
            self.click(MainPageLocators.LOGIN_BUTTON)
        except Exception as e:
            element = self.find(MainPageLocators.LOGIN_BUTTON)
            self.driver.execute_script("arguments[0].click();",element)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
         self.open_login_form()

         email_field = self.find(AuthLocators.EMAIL_INPUT)
         email_field.send_keys(email)

         password_field = self.find(AuthLocators.PASSWORD_INPUT)
         password_field.send_keys(password)

         self.click(AuthLocators.LOGIN_BUTTON_AUTH)



