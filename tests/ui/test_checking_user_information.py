import allure
import pytest
from src.utils.test_data import USER_OLGA


@allure.epic("Аккаунт")
class TestMainPage:

    @pytest.mark.ui
    @allure.title("Аккаунт пользователя")
    @allure.link("https://testit.example.com/tc-1")
    def test_checking_user_information(self, login_page, account_page):
        (login_page
         .authorization(USER_OLGA))

        (account_page
         .click_change_information()
         .assert_field_headers()
         .assert_profile_field_values(["Ольга", "Тверская", "helgaautotests@gmail.com", "+7 (900) 000-00-00"])
         .assert_back_continue_buttons()
         .assert_pers_account_and_home_buttons())