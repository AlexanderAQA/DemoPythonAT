from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        """Открываем страницу логина"""
        print(f"Открываем страницу логина: {self.login_url}")
        self.driver.get(self.login_url)
        return self

    def enter_username(self, username):
        """Вводим логин"""
        print("Заполняем поле username")
        self.enter_text(BasePageLocators.login_field, username)
        return self

    def get_username_field_value(self):
        """Получаем значение введенное в поле 'username'"""
        return self.get_element_text(BasePageLocators.login_field)

    def enter_password(self, password):
        """Вводим пароль"""
        print(f"Заполняем поле password: '{password}'")
        self.enter_text(BasePageLocators.password_field, password)
        return self

    def click_login(self):
        """Кликаем кнопку Войти"""
        print("Кликаем кнопку Войти")
        self.click(BasePageLocators.login_button)
        return self

    def login(self, username, password):
        """Вводим логин, пароль и кликаем войти"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self):
        """Получаем текст ошибки"""
        return self.get_element_text(BasePageLocators.error_message)

    def click_login_field(self):
        locator = BasePageLocators.login_field
        self.click(locator)
        return self

    def click_password_field(self):
        locator = BasePageLocators.password_field
        self.click(locator)
        return self

    def click_login_button(self):
        locator = BasePageLocators.login_button
        self.click(locator)
        return self

    def fill_login_field(self, email: str):
        self.enter_text(BasePageLocators.login_field, email)
        return self

    def fill_password_field(self, password: str):
        self.enter_text(BasePageLocators.password_field, password)
        return self