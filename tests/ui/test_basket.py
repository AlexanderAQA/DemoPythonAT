import allure
import pytest

from conftest import books_page
from src.utils.test_data import USER_OLGA


@allure.epic("Корзина")
class TestMainPage:

    @pytest.mark.ui
    @allure.title("Товары в корзине")
    @allure.link("https://testit.example.com/tc-1")
    def test_basket(self, login_page, books_page, base_page, cart_page):
        (login_page
            .authorization(USER_OLGA))

        (cart_page
            .clear_cart()
            .click_books_link())

        book_name = "3 в 1: три книги Яна Арта из серии «Библиотека Finversia»"
        price = books_page.get_price_from_book(book_name)

        (books_page
          .scroll_to_book(book_name)
          .click_buy_button(book_name)
          .assert_product_added_alert()
          .click_product_in_cart_button()
          .click_go_to_cart_button())

        (cart_page
          .assert_quantity(1)
          .check_price(price))
