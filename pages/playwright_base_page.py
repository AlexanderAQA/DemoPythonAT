import re

import allure
from playwright.sync_api import Page, expect

from src.utils.assertions import CommonAssertions
from src.utils.logger import get_logger


class PlaywrightBasePage:

    PLUS_BUTTON = "span.bt_plus"
    QTY_INPUT = "input.quantity"
    BUY_BUTTON = "#button-cart"

    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(__name__)
        self.BASE_URL = 'https://shop.finarty.ru'
        self.asserts = CommonAssertions(self)


    def allure_and_logger(self, text):
        with allure.step(text):
            self.logger.info(text)
        return self

    def open(self, url: str):
        self.logger.info(f"Открываем страницу: '{url}'")
        self.page.goto(url)
        self.accept_chrome_cookies(self.page)
        self.accept_cookie(self.page)
        return self

    def open_with_response(self, url: str):
        """Открывает URL и возвращает ответ на основной запрос страницы."""
        self.logger.info(f"Открываем страницу и получаем ответ: '{url}'")
        return self.page.goto(url)

    def accept_chrome_cookies(self, page):
        self.logger.info("Принимаем куки в хром браузере")
        button = page.get_by_role("button", name="Принять все")

        if button.is_visible():
            button.click()

        return self

    def accept_cookie(self, page):
        self.logger.info("Принимаем куки на сайте")
        cookie_btn = page.get_by_role("button", name="ОК")
        if cookie_btn.is_visible():
            cookie_btn.click()

        return self

    def should_have_title(self, expected_title):
        self.logger.info(f"Проверяем, что в заголовке есть '{expected_title}'")
        expect(self.page).to_have_title(
            expected_title
        )
        return self

    def should_have_partial_url(self, path_url):
        self.logger.info(f"CoursesPage: проверяем что в url содержится '{path_url}'")
        expect(self.page).to_have_url(
            re.compile(fr".*{path_url}")
        )
        return self

    def should_have_text(self, expected_text: str):
        """Проверяет, что указанный текст отображается на странице."""
        self.logger.info(f"Проверяем отображение текста: '{expected_text}'")
        text_elements = self.page.get_by_text(expected_text, exact=True)

        for index in range(text_elements.count()):
            text_element = text_elements.nth(index)
            if text_element.is_visible():
                expect(text_element).to_be_visible()
                return self

        raise AssertionError(f"Текст '{expected_text}' не отображается на странице")

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

        plus_button = self.page.locator(self.PLUS_BUTTON)
        clicks_needed = target_quantity - 1

        for _ in range(clicks_needed):
            plus_button.click()
            self.page.wait_for_timeout(200)  # для паузы между кликами

        qty_input = self.page.locator(self.QTY_INPUT)
        expect(qty_input).to_have_value(str(target_quantity))

        return self

    def click_buy(self):
        self.logger.info("Нажимаем кнопку 'Купить'")
        self.page.locator(self.BUY_BUTTON).click()
        return self

    def open_product(self, name):
        self.logger.info("Открыть карточку конкретного товара по названию")
        self.page.get_by_text(name).click()

        return self

    def get_field_value(self, locator):
        """Возвращает значение текстового поля по локатору"""
        return self.page.locator(locator).input_value()

    def check_text_result(self, text):
        self.logger.info("Проверка текста в уведомлении при отправке")
        result = self.page.get_by_text(text)
        expect(result).to_be_visible()
        return self

    def assert_is_visible(self, locator):
        self.logger.info(f"Проверяем, что элемент '{locator}' виден")
        expect(self.page.locator(locator)).to_be_visible()
        return self
