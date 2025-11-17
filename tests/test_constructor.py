import allure
from pages.main_page import MainPage
from utils.constants import BASE_URL
from locators.locators import MainPageLocators

@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("Переход на Конструктор")
    def test_go_to_constructor(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.go_to_constructor()

        assert page.is_constructor_tab_displayed()

    @allure.title("Переход в Ленту заказов")
    def test_go_to_feed(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.go_to_orders_feed()
        assert page.is_orders_feed_tab_displayed()

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal_open(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.open_ingredient(MainPageLocators.INGREDIENT_BUN)
        assert page.is_ingredient_modal_opened()
    @allure.title("Модалка закрывается по крестику")
    def test_ingredient_modal_close(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)
        page.open_ingredient(MainPageLocators.INGREDIENT_BUN)
        page.close_ingredient_modal()

        assert page.is_ingredient_modal_closed()

    @allure.title("Счетчик ингредиента увеличивается после добавления")
    def test_ingredient_counter_increases(self, driver):
        page = MainPage(driver)
        page.open(BASE_URL)

        before = page.get_bun_counter()
        page.add_bun_to_constructor()
        after = page.get_bun_counter()

        assert after == before + 1



