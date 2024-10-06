import allure
import pytest

import data_burgers
from pages.home_page import HomePage
import helpers
from burgers_locators import BurgerLocators


class TestHomePage:

    @allure.title('Проверка перехода на главную страницу при клике на кнопку "Конструктор"')
    def test_click_on_button_constructor_go_to_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_login_page()
        home_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        home_page.click_on_button_constructor()
        assert home_page.get_url() == data_burgers.URL_BASE

    @allure.title('Проверка перехода на страницу заказов при клике на кнопку "Лента Заказов"')
    def test_click_on_button_order_list_go_to_order_list_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        home_page.wait_for_element_to_be_clickable(BurgerLocators.BUTTON_ORDER_LIST)
        home_page.click_on_button_order_list()
        assert home_page.get_url() == data_burgers.URL_ORDER_LIST

    @allure.title('Проверка pop-окна с информацией об ингредиете при клике на ингредиент')
    def test_click_on_img_ingredient(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.wait_for_visibility_of_element(BurgerLocators.NAME_INGREDIENT)
        home_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        name_ingredient = home_page.get_text_of_element(BurgerLocators.NAME_INGREDIENT)
        home_page.click_on_img_ingredient()
        name_ingredient_in_window = home_page.get_text_of_element(BurgerLocators.NAME_INGREDIENT_INF_WINDOW)
        assert name_ingredient == name_ingredient_in_window

    @allure.title('Проверка закрытие pop-окна кликом по крестику')
    def test_click_on_close_inf_window(self, driver):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        home_page.wait_for_element_to_be_clickable(BurgerLocators.IMG_INGREDIENT)
        home_page.click_on_img_ingredient()
        home_page.click_on_button_close()
        home_page.wait_for_invisibility_of_element(BurgerLocators.NAME_INGREDIENT_INF_WINDOW)
        visible_inf_window = home_page.check_displayed_element(BurgerLocators.NAME_INGREDIENT_INF_WINDOW)
        assert visible_inf_window is False

    @pytest.mark.parametrize('ingredient, count, expected_count', data_burgers.LIST_INGREDIENT)
    @allure.title('Проверка добавления ингредиента к заказу')
    def test_drag_elemen_to_basket(self, driver, ingredient, count, expected_count):
        home_page = HomePage(driver)
        home_page.open_home_page()
        home_page.wait_for_element_to_be_clickable(BurgerLocators.IMG_INGREDIENT)
        home_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        home_page.wait_for_visibility_of_element(BurgerLocators.BURGER_CONSTRUCTOR_BASKET)
        home_page.add_ingredient_to_basket(ingredient)
        assert home_page.get_text_of_element(count) == expected_count

    @allure.title('Проверка оформления заказа авторезированным пользователем')
    def test_order_auth_user(self, driver):
        home_page = HomePage(driver)
        token_test_user = helpers.login_test_user(home_page)
        home_page.wait_for_element_to_be_clickable(BurgerLocators.IMG_INGREDIENT)
        helpers.create_burger(home_page)
        home_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        home_page.click_on_button_place_an_order()
        home_page.wait_for_visibility_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        order_number = home_page.check_displayed_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        helpers.delete_test_user(token_test_user)
        assert order_number is True
