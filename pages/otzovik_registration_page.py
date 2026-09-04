import allure
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.otzovik_registration_locators import OtzovikLocators
from src.utils.assertions import CommonAssertions


class OtzovikRegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)
        self.assertions = CommonAssertions(self)

    @allure.step("Открытие страницы регистрации Отзовик")
    def open_registration_page(self):
        self.logger.info("Открываем страницу регистрации Отзовик")
        self.driver.get("https://otzovik.com/signup.php")
        return self

    @allure.step("Заполнение поля Логин: {login}")
    def fill_login_field(self, login):
        self.logger.info(f"Вводим логин: {login}")
        field = self.driver.find_element(*OtzovikLocators.LOGIN_INPUT)
        field.clear()
        field.send_keys(login)
        return self

    @allure.step("Заполнение поля Пароль: {password}")
    def fill_password_field(self, password):
        self.logger.info(f"Вводим пароль (длина: {len(password)} символов)")
        field = self.driver.find_element(*OtzovikLocators.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)
        return self

    @allure.step("Заполнение поля E-mail: {email}")
    def fill_email_field(self, email):
        self.logger.info(f"Вводим E-mail: {email}")
        field = self.driver.find_element(*OtzovikLocators.EMAIL_INPUT)
        field.clear()
        field.send_keys(email)
        return self

    @allure.step("Принятие пользовательского соглашения")
    def accept_agreement(self):
        self.logger.info("Принимаем пользовательское соглашение")
        checkbox = self.driver.find_element(*OtzovikLocators.AGREEMENT_CHECKBOX)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.logger.info("Чекбокс отмечен")
        return self

    @allure.step("Нажатие кнопки Зарегистрироваться")
    def click_submit(self):
        self.logger.info("Нажимаем кнопку 'Зарегистрироваться'")
        btn = self.driver.find_element(*OtzovikLocators.SUBMIT_BUTTON)
        btn.click()
        return self

    @allure.step("Проверка наличия ошибки с текстом: {expected_text}")
    def assert_error_message_contains(self, expected_text):
        self.logger.info(f"Ожидаем ошибку: '{expected_text}'")
        error_element = self.wait.until(
            EC.visibility_of_element_located(OtzovikLocators.ERROR_MESSAGE)
        )
        actual_text = error_element.text.strip()
        self.logger.info(f"Реальный текст ошибки: '{actual_text}'")
        self.assertions.assert_text_match(expected_text, actual_text)
        self.logger.info("Проверка пройдена")

        return self
