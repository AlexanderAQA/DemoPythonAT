import time

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
    def test_valid_login(self, driver, main_arty_page):
        (main_arty_page
         .open_main_page()
         .open_user_menu()
         .click_authorization()
         .click_login_field()
         .enter_text('helgaautotests@gmail.com')
         .click_password_field()
         .enter_text('Helgaautotests26')
         .click_login_button())
        main_arty_page.assert_account_header()

        # TODO: Дз от 20.04: дописать автотест на авторизацию учетки (предварительно зарегаться руками 1 раз)
