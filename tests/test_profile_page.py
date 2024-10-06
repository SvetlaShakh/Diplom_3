import allure

import data_burgers
from pages.profile_page import ProfilePage
import helpers
from burgers_locators import BurgerLocators


class TestProfilePage:

    @allure.title('Проверка перехода в личный кабинет по клику на кнопку "Личный кабинет"')
    def test_go_to_profile_page_click_on_button_personal_account(self, driver):
        profile_page = ProfilePage(driver)
        token_test_user = helpers.login_test_user(profile_page)
        profile_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        profile_page.wait_for_element_to_be_clickable(BurgerLocators.BUTTON_PERSONAL_ACCOUNT)
        profile_page.click_on_personal_account_button()
        profile_page.wait_for_load_page(data_burgers.URL_PROFILE_PAGE)
        helpers.delete_test_user(token_test_user)
        assert profile_page.get_url() == data_burgers.URL_PROFILE_PAGE

    @allure.title('Проверка перехода в личном кабинете в раздел "История заказов"')
    def test_go_to_history_orders_click_on_link_order_history(self, driver):
        profile_page = ProfilePage(driver)
        token_test_user = helpers.login_test_user(profile_page)
        profile_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        profile_page.wait_for_element_to_be_clickable(BurgerLocators.BUTTON_PERSONAL_ACCOUNT)
        profile_page.click_on_personal_account_button()
        profile_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        profile_page.wait_for_element_to_be_clickable(BurgerLocators.LINK_ORDER_HISTORY)
        profile_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW_SECTION)
        profile_page.click_on_link_order_history()
        helpers.delete_test_user(token_test_user)
        assert profile_page.get_url() == data_burgers.URL_ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта - клик по кнопке "Выход"')
    def test_logout_click_on_button_exit(self, driver):
        profile_page = ProfilePage(driver)
        token_test_user = helpers.login_test_user(profile_page)
        profile_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        profile_page.wait_for_element_to_be_clickable(BurgerLocators.BUTTON_PERSONAL_ACCOUNT)
        profile_page.click_on_personal_account_button()
        profile_page.wait_for_element_to_be_clickable(BurgerLocators.BUTTON_EXIT)
        profile_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        profile_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW_SECTION)
        profile_page.click_on_button_exit()
        profile_page.wait_for_visibility_of_element(BurgerLocators.BUTTON_LOGIN_IN_LOGIN_WINDOW)
        helpers.delete_test_user(token_test_user)
        assert profile_page.get_url() == data_burgers.URL_LOGIN_PAGE
