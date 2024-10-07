import allure
import pytest
import data_burgers
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Проверка перехода на главную страницу при клике на кнопку "Конструктор"')
    def test_click_on_button_constructor_go_to_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_login_page()
        home_page.click_on_button_constructor()
        assert home_page.get_url() == data_burgers.URL_BASE

    @allure.title('Проверка перехода на страницу заказов при клике на кнопку "Лента Заказов"')
    def test_click_on_button_order_list_go_to_order_list_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_on_button_order_list()
        assert home_page.get_url() == data_burgers.URL_ORDER_LIST

    @allure.title('Проверка pop-окна с информацией об ингредиете при клике на ингредиент')
    def test_click_on_img_ingredient_open_inf_window(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        name_ingredient = home_page.get_name_ingredient()
        home_page.click_on_img_ingredient()
        name_ingredient_in_window = home_page.get_name_ingredient_in_inf_window()
        assert name_ingredient == name_ingredient_in_window

    @allure.title('Проверка закрытие pop-окна кликом по крестику')
    def test_click_on_close_inf_window(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.click_on_img_ingredient()
        home_page.click_on_button_close()
        assert home_page.visible_inf_window() is False

    @pytest.mark.parametrize('ingredient, count, expected_count', data_burgers.LIST_INGREDIENT)
    @allure.title('Проверка добавления ингредиента к заказу')
    def test_drag_elemen_to_basket(self, driver, ingredient, count, expected_count):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.add_ingredient_to_basket(ingredient)
        assert home_page.get_text_of_element(count) == expected_count

    @allure.title('Проверка оформления заказа авторезированным пользователем')
    def test_order_auth_user(self, driver, test_user):
        home_page = HomePage(driver)
        home_page.auth_test_user(test_user)
        home_page.create_burger()
        home_page.click_on_button_place_an_order()
        assert home_page.assigned_number_order() is True
