import allure

from page.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_for_element(OrderPageLocators.order_button_in_header)

    @allure.step('Нажатие на кнопку "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.click_element(OrderPageLocators.order_button_in_header)

    @allure.step('Ожидание загрузки кнопки "Заказать" в мэйне')
    def wait_visibility_of_order_button_in_main(self):
        self.wait_for_element(OrderPageLocators.order_button_in_main)

    @allure.step('Нажатие на кнопку "Заказать" в мэйне')
    def click_on_order_button_in_main(self):
        self.click_element(OrderPageLocators.order_button_in_main)

    @allure.step('Ввод имени')
    def input_first_name(self, user_info):
        self.find_element(OrderPageLocators.input_name).click()
        self.set_value(OrderPageLocators.input_name, user_info['first_name'])

    @allure.step('Ввод фамилии')
    def input_last_name(self, user_info):
        self.find_element(OrderPageLocators.input_lastname).click()
        self.set_value(OrderPageLocators.input_lastname, user_info['last_name'])

    @allure.step('Ввод адреса')
    def input_address(self, user_info):
        self.find_element(OrderPageLocators.input_address).click()
        self.set_value(OrderPageLocators.input_address, user_info['address'])

    @allure.step('Выбор метро')
    def choose_subway(self, user_info):
        self.find_element(OrderPageLocators.input_metro).click()
        self.set_value(OrderPageLocators.input_metro, user_info['station'])
        self.click_element(OrderPageLocators.select_item_in_dropdown_metro)

    @allure.step('Ввод номера телефона')
    def input_number(self, user_info):
        self.find_element(OrderPageLocators.input_phone).click()
        self.set_value(OrderPageLocators.input_phone, user_info['tel_number'])

    @allure.step('Заполнить данные на этапе "Для кого самокат"')
    def fill_user_data(self, data_set: dict):
        self.input_first_name(data_set)
        self.input_last_name(data_set)
        self.input_address(data_set)
        self.choose_subway(data_set)
        self.input_number(data_set)

    @allure.step('Перейти на следующий этап заказа')
    def go_next(self):
        self.find_element(OrderPageLocators.button_next).click()

    @allure.step('Выбор даты доставки')
    def choose_date(self, user_info):
        self.find_element(OrderPageLocators.input_date).click()
        self.set_value(OrderPageLocators.input_date, user_info['date'])
        self.wait_for_element(OrderPageLocators.calendar)
        self.wait_for_element(OrderPageLocators.calendar_item)
        self.click_element(OrderPageLocators.calendar_item)

    @allure.step('Выбор периода аренды')
    def choose_time(self):
        self.find_element(OrderPageLocators.field_rental_period).click()
        self.wait_for_element(OrderPageLocators.dropdown_item_rental_period).click()

    @allure.step('Выбор цвета')
    def choose_color(self):
        self.find_element(OrderPageLocators.checkbox_grey_color_scooter).click()

    @allure.step('Комментарий курьеру')
    def input_comment(self, user_info):
        self.find_element(OrderPageLocators.input_comment).click()
        self.set_value(OrderPageLocators.input_comment, user_info['comment_for_courier'])

    @allure.step('Заполнить данные на этапе "Про аренду"')
    def fill_rent_data(self, data_set: dict):
        self.choose_date(data_set)
        self.choose_time()
        self.choose_color()
        self.input_comment(data_set)

    @allure.step('Перейти на следующий этап заказа')
    def next_step(self):
        self.find_element(OrderPageLocators.button_make_order).click()
        self.wait_for_element(OrderPageLocators.button_yes_confirm_order).click()

    @allure.step('Проверить отображение кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.is_element_present(OrderPageLocators.button_check_status_of_order)