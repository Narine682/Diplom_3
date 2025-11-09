from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from utils.constants import IMPLICIT_WAIT


def create_driver(browser="chrome"):
    browser = browser.lower()

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser must be 'chrome' or 'firefox")

    driver.maximize_window()
    return driver