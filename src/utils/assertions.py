class CommonAssertions:
    """Класс базовых проверок"""
    def __init__(self, driver, parent_page):
        self.driver = driver
        self.parent_page = parent_page

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

    def assert_value_is_empty(self, element):
        """Проверяем, что значение веб элемента пустое"""
        # base_page = BasePage(self.driver)
        # value = base_page.get_element_text(element)
        value = self.to_base_page().get_element_text(element)
        self.assert_is_empty(value)
        return self

    def to_base_page(self):
        from pages.base_page import BasePage
        return BasePage(self.driver)

    def to_parent_page(self):
        return self.parent_page
