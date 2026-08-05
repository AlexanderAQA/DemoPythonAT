from playwright.sync_api import expect
from pages.playwright_base_page import PlaywrightBasePage

import random


class CoursesPage(PlaywrightBasePage):
    COURSES_PATH = "/kursy"

    def open_page(self):
        url = self.BASE_URL + self.COURSES_PATH
        self.open(url)
        return self

    def should_have_h1_title(self, expected_title):
        self.logger.info("Проверяем что есть заголовок h1")
        expect(self.page.locator("h1")).to_have_text(expected_title)
        return self

    def assert_items_count(self, expected_count):
        self.logger.info("Проверяем количество карточек товаров")
        cards = self.page.locator(".product-thumb")

        expect(cards).to_have_count(expected_count)
        return self

    def assert_course_items(self):
        cards = self.page.locator(".product-thumb")
        self.logger.info("Проверяем каждую карточку\n")
        for num, card in enumerate(cards.all(), start=1):
            self.logger.info(f"Карточка №{num}")

            self.logger.info("Картинка")
            expect(
                card.locator(".img-fluid")
            ).to_be_visible()

            product_name = card.locator(".img-fluid").get_attribute("title")
            self.logger.info(f"Название: {product_name}")
            assert product_name is not None, "Атрибут title отсутствует"
            assert product_name.strip() != "", "Атрибут title пустой"


            self.logger.info("Цена")
            price = card.locator(".price-new")

            expect(price).to_be_visible()

            self.logger.info("Кнопка купить\n")
            buy_button = card.get_by_text("Купить")

            expect(
                buy_button
            ).to_be_visible()

        return self

    def open_random_course(self):
        self.logger.info("Клик на рандомную карточку курса и переход на страницу")
        cards = self.page.locator(".product-thumb")
        count = cards.count()
        assert count > 0, "На странице нет карточек курсов!"

        random_index = random.randint(0, count - 1)
        self.logger.info(f"Клик на случайную карточку №{random_index + 1}")

        cards.nth(random_index).locator("a").first.click()

        self.page.wait_for_load_state("domcontentloaded")
        return self
