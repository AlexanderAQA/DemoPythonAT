from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Страница логина"""
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

        # URL для тестов
        self.login_url = ("https://ru.wikipedia.org/w/index.php?returnto=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F+%D1%"
                     "81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0"
                     "%92%D1%85%D0%BE%D0%B4&centralAuthAutologinTried=1&centralAuthError=Not+centrally+logged+in")

    # Локаторы
    username_input = (By.XPATH, "//input[@id='wpName1']")
    password_input = (By.ID, "wpPassword1")
    login_button = (By.ID, "pt-login")
    error_message = (By.XPATH, "//*[@class='cdx-message__content']")
    submit_button = (By.ID, 'wpLoginAttempt')
    username_element = (By.ID, "pt-userpage")
    actual_username = (By.XPATH, "//*[@id='pt-userpage']/a/span")

    def open(self):
        """Открываем страницу логина"""
        self.driver.get(self.login_url)
        return self

    def enter_username(self, username):
        """Вводим логин"""
        self.enter_text(self.username_input, username)
        return self

    def enter_password(self, password):
        """Вводим пароль"""
        self.enter_text(*self.password_input, password)
        return self

    def click_login(self):
        """Кликаем кнопку Войти"""
        self.click(*self.login_button)
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

    def get_logged_in_username(self):
        """Получаем имя авторизованного пользователя в нижнем регистре"""
        element = self.driver.find_element(*self.actual_username)
        return element.text.lower()
