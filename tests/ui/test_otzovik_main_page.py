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
         .search('Фильм "Курьер" (1986)')
         .check_film())


         # Ввести поисковый запрос и нажать на поиск
        # Проверить что в результате поиска отображается 'Сериал "Кремниевая долина"'

    @pytest.mark.ui
    @allure.title("Поисковый запрос")
    @allure.link("https://testit.example.com/tc-1")
    def test_valid_search(self, otzivik_main_page):
        (otzivik_main_page
         .open()
         .search('Сериал \"Кремниевая долина\"')
         .check_film())

    @pytest.mark.ui
    @allure.title("Переход по результату поиска")
    @allure.link("https://testit.example.com/tc-1")
    def test_valid_search(self, otzivik_main_page):
        (otzivik_main_page
         .open()
         .search_by_button()

