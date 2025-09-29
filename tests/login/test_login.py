import allure
import pytest

from pages.base_page import BasePage
from pages.login_page.login_page import LoginPage
from src.utils.test_data import get_valid_user, get_login_list, get_invalid_user
from conftest import driver, main_page


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("Sign")
@allure.story("Sign Feature Functionality")
@allure.severity(allure.severity_level.BLOCKER)
class TestLogin:

    # Креды для входа
    username, password = get_valid_user()
    invalid_username, invalid_password = get_invalid_user()

    @pytest.mark.login
    @pytest.mark.positive
    @allure.title("Валидный логин")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://testit.example.com/tc-1", name="ТК 1")
    def test_valid_login(self, driver, login_page, main_page):
        (login_page
         .open()
         .login(self.username, self.password))

        actual_username = main_page.get_logged_in_username().lower()

        print(f"Проверка что введенное имя пользователя: '{self.username}'\n"
              f"совпадает с указанным на сайте после входа: '{actual_username}'")
        login_page.asserts.assert_is_equal(self.username, actual_username)

    @pytest.mark.negative
    @pytest.mark.login
    @allure.title("Логин с невалидными данными")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://testit.example.com/tc-5", name="ТК 5")
    def test_invalid_login(self, driver, login_page):
        expected_url = ("https://ru.wikipedia.org/w/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F"
                        ":%D0%92%D1%85%D0%BE%D0%B4&returnto=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F+%D1%81"
                        "%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
        expected_error_1 = "Введены неверные имя участника или пароль. Попробуйте ещё раз."
        expected_error_2 = "Возникли проблемы с отправленными данными"

        (login_page
         .open()
         .login(self.invalid_username, self.invalid_password))

        error_message = login_page.get_error_message()

        print(f"\nПроверяем, что сообщение об ошибке совпадает с ожидаемой:\n{expected_error_1}\nили\n{expected_error_2}")
        assert error_message == expected_error_1 or error_message == expected_error_2

        login_page.assert_is_equal(driver.current_url, expected_url)

    @allure.title("Валидация поля логин")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://testit.example.com/tc-2262", name="ТК 2262")
    @pytest.mark.parametrize("login", get_login_list())
    @pytest.mark.login
    def test_login_input_validation(self, login, login_page):
        username_field = login_page.username_input

        (login_page
         .open()
         .assert_value_is_empty(username_field)
         .enter_username(login)
         .asserts.assert_is_equal(login, login_page.get_username_field_value()).to_parent_page()
         .refresh_page()
         .assert_value_is_empty(username_field))
