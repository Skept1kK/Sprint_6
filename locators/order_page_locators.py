from selenium.webdriver.common.by import By


class OrderPageLocators:
    title_page_personal_info = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")
    input_name = (By.XPATH, "//input[@placeholder='* Имя']")
    input_lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")
    input_address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    input_metro = (By.XPATH, "//input[@placeholder='* Станция метро']")
    select_item_in_dropdown_metro = (By.XPATH, ".//li[@class='select-search__row']")
    input_phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, "//button[text()='Далее']")
    title_page_rent_info = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")
    input_date = [By.XPATH, ".//div[@class='react-datepicker__input-container']/input"]
    calendar = [By.XPATH, ".//div[@class='react-datepicker__week']"]
    calendar_item = [By.CSS_SELECTOR, ".react-datepicker__day[tabindex='0']"]
    checkbox_grey_color_scooter = (By.XPATH, "//input[@id='grey']")
    field_rental_period = (By.XPATH, ".//div[text()='* Срок аренды']")
    dropdown_item_rental_period = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    DAY_ORDER = (By.XPATH, "//div[@class='Dropdown-option'and text()='сутки']")
    input_comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    button_make_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    button_yes_confirm_order = (By.XPATH, "//button[text()='Да']")
    button_check_status_of_order = (By.XPATH, ".//*[text()='Посмотреть статус']")
    order_button_in_main = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')
    order_button_in_header = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')

