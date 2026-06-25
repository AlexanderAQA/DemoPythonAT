import pytest
import allure
from src.utils.test_data import USER_OLGA

class TestAuthMethod:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Авторизация пользователя по customer_token")
    def test_get_check_authorization_method(self, api_client):
        """Проверка авторизации через GET запрос с customer_token"""

        user = USER_OLGA

        # логин (вход)
        customer_token, login_status = api_client.login(
            email=user.login,
            password=user.password
        )

        # проверка успешного логина и что есть токен
        (api_client.assertions
         .assert_symbol_length(26, customer_token)
         .assert_is_equal(200, login_status))

        # Данные для проверки
        expected_username = user.name
        expected_page_title = "Личный Кабинет"
        expected_token_param = f"customer_token={customer_token}"
        expected_logout_link = "route=account/logout"

        # запрос страницы ЛК клиента
        response_html, status_code = api_client.get_account_page(customer_token=customer_token)

        # проверки ответа и ожидаемых параметров - код 200, заголовок, имя пользователя, токен в ссылке, ссылка выхода
        (api_client.assertions
         .assert_is_equal(200, status_code)
         .assert_text_match(expected_page_title, response_html)
         .assert_text_match(expected_username, response_html)
         .assert_text_match(expected_token_param, response_html)
         .assert_text_match(expected_logout_link, response_html))

def test_auth_with_invalid_token(api_client):
    """Проверка авторизации с невалидным токеном"""

    invalid_token = "12345_fake_token"

    # Маркеры страницы входа
    expected_url = 'content="https://shop.finarty.ru/login"'
    expected_title = "Авторизация"
    expected_password_field = "input-password"
    expected_login_button = ">Войти</"
    expected_username = USER_OLGA.name

    # Запрос с невалидным токеном
    response_html, status_code = api_client.get_account_page(customer_token=invalid_token)

    # Проверки
    (api_client.assertions
     .assert_is_equal(200, status_code)  # что страница загрузилась (там нет кодов ошибок нигде, только 200 и редирект на страницу логина)
     .assert_text_match(expected_title, response_html)  # что есть заголовок "Авторизация"
     .assert_text_match(expected_url, response_html)  # в url есть /login
     .assert_text_match(expected_password_field, response_html)  # что есть поле пароля
     .assert_text_match(expected_login_button, response_html))  # что есть кнопка "Войти"

    # Проверка, что пользователь не авторизован с невалидным токеном
    assert expected_username not in response_html, (
        f"Пользователь '{expected_username}' найден на странице входа."
        f"Пользователь авторизовался с невалидным токеном."
    )

