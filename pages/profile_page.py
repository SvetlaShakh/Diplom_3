import allure
from pages.base_page import BasePage
from burgers_locators import BurgerLocators


class ProfilePage(BasePage):

    @allure.step('Кликнуть по кнопке "Выход"')
    def click_on_button_exit(self):
        self.click_on_button(BurgerLocators.BUTTON_EXIT)
