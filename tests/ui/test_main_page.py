import allure
import pytest

from src.utils.test_data import USER_OLGA
from src.utils.test_data import get_valid_user, get_invalid_user

@allure.epic("Главная страница")
# @allure.story("")
class TestMainPage:
    # Креды для входа
    username, password = get_valid_user()
    invalid_username, invalid_password = get_invalid_user()

    @pytest.mark.ui
    @allure.title("Валидный логин")
    @allure.link("https://testit.example.com/tc-1")
    def test_valid_login(self, main_page, login_page, account_page):
        (main_page
           .open_main_page()
           .accept_cookies()
           .open_user_menu()
           .click_authorization())

        (login_page
          .enter_username(USER_OLGA)
          .enter_password(USER_OLGA)
          .click_login_button())

        (account_page
           .assert_account_header()
           .assert_exit_button()
           .assert_username(USER_OLGA))

    @pytest.mark.ui
    @allure.title("Сортировка от А до Я")
    def test_sort_a_z(self, main_page, books_page):
        (main_page
         .open_main_page()
         .accept_cookies())

        # Выбираем сортировку по имени
        (books_page
         .select_sort_by_name("name_asc"))

        # Проверка названий первых нескольких книг (10)
        titles = books_page.get_book_titles_list(limit=10)

        sorted_titles = sorted(titles)

        books_page.asserts.assert_is_equal(sorted_titles, titles)
