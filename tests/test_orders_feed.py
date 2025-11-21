import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from utils.constants import TEST_EMAIL, TEST_PASSWORD, BASE_URL



@allure.feature("Лента заказов")
class TestOrdersFeed:
    @allure.title("Общий счётчик увеличивается после создания заказа")
    def test_total_counter_updates(self, driver):
        main = MainPage(driver)
        main.open(BASE_URL)

        LoginPage(driver).login(TEST_EMAIL, TEST_PASSWORD)
        main.go_to_orders_feed()
        feed = FeedPage(driver)

        total_before = feed.get_total_count()
        main.go_to_constructor()
        main.create_order_and_get_number()

        main.go_to_orders_feed()
        total_after = feed.get_total_count()

        assert total_after >= total_before + 1

    @allure.title("Счетчик 'за сегодня' увеличивается после заказа")
    def test_today_counter_updates(self, driver):
        main = MainPage(driver)
        main.open(BASE_URL)

        LoginPage(driver).login(TEST_EMAIL, TEST_PASSWORD)
        main.go_to_orders_feed()
        feed = FeedPage(driver)

        today_before = feed.get_today_count()

        main.go_to_constructor()
        main.create_order_and_get_number()

        main.go_to_orders_feed()
        today_after = feed.get_today_count()

        assert today_after >= today_before + 1


    @allure.title("Новый заказ отображается в блоке 'В работе'")
    def test_order_appears_in_progress(self, driver):
        main = MainPage(driver)
        main.open(BASE_URL)

        LoginPage(driver).login(TEST_EMAIL, TEST_PASSWORD)

        main.go_to_constructor()
        order_number = main.create_order_and_get_number()

        main.go_to_orders_feed()
        feed = FeedPage(driver)

        in_progress = feed.get_orders_in_progress_numbers()
        assert order_number in in_progress