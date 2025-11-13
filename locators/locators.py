from selenium.webdriver.common.by import By
class MainPageLocators:
    """Локаторы для главной страницы(Конструктор)"""
    # Кнопки навигации в шапке
    CONSTRUCTOR_TAB = (By.XPATH, "//P[text()='Конструктор']")
    ORDERS_FEED_TAB = (By.XPATH, "//a[@href='/feed']")  
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

    #Ингредиенты
    INGREDIENT_COUNTER = (By.XPATH, ".//p[contains(@class,'counter_counter_num_3nue1')]")

    #  разделы ингредиентов
    INGREDIENT_SECTION_BUN =(By.XPATH, "//h2[text()='Булки']")
    INGREDIENT_SECTION_SAUCE = (By.XPATH, "//h2[text()='Соусы']")
    INGREDIENT_SECTION_MAIN = (By.XPATH, "//h2[text()='Начинки']")

    INGREDIENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    INGREDIENT_SAUCE = (By.XPATH, "//P[text()='Соус фирменный Space Sauce']")
    INGREDIENT_MAIN = (By.XPATH, "//p[text()='Мясо бессмертных моллюсков Protostomia']")
    INGREDIENT_DETAILS_NAME = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    INGREDIENT_PARENT = (By.XPATH, "./..")          # Родитель ингредиента
    INGREDIENT_COUNTER_RELATIVE = (By.XPATH, ".//p[contains(@class, 'counter_counter_num_3nue1')]")   #Относительный счетчик ингредиента

    #Модальное окна
    INGREDIENT_MODAL_CLOSE = (By.CLASS_NAME, "Modal_modal_close_modified_3V5XS")
    MODAL_OPENED_CLASS = "Modal_modal_opened_3ISs4"
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button_33qZ0.button_button_type_primary_107Bx.button_button_size_large_G21Vg")

    #Зона конструктора (куда перетаскивают)
    CONSTRUCTOR_DROP_AREA = (By.CLASS_NAME, "BurgerConstructor_basket_list_19dp_")


    # Оформление заказа
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__') and contains(text(), 'Оформить заказ')]")
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__P3_V5")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")


class FeedPageLocators:
    """Локаторы для страницы Ленты заказов"""
    #Счетсики в ленте заказов

    TOTAL_COUNTER = (By.XPATH, "//p[contains(@class, 'Orderfeed_number__2MbY') and preceding-sibling::p[contains(text(), 'Выполнено за все время')]]")
    TODAY_COUNTER = (By.XPATH, "//p[contains(@class, 'Orderfeed_number__2MbY') and preceding-sibling::p[contains(text(), 'Выполнено за сегодня')]]")
    ORDER_CARDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_listItem')]")
    ORDER_IN_PROGRESS_SECTION = (By.XPATH, "//a//preceding-sibling::p[contains(text(), 'В РОБОТi')]]")
    ORDERS_IN_PROGRESS = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")

class AuthLocators:
    """Локаторы для авторизации"""
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON_AUTH = (By.XPATH, "//button[text()='Войти']")

