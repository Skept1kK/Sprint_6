import allure

from conftest import driver
from page.main_page import MainPage
from page.order_page import OrderPage
from page.base_page import BasePage
from data import URLS

class TestLogoRedirect:
    @allure.title('Тестирование перехода на главную страницу сервиса с помощью клика на лого "Самокат" ')
    def test_redirect_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page=OrderPage(driver)
        order_page.wait_visibility_of_order_button_in_header()
        order_page.click_on_order_button_in_header()
        main_page.wait_visibility_logo_scooter()
        main_page.click_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Тестирование перехода на страницу "Дзен" с помощью клика на лого "Яндекс"')
    def test_redirect_to_dzen(self, driver):
        main_page = MainPage(driver)
        base_page= BasePage(driver)
        main_page.wait_visibility_logo_yandex()
        main_page.click_logo_yandex()
        base_page.switch_to_new_window()
        base_page.wait_for_new_window()
        assert driver.current_url == URLS.DZEN_URL