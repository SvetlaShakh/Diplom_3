import allure
from pages.base_page import BasePage
from burgers_locators import BurgerLocators


class ProfilePage(BasePage):

    @allure.step('Кликнуть по кнопке "Выход"')
    def click_on_button_exit(self):
        self.wait_for_element_to_be_clickable(BurgerLocators.BUTTON_EXIT)
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW_SECTION)
        self.click_on_button(BurgerLocators.BUTTON_EXIT)
