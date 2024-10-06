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
        self.click_on_button(BurgerLocators.ORDER_IN_LIST)

    @allure.step('Кликнуть по крестику в окне заказа')
    def click_on_button_close_order_window(self):
        self.click_on_button(BurgerLocators.BUTTON_CLOSE_ORDER_WINDOW)

    @allure.step('Найти номер заказа в истории заказов')
    def find_order_in_order_history(self, number):
        number_order = f'#0{number}'
        number_locator = [By.XPATH, ".//div[contains(@class, 'OrderHistory')]/p[text()='{}']".format(number_order)]
        chek_order = self.check_displayed_element(number_locator)
        return chek_order

    @staticmethod
    def get_locator_order_in_rady_list(number):
        return [By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li[contains(text()[2],'{}')]".format(number)]

    @allure.step('Найти номер заказа в списке заказов')
    def find_order_in_rady_list(self, number):
        number_locator = [By.XPATH,
                          ".//ul[contains(@class, 'orderListReady')]/li[contains(text()[2],'{}')]".format(number)]
        return self.check_displayed_element(number_locator)

    @allure.step('Найти номер заказа в списке заказов')
    def find_order_in_order_list(self, number):
        number_order = f'#0{number}'
        number_locator = [By.XPATH, ".//div[contains(@class, 'OrderHistory')]/p[text() = '{}']".format(number_order)]
        chek_order = self.check_displayed_element(number_locator)
        return chek_order
