import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from seletools.actions import drag_and_drop

import data_burgers
from burgers_locators import BurgerLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_button(self, button):
        self.driver.find_element(*button).click()

    def wait_for_element_to_be_clickable(self, element):
        WebDriverWait(self.driver, 5000).until(
            expected_conditions.element_to_be_clickable(element))

    def wait_for_visibility_of_element(self, element):
        WebDriverWait(self.driver, 5000).until(
            expected_conditions.visibility_of_element_located(element))

    def wait_for_invisibility_of_element(self, element):
        WebDriverWait(self.driver, 5000).until(
            expected_conditions.invisibility_of_element_located(element))

    def wait_for_load_page(self, url):
        WebDriverWait(self.driver, 5000).until(
            expected_conditions.url_contains(url))

    def send_key_to_field(self, element, key):
        self.driver.find_element(*element).send_keys(key)

    def get_text_of_element(self, element):
        return self.driver.find_element(*element).text

    def check_displayed_element(self, element):
        return self.driver.find_element(*element).is_displayed()

    @allure.step('Открыть главную страницу "Stellar Burgers')
    def open_home_page(self):
        self.driver.get(data_burgers.URL_BASE)

    @allure.step('Открыть главную страницу авторизации "Stellar Burgers')
    def open_login_page(self):
        self.driver.get(data_burgers.URL_LOGIN_PAGE)

    @allure.step('Заполнить поле "Email"')
    def send_email(self, email):
        element = BurgerLocators.INPUT_EMAIL_LOGIN_WINDOW
        self.send_key_to_field(element, email)

    @allure.step('Заполнить поле "Пароль"')
    def send_password(self, password):
        element = BurgerLocators.INPUT_PASSWORD_LOGIN_WINDOW
        self.send_key_to_field(element, password)

    @allure.step('Перетащить элемент')
    def drag_element(self, ingredient, basket):
        driver = self.driver
        element = self.driver.find_element(*ingredient)
        target = self.driver.find_element(*basket)
        drag_and_drop(driver, element, target)

    @allure.step('Кликнуть по кнопке "Войти в аккаунт"')
    def click_on_personal_account_button(self):
        self.click_on_button(BurgerLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Кликнуть по кнопке "Лента Заказов"')
    def click_on_button_order_list(self):
        self.click_on_button(BurgerLocators.BUTTON_ORDER_LIST)

    @allure.step('Кликнуть по кнопке "Войти"')
    def click_on_login_button(self):
        self.click_on_button(BurgerLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW)

    @allure.step('Кликнуть по кнопке "Оформить заказ"')
    def click_on_button_place_an_order(self):
        self.click_on_button(BurgerLocators.BUTTON_PLACE_AN_ORDER)

    @allure.step('Кликнуть по кнопке "История заказов"')
    def click_on_link_order_history(self):
        self.click_on_button(BurgerLocators.LINK_ORDER_HISTORY)

    @allure.step('Получить текущий URL страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Удалить куки')
    def delete_cookie(self):
        self.driver.delete_all_cookies()
