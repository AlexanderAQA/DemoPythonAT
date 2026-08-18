from pages.playwright_base_page import PlaywrightBasePage
from locators.web_element_practice_locators import WebElementPracticeLocators as Practice
from playwright.sync_api import expect


class WebElementPracticePage(PlaywrightBasePage):
    WEB_ELEMENT_URL = 'https://testautomationpractice.blogspot.com/'

    def open_practice_page(self):
        self.logger.info(f"Открываем страницу {self.WEB_ELEMENT_URL}")
        self.page.goto(self.WEB_ELEMENT_URL)
        return self

    def close_google_popup(self):
        """Закрывает всплывающее окно выбора языка Google"""
        try:
            close_button = self.page.locator(Practice.CLOSE_GOOGLE_POPUP)
            close_button.wait_for(state="visible", timeout=2000)
            self.logger.info("Закрываем всплывающее окно Google")
            close_button.click()
            self.page.wait_for_timeout(300)
        except Exception:
            self.logger.warning("Popup Google не появился или уже закрыт")
        return self

    def fill_name_field(self, name):
        self.logger.info("Заполняем поле Имя")
        self.page.locator(Practice.NAME_FIELD).fill(name)
        return self

    def fill_email_field(self, email):
        self.logger.info("Заполняем поле Email")
        self.page.locator(Practice.EMAIL_FIELD).fill(email)
        return self

    def fill_phone_field(self, phone):
        self.logger.info("Заполняем поле Phone")
        self.page.locator(Practice.PHONE_FIELD).fill(phone)
        return self

    def fill_address_field(self, address):
        self.logger.info("Заполняем поле Address")   # <-- было "Email", стало "Address"
        self.page.locator(Practice.ADDRESS_FIELD).fill(address)
        return self

    def select_gender(self, gender: str):
        self.logger.info(f"Выбираем пол: {gender}")
        gender_locator = Practice.get_gender_button(gender)
        self.page.locator(gender_locator).check()
        return self

    def select_days(self, days_list: list):
        self.logger.info(f"Выбираем дни недели: {days_list}")
        for day in days_list:
            self.page.locator(Practice.get_day_button(day)).check()
        return self

    def select_country(self, country: str):
        self.logger.info(f"Выбираем страну: {country}")
        self.page.locator(Practice.COUNTRY_DROPDOWN).select_option(value=country)
        return self

    def get_selected_country_value(self):
        return self.get_field_value(Practice.COUNTRY_DROPDOWN)

    def click_submit(self):
        self.logger.info("Нажимаем кнопку Submit")
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.locator(Practice.SUBMIT_BUTTON).click()
        return self

    def assert_is_checked(self, locator):
        self.logger.info(f"Проверяем, что элемент '{locator}' отмечен")
        expect(self.page.locator(locator)).to_be_checked()
        return self

    def assert_is_visible(self, locator):
        self.logger.info(f"Проверяем, что элемент '{locator}' виден")
        expect(self.page.locator(locator)).to_be_visible()
        return self

