import time
from pages.old.login_page import LoginPage
import allure
import pytest
from conftest import main_arty_page
from src.utils.test_data import get_valid_user, get_login_list, get_invalid_user

@allure.epic("Главная страница")
# @allure.story("")
class TestMainPage:
    # Креды для входа
    username, password = get_valid_user()
    invalid_username, invalid_password = get_invalid_user()

    @pytest.mark.ui
    @allure.title("Валидный логин")
    @allure.link("https://testit.example.com/tc-1")
    def test_valid_login(self, driver, main_arty_page, login_page):
        login_page = (main_arty_page
                     .open_main_page()
                     .accept_cookies()
                     .open_user_menu()
                     .click_authorization())

        (login_page
          .click_login_field()
          .fill_login_field("helgaautotests@gmail.com")
          .click_password_field()
          .fill_password_field ("Helgaautotests26")
          .click_login_button())
        main_arty_page.assert_account_header()

        # TODO: Дз от 20.04: дописать автотест на авторизацию учетки (предварительно зарегаться руками 1 раз)