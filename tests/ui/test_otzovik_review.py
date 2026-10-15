import allure
import pytest

@allure.epic("Форма создания отзыва")
# @allure.story("")
class TestOtzovikReviewPage:

    @pytest.mark.ui
    @allure.title("Проверка формы создания отзыва")
    @allure.link("https://testit.example.com/tc-1")
    def test_great_form_review(self, otzovik_main_page, otzovik_prereview_page):
        (otzovik_main_page
         .open()
         .open_prereview_form())
        (otzovik_prereview_page
         .check_have_text_prereview('Для добавления нового отзыва необходимо указать объект, о котором Вы собираетесь написать отзыв.')
         .check_have_text_prereview('Если во всплывающей подсказке вы обнаружите нужный объект, то выберите его, чтобы пропустить лишние шаги.')
         .entre_reveiw_name('айфон 17')
         .select_iphone_17_pro_max()
         .check_review_headline_iphone_17_pro_max()
         .check_label('Общая оценка')
         .check_label('Ваше общее впечатление')
         .check_label('Текст отзыва')
         .check_field()
         )

    @pytest.mark.ui
    @allure.title("Проверка поля объекта отзыва")
    @allure.link("https://testit.example.com/tc-1")
    def test_field_review(self, otzovik_prereview_page):
        (otzovik_prereview_page
        .open()
        .entre_reveiw_name('Бумер')
        .check_entry_text('Бумер')
        )

    @pytest.mark.ui
    @allure.title("Проверка случайного фильма")
    @allure.link("https://testit.example.com/tc-1")
    def test_field_review_random(self, otzovik_prereview_page):
        (otzovik_prereview_page
        .open()
        .entre_reveiw_name('Фильм подарок с характером')
        .select_movies_gift_with_character()
        .check_review_headline('Фильм подарок с характером'))

    @pytest.mark.ui
    @allure.title("Проверка дополнительных полей в форме отзыва")
    @allure.link("https://testit.example.com/tc-1")
    def test_add_field_form_review(self, otzovik_review_page):
        (otzovik_review_page
        .open()
        .check_headline_info_your_review())







