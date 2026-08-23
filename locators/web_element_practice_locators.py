class WebElementPracticeLocators:
    """Локаторы учебной страницы"""

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
