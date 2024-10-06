from selenium.webdriver.common.by import By


class BurgerLocators:
    # header
    BUTTON_PERSONAL_ACCOUNT = [By.XPATH, ".//header//p[text()='Личный Кабинет']/parent::a"]
    BUTTON_ORDER_LIST = [By.XPATH, ".//header//p[text()='Лента Заказов']/parent::a"]
    BUTTON_CONSTRUCTOR = [By.XPATH, ".//header//p[text()='Конструктор']/parent::a"]

    # home page
    BUTTON_PLACE_AN_ORDER = [By.XPATH, ".//button[text()='Оформить заказ']"]
    IMG_INGREDIENT = [By.XPATH, ".//div[contains(@class, 'BurgerIngredients')]/ul[1]/a[1]/img"]
    NAME_INGREDIENT = [By.XPATH, ".//div[contains(@class, 'BurgerIngredients')]/ul[1]/a[1]/p"]
    IMG_INGREDIENT_BUN = [By.XPATH, ".//h2[text()='Булки']/following-sibling::ul/a[1]/img"]
    COUNT_INGREDIENT_BUN = [By.XPATH,
                            ".//h2[text()='Булки']/following-sibling::ul/a[1]//p[contains(@class, 'counter')]"]
    IMG_INGREDIENT_SAUCE = [By.XPATH, ".//h2[text()='Соусы']/following-sibling::ul/a[1]/img"]
    COUNT_INGREDIENT_SAUCE = [By.XPATH,
                              ".//h2[text()='Соусы']/following-sibling::ul/a[1]//p[contains(@class, 'counter')]"]
    IMG_INGREDIENT_FILLING = [By.XPATH, ".//h2[text()='Начинки']/following-sibling::ul/a[1]/img"]
    COUNT_INGREDIENT_FILLING = [By.XPATH,
                                ".//h2[text()='Начинки']/following-sibling::ul/a[1]//p[contains(@class, 'counter')]"]
    # BURGER_CONSTRUCTOR_BASKET = [By.XPATH, ".//section[contains(@class, 'basket')]/ul"]
    BURGER_CONSTRUCTOR_BASKET = [By.XPATH, ".//section[contains(@class, 'basket')]"]

    # order window in home page
    BUTTON_CLOSE_ORDER_WINDOW = [By.XPATH, ".//button[contains(@class, 'close')]"]
    ASSIGNED_NUMBER_ORDER = [By.XPATH, ".//p[text()='идентификатор заказа']/parent::div/h2[string-length(text()) > 4]"]

    # info window in home page
    NAME_INGREDIENT_INF_WINDOW = [By.XPATH, ".//h2[text()='Детали ингредиента']/parent::div/p"]
    BUTTON_CLOSE_INF_WINDOW = [By.XPATH, ".//button[contains(@class, 'close')]"]

    # login page
    INPUT_EMAIL_LOGIN_WINDOW = [By.XPATH, ".//label[text() = 'Email']/parent::div/input"]
    INPUT_PASSWORD_LOGIN_WINDOW = [By.XPATH, ".//label[text() = 'Пароль']/parent::div/input"]
    BUTTON_LOGIN_IN_LOGIN_WINDOW = [By.XPATH, ".//button[text()='Войти']"]
    LINK_FORGOT_PASSWORD = [By.XPATH, ".//a[text()='Восстановить пароль']"]

    # forgot password page
    INPUT_EMAIL = [By.XPATH, ".//label[text()='Email']/parent::div/input"]
    BUTTON_RESTORE = [By.XPATH, ".//button[text()='Восстановить']"]

    # reset password page
    BUTTON_SAVE = [By.XPATH, ".//button[text()='Сохранить']"]
    INPUT_PASSWORD_ACTIVE = [By.XPATH, ".//label[text()='Пароль']/parent::div[contains(@class, 'active')]"]
    ICON_VISIBLE_PASSWORD = [By.XPATH, ".//label[text()='Пароль']/parent::div/div"]

    # account page
    LINK_ORDER_HISTORY = [By.XPATH, ".//a[text()='История заказов']"]
    BUTTON_EXIT = [By.XPATH, ".//button[text()='Выход']"]

    # account page/ order history
    ORDER_IN_ORDER_HISTORY_LIST = [By.XPATH, ".//li[contains(@class, 'OrderHistory')][1]"]

    # feed page
    ORDER_IN_LIST = [By.XPATH, ".//li[contains(@class, 'OrderHistory')][1]"]
    COUNT_TOTAL_ORDER = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p[1]"]
    COUNT_TOTAL_TODAY_ORDER = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p[1]"]
    ORDER_IN_REDY_LIST = [By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li[contains(text()[1],'0')]"]

    # feed page receipt window
    RECEIPT_BURGER = [By.XPATH, ".//div[contains(@class, 'orderBox')]/p[text()='Cостав']"]

    # Modal_modal_overlay__x2ZCr
    OVERLAY_WINDOW = [By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"]
    OVERLAY_WINDOW_SECTION = [By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::section"]
