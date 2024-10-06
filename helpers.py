import allure
import random

import string
import time

import requests
import data_burgers
from pages.base_page import BasePage
from pages.home_page import HomePage
from burgers_locators import BurgerLocators


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_registration_body(length):
    registration_body = {}
    registration_body['email'] = f'{generate_random_string(length)}@mail.com'
    registration_body['password'] = generate_random_string(length)
    registration_body['name'] = generate_random_string(length)
    return registration_body


def registration_user_api(body):
    return requests.post(data_burgers.URL_BASE + data_burgers.REGISTER_USER, json=body)


@allure.step('Создать пользователя')
def registration_test_user():
    registration_body = generate_registration_body(6)
    response = registration_user_api(registration_body)
    token = response.json()['accessToken']
    return registration_body, token


@allure.step('Авторизоваться на сайте')
def login_test_user(b_page):
    test_user = registration_test_user()
    email_test_user = test_user[0]['email']
    password_test_user = test_user[0]['password']
    token_test_user = test_user[1]
    base_page = b_page
    base_page.open_home_page()
    base_page.delete_cookie()
    base_page.wait_for_invisibility_of_element(BurgerLocators.OVERLAY_WINDOW)
    base_page.wait_for_element_to_be_clickable(BurgerLocators.BUTTON_PERSONAL_ACCOUNT)
    base_page.click_on_personal_account_button()
    base_page.wait_for_visibility_of_element(BurgerLocators.INPUT_EMAIL_LOGIN_WINDOW)
    base_page.send_email(email_test_user)
    base_page.send_password(password_test_user)
    base_page.click_on_login_button()
    return token_test_user


@allure.step('Собрать бургер')
def create_burger(b_page):
    base_page = b_page
    base_page.drag_element(BurgerLocators.IMG_INGREDIENT_BUN, BurgerLocators.BURGER_CONSTRUCTOR_BASKET)
    base_page.drag_element(BurgerLocators.IMG_INGREDIENT_SAUCE, BurgerLocators.BURGER_CONSTRUCTOR_BASKET)
    base_page.drag_element(BurgerLocators.IMG_INGREDIENT_FILLING, BurgerLocators.BURGER_CONSTRUCTOR_BASKET)


@allure.step('Заказать бургер')
def order_burger(b_page):
    base_page = b_page
    create_burger(base_page)
    base_page.click_on_button_place_an_order()


def delete_test_user(token):
    headers = {'Authorization': token}
    return requests.delete(data_burgers.URL_BASE + data_burgers.DATA_USER, headers=headers)
