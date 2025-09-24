
def assert_is_equal(expected, actual):
    """Проверяем что значения равны"""
    assert expected == actual, (f"Ожидаемое значение: '{expected}'\n"
                                f"НЕ совпадает с фактическим: '{actual}'")

def assert_is_empty(element):
    """Проверяем что значение веб элемента пустое"""
    value = element.get_attribute("value")
    assert value == "", f"Поле не пустое! Его значение: '{value}'"