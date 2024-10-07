import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import data_burgers
from burgers_locators import BurgerLocators


class FeedPage(BasePage):

    @allure.step('Открыть страницу "Лента заказов" "Stellar Burgers')
    def open_order_list_page(self):
        self.driver.get(data_burgers.URL_ORDER_LIST)

    @allure.step('Кликнуть по заказу в списке')
    def click_on_order_in_list(self):
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        self.wait_for_visibility_of_element(BurgerLocators.ORDER_IN_LIST)
        self.click_on_button(BurgerLocators.ORDER_IN_LIST)

    @allure.step('Кликнуть по крестику в окне заказа')
    def click_on_button_close_order_window(self):
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        self.wait_for_visibility_of_element(BurgerLocators.BUTTON_CLOSE_ORDER_WINDOW)
        self.click_on_button(BurgerLocators.BUTTON_CLOSE_ORDER_WINDOW)

    @allure.step('Найти номер заказа в истории заказов')
    def find_order_in_order_history(self, number):
        self.wait_for_visibility_of_element(BurgerLocators.ORDER_IN_ORDER_HISTORY_LIST)
        number_order = f'#0{number}'
        number_locator = [By.XPATH, ".//div[contains(@class, 'OrderHistory')]/p[text()='{}']".format(number_order)]
        chek_order = self.is_displayed_element(number_locator)
        return chek_order

    @staticmethod
    def get_locator_order_in_rady_list(number):
        return [By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li[contains(text()[2],'{}')]".format(number)]

    @allure.step('Найти номер заказа в списке заказов')
    def find_order_in_rady_list(self, number):
        self.wait_for_visibility_of_element(self.get_locator_order_in_rady_list(number))
        number_locator = [By.XPATH,
                          ".//ul[contains(@class, 'orderListReady')]/li[contains(text()[2],'{}')]".format(number)]
        return self.is_displayed_element(number_locator)

    @allure.step('Найти номер заказа в списке заказов')
    def find_order_in_order_list(self, number):
        self.wait_for_visibility_of_element(BurgerLocators.ORDER_IN_LIST)
        number_order = f'#0{number}'
        number_locator = [By.XPATH, ".//div[contains(@class, 'OrderHistory')]/p[text() = '{}']".format(number_order)]
        chek_order = self.is_displayed_element(number_locator)
        return chek_order

    @allure.step('Получить номер созданного заказа')
    def get_number_created_order(self):
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        self.wait_for_visibility_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        number = self.get_text_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        return number

    @allure.step('Получить колличество заказов')
    def get_count_orders(self, type_count):
        self.wait_for_visibility_of_element(type_count)
        count = self.get_text_of_element(type_count)
        return count

    @allure.step('Проверить видимость окна с рецептом')
    def visible_receipt_burger(self):
        return self.is_displayed_element(BurgerLocators.RECEIPT_BURGER)
