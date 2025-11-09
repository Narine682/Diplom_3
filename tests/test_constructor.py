import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import TEST_EMAIL, TEST_PASSWORD


def test_constructor_tab(driver):
    login = LoginPage(driver)
    login.login()

    main = MainPage(driver)
    main.go_to_constructor()

    constructor = ConstructorPage(driver)
    constructor.open_ingredient()

    assert constructor.modal.is_open()
    constructor.modal.close()



