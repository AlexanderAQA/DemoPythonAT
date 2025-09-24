import pytest
from selenium.webdriver import Keys
from src.utils.test_data import get_valid_user, get_login_list, get_invalid_user
from src.utils.assertions import *
from tests.conftest import driver

# Креды для входа
username, password = get_valid_user()
invalid_username, invalid_password = get_invalid_user()

@pytest.mark.login
@pytest.mark.positive
def test_valid_login(driver, login_page):
    (login_page
     .open()
     .login(username, password))

    actual_username = login_page.get_logged_in_username()

    print(f"Проверка что введеное имя пользователя: '{username}'\n"
          f"совпадает с указанным на сайте после входа: '{actual_username}'")
    assert_is_equal(username, actual_username)

@pytest.mark.negative
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

    assert error_message == expected_error_1 or error_message == expected_error_2
    print(f"\nПроверяем, что сообщение об ошибке совпадает с ожидаемой:\n{expected_error_1}\nили\n{expected_error_2}")

    assert_is_equal(driver.current_url, expected_url)

@pytest.mark.parametrize("login", get_login_list())
def test_login_input_validation(driver, login, base_page, login_page):
    login_page.open()

    assert_is_empty(driver.find_element(*login_page.username_input))

    driver.find_element(*login_page.username_input).send_keys(login)
    print(f"Вводим значение: {login}")

    assert_is_equal(login, driver.find_element(*login_page.username_input).get_attribute("value"))

    base_page.refresh()
    print("Обновляем страницу")

    base_page.assert_is_empty(driver.find_element(*login_page.username_input))
    print("Проверяем, что поле логин снова пустое")

def test_key_enter(driver, base_page, login_page):
    old_expected_url = "https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD"
    expected_url = "https://ru.wikipedia.org/w/index.php?fulltext=%D0%9D%D0%B0%D0%B9%D1%82%D0%B8&search=%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1"

    driver.get(login_page.main_page_url)
    print(f"Открываем главную страницу Википедии:\n{login_page.main_page_url}")

    driver.find_element(*base_page.search_input_field).send_keys("Цицерон")
    print("Вводим в поисковую строку: Цицерон")

    driver.find_element(*base_page.search_input_field).send_keys(Keys.ENTER)
    # driver.find_element(*base_page.search_input_field).send_keys(Keys.TAB * 5)
    print("Нажимаем кнопку Enter")

    assert driver.current_url == expected_url
    # assert driver.current_url != old_expected_url
    print(f"Проверяем что фактический URL:\n{driver.current_url}\nсовпадает с ожидаемым:\n{expected_url}")


def test_always_fails(driver):
    driver.get("https://ru.wikipedia.org/wiki/%D0%A6%D0%B8%D1%86%D0%B5%D1%80%D0%BE%D0%BD")
    assert driver.title == "ASDJHALSKJDHIUHkJSHDJNSDKJHKSHDKSHD"  # Тест гарантировано упадет


