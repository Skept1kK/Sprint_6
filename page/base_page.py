import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from data import URLS

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скроллим страницу до  нужного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ждем загрузку элемента')
    def wait_for_element(self, locator, visibility=True, timeout=15):
        condition = (EC.visibility_of_element_located if visibility
                     else EC.presence_of_element_located)
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    @allure.step('Получаем текущий URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Ждем загрузки новой вкладки Дзен')
    def wait_for_new_window(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_changes(URLS.BLANK_URL))
        return WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

    @allure.step('Ищем элемент по локатору')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Кликаем по элементу')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Вводим текст в поле')
    def set_value(self, locator, value):
        self.find_element(locator).send_keys(value)

    @allure.step("Проверяем наличие элемента")
    def is_element_present(self,locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Переключаемся на другую вкладку")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
