import allure
import pytest
import random

from pages import playwright_product_page, playwright_cart_page


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

    def test_add_random_course_to_cart(self, courses_page, playwright_product_page, playwright_cart_page):
        (courses_page
         .open_page()
         .should_have_h1_title("Курсы")
         .open_random_course())

        product = playwright_product_page.get_product_info()

        random_qty = random.randint(1, 5)
        product["quantity"] = random_qty
        playwright_product_page.set_quantity_by_clicks(random_qty)

        playwright_product_page.click_buy()

        (playwright_cart_page
         .open_cart_from_alert()
         .verify_product_in_cart(product))
