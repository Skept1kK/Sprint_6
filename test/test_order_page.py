import allure
import pytest

from conftest import driver
from page.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from data import OrderUser

class TestOrderPageOrder:

    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Тестирование функциональности оформления заказа из хэдера')
    @pytest.mark.parametrize('button, test_data', [(OrderPageLocators.order_button_in_header, OrderUser.data_sets)])
    def test_order_button_in_header(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_order_button_in_header()
        order_page.click_on_order_button_in_header()
        order_page.fill_user_data(test_data['data_set1'])
        order_page.go_next()
        order_page.fill_rent_data(test_data['data_set1'])
        order_page.next_step()
        assert order_page.check_displaying_of_button_check_status_of_order()


    @allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Тестирование функциональности оформления заказа из мэйна')
    @pytest.mark.parametrize('button, test_data', [(OrderPageLocators.order_button_in_main, OrderUser.data_sets)])
    def test_order_button_in_main(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_visibility_of_order_button_in_main()
        order_page.click_on_order_button_in_main()
        order_page.fill_user_data(test_data['data_set2'])
        order_page.go_next()
        order_page.fill_rent_data(test_data['data_set2'])
        order_page.next_step()
        assert order_page.check_displaying_of_button_check_status_of_order()