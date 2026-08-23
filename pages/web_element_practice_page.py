from pages.playwright_base_page import PlaywrightBasePage
from locators.web_element_practice_locators import WebElementPracticeLocators as Practice
from playwright.sync_api import expect
from datetime import datetime, timedelta


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

    def select_colors(self, colors_list: list):
        self.logger.info(f"Выбор цветов: {colors_list}")
        self.page.locator(Practice.COLORS_LISTBOX).select_option(value=colors_list)
        return self

    def assert_colors_selected(self, colors_list: list):
        self.logger.info(f"Проверка, что цвета {colors_list} выбраны")
        for color in colors_list:
            selected_option = self.page.locator(f"{Practice.COLORS_LISTBOX} option[value='{color}']:checked")
            expect(selected_option).to_have_count(1)
        return self

    def select_animal(self, animal: str):
        self.logger.info(f"Выбор животного: {animal}")
        self.page.locator(Practice.ANIMALS_LISTBOX).select_option(value=animal)
        return self

    def assert_animal_selected(self, animal: str):
        self.logger.info(f"Проверка, что животное {animal} выбрано")
        selected_option = self.page.locator(f"{Practice.ANIMALS_LISTBOX} option[value='{animal}']:checked")
        expect(selected_option).to_have_count(1)
        return self

    def select_date_from_calendar(self, input_locator: str, target_date: datetime):
        self.logger.info(f"Выбор даты через календарь: {target_date.strftime('%m/%d/%Y')}")

        self.page.locator(input_locator).click()
        self.page.wait_for_timeout(500)

        current_month_text, current_year_text = self.get_current_calendar_date()
        self.logger.info(f"Текущий месяц в календаре: {current_month_text} {current_year_text}")

        current_date = datetime.strptime(f"{current_month_text} {current_year_text}", "%B %Y")
        target_month_year = datetime(target_date.year, target_date.month, 1)

        while current_date < target_month_year:
            self.page.locator(Practice.CALENDAR_NEXT_MONTH).click()
            self.page.wait_for_timeout(200)
            current_month_text, current_year_text = self.get_current_calendar_date()
            current_date = datetime.strptime(f"{current_month_text} {current_year_text}", "%B %Y")

        while current_date > target_month_year:
            self.page.locator(Practice.CALENDAR_PREV_MONTH).click()
            self.page.wait_for_timeout(200)
            current_month_text, current_year_text = self.get_current_calendar_date()
            current_date = datetime.strptime(f"{current_month_text} {current_year_text}", "%B %Y")

        day_str = str(target_date.day)
        self.page.locator(f"td[data-handler='selectDay'] a[data-date='{day_str}']").click()

        self.page.locator("body").click(position={"x": 10, "y": 10})
        self.page.wait_for_timeout(300)

        return self

    def get_current_calendar_date(self) -> tuple[str, str]:
        """
        Определяет текущий месяц и год в открытом календаре"""
        month_locator = self.page.locator(Practice.CALENDAR_MONTH_TITLE).first
        year_locator = self.page.locator(Practice.CALENDAR_YEAR_TITLE).first
        tag_name = month_locator.evaluate("el => el.tagName.toLowerCase()")

        if tag_name == "select":
            month_text = month_locator.locator("option[selected]").text_content().strip()
            year_text = year_locator.locator("option[selected]").text_content().strip()
        else:
            month_text = month_locator.text_content().strip()
            year_text = year_locator.text_content().strip()

        month_mapping = {
            "Jan": "January", "Feb": "February", "Mar": "March",
            "Apr": "April", "May": "May", "Jun": "June",
            "Jul": "July", "Aug": "August", "Sep": "September",
            "Oct": "October", "Nov": "November", "Dec": "December"
        }

        if month_text in month_mapping:
            month_text = month_mapping[month_text]

        return month_text, year_text

    def fill_native_date(self, input_locator: str, target_date: datetime):
        """Для заполнения input type=date в формате YYYY-MM-DD"""
        date_str = target_date.strftime("%Y-%m-%d")
        self.logger.info(f"Заполнить дату: {date_str}")
        self.page.locator(input_locator).fill(date_str)
        return self
