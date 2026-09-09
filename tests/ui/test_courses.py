import allure
import pytest
import random

from src.utils.test_data import COURSES, work_with_price


@allure.epic("Раздел 'Курсы'")
class TestCoursesPage:

    @pytest.mark.ui
    @pytest.mark.negative
    @allure.title("Несуществующая страница курса возвращает 404")
    def test_nonexistent_course_page_returns_404(self, courses_page):
        nonexistent_course_url = (
            f"{courses_page.BASE_URL}{courses_page.COURSES_PATH}"
            "/course-does-not-exist"
        )
        response = courses_page.open_with_response(nonexistent_course_url)

        (courses_page.asserts
         .assert_is_not_empty(response)
         .assert_is_equal(404, response.status))

        courses_page.should_have_text("Запрашиваемая страница не найдена!")

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

    def test_add_random_course_to_cart(self, courses_page, playwright_cart_page):
        product = random.choice(COURSES)

        random_qty = random.randint(1, 5)

        (courses_page
         .open_page()
         .open_product(product.name))

        product_info = courses_page.get_product_info()
        product_info["quantity"] = random_qty

        (playwright_cart_page
         .set_quantity_by_clicks(random_qty)
         .click_buy()
         .open_cart_from_alert()
         .verify_product_name(product_info)
         .verify_product_article(product_info)
         .verify_product_quantity(product_info)
         .verify_product_price(product_info))
