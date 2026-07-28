import re
from playwright.sync_api import Page, expect
from src.utils.logger import get_logger


class PlaywrightBasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(__name__)
        self.BASE_URL = 'https://shop.finarty.ru'

    def open(self, url: str):
        self.logger.info(f"Открываем страницу: '{url}'")
        self.page.goto(url)
        self.accept_chrome_cookies(self.page)
        self.accept_cookie(self.page)
        return self

    def accept_chrome_cookies(self, page):
        self.logger.info("Принимаем куки в хром браузере")
        button = page.get_by_role("button", name="Принять все")

        if button.is_visible():
            button.click()

        return self

    def accept_cookie(self, page):
        self.logger.info("Принимаем куки на сайте")
        page.get_by_role("button", name="ОК").click()
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
