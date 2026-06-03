import allure
import pytest
from src.utils.test_data import USER_OLGA

@allure.epic("Карточка товара раздела `Книги`")
class TestMainPage:

    @pytest.mark.ui
    @allure.title("Карточка товара раздела `Книги`")
    @allure.link("https://testit.example.com/tc-1")
    def test_book_section_card(self, login_page, books_page):
        (login_page
         .authorization(USER_OLGA)
         .click_books_link())
        book_name = "3 в 1: три книги Яна Арта из серии «Библиотека Finversia»"
        expected_price = "1 480 ₽"
        expected_article = "ФК0179"
        bookmarks_count = 0

        (books_page
          .scroll_to_book(book_name)
          .click_book_name(book_name)
          .assert_book_info_displayed(
                book_cart_name=book_name,
                book_price=expected_price,
                article_code=expected_article
          )
          .check_quantity_buttons()
          .check_wishlist(count=bookmarks_count)
          .assert_description_content())