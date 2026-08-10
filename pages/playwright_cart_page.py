from playwright.sync_api import expect
from pages.playwright_base_page import PlaywrightBasePage


class CartPage(PlaywrightBasePage):
    CART_PATH = "/cart"

    def open_cart_from_alert(self):
        self.logger.info("Уведомление и клик на текст 'в корзину покупок'")
        self.page.get_by_text("в корзину покупок").click(force=True)

        self.should_have_partial_url(self.CART_PATH)
        return self

    def verify_product_name(self, product_data: dict):
        self.page.wait_for_load_state("networkidle")
        cart_item = self.page.locator("tbody tr:visible", has_text=product_data["name"]).first
        item_text = cart_item.inner_text()
        self.asserts.assert_text_match(product_data["name"], item_text)
        return self

    def verify_product_article(self, product_data: dict):
        cart_item = self.page.locator("tbody tr:visible", has_text=product_data["name"]).first
        item_text = cart_item.inner_text()
        self.asserts.assert_text_match(product_data["article"], item_text)
        return self

    def verify_product_quantity(self, product_data: dict):
        qty_locator = self.page.locator('input[name="quantity"]')
        expect(qty_locator).to_have_value(str(product_data["quantity"]))
        return self

    def verify_product_price(self, product_data: dict):
        cart_item = self.page.locator("tbody tr:visible", has_text=product_data["name"]).first
        total_price = product_data["price"] * product_data["quantity"]
        expected_price_text = f"{total_price:,.0f}".replace(',', ' ')
        price_locator = cart_item.locator("td.text-end, .product-total").last
        expect(price_locator).to_contain_text(expected_price_text)
        return self
