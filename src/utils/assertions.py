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

    def assert_text_match(self, expected_text, actual_text):
        with allure.step("Проверка, что ожидаемый текст содержится в фактическом"):
            assert expected_text in actual_text, f"Text '{expected_text}' not found in: {actual_text}"

            return self

    def assert_symbol_length(self, expected_length, actual_text):
        with allure.step("Проверка количества букв и чисел в строке"):
            assert len(actual_text) == expected_length, "Количество символов не совпадает с ожидаемым"

            return self

    def assert_not_match(self, expected, actual):
        with allure.step("Проверка что текст не совпадает с фактическим"):
            assert expected not in actual, (
                f"Текст '{expected}' найден на странице, но не должен был там находиться."
            )

            return self
