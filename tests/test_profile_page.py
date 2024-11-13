import allure
import data_burgers
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Проверка перехода в личный кабинет по клику на кнопку "Личный кабинет"')
    def test_go_to_profile_page_click_on_button_personal_account(self, driver, test_user):
        profile_page = ProfilePage(driver)
        profile_page.auth_test_user(test_user)
        profile_page.click_on_personal_account_button()
        profile_page.wait_for_load_page(data_burgers.URL_PROFILE_PAGE)
        assert profile_page.get_url() == data_burgers.URL_PROFILE_PAGE

    @allure.title('Проверка перехода в личном кабинете в раздел "История заказов"')
    def test_go_to_history_orders_click_on_link_order_history(self, driver, test_user):
        profile_page = ProfilePage(driver)
        profile_page.auth_test_user(test_user)
        profile_page.click_on_personal_account_button()
        profile_page.click_on_link_order_history()
        assert profile_page.get_url() == data_burgers.URL_ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта - клик по кнопке "Выход"')
    def test_logout_click_on_button_exit(self, driver, test_user):
        profile_page = ProfilePage(driver)
        profile_page.auth_test_user(test_user)
        profile_page.click_on_personal_account_button()
        profile_page.click_on_button_exit()
        profile_page.wait_for_load_page(data_burgers.URL_LOGIN_PAGE)
        assert profile_page.get_url() == data_burgers.URL_LOGIN_PAGE
