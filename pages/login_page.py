import allure

from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from src.utils.test_data import TestUsers, USER_OLGA


class LoginPage(BasePage):
    """Страница Логина"""
    def __init__(self, driver):
        super().__init__(driver)
        self.login_url = 'https://shop.finarty.ru/login'

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

    def authorization(self):
        with allure.step("Авторизация в личном кабинете"):
            elements = self.driver.find_elements(*AccountPageLocators.get_actual_username('{text}'))
            is_authorized = elements and elements[0].text.strip() != ""

            if not is_authorized:
                with allure.step("Пользователь не авторизован, выполняем вход"):
                    self.open()
                    self.open_user_menu()
                    self.click_authorization()
                    self.enter_username(USER_OLGA)
                    self.enter_password(USER_OLGA)
                    self.click_login_button()
                    self.wait_for()
            else:
                user_name = elements[0].text.strip()
                with allure.step(f"Пользователь '{user_name}' уже авторизован"):
                    pass

            return self