from pages.playwright_base_page import PlaywrightBasePage
from src.utils.logger import allure_and_logger
from playwright.sync_api import expect


class LenovoPage(PlaywrightBasePage):

    LENOVO_ACCEPT_COOKIES_BUTTON = "#_evidon-banner-acceptbutton"
    LENOVO_LOGO = "img[alt='Lenovo']"


    def accept_lenovo_cookies(self):
        allure_and_logger("Проверяет и принимает куки на сайте Lenovo если баннер есть")
        accept_cookie_btn = self.page.locator(self.LENOVO_ACCEPT_COOKIES_BUTTON)
        if accept_cookie_btn.is_visible():
           accept_cookie_btn.click()
        return self


    def assert_lenovo_logo_visible(self):
        allure_and_logger("Проверяет видимость логотипа Lenovo")
        expect(self.page.locator(self.LENOVO_LOGO)).to_be_visible()
        return self
