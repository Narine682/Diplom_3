import allure
from locators.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    def go_to_constructor(self):
        tab = self.wait_for_clickable(MainPageLocators.CONSTRUCTOR_TAB, timeout=30)
        self.js_click(tab)

    def go_to_orders_feed(self):
        tab = self.wait_for_clickable(MainPageLocators.ORDERS_FEED_TAB, timeout=30)
        self.js_click(tab)

    def open_ingredient(self, locator):
        element = self.wait_for_visible_and_scroll(locator, timeout=30)
        self.wait_for_clickable(locator, timeout=30).click()
        self.wait_for_visible(MainPageLocators.MODAL_WINDOW, timeout=20)

    def close_ingredient_modal(self):
        try:
            self.wait_for_visible(MainPageLocators.MODAL_WINDOW, timeout=15)
            close_btn = self.wait_for_clickable(MainPageLocators.INGREDIENT_MODAL_CLOSE, timeout=15)
            self.js_click(close_btn)
            self.wait_for_not_visible(MainPageLocators.MODAL_WINDOW, timeout=15)

        except TimeoutException:
            try:
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                self.wait_for_visible(MainPageLocators.MODAL_WINDOW, timeout=30)
            except:
                raise AttributeError("Не удалось закрыть модальное окно ингредиента")



    def is_ingredient_modal_opened(self):
         return self.is_visible(MainPageLocators.MODAL_WINDOW)

    def is_ingredient_modal_closed(self):
        return not self.is_visible(MainPageLocators.MODAL_WINDOW )

    def get_ingredient_counter(self, ingredient):
        try:
            counter = ingredient.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
        except :
            return 0

    def drag_bun(self):
        bun_text = self.find(MainPageLocators.INGREDIENT_BUN)
        bun_parent = bun_text.find_element(*MainPageLocators.INGREDIENT_PARENT)
        self.drag_to_constructor(bun_parent)

    def drag_and_drop(self, source_locator, target_locator):

        source = self.wait_for_visible(source_locator)
        target = self.wait_for_visible(target_locator)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
        
            source.dispatchEvent(new DragEvent('dragstart', { dataTransfer }));
            target.dispatchEvent(new DragEvent('dragenter', { dataTransfer }));
            target.dispatchEvent(new DragEvent('dragover', { dataTransfer }));
            target.dispatchEvent(new DragEvent('drop', { dataTransfer }));
            source.dispatchEvent(new DragEvent('dragend', { dataTransfer }));
        """, source, target)

    def add_bun_to_constructor(self):
        try:
            self.close_overlay_if_present()
            bun = self.wait_for_visible_and_scroll(MainPageLocators.INGREDIENT_BUN, timeout=30)
            drop_area = self.wait_for_visible(MainPageLocators.CONSTRUCTOR_DROP_AREA, timeout=30)
            self.drag_and_drop(MainPageLocators.INGREDIENT_BUN, MainPageLocators.CONSTRUCTOR_DROP_AREA)
            WebDriverWait(self.driver, 15).until(
            lambda d: self.get_bun_counter() >= 1)
        except Exception as e:
            print(f"Ошибка при добавлении булки: {e}")
            raise


    def get_bun_counter(self):
         try:
            bun = self.find(MainPageLocators.INGREDIENT_BUN)
            counter = bun.find_element(*MainPageLocators.INGREDIENT_COUNTER)
            return int(counter.text) if counter.text else 0
         except Exception:
            return 0

    def click_place_an_order_safe(self):
        overlay_locator = MainPageLocators.ORDER_LOADING_MODAL
        try:
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(overlay_locator))
        except TimeoutException:
            pass
        self.wait_for_clickable(MainPageLocators.PLACE_ORDER_BUTTON, timeout=30).click()

    def create_order_and_get_number(self):
        self.add_bun_to_constructor()
        self.click_place_an_order_safe()
        order_number_element = self.wait_for_visible(MainPageLocators.ORDER_NUMBER, timeout=30)
        order_number = order_number_element.text.strip()
        self.close_order_modal()
        return order_number

    def is_constructor_tab_displayed(self):
        return self.is_visible(MainPageLocators.CONSTRUCTOR_TAB)


    def is_orders_feed_tab_displayed(self):
        return self.is_visible(MainPageLocators.ORDERS_FEED_TAB)


    def close_order_modal(self):
        self.wait_for_visible(MainPageLocators.ORDER_MODAL, timeout=30)
        close_btn = self.wait_for_clickable(MainPageLocators.ORDER_MODAL_CLOSE, timeout=30)
        close_btn.click()
        self.wait_for_not_visible(MainPageLocators.ORDER_MODAL, timeout=30)
        overlay_locator = MainPageLocators.ORDER_LOADING_MODAL
        try:
           WebDriverWait(self.driver,30).until(EC.invisibility_of_element_located(overlay_locator))
        except TimeoutException:
            pass