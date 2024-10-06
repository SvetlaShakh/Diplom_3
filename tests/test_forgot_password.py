import allure
from selenium import webdriver
from pages.forgot_password_page import ForgotPasswordPage
import helpers
import data_burgers
from burgers_locators import BurgerLocators


class TestForgotPasswordPage:

    @allure.title('Проверка перехода на страницу восстановления пароля по клику на ссылку "Восстановить пароль"')
    def test_go_to_forgot_password_window(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_login_page()
        forgot_password_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        forgot_password_page.wait_for_element_to_be_clickable(BurgerLocators.LINK_FORGOT_PASSWORD)
        forgot_password_page.click_on_link_forgot_password()
        assert forgot_password_page.get_url() == data_burgers.URL_FORGOT_PASSWORD_PAGE

    @allure.title('Проверка перехода на страницу восстановления пароля(установка нового пароля)'
                  'при заполнении поля "email" по клику на кнопку "Восстановить"')
    def test_go_to_reset_password_window(self, driver):
        test_user = helpers.registration_test_user()
        email_test_user = test_user[0]['email']
        token_test_user = test_user[1]
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.send_email(email_test_user)
        forgot_password_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        forgot_password_page.click_on_button_restore()
        helpers.delete_test_user(token_test_user)
        forgot_password_page.wait_for_visibility_of_element(BurgerLocators.BUTTON_SAVE)
        assert forgot_password_page.get_url() == data_burgers.URL_RESET_PASSWORD_PAGE

    @allure.title('Проверка перехода поля "Пароль" в активное состояние при клике на иконку видимости пароля')
    def test_delight_input_password(self, driver):
        test_user = helpers.registration_test_user()
        email_test_user = test_user[0]['email']
        token_test_user = test_user[1]
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open_forgot_password_page()
        forgot_password_page.send_email_forgot_password_page(email_test_user)
        forgot_password_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        forgot_password_page.click_on_button_restore()
        forgot_password_page.wait_for_element_to_be_clickable(BurgerLocators.ICON_VISIBLE_PASSWORD)
        forgot_password_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        forgot_password_page.click_on_icon_visible()
        active_input = forgot_password_page.check_displayed_element(BurgerLocators.INPUT_PASSWORD_ACTIVE)
        helpers.delete_test_user(token_test_user)
        assert active_input is True
