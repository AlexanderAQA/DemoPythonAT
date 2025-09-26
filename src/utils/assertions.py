
def assert_is_equal(expected, actual):
    """Проверяем, что значения равны"""
    print(f"Проверяем, что значения равны")
    assert expected == actual, (f"Ожидаемое значение: '{expected}'\n"
                                f"НЕ совпадает с фактическим: '{actual}'")

def assert_is_empty(actual):
    """Проверяем, что фактическое значение - пустое"""
    print("Проверяем, что фактическое значение - пустое")
    assert actual == "", f"Ожидали пустое значение, но получили: '{actual}'!"
