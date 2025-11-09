from selenium.webdriver.common.by import By

NAME_INPUT = (By.NAME, "name")
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
ACCOUNT_HEADER = (By.CSS_SELECTOR, "header.AccountHeader_header__")

CONSTRUCTOR_TAB = (By.XPATH, "//P[text()='Конструктор'']")
ORDERS_FEED_TAB = (By.LINK_TEXT, "Лента заказов")

INGREDIENT = (By.CSS_SELECTOR, "div[class*='BurgerIngredient_ingredient__']")
INGREDIENT_COUNTER = (By.CSS_SELECTOR, ".counter")

INGREDIENT_CARD = (By.CSS_SELECTOR, "div.BurgerIngredient_ingredient__")

INGREDIENT_MODAL = (By.CSS_SELECTOR, "div[class*='Modal_modal__']")
MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_closeButton__']")
MODAL_WINDOW =(By.CSS_SELECTOR, "div.Modal_modal__")

TOTAL_COUNTER = (By.XPATH, "//p[contains(text(), 'Всего заказов')]/following-sibling::p")
TODAY_COUNTER = (By.XPATH, "//p[contains(text(), 'За сегодня')]/following-sibling::p")
TOTAL_DONE_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")

TODAY_DONE_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня'0]/following-sibling::p")
ORDERIN_PROGRESS = (By.CSS_SELECTOR, "div.OrderCard_card__")
