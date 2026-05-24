import allure
import pytest
from src.utils.test_data import USER_OLGA

@allure.epic("Корзина")
class TestMainPage:

    @pytest.mark.ui
    @allure.title("Товары в корзине")
    @allure.link("https://testit.example.com/tc-1")
    def test_basket(self, main_page, books_page, login_page, base_page, cart_page):
        (cart_page
            .clear_cart()
            .accept_cookies())

        (base_page
            .click_books_link())

        (books_page
          .scroll_to_book("3 в 1: три книги Яна Арта из серии «Библиотека Finversia»")
          .click_buy_button("3 в 1: три книги Яна Арта из серии «Библиотека Finversia»")
          .assert_product_added_alert()
          .click_product_in_cart_button()
          .click_go_to_cart_button())

        (cart_page
          .assert_quantity(1))
