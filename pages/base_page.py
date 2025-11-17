from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import IMPLICIT_WAIT
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, IMPLICIT_WAIT)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.wait_for_clickable(locator)
        element.click()

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_visible(self, locator, timeout=IMPLICIT_WAIT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_not_visible(self, locator, timeout=IMPLICIT_WAIT):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=IMPLICIT_WAIT):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    def is_visible(self, locator, timeout=IMPLICIT_WAIT):
        try:
            self.wait_for_visible(locator, timeout)
            return True
        except TimeoutException:
            return False
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)


    def wait_for_visible_and_scroll(self, locator, timeout= IMPLICIT_WAIT):
        element = self.wait_for_visible(locator, timeout)
        self.scroll_into_view(element)
        return element













