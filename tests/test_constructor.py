import allure
from pages.main_page import MainPage
from utils.constants import BASE_URL
from locators.locators import MainPageLocators

@allure.feature("Конструктор")
class TestConstructor:
    @allure.story("Переход на Конструктор")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        driver.get(BASE_URL)
        page.go_to_constructor()
    @allure.story("Переход в Ленту заказов")
    def test_go_to_feed(self, driver):
        page = MainPage(driver)
        driver.get(BASE_URL)
        page.go_to_orders_feed()
    @allure.story("Клик по ингредиенту открывает модалку")
    def test_ingredient_modal_open(self, driver):
        page = MainPage(driver)
        driver.get(BASE_URL)
        page.open_ingredient(MainPageLocators.INGREDIENT_BUN)
        page.find(MainPageLocators.MODAL_WINDOW)
    @allure.story("Модалка закрывается по крестику")
    def test_ingredient_modal_close(self, driver):
        page = MainPage(driver)
        driver.get(BASE_URL)
        page.open_ingredient(MainPageLocators.INGREDIENT_BUN)
        page.close_modal()
    @allure.story("Счетчик ингредиента увеличивается после добавления")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        driver.get(BASE_URL)
        bun = page.find(MainPageLocators.INGREDIENT_BUN)
        before = page.get_ingredient_counter(bun)
        page.drag_to_constructor(bun)
        after = page.get_ingredient_counter(bun)
        assert int(after) == int(before) + 1, f"Счетчик не увеличится: было {before}, стало {after}"



