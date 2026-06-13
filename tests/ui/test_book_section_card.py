import random
import allure
import pytest
from src.utils.test_data import USER_OLGA, BOOK_1, BOOK_2, BOOK_3


@allure.epic("Карточка товара раздела `Книги`")
class TestBooksCardPage:
    books_list = [BOOK_1, BOOK_2, BOOK_3]

    @pytest.mark.ui
    @allure.title("Карточка товара раздела `Книги`")
    @allure.link("https://testit.example.com/tc-1")
    def test_book_section_card(self, login_page, books_page):
        (login_page
             .authorization(USER_OLGA)
             .click_books_link())
        book = random.choice(self.books_list)

        (books_page
            .scroll_to_book(book.name)
            .click_book_name(book.name)
            .assert_book_cart_name_displayed(book.name)
            .assert_book_cart_price_displayed(book.price)
            .assert_article_code_displayed(book.article)
            .assert_article_label_displayed()
            .get_quantity_books()
            .click_plus_button()
            .assert_plus()
            .click_minus_button()
            .assert_minus()
            .get_wishlist_count()
            .click_add_to_wishlist()
            .assert_wishlist_count_add()
            .click_delete_from_wishlist()
            .assert_wishlist_count_delete()
            .assert_description_content(book.name))
