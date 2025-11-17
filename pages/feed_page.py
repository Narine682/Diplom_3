from locators.locators import FeedPageLocators
from pages.base_page import BasePage

class FeedPage(BasePage):
    def get_total_count(self):
        total = self.wait_for_visible_and_scroll(FeedPageLocators.TOTAL_COUNTER)
        return int(total.text)
    def get_today_count(self):
        today = self.wait_for_visible_and_scroll(FeedPageLocators.TODAY_COUNTER)
        return int(today.text)

    def get_orders_in_progress_numbers(self):
        numbers = self.find_all(FeedPageLocators.ORDERS_IN_PROGRESS)
        return [num.text for num in numbers if num.text.strip()]



        