from pages.playwright_base_page import PlaywrightBasePage
from locators.web_element_practice_locators import WebElementPracticeLocators as Practice
import random
from src.utils.test_data import WebElementPractice
from playwright.sync_api import expect


class WebElementPracticePage(PlaywrightBasePage):
    WEB_ELEMENT_URL = 'https://testautomationpractice.blogspot.com/'

    def __init__(self, page, test_data: WebElementPractice = None):
        super().__init__(page)
        self.test_data = test_data if test_data is not None else WebElementPractice()

    def open_practice_page(self):
        self.logger.info(f"Открываем страницу {self.WEB_ELEMENT_URL}")
        self.page.goto(self.WEB_ELEMENT_URL)
        return self

    def close_google_popup(self):
        """Закрывает всплывающее окно выбора языка Google"""
        try:
            close_button = self.page.locator("button.VfPpkd-LgbsSe, .nJThJe, button[aria-label='Close']")
            if close_button.count() > 0 and close_button.first.is_visible(timeout=2000):
                self.logger.info("Закрываем всплывающее окно Google")
                close_button.first.click()
                self.page.wait_for_timeout(500)
        except Exception as e:
            self.logger.warning(f"Popup Google не найден или закрыт: {e}")

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
        self.logger.info("Заполняем поле Email")
        self.page.locator(Practice.ADDRESS_FIELD).fill(address)
        return self

    def select_gender(self, gender="random"):
        self.logger.info(f"Выбираем пол: {gender}")
        genders = self.test_data.genders

        if gender.lower() == "random":
            gender = random.choice(list(genders.keys()))

        locator, gender_name = genders[gender.lower()]
        self.page.locator(locator).check()
        self.logger.info(f"Выбран пол: {gender_name}")

        return gender, locator

    def select_random_days(self):
        self.logger.info("Выбираем дни недели")
        days_locators = [f"#{day}" for day in self.test_data.available_days]

        num_of_days = random.randint(1, min(3, len(days_locators)))
        selected_days = random.sample(days_locators, num_of_days)

        for day in selected_days:
            self.page.locator(day).check(force=True)

        self.logger.info(f"Выбраны дни: {selected_days}")
        return self

    def select_random_country(self):
        self.logger.info("Выбираем страну")
        random_country_value = random.choice(self.test_data.country_values)

        self.page.locator(Practice.COUNTRY_DROPDOWN).select_option(value=random_country_value)
        self.logger.info(f"Выбрана страна: {random_country_value}")
        return random_country_value

    def assert_is_checked(self, locator, element_name="Элемент"):
        self.logger.info(f"Проверяем, что {element_name} отмечен")
        expect(self.page.locator(locator)).to_be_checked()
        return self

    def assert_is_visible(self, locator, element_name="Элемент"):
        self.logger.info(f"Проверяем, что {element_name} виден")
        expect(self.page.locator(locator)).to_be_visible()
        return self

    def assert_element_exists(self, element_name="Элементы"):
        self.logger.info(f"Проверяем, что выбран {element_name}")
        days_locators = [f"#{day}" for day in self.test_data.available_days]
        checked_count = sum(
            1 for loc in days_locators
            if self.page.locator(loc).is_checked()
        )
        assert checked_count > 0, f"Не выбрано ни одного {element_name}!"
        return self

    def get_field_value(self, locator):
        """Возвращает значение текстового поля по локатору"""
        return self.page.locator(locator).input_value()

    def get_selected_country_value(self):
        """Возвращает значение выбранной страны из выпадающего списка"""
        return self.page.locator(Practice.COUNTRY_DROPDOWN).input_value()
