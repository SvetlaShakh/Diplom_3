import pytest
import allure
import requests
import helpers
from selenium import webdriver
import data_burgers


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):

    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.maximize_window()
    browser.get(data_burgers.URL_BASE)

    yield browser

    browser.quit()


@allure.step('Создать тестового пользователя')
@pytest.fixture
def test_user(driver):
    data_test_user = helpers.generate_registration_body(6)
    response = helpers.registration_user_api(data_test_user)
    token_test_user = response.json()['accessToken']

    yield data_test_user

    headers = {'Authorization': token_test_user}
    requests.delete(data_burgers.URL_BASE + data_burgers.DATA_USER, headers=headers)
