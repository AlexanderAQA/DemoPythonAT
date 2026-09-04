import pytest
import allure
from src.utils.test_data import otzovik_negative_cases

@pytest.mark.ui
class TestOtzovikRegistration:

    @allure.title("Регистрация на Отзовике, негативные кейсы")
    @pytest.mark.parametrize("user, expected_error", otzovik_negative_cases)
    def test_otzovik_registration(self, otzovik_registration_page, user, expected_error):
        (otzovik_registration_page
         .open_registration_page()
         .fill_login_field(user.login)
         .fill_password_field(user.password)
         .fill_email_field(user.email)
         .accept_agreement()
         .click_submit()
         .assert_error_message_contains(expected_error)
        )
