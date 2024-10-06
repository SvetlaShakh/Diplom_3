import allure
from pages.base_page import BasePage
from burgers_locators import BurgerLocators


class HomePage(BasePage):

    @allure.step('Кликнуть по кнопке "Конструктор"')
    def click_on_button_constructor(self):
        self.click_on_button(BurgerLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Кликнуть по кнопке "Лента Заказов"')
    def click_on_img_ingredient(self):
        self.click_on_button(BurgerLocators.IMG_INGREDIENT)

    @allure.step('Кликнуть по крестику в информационном окне')
    def click_on_button_close(self):
        self.click_on_button(BurgerLocators.BUTTON_CLOSE_INF_WINDOW)

    @allure.step('Кликнуть по кнопке "Оформить заказ"')
    def click_on_button_place_an_order(self):
        self.click_on_button(BurgerLocators.BUTTON_PLACE_AN_ORDER)

    @allure.step('Добавить ингредиет в корзину')
    def add_ingredient_to_basket(self, ingredient):
        self.drag_element(ingredient, BurgerLocators.BURGER_CONSTRUCTOR_BASKET)
