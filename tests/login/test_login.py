import allure
import pytest
from src.utils.test_data import get_valid_user, get_login_list, get_invalid_user
from src.utils.assertions import *
from conftest import driver

# Креды для входа
username, password = get_valid_user()
invalid_username, invalid_password = get_invalid_user()

@pytest.mark.login
@pytest.mark.positive
@allure.title("Валидный логин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://testit.example.com/tc-1", name="ТК 1")
def test_valid_login(driver, login_page):
    (login_page
     .open()
     .login(username, password))

    actual_username = login_page.get_logged_in_username().lower()

    print(f"Проверка что введенное имя пользователя: '{username}'\n"
          f"совпадает с указанным на сайте после входа: '{actual_username}'")
    CommonAssertions(driver).assert_is_equal(username, actual_username)

@pytest.mark.negative
@allure.title("Логин с невалидными данными")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://testit.example.com/tc-5", name="ТК 5")
def test_invalid_login(driver, login_page):
    (login_page
     .open()
     .login(invalid_username, invalid_password))
    expected_url = ("https://ru.wikipedia.org/w/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F"
                    ":%D0%92%D1%85%D0%BE%D0%B4&returnto=%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F+%D1%81"
                    "%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
    error_message = login_page.get_error_message()

    expected_error_1 = "Введены неверные имя участника или пароль. Попробуйте ещё раз."
    expected_error_2 = "Возникли проблемы с отправленными данными"

    print(f"\nПроверяем, что сообщение об ошибке совпадает с ожидаемой:\n{expected_error_1}\nили\n{expected_error_2}")
    assert error_message == expected_error_1 or error_message == expected_error_2

    CommonAssertions(driver).assert_is_equal(driver.current_url, expected_url)

@pytest.mark.parametrize("login", get_login_list())
@allure.title("Валидация поля логин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://testit.example.com/tc-2262", name="ТК 2262")
def test_login_input_validation(driver, login, base_page, login_page):
    username_field = login_page.username_input

    (login_page
     .open()
     .asserts.assert_value_is_empty(username_field).to_parent_page()
     .enter_username(login)
     .asserts.assert_is_equal(login, login_page.get_username_field_value()).to_parent_page()
     .refresh()
     .asserts.assert_value_is_empty(username_field))
