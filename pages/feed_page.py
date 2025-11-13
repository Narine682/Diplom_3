from locators.locators import FeedPageLocators
from pages.base_page import BasePage

class FeedPage(BasePage):
    def get_total_count(self):
        return int(self.find(FeedPageLocators.TOTAL_COUNTER).text)
    def get_today_count(self):
        return int(self.find(FeedPageLocators.TODAY_COUNTER).text)

    def get_orders_in_progress_numbers(self):
        orders = self.find_all(FeedPageLocators.ORDERS_IN_PROGRESS)
        numbers = [o.text for o in orders]
        return numbers



        