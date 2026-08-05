import re
from playwright.sync_api import expect
from pages.playwright_base_page import PlaywrightBasePage


class ProductPage(PlaywrightBasePage):

    def get_product_info(self) -> dict:
        self.logger.info("Собираем информацию о товаре")

        name = self.page.locator("h1.mb-3").inner_text().strip()

        article_li = self.page.locator("li", has_text="Артикул:")
        article = article_li.locator("b").inner_text().strip()

        price_text = self.page.locator("span.price-new").inner_text()
        price = float(re.sub(r'[^\d.]', '', price_text))

        product_data = {
            "name": name,
            "article": article,
            "price": price,
            "quantity": 1
        }

        self.logger.info(f"Товар: {product_data}")
        return product_data

    def set_quantity_by_clicks(self, target_quantity: int):
        self.logger.info(f"Выбор количества: {target_quantity} кликом по +")

        plus_button = self.page.locator("span.bt_plus")
        clicks_needed = target_quantity - 1

        for _ in range(clicks_needed):
            plus_button.click()
            self.page.wait_for_timeout(200)  # для паузы между кликами

        qty_input = self.page.locator("input.quantity")
        expect(qty_input).to_have_value(str(target_quantity))

        return self

    def click_buy(self):
        self.logger.info("Нажимаем кнопку 'Купить'")
        self.page.locator("#button-cart").click()
        return self
