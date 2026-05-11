import allure


class CommonAssertions:
    """Класс базовых проверок"""

    def __init__(self, page):
        self.parent_page = page

    def assert_is_equal(self, expected, actual):
        """Проверяем, что значения равны"""
        with allure.step(f"Проверяем, что значения равны"):
            assert expected == actual, (f"Ожидаемое значение: '{expected}'\n"
                                    f"НЕ совпадает с фактическим: '{actual}'")
            return self

    def assert_is_empty(self, actual):
        """Проверяем, что фактическое значение - пустое"""
        with allure.step("Проверяем, что фактическое значение - пустое"):
            assert actual == "", f"Ожидали пустое значение, но получили: '{actual}'!"

            return self

    def to_parent_page(self):
        """Возврат на родительскую страницу"""
        return self.parent_page