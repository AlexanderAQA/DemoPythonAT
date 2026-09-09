import allure

from pages.playwright_base_page import PlaywrightBasePage
from playwright.sync_api import expect
from datetime import datetime

class WebElementPracticePage(PlaywrightBasePage):
    WEB_ELEMENT_URL = 'https://testautomationpractice.blogspot.com/'
    
    NAME_FIELD = "#name"
    PHONE_FIELD = "#phone"
    EMAIL_FIELD = "#email"
    ADDRESS_FIELD = "textarea"
    GENDER_MALE = "#male"
    GENDER_FEMALE = "#female"
    DAY_SUNDAY = "#sunday"
    DAY_MONDAY = "#monday"
    DAY_TUESDAY = "#tuesday"
    DAY_FRIDAY = "#friday"
    DAY_SATURDAY = "#saturday"
    COUNTRY_DROPDOWN = "#country"
    SUBMIT_BUTTON = "button.submit-btn"
    CLOSE_GOOGLE_POPUP = "button[aria-label='Close']"
    RESULT_MESSAGE = "#result.result"
    COLORS_LISTBOX = "#colors"
    ANIMALS_LISTBOX = "#animals"
    DATE_PICKER_1 = "#datepicker"
    DATE_PICKER_2 = "#txtDate"
    DATE_PICKER_3_START = "input[placeholder='Start Date']"
    DATE_PICKER_3_END = "input[placeholder='End Date']"
    CALENDAR_NEXT_MONTH = ".ui-datepicker-next"
    CALENDAR_PREV_MONTH = ".ui-datepicker-prev"
    CALENDAR_MONTH_TITLE = ".ui-datepicker-month"
    CALENDAR_YEAR_TITLE = ".ui-datepicker-year"

    @staticmethod
    def get_gender_button(gender: str):
        locator = f"#{gender}"

        return locator

    @staticmethod
    def get_day_button(day: str):
        locator = f"#{day}"

        return locator


    def open_practice_page(self):
        self.logger.info(f"Открываем страницу {self.WEB_ELEMENT_URL}")
        self.page.goto(self.WEB_ELEMENT_URL)
        return self

    def close_google_popup(self):
        """Закрывает всплывающее окно выбора языка Google"""
        try:
            close_button = self.page.locator(self.CLOSE_GOOGLE_POPUP)
            close_button.wait_for(state="visible", timeout=2000)
            self.logger.info("Закрываем всплывающее окно Google")
            close_button.click()
            self.page.wait_for_timeout(300)
        except Exception:
            self.logger.warning("Popup Google не появился или уже закрыт")
        return self

    def fill_name_field(self, name):
        self.logger.info("Заполняем поле Имя")
        self.page.locator(self.NAME_FIELD).fill(name)
        return self

    def fill_email_field(self, email):
        self.logger.info("Заполняем поле Email")
        self.page.locator(self.EMAIL_FIELD).fill(email)
        return self

    def assert_field_is_invalid(self, locator: str):
        """Проверяет, что поле не проходит встроенную HTML-валидацию."""
        self.logger.info(f"Проверяем, что поле '{locator}' невалидно")
        is_valid = self.page.locator(locator).evaluate(
            "element => element.checkValidity()"
        )
        assert not is_valid, f"Поле '{locator}' должно быть невалидным"
        return self

    def fill_phone_field(self, phone):
        self.logger.info("Заполняем поле Phone")
        self.page.locator(self.PHONE_FIELD).fill(phone)
        return self

    def fill_address_field(self, address):
        self.logger.info("Заполняем поле Address")
        self.page.locator(self.ADDRESS_FIELD).fill(address)
        return self

    def select_gender(self, gender: str):
        self.logger.info(f"Выбираем пол: {gender}")
        gender_locator = self.get_gender_button(gender)
        self.page.locator(gender_locator).check()
        return self

    def select_days(self, days_list: list):
        self.logger.info(f"Выбираем дни недели: {days_list}")
        for day in days_list:
            self.page.locator(self.get_day_button(day)).check()
        return self

    def select_country(self, country: str):
        self.logger.info(f"Выбираем страну: {country}")
        self.page.locator(self.COUNTRY_DROPDOWN).select_option(value=country)
        return self

    def get_selected_country_value(self):
        return self.get_field_value(self.COUNTRY_DROPDOWN)

    def click_submit(self):
        self.logger.info("Нажимаем кнопку Submit")
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.locator(self.SUBMIT_BUTTON).click()
        return self

    def assert_is_checked(self, locator):
        self.logger.info(f"Проверяем, что элемент '{locator}' отмечен")
        expect(self.page.locator(locator)).to_be_checked()
        return self

    def select_colors(self, colors_list: list):
        self.logger.info(f"Выбор цветов: {colors_list}")
        self.page.locator(self.COLORS_LISTBOX).select_option(value=colors_list)
        return self

    def assert_colors_selected(self, colors_list: list):
        self.logger.info(f"Проверка, что цвета {colors_list} выбраны")
        for color in colors_list:
            selected_option = self.page.locator(f"{self.COLORS_LISTBOX} option[value='{color}']:checked")
            expect(selected_option).to_have_count(1)
        return self

    def select_animal(self, animal: str):
        self.logger.info(f"Выбор животного: {animal}")
        self.page.locator(self.ANIMALS_LISTBOX).select_option(value=animal)
        return self

    def assert_animal_selected(self, animal: str):
        self.logger.info(f"Проверка, что животное {animal} выбрано")
        selected_option = self.page.locator(f"{self.ANIMALS_LISTBOX} option[value='{animal}']:checked")
        expect(selected_option).to_have_count(1)
        return self

    def select_future_date_1(self, future_date_1):
        self.select_date_from_calendar(self.DATE_PICKER_1, future_date_1)
        return self

    def select_future_date_2(self, future_date_2):
        self.select_date_from_calendar(self.DATE_PICKER_2, future_date_2)
        return self

    def select_end_date(self, end_date):
        self.fill_native_date(self.DATE_PICKER_3_END, end_date)
        return self

    def select_start_date(self, start_date):
        self.fill_native_date(self.DATE_PICKER_3_START, start_date)
        return self

    def select_date_from_calendar(self, input_locator: str, target_date: datetime):
        self.logger.info(f"Выбор даты через календарь: {target_date.strftime('%m/%d/%Y')}")

        self.page.locator(input_locator).click()
        self.page.wait_for_timeout(500)

        current_month_text, current_year_text = self.get_current_calendar_date()
        self.logger.info(f"Текущий месяц в календаре: {current_month_text} {current_year_text}")

        current_date = datetime.strptime(f"{current_month_text} {current_year_text}", "%B %Y")

        month_diff = (
                (target_date.year - current_date.year) * 12
                + target_date.month - current_date.month
        )

        month_locator = (
            self.CALENDAR_NEXT_MONTH
            if month_diff > 0
            else self.CALENDAR_PREV_MONTH
        )

        for _ in range(abs(month_diff)):
            self.page.locator(month_locator).click()

        day_str = str(target_date.day)
        self.page.locator(f"td[data-handler='selectDay'] a[data-date='{day_str}']").click()

        return self

    def get_current_calendar_date(self) -> tuple[str, str]:
        """
        Определяет текущий месяц и год в открытом календаре"""
        month_locator = self.page.locator(self.CALENDAR_MONTH_TITLE).first
        year_locator = self.page.locator(self.CALENDAR_YEAR_TITLE).first
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

    @allure.step("Проверка наличия полей и кнопок")
    def assert_form(self):
        self.logger.info(f"Проверка наличия полей и кнопок")
        self.assert_is_visible(self.NAME_FIELD)
        self.assert_is_visible(self.EMAIL_FIELD)
        self.assert_is_visible(self.PHONE_FIELD)
        self.assert_is_visible(self.ADDRESS_FIELD)
        self.assert_is_visible(self.COUNTRY_DROPDOWN)
        self.assert_is_visible(self.COLORS_LISTBOX)
        self.assert_is_visible(self.ANIMALS_LISTBOX)

        return self

    def assert_test_user_name(self, user_name):
        self.asserts.assert_is_equal(user_name, self.get_field_value(self.NAME_FIELD))
        return self

    def assert_test_user_email(self, user_email):
        self.asserts.assert_is_equal(user_email, self.get_field_value(self.EMAIL_FIELD))
        return self

    def assert_test_user_phone(self, phone):
        self.asserts.assert_is_equal(phone, self.get_field_value(self.PHONE_FIELD))
        return self

    def assert_test_address(self, address):
        self.asserts.assert_is_equal(address, self.get_field_value(self.ADDRESS_FIELD))
        return self

    def assert_check_gender(self, gender):
        self.assert_is_checked(self.get_gender_button(gender))
        return self

    def assert_check_day(self, day):
        self.assert_is_checked(self.get_day_button(day))
        return self

    def assert_check_date_1(self, date):
        self.asserts.assert_is_equal(date, self.get_field_value(self.DATE_PICKER_1))
        return self

    def assert_check_date_2(self, date):
        self.asserts.assert_is_equal(date, self.get_field_value(self.DATE_PICKER_2))
        return self

    def assert_check_start_date(self, date):
        self.asserts.assert_is_equal(date, self.get_field_value(self.DATE_PICKER_3_START))
        return self

    def assert_check_end_date(self, date):
        self.asserts.assert_is_equal(date, self.get_field_value(self.DATE_PICKER_3_END))
        return self

