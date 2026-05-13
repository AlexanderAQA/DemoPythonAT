import allure

from locators.account_page_locators import AccountPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from src.utils.test_data import TestUsers


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Открываем страницу логина"""
        with allure.step(f"Открываем страницу логина: {self.login_url}"):
            self.driver.get(self.login_url)
            return self

    def enter_username(self, user: TestUsers):
        """Вводим логин"""
        with allure.step("Заполняем поле username"):
            self.enter_text(LoginPageLocators.LOGIN_FIELD, user.login)
            return self

    def get_username_field_value(self):
        """Получаем значение введенное в поле 'username'"""
        return self.get_element_text(LoginPageLocators.LOGIN_FIELD)

    def enter_password(self, user: TestUsers):
        """Вводим пароль"""
        with allure.step(f"Заполняем поле password"):
            self.enter_text(LoginPageLocators.PASSWORD_FIELD, user.password)
        return self

    def click_login(self):
        """Кликаем кнопку Войти"""
        with allure.step("Кликаем кнопку Войти"):
            self.click(LoginPageLocators.LOGIN_BUTTON)
            return self

    def login(self, username, password):
        """Вводим логин, пароль и кликаем войти"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self):
        """Получаем текст ошибки"""
        return self.get_element_text(LoginPageLocators.error_message)

    def click_login_field(self):
        with allure.step(f"Клик по полю ввода E-Mail на странице авторизации"):
            locator = LoginPageLocators.LOGIN_FIELD
            self.click(locator)

            return self

    def click_password_field(self):
        with allure.step(f"Клик по полю ввода пароля на странице авторизации"):
            locator = LoginPageLocators.PASSWORD_FIELD
            self.click(locator)

            return self

    def click_login_button(self):
        with allure.step(f"Клик по кнопке `Войти`"):
            locator = LoginPageLocators.LOGIN_BUTTON
            self.click(locator)

            return self
