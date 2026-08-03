import allure
import pytest
import random
from src.utils.test_data import SUNDRY_TSHIRT_ECONOMICS


@allure.epic("Всякая всячина")
class TestBasketPage:

    @pytest.mark.ui
    @allure.title("Товары в корзине из раздела Всякая всячина")
    @allure.link("https://testit.example.com/tc-1")
    def test_sundry_basket(self, main_page, sundry_page, cart_page):
        product = SUNDRY_TSHIRT_ECONOMICS
        # product = random.choice(SUNDRY_PRODUCTS)

        random_qty = random.randint(1, 5)
        expected_total = main_page.work_with_price(product.price, random_qty)

        selected_sex = product.sex or sundry_page.random_choice(sundry_page.SEX_OPTIONS)
        selected_size = product.size or sundry_page.random_choice(sundry_page.SIZE_OPTIONS)

        (main_page
         .open_main_page()
         .accept_cookies()
         .click_sundry_link())

        (sundry_page
         .scroll_to_item(product.name)
         .click_buy_button(product.name))

        (sundry_page
         .select_sex(selected_sex)
         .select_size(selected_size)
         .set_quantity(random_qty)
         .click_add_to_cart())

        (cart_page
         .assert_quantity(random_qty)
         .check_size(selected_size)
         .check_sex(selected_sex)
         .check_price(expected_total))
