import pytest
from selenium import webdriver
from data import URLS

@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    firefox_driver = webdriver.Firefox(options=options)
    firefox_driver.maximize_window()
    firefox_driver.get(URLS.BASE_URL)
    yield firefox_driver
    firefox_driver.quit()