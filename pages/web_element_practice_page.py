from pages.playwright_base_page import PlaywrightBasePage
from locators.web_element_practice_locators import WebElementPracticeLocators as Practice



class WebElementPracticePage(PlaywrightBasePage):
    WEB_ELEMENT_URL = 'https://testautomationpractice.blogspot.com/'

    def fill_name_field(self, name):
        self.logger.info("Заполняем поле Имя")
        self.page.locator(Practice.NAME_FIELD).fill(name)

        return self
