from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonAssertions:
    """Класс базовых проверок"""

    # Локаторы
    exit_button = (By.XPATH, "//div[contains(@class,'list-group')]//a[normalize-space()='Выход']")

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

    def assert_account_header(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.account_header)
        )
        return self

    def assert_logged_in(self, timeout: int = 10):
        return (self.is_element_visible(self.account_header, timeout) and
                self.is_element_visible(self.exit_button, timeout))