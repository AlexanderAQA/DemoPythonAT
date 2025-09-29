class CommonAssertions:
    """Класс базовых проверок"""

    def __init__(self, page):
        self.parent_page = page

    def assert_is_equal(self, expected, actual):
        """Проверяем, что значения равны"""
        print(f"Проверяем, что значения равны")
        assert expected == actual, (f"Ожидаемое значение: '{expected}'\n"
                                    f"НЕ совпадает с фактическим: '{actual}'")
        return self.parent_page

    def assert_is_empty(self, actual):
        """Проверяем, что фактическое значение - пустое"""
        print("Проверяем, что фактическое значение - пустое")
        assert actual == "", f"Ожидали пустое значение, но получили: '{actual}'!"

        return self.parent_page
