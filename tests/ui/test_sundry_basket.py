import allure
import pytest


@allure.epic("Всякая всячина")
class TestBasketPage:

    @pytest.mark.ui
    @allure.title("Товары в корзине из раздела Всякая всячина")
    @allure.link("https://testit.example.com/tc-1")
    def test_sundry_basket(self, main_page, sundry_page, base_page, cart_page):
        (main_page
            .open_main_page()
            .accept_cookies()
            .click_sundry_link())

        item_name = "Футболка «1001 секунда об экономике. От Я до А»-1 (черная)"

        (sundry_page
          .scroll_to_item(item_name)
          .click_buy_button(item_name)
          .click_product_in_cart_button()
          .click_go_to_cart_button())

        (cart_page
          .assert_quantity(1)
          .check_price(price))