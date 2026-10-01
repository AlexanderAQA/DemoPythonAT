from src.utils.logger import allure_and_logger
from pages.playwright_base_page import PlaywrightBasePage

class OtzovikAuthorizationPage(PlaywrightBasePage):
    otzovik_auth_page = "https://otzovik.com/loginnew.php"

    # Поле логина
    LOGIN_INPUT = "#login-win-input"
    # Поле пароля
    PASSWORD_INPUT = "input[name='pass'][data-error='auth']"
    # Кнопка "Войти"
    SUBMIT_BUTTON = "button.submit.button2023.button-blue:has-text('Войти')"
    # Блок с ошибкой авторизации
    ERROR_MESSAGE = "#error-auth"
    # Ошибка капчи
    CAPTCHA_ERROR_MESSAGE = "#error-logcap"

    def open_authorization_page(self):
        allure_and_logger("Открытие страницы авторизации Отзовик")
        self.open(self.otzovik_auth_page)
        return self

    def fill_login(self, login):
        allure_and_logger(f"Ввод логина: {login}")
        self.page.locator(self.LOGIN_INPUT).fill(login)
        return self


    def fill_password(self, password):
        allure_and_logger("Ввод пароля")
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        return self


    def get_captcha_error_text(self):
        allure_and_logger("Ожидание появления ошибки капчи")
        error_locator = self.page.locator(self.CAPTCHA_ERROR_MESSAGE)
        error_locator.wait_for(state="visible", timeout=5000)
        return error_locator.text_content().strip()


    def click_submit(self):
        allure_and_logger("Нажатие кнопки 'Войти'")
        self.page.locator(self.SUBMIT_BUTTON).click()
        return self


    def get_error_text(self):
        allure_and_logger("Ожидание появления ошибки авторизации")
        error_locator = self.page.locator(self.ERROR_MESSAGE)
        error_locator.wait_for(state="visible", timeout=5000)
        return error_locator.text_content().strip()
