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

    @staticmethod
    def get_gender_button(gender: str):
        locator = f"#{gender}"

        return locator

    @staticmethod
    def get_day_button(day: str):
        locator = f"#{day}"

        return locator
