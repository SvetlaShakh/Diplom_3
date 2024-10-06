import pytest
import allure

import data_burgers
from pages.feed_page import FeedPage
from burgers_locators import BurgerLocators
import helpers


class TestFeedPage:

    @allure.title('Проверка всплывающее окно с деталями заказа при клике на заказ в листе')
    def test_click_on_order_inform_window(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_order_list_page()
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.wait_for_visibility_of_element(BurgerLocators.ORDER_IN_LIST)
        feed_page.click_on_order_in_list()
        visible_receipt = feed_page.check_displayed_element(BurgerLocators.RECEIPT_BURGER)
        assert visible_receipt is True

    @allure.title('Проверка номера оформленого заказа в листе заказов и в истории заказов')
    def test_number_order_in_order_list_ahd_order_history(self, driver):
        feed_page = FeedPage(driver)
        test_user = helpers.login_test_user(feed_page)
        token_test_user = test_user
        feed_page.wait_for_visibility_of_element(BurgerLocators.BUTTON_PLACE_AN_ORDER)
        helpers.order_burger(feed_page)
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.wait_for_visibility_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        order_number = feed_page.get_text_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        feed_page.click_on_button_close_order_window()
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.click_on_personal_account_button()
        feed_page.wait_for_element_to_be_clickable(BurgerLocators.LINK_ORDER_HISTORY)
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW_SECTION)
        feed_page.click_on_link_order_history()
        feed_page.wait_for_visibility_of_element(BurgerLocators.ORDER_IN_ORDER_HISTORY_LIST)
        order_in_order_history = feed_page.find_order_in_order_history(order_number)
        feed_page.click_on_button_order_list()
        feed_page.wait_for_visibility_of_element(BurgerLocators.ORDER_IN_LIST)
        order_in_order_list = feed_page.find_order_in_order_list(order_number)
        helpers.delete_test_user(token_test_user)
        assert order_in_order_history == order_in_order_list

    @pytest.mark.parametrize('type_count', data_burgers.COUNT_LOCATOR)
    @allure.title('Проверка колличества заказов за все время')
    def test_count_total_order_in_order_list(self, driver, type_count):
        feed_page = FeedPage(driver)
        feed_page.open_order_list_page()
        feed_page.wait_for_visibility_of_element(type_count)
        before_count_total = feed_page.get_text_of_element(type_count)
        token_test_user = helpers.login_test_user(feed_page)
        feed_page.wait_for_visibility_of_element(BurgerLocators.IMG_INGREDIENT)
        helpers.create_burger(feed_page)
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.wait_for_visibility_of_element(BurgerLocators.BUTTON_PLACE_AN_ORDER)
        feed_page.click_on_button_place_an_order()
        feed_page.wait_for_visibility_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        order_number = feed_page.get_text_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.click_on_button_close_order_window()
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.click_on_button_order_list()
        feed_page.wait_for_visibility_of_element(feed_page.get_locator_order_in_rady_list(order_number))
        after_count_total = feed_page.get_text_of_element(type_count)
        helpers.delete_test_user(token_test_user)
        feed_page.delete_cookie()
        assert before_count_total < after_count_total

    @allure.title('Проверка созданный заказ появляется в разделе "В работе"')
    def test_order_in_redy_list(self, driver):
        feed_page = FeedPage(driver)
        token_test_user = helpers.login_test_user(feed_page)
        feed_page.wait_for_visibility_of_element(BurgerLocators.IMG_INGREDIENT)
        helpers.create_burger(feed_page)
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.wait_for_visibility_of_element(BurgerLocators.BUTTON_PLACE_AN_ORDER)
        feed_page.click_on_button_place_an_order()
        feed_page.wait_for_visibility_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        order_number = feed_page.get_text_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        feed_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        feed_page.click_on_button_close_order_window()
        feed_page.click_on_button_order_list()
        feed_page.wait_for_visibility_of_element(feed_page.get_locator_order_in_rady_list(order_number))
        order_in_rady_list = feed_page.find_order_in_rady_list(order_number)
        helpers.delete_test_user(token_test_user)
        feed_page.delete_cookie()
        assert order_in_rady_list is True
