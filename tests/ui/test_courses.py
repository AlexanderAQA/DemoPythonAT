import allure
import pytest


@allure.epic("Раздел 'Курсы'")
class TestCoursesPage:

    @pytest.mark.ui
    @allure.title("Переход в раздел 'Курсы'")
    @allure.link("https://testit.example.com/tc-2281")
    def test_open_courses_page(self, courses_page):
        (courses_page
         .open_page()
         .should_have_partial_url(courses_page.COURSES_PATH)
         .should_have_title("Курсы в интернет-магазине Finarty")
         .should_have_h1_title("Курсы")
         .assert_items_count(4)
         .assert_course_items())
