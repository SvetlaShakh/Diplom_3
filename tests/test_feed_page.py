import pytest
import allure
import data_burgers
from pages.feed_page import FeedPage


class TestFeedPage:

    @allure.title('Проверка всплывающее окно с деталями заказа при клике на заказ в листе')
    def test_click_on_order_inform_window(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open_order_list_page()
        feed_page.click_on_order_in_list()
        assert feed_page.visible_receipt_burger() is True

    @allure.title('Проверка номера оформленого заказа в листе заказов и в истории заказов')
    def test_number_order_in_order_list_ahd_order_history(self, driver, test_user):
        feed_page = FeedPage(driver)
        feed_page.auth_test_user(test_user)
        feed_page.order_burger()
        order_number = feed_page.get_number_created_order()
        feed_page.click_on_button_close_order_window()
        feed_page.click_on_personal_account_button()
        feed_page.click_on_link_order_history()
        order_in_order_history = feed_page.find_order_in_order_history(order_number)
        feed_page.click_on_button_order_list()
        order_in_order_list = feed_page.find_order_in_order_list(order_number)
        assert order_in_order_history == order_in_order_list

    @pytest.mark.parametrize('type_count', data_burgers.COUNT_LOCATOR)
    @allure.title('Проверка колличества заказов за все время')
    def test_count_total_order_in_order_list(self, driver, test_user, type_count):
        feed_page = FeedPage(driver)
        feed_page.auth_test_user(test_user)
        feed_page.open_order_list_page()
        before_count_total = feed_page.get_count_orders(type_count)
        feed_page.open_home_page()
        feed_page.order_burger()
        feed_page.get_number_created_order()
        feed_page.click_on_button_close_order_window()
        feed_page.click_on_button_order_list()
        after_count_total = feed_page.get_count_orders(type_count)
        feed_page.delete_cookie()
        assert before_count_total < after_count_total

    @allure.title('Проверка созданный заказ появляется в разделе "В работе"')
    def test_order_in_redy_list(self, driver, test_user):
        feed_page = FeedPage(driver)
        feed_page.auth_test_user(test_user)
        feed_page.order_burger()
        order_number = feed_page.get_number_created_order()
        feed_page.click_on_button_close_order_window()
        feed_page.click_on_button_order_list()
        order_in_rady_list = feed_page.find_order_in_rady_list(order_number)
        assert order_in_rady_list is True
