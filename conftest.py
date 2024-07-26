import pytest
from selenium import webdriver
import data
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.redirect_page import RedirectPage




@pytest.fixture()
def chromedriver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def firefoxdriver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope = 'function')
def main_page(chromedriver):
    main_page = MainPage(chromedriver)
    main_page.get_url(data.url)
    return main_page

@pytest.fixture(scope = 'function')
def order_page(firefoxdriver):
    order_page = OrderPage(firefoxdriver)
    order_page.get_url(data.url)
    return order_page

@pytest.fixture(scope = 'function')
def redirect_page(chromedriver):
    redirect_page = RedirectPage(chromedriver)
    redirect_page.get_url(data.url)
    return redirect_page



