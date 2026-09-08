import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.otzovik_registration_locators import OtzovikLocators
from pages.playwright_base_page import PlaywrightBasePage


class OtzovikRegistrationPage(PlaywrightBasePage):
    otzovik_page = "https://otzovik.com/signup.php"

    @allure.step("Открытие страницы регистрации Отзовик")
    def open_registration_page(self):
        self.logger.info("Открываем страницу регистрации Отзовик")
        self.open(self.otzovik_page)
        return self

    @allure.step("Заполнение поля Логин: {login}")
    def fill_login_field(self, login):
        self.logger.info(f"Вводим логин: {login}")
        self.page.locator('input[name="newlogin"]').fill(login)

        return self

    @allure.step("Заполнение поля Пароль: {password}")
    def fill_password_field(self, password):
        self.logger.info(f"Вводим пароль (длина: {len(password)} символов)")
        self.page.locator(OtzovikLocators.PASSWORD_INPUT).fill(password)

        return self

    @allure.step("Заполнение поля E-mail: {email}")
    def fill_email_field(self, email):
        self.logger.info(f"Вводим E-mail: {email}")
        self.page.locator(OtzovikLocators.EMAIL_INPUT).fill(email)

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
        self.page.locator(OtzovikLocators.SUBMIT_BUTTON).click()

        return self

    @allure.step("Проверка наличия ошибки с текстом: {expected_text}")
    def assert_error_message_contains(self, expected_text):
        self.logger.info(f"Ожидаем ошибку: '{expected_text}'")
        self.check_text_result(expected_text)

        return self
