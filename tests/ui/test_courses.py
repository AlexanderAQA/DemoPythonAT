import allure
import pytest
import random

from src.utils.test_data import COURSES, work_with_price


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

    def test_add_random_course_to_cart(self, courses_page, playwright_cart_page):
        product = random.choice(COURSES)

        random_qty = random.randint(1, 5)
        expected_total = work_with_price(product.price, random_qty)


        (courses_page
         .open_page()
         .open_product(product.name))

        product_info = courses_page.get_product_info()

        (playwright_cart_page
         .set_quantity_by_clicks(random_qty)
         .click_buy()
         .open_cart_from_alert()
         .verify_product_in_cart(product_info))
