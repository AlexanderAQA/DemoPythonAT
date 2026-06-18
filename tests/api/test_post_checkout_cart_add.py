import allure
import pytest

@allure.epic("API")
@allure.story("Корзина товаров")

class TestCart:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Добавление товара в корзину")
    @allure.link("https://testit.example.com/tc-cart-add")
    def test_post_checkout_cart_add(self, api_client):

        product_id = 189
        quantity = 1

        expected_text = ('<a href="https://shop.finarty.ru/189">3 в 1: три книги Яна Арта из серии «Библиотека '
                         'Finversia»</a> добавлен <a href="https://shop.finarty.ru/cart">в корзину покупок</a>!')

        response_data, status_code = api_client.add_product_to_cart(
            product_id=product_id,
            quantity=quantity
        )
        actual_message = response_data.get("success", "")
        (api_client.assertions
         .assert_text_match(expected_text, actual_message)
         .assert_is_equal(200, status_code))
