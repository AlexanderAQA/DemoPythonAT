import allure
import pytest

@allure.epic("Форма создания отзыва")
# @allure.story("")
class TestOtzovikReviewPage:

    @pytest.mark.ui
    @allure.title("Проверка формы создания отзыва")
    @allure.link("https://testit.example.com/tc-1")
    def test_great_form_review(self, otzivik_main_page, otzivik_prereview_page):
        (otzivik_main_page
         .open()
         .open_prereview_form())
        (otzivik_prereview_page
         .check_have_text_prereview()
         .check_entre_text('айфон 17'))