import allure
import pytest
import time
from src.utils.test_data import USER_OLGA
from src.utils.test_data import get_valid_user, get_invalid_user

@allure.epic("Корзина")
# @allure.story("")
class TestMainPage:
    # Креды для входа
    username, password = get_valid_user()
    invalid_username, invalid_password = get_invalid_user()

    @pytest.mark.ui
    @allure.title("Товары в корзине")
    @allure.link("https://testit.example.com/tc-1")
    def test_basket(self, clear_cart, main_page, books_page, login_page, base_page):
        (main_page
           .open_main_page()
           .accept_cookies()
           .open_user_menu()
           .click_authorization())

        (login_page
          .enter_username(USER_OLGA)
          .enter_password(USER_OLGA)
          .click_login_button())

        (books_page
            .click_books_link()
            .scroll_to_element("3 в 1: три книги Яна Арта")
            .click_buy_button("3 в 1: три книги Яна Арта")
            .assert_product_added_alert()
            .click_product_in_cart_button()
            .click_go_to_cart_button()
            .assert_quantity())
