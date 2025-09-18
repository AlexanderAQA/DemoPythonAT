
def assert_is_equal(expected, actual):
    """Проверяем что значения равны"""
    try:
        assert expected == actual, (f"Проверяем, что ожидаемое значение: '{expected}',"
                                    f" совпадает с фактическим: '{actual}'")
    except TypeError as e:
        print(f"TypeError: {e}")

def assert_is_empty(element):
    """Проверяем что значение веб элемента пустое"""
    value = element.get_attribute("value")
    assert value == "", f"Поле не пустое! Его значение: '{value}'"