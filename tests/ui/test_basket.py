import allure
import pytest

@allure.epic("Корзина")
class TestMainPage:

    @pytest.mark.ui
    @allure.title("Товары в корзине")
    @allure.link("https://testit.example.com/tc-1")
    def test_basket(self, main_page, login_page, books_page, base_page, cart_page):
        (main_page
            .open_main_page()
            .accept_cookies())

        (login_page
            .authorization())

        (cart_page
            .clear_cart()
            .click_books_link())

        (books_page
          .scroll_to_book("3 в 1: три книги Яна Арта из серии «Библиотека Finversia»")
          .click_buy_button("3 в 1: три книги Яна Арта из серии «Библиотека Finversia»")
          .assert_product_added_alert()
          .click_product_in_cart_button()
          .click_go_to_cart_button())

        (cart_page
          .assert_quantity(1))
