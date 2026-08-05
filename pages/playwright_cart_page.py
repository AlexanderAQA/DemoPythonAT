from playwright.sync_api import expect
from pages.playwright_base_page import PlaywrightBasePage


class CartPage(PlaywrightBasePage):
    CART_PATH = "/cart"

    def open_cart_from_alert(self):  # ← Отступ 4 пробела от class
        self.logger.info("Уведомление и клик на текст 'в корзину покупок'")
        self.page.get_by_text("в корзину покупок").click(force=True)

        self.should_have_partial_url(self.CART_PATH)
        return self

    def verify_product_in_cart(self, product_data: dict):
        self.logger.info(f"Проверка товара в корзине: {product_data['name']}")

        self.page.wait_for_load_state("networkidle")

        cart_item = self.page.locator("tbody tr:visible", has_text=product_data["name"]).first
        cart_item.wait_for(state="visible", timeout=10000)

        item_text = cart_item.inner_text()
        assert product_data["name"] in item_text
        assert product_data["article"] in item_text

        qty_locator = cart_item.locator("input[name^='quantity'], input.form-control").first
        expect(qty_locator).to_have_value(str(product_data["quantity"]))

        total_price = product_data["price"] * product_data["quantity"]
        # Форматирование числа с пробелами (36900 в "36 900")
        expected_price_text = f"{total_price:,.0f}".replace(',', ' ')
        price_locator = cart_item.locator("td.text-end, .product-total").last
        expect(price_locator).to_contain_text(expected_price_text)

        self.logger.info("Все параметры товара в корзине совпадают!")
        return self
