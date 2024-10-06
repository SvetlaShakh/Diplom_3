import pytest
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
