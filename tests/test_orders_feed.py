import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.constants import TEST_EMAIL, TEST_PASSWORD
from locators.locators import TODAY_COUNTER, TOTAL_COUNTER
def test_order_feed_counters(driver):
    login = LoginPage(driver)
    login.login(TEST_EMAIL, TEST_PASSWORD)

    main = MainPage(driver)
    main.go_to_orders_feed()

    total_before = int(driver.find_element(*TOTAL_COUNTER).text)
    today_before = int(driver.find_element(*TODAY_COUNTER).text)


    total_after = int(driver.find_element(*TODAY_COUNTER).text)
    today_after = int(driver.find_element(*TODAY_COUNTER).text)
    assert total_after >= total_before
    assert today_after >= today_before