from telnetlib import EC
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.account_page_locators import AccountPageLocators


class CommonAssertions:
    """Класс базовых проверок"""

    # Локаторы


    def __init__(self, page):
        self.account_header = None
        self.driver = None
        self.logger = None
        self.parent_page = page

    def assert_is_equal(self, expected, actual):
        """Проверяем, что значения равны"""
        print(f"Проверяем, что значения равны")
        assert expected == actual, (f"Ожидаемое значение: '{expected}'\n"
                                    f"НЕ совпадает с фактическим: '{actual}'")
        return self

    def assert_is_empty(self, actual):
        """Проверяем, что фактическое значение - пустое"""
        print("Проверяем, что фактическое значение - пустое")
        assert actual == "", f"Ожидали пустое значение, но получили: '{actual}'!"

        return self

    def to_parent_page(self):
        """Возврат на родительскую страницу"""
        return self.parent_page