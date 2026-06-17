import allure
import pytest
class TestCart:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Добавление товара в корзину")
    @allure.link("https://testit.example.com/tc-cart-add")
    def test_post_checkout_cart_add(self, api_client):

        product_id = 189
        quantity = 1

        expected_text_part = "добавлен"
        expected_product_link = "https://shop.finarty.ru/189"
        expected_cart_link = "https://shop.finarty.ru/cart"

        response_data, status_code = api_client.add_product_to_cart(
            product_id=product_id,
            quantity=quantity
        )
        actual_message = response_data.get("html") or response_data.get("success", "")
        assert status_code == 200, f"Status code is not 200, got {status_code}"

        assert actual_message, "Response message is empty"

        assert expected_text_part in actual_message, f"Text '{expected_text_part}' not found in: {actual_message}"
        assert expected_product_link in actual_message, f"Link '{expected_product_link}' not found in: {actual_message}"
        assert expected_cart_link in actual_message, f"Link '{expected_cart_link}' not found in: {actual_message}"
