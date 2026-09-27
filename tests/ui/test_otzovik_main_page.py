import allure
import pytest

@allure.epic("Главная страница Отзовик")
# @allure.story("")
class TestOtzovikMainPage:


    @pytest.mark.ui
    @allure.title("Поисковый запрос")
    @allure.link("https://testit.example.com/tc-1")
    def test_valid_search(self, otzivik_main_page):
        (otzivik_main_page
         .open()
         .search_by_button('Сериал \"Кремниевая долина\"')
         .check_film('Сериал \"Кремниевая долина\"'))


    @pytest.mark.ui
    @allure.title("Переход по результату поиска")
    @allure.link("https://testit.example.com/tc-1")
    def test_open_after_search(self, otzivik_main_page):
        (otzivik_main_page
         .open()
         .search_by_button('Смартфон Apple iPhone 17')
         .open_card('Смартфон Apple iPhone 17')
         .check_review_tab()
         .check_negative_tab()
         .check_positive_tab()
         .check_headline ('Смартфон Apple iPhone 17'))


