import pytest
import allure
from src.utils.test_data import USER_OLGA


@pytest.mark.positive
@pytest.mark.api
@allure.title("Авторизация пользователя по customer_token")
@allure.link("https://testit.example.com/tc-auth-token")
def test_get_check_authorization_method(api_client):
    """Проверка авторизации через GET запрос с customer_token"""

    user = USER_OLGA

    # логин (вход)
    customer_token, login_status = api_client.login(
        email=user.login,
        password=user.password
    )

    # проверка успешного логина
    assert login_status == 200, f"Login failed with status {login_status}"
    assert customer_token, "Customer token not received after login"

    # проверка авторизации в личном кабинете
    expected_username = user.name
    expected_page_title = "Личный Кабинет"
    expected_token_param = f"customer_token={customer_token}"
    expected_logout_link = "route=account/logout"

    response_html, status_code = api_client.get_account_page(customer_token=customer_token)

    # проверки ответа и ожидаемых параметров
    assert status_code == 200
    assert expected_page_title in response_html
    assert expected_username in response_html
    assert expected_token_param in response_html
    assert expected_logout_link in response_html

