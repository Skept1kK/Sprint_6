import allure
import pytest
from conftest import driver
from data import TestData
from page.main_page import MainPage

class TestMainPageFaq:
    @allure.title('Проверка секции "Вопросы о важном"')
    @pytest.mark.parametrize('index,questions_items, answers_items', TestData.test_data_answer_questions)
    def test_faq_questions(self, index, driver, questions_items, answers_items):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.find_question_section()
        main_page.wait_questions_section(index)
        main_page.click_of_element(index)
        main_page.wait_for_answer(index)
        assert main_page.get_answer_text(index) == answers_items