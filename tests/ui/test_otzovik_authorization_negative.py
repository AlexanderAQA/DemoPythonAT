import pytest
import allure
from src.utils.test_data import generate_otzovik_user

@pytest.mark.ui
class TestOtzovikAuthorizationNegative:

    @allure.title("Негативный тест авторизации без captcha на Отзовике")
    def test_otzovik_authorization_captcha_negative(self, otzovik_authorization_page):
        fake_user = generate_otzovik_user()

        (otzovik_authorization_page
         .open_authorization_page()
         .fill_login(fake_user.login)
         .fill_password(fake_user.password)
         .click_submit())

        error_text = otzovik_authorization_page.get_captcha_error_text()
        expected_text = "Введенные символы не совпадают с символами на картинке."
        otzovik_authorization_page.asserts.assert_is_equal(expected_text, error_text)
