from tests.conftest import driver
from tests.pages.base_page import BasePage
from tests.web_elements_tests.test_web_elements import *

# TODO: Модуль 14. Детали Selenium и Практика


# 1.1 Неявное - имплицитное ожидание.
driver()

# 1.2 Явное ожидание (конкретного условия или элемента)
test_long_loading()

# 1.3 Работа с чек-боксами, раскрытием и скрытием дерева (иерархических узлов)
test_web_elements()

# 2. ActionChains
# 2.1 Двойной клик (левой кнопкой мыши)
test_double_click()

# 2.2 Клик правой кнопкой мыши
test_right_click()

# 3. Взаимодействие с календарем
test_calendar()

# 4. Взаимодействие с DropDown (Выпадающий список)
test_select_dropdown()

# 5. Обработка исключений в автотестах
BasePage.click()


