from selenium.webdriver.common.by import By
class MainPageLocators:
    """Локаторы для главной страницы(Конструктор)"""
    # Кнопки навигации в шапке
    CONSTRUCTOR_TAB = (By.XPATH, "//P[text()='Конструктор']")
    ORDERS_FEED_TAB = (By.XPATH, "//a[@href='/feed']")  
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BURGER = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and contains(., 'Соберите бургер')]")
    OVERLAY = (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")
    DRAG = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]//span[contains(text(), 'Перетяните')]")
    LENTA_BUT = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Лента Заказов')]")
    LENTA = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(., 'Лента Заказов')]")
    CONSTR = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(., 'Конструктор')]")
    BUN = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient') and contains(., 'булка')]")
    DETAILS = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_modified')]")
    CROSS = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")
    BURGER_CONSTR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")


    #  разделы ингредиентов
    INGREDIENT_SECTION_BUN =(By.XPATH, "//h2[text()='Булки']")
    INGREDIENT_SECTION_SAUCE = (By.XPATH, "//h2[text()='Соусы']")
    INGREDIENT_SECTION_MAIN = (By.XPATH, "//h2[text()='Начинки']")


    INGREDIENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_SAUCE = (By.XPATH, "//p[text()='Соус фирменный Space Sauce']")

    INGREDIENT_MAIN = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")

    INGREDIENT_DETAILS_NAME = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    INGREDIENT_PARENT = (By.XPATH, "./..")
    INGREDIENT_COUNTER = (By.XPATH, ".//p[@class='counter_counter__num__3nue1']")

    #  Модальное окна
    MODAL_OPENED_CLASS = "Modal_modal_opened"
    MODAL_WINDOW = (By.CSS_SELECTOR, "section[class*='Modal_modal']")
    INGREDIENT_MODAL_CLOSE = (By.CSS_SELECTOR, "button[class*='modal__close']")

    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button') and contains(text(), 'Оформить заказ')]")

    #   Зона конструктора (куда перетаскивают)
    CONSTRUCTOR_DROP_AREA = (By.CLASS_NAME, "BurgerConstructor_basket__list__19dp_")

    ORDER_MODAL = (By.CSS_SELECTOR, "section[class*='Modal_modal']")
    ORDER_MODAL_CLOSE = (By.CSS_SELECTOR, "button[class*='modal_close']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
    ORDER_LOADING_MODAL = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")

class FeedPageLocators:
    """Локаторы для страницы Ленты заказов"""

    #   Счётчики в ленте заказов
    ORDER_LOADING_MODAL = (By.XPATH, "//div[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal_overlay__x2ZCr']")
    TOTAL_COUNTER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number_2MbrQ') and preceding-sibling::p[contains(text(), 'Выполнено за все время')]]")
    TODAY_COUNTER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number_2MbrQ' and preceding-sibling::p[contains(text(),'Выполнено за сегодня')]]")

    ORDER_CARDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]")

    ORDERS_IN_PROGRESS_SECTION = (By.XPATH, "//ul[preceding-sibling::p[contains(text(), 'В работе')]]")
    ORDERS_IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")



class AuthLocators:
    """Локаторы для авторизации"""
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON_AUTH = (By.XPATH, "//button[text()='Войти']")

