import allure
from pages.playwright_base_page import PlaywrightBasePage

class OtzovikRegistrationPage(PlaywrightBasePage):
    otzovik_page = "https://otzovik.com/signup.php"

    LOGIN_INPUT = 'input[name="newlogin"]'
    PASSWORD_INPUT = "#id_pwd"
    EMAIL_INPUT = "#id_mail"
    AGREEMENT_CHECKBOX = "span.check-label:has-text('Я принимаю')"
    SUBMIT_BUTTON = "button.submit.button2023.button-blue:has-text('Зарегистрироваться')"
    ERROR_MESSAGE = "div.auth-error.not-empty"

    @allure.step("Открытие страницы регистрации Отзовик")
    def open_registration_page(self):
        self.logger.info("Открываем страницу регистрации Отзовик")
        self.open(self.otzovik_page)
        return self

    @allure.step("Заполнение поля Логин: {login}")
    def fill_login_field(self, login):
        self.logger.info(f"Вводим логин: {login}")
        self.page.locator(self.LOGIN_INPUT).fill(login)

        return self

    @allure.step("Заполнение поля Пароль: {password}")
    def fill_password_field(self, password):
        self.logger.info(f"Вводим пароль (длина: {len(password)} символов)")
        self.page.locator(self.PASSWORD_INPUT).fill(password)

        return self

    @allure.step("Заполнение поля E-mail: {email}")
    def fill_email_field(self, email):
        self.logger.info(f"Вводим E-mail: {email}")
        self.page.locator(self.EMAIL_INPUT).fill(email)

        return self

    @allure.step("Принятие пользовательского соглашения")
    def accept_agreement(self):
        self.logger.info("Принимаем пользовательское соглашение")
        self.page.evaluate("""() => {
            const label = document.querySelector('span.check-label');
            if (label) {
                label.click();
                return true;
            }
            return false;
        }""")

        return self

    @allure.step("Нажатие кнопки Зарегистрироваться")
    def click_submit(self):
        self.logger.info("Нажимаем кнопку 'Зарегистрироваться'")
        self.page.locator(self.SUBMIT_BUTTON).click()

        return self

    @allure.step("Проверка наличия ошибки с текстом: {expected_text}")
    def assert_error_message_contains(self, expected_text):
        self.logger.info(f"Ожидаем ошибку: '{expected_text}'")
        self.check_text_result(expected_text)

        return self
