from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from src.utils import assertions
from src.utils.assertions import CommonAssertions


class LoginPage(BasePage):
    """Страница логина"""
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

        # URL для тестов
        self.login_url = ("https://auth.wikimedia.org/ruwiki/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:"
                          "%D0%92%D1%85%D0%BE%D0%B4?useformat=desktop&usesul3=1&returnto=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%"
                          "D0%B2%D0%BD%D0%B0%D1%8F+%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    # Локаторы
    username_input = (By.XPATH, "//input[@id='wpName1']")
    password_input = (By.ID, "wpPassword1")
    login_button = (By.ID, "pt-login")
    error_message = (By.XPATH, "//*[@class='cdx-message__content']")
    submit_button = (By.ID, 'wpLoginAttempt')
    username_element = (By.ID, "pt-userpage")

    def open(self):
        """Открываем страницу логина"""
        print(f"Открываем страницу логина: {self.login_url}")
        self.driver.get(self.login_url)
        return self

    def enter_username(self, username):
        """Вводим логин"""
        print(f"Заполняем поле username: '{username}'")
        self.enter_text(self.username_input, username)
        return self

    def to_assertions(self):
        """Переходим к проверкам"""
        return CommonAssertions(self.driver)

    def get_username_field_value(self):
        """Получаем значение введенное в поле 'username'"""
        return self.get_element_text(self.username_input)

    def enter_password(self, password):
        """Вводим пароль"""
        print(f"Заполняем поле password: '{password}'")
        self.enter_text(self.password_input, password)
        return self

    def click_login(self):
        """Кликаем кнопку Войти"""
        print("Кликаем кнопку Войти")
        self.click(self.login_button)
        return self

    def login(self, username, password):
        """Вводим логин, пароль и кликаем войти"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self):
        """Получаем текст ошибки"""
        return self.get_element_text(self.error_message)
