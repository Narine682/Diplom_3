import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from utils.constants import TEST_EMAIL, TEST_PASSWORD, BASE_URL
from locators.locators import MainPageLocators
import time

class TestOrdersFeed:
    def test_new_order_updates_counters_and_in_progress(self, driver):
        driver.get(BASE_URL)
        login = LoginPage(driver)
        login.login(TEST_EMAIL, TEST_PASSWORD)

        main = MainPage(driver)
        main.go_to_orders_feed()
        feed = FeedPage(driver)
        total_before = feed.get_total_count()
        today_before = feed.get_today_count()
        in_progress_before = feed.get_orders_in_progress_numbers()

        main.go_to_constructor()
        bun = main.find(MainPageLocators.INGREDIENT_BUN)
        main.drag_to_constructor(bun)
        main.click(MainPageLocators.ORDER_BUTTON)

        order_number = main.wait_for_order_modal()
        assert order_number != "", "Номер заказа не появился"
        main.close_order_modal()


        main.go_to_orders_feed()
        total_after = feed.get_total_count()
        today_after = feed.get_today_count()
        in_progress_after = feed.get_orders_in_progress_numbers()

        assert total_after >= total_before + 1
        assert today_after >= today_before + 1
        assert order_number in in_progress_after