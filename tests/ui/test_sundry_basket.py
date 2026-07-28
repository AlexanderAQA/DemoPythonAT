import allure
import pytest
import random
from pages.base_page import work_with_price


@allure.epic("Всякая всячина")
class TestBasketPage:

    @pytest.mark.ui
    @allure.title("Товары в корзине из раздела Всякая всячина")
    @allure.link("https://testit.example.com/tc-1")
    def test_sundry_basket(self, main_page, sundry_page, cart_page):
        item_name = "Футболка «1001 секунда об экономике. От Я до А»-1 (черная)"
        unit_price = 2800
        random_qty = random.randint(1, 5)
        expected_total = work_with_price(unit_price, random_qty)

        (main_page
         .open_main_page()
         .accept_cookies()
         .click_sundry_link())

        (sundry_page
         .scroll_to_item(item_name)
         .click_buy_button(item_name))

        (sundry_page
         .select_random_sex()
         .select_random_size()
         .set_quantity(random_qty)
         .click_add_to_cart())

        (cart_page
         .assert_quantity(random_qty)
         .check_price(expected_total))
