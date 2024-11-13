import allure
from pages.base_page import BasePage
from burgers_locators import BurgerLocators


class HomePage(BasePage):

    @allure.step('Кликнуть по кнопке "Конструктор"')
    def click_on_button_constructor(self):
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        self.click_on_button(BurgerLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Кликнуть по кнопке "Лента Заказов"')
    def click_on_img_ingredient(self):
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        self.wait_for_element_to_be_clickable(BurgerLocators.IMG_INGREDIENT)
        self.click_on_button(BurgerLocators.IMG_INGREDIENT)

    @allure.step('Кликнуть по крестику в информационном окне')
    def click_on_button_close(self):
        self.click_on_button(BurgerLocators.BUTTON_CLOSE_INF_WINDOW)

    @allure.step('Кликнуть по кнопке "Оформить заказ"')
    def click_on_button_place_an_order(self):
        self.click_on_button(BurgerLocators.BUTTON_PLACE_AN_ORDER)

    @allure.step('Добавить ингредиет в корзину')
    def add_ingredient_to_basket(self, ingredient):
        self.wait_for_element_to_be_clickable(BurgerLocators.IMG_INGREDIENT)
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        self.wait_for_visibility_of_element(BurgerLocators.BURGER_CONSTRUCTOR_BASKET)
        self.drag_element(ingredient, BurgerLocators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Получить название ингредиета')
    def get_name_ingredient(self):
        self.wait_for_visibility_of_element(BurgerLocators.NAME_INGREDIENT)
        self.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
        return self.get_text_of_element(BurgerLocators.NAME_INGREDIENT)

    @allure.step('Получить название ингредиета в информационном окне')
    def get_name_ingredient_in_inf_window(self):
        return self.get_text_of_element(BurgerLocators.NAME_INGREDIENT_INF_WINDOW)

    @allure.step('Проверить видимость информационного окна')
    def visible_inf_window(self):
        self.wait_for_invisibility_of_element(BurgerLocators.NAME_INGREDIENT_INF_WINDOW)
        return self.is_displayed_element(BurgerLocators.NAME_INGREDIENT_INF_WINDOW)

    @allure.step('Проверить назначение номера для созданного заказа')
    def assigned_number_order(self):
        self.wait_for_visibility_of_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
        return self.is_displayed_element(BurgerLocators.ASSIGNED_NUMBER_ORDER)
