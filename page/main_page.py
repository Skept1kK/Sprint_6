import allure

from page.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import TestData

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидаем загрузки лого "Самокат" в хэдере')
    def wait_visibility_logo_scooter(self):
        self.wait_for_element(MainPageLocators.header_logo_scooter)

    @allure.step('Ожидаем загрузки лого с надписью "Яндекс" в хэдере')
    def wait_visibility_logo_yandex(self):
        self.wait_for_element(MainPageLocators.header_logo_yandex)

    @allure.step('Нажатие на лого с надписью "Самокат" в хэдере')
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.header_logo_scooter)

    @allure.step('Нажатие на лого с надписью "Яндекс" в хэдере')
    def click_logo_yandex(self):
        self.click_element(MainPageLocators.header_logo_yandex)

    @allure.step('Ожидание отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_for_element(MainPageLocators.main_header)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.is_element_present(MainPageLocators.main_header)

    @allure.step('Листаем страницу до секции с вопросам')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.questions_section)

    @allure.step('Ищем секцию с вопросам')
    def find_question_section(self):
        self.find_element(MainPageLocators.questions_section)

    @allure.step('Ждем загрузки вопроса в секции с вопросам')
    def wait_questions_section(self, data):
        self.wait_for_element(MainPageLocators.questions_items[data])

    @allure.step('Нажимаем на необходимый вопрос из секции с вопросам')
    def click_of_element(self, data):
        self.click_element(MainPageLocators.questions_items[data])

    @allure.step('Ждем текст ответа на выбранный вопрос из секции с вопросам')
    def wait_for_answer(self, data):
        self.wait_for_element(MainPageLocators.questions_items[data])

    @allure.step('Получаем текст ответа на выбранный вопрос из секции с вопросам')
    def get_answer_text(self, index ):
        return TestData.test_data_answer_questions[index-1][2]

