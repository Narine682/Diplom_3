from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators.locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def open(self, url):
        self.driver.get(url)

    def click(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def js_click(self, element):
         self.driver.execute_script("arguments[0].click();", element)

    def find(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_all(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))


    def wait_for_visible(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_not_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))

    def wait_for_text_greater_then(self, locator, value, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: int(self.find(locator).text.strip()) > value
        )

    def wait_for_order_in_list(self, locator, order_number, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: order_number in [e.text.strip() for e in self.find_all(locator, timeout=20)]
        )

    def is_visible(self, locator, timeout=20):
        try:
            self.wait_for_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)



    def wait_for_visible_and_scroll(self, locator, timeout= 30):
        element = self.wait_for_visible(locator, timeout)
        self.scroll_into_view(element)
        return element

    def close_overlay_if_present(self):
        overlay_locator = MainPageLocators.ORDER_LOADING_MODAL
        try:
            WebDriverWait(self.driver, 30).until(
                EC.invisibility_of_element_located(overlay_locator))
        except TimeoutException:
            try:
                overlay = self.driver.find_element(*overlay_locator)
                self.driver.execute_script("arguments[0].click();", overlay)
                WebDriverWait(self.driver, 30).until(
                    EC.invisibility_of_element_located(overlay_locator)
                )
            except Exception as e:
                print("Не удалось закрыть overlay:", e)

















