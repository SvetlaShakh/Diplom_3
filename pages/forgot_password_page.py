import allure
from pages.base_page import BasePage
import data_burgers
from burgers_locators import BurgerLocators


class ForgotPasswordPage(BasePage):

    @allure.step('Открыть страницу "Восстановление пароля" "Stellar Burgers')
    def open_forgot_password_page(self):
        self.driver.get(data_burgers.URL_FORGOT_PASSWORD_PAGE)

    @allure.step('Кликнуть по ссылке "Восстановить пароль"')
    def click_on_link_forgot_password(self):
        self.click_on_button(BurgerLocators.LINK_FORGOT_PASSWORD)

    @allure.step('Заполнить поле "email" на странице восстановления пароля')
    def send_email_forgot_password_page(self, email):
        element = BurgerLocators.INPUT_EMAIL
        self.send_key_to_field(element, email)

    @allure.step('Кликнуть по кнопке "Восстановить"')
    def click_on_button_restore(self):
        self.click_on_button(BurgerLocators.BUTTON_RESTORE)

    @allure.step('Кликнуть по иконке видимости пароля')
    def click_on_icon_visible(self):
        self.click_on_button(BurgerLocators.ICON_VISIBLE_PASSWORD)
