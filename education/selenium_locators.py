"""
ПАМЯТКА: ЛОКАТОРЫ В SELENIUM + PYTHON
======================================

Главный упор: ID и XPath.
"""

from selenium.webdriver.common.by import By


# ============================================================
# 1. БАЗОВЫЙ ШАБЛОН
# ============================================================

# ID
driver.find_element(By.ID, "email")

# XPath
driver.find_element(By.XPATH, "//input[@id='email']")
locator = By.XPATH, "//label[text()='Name:']"
locator = (By.ID, "name")


# ============================================================
# 2. ID — ПЕРВЫЙ ВАРИАНТ, ЕСЛИ ОН СТАБИЛЬНЫЙ
# ============================================================

# HTML:
# <input id="email" type="email">

email = (By.ID, "email")

# Использование:
driver.find_element(*email).send_keys("user@example.com")


# Если ID уникальный и постоянный — это обычно самый простой локатор.
#
# Хорошо:
#   id="email"
#   id="login-button"
#   id="checkout"
#
# Осторожно:
#   id="input-849372"
#   id="element-123456789"
#
# Если значение ID генерируется динамически, лучше искать другой
# стабильный атрибут.


# ============================================================
# 3. ПРОВЕРКА ID В DEVTOOLS
# ============================================================

# В Chrome DevTools -> Console:
#
# document.getElementById("email")
#
# Если элемент найден — браузер вернет элемент.
#
# Для проверки количества:
#
# document.querySelectorAll("#email")
#
# Идеально: найден ровно один элемент.


# ============================================================
# 4. ОСНОВЫ XPATH
# ============================================================

# HTML:
# <input id="email">

# По ID:
xpath_1 = (By.XPATH, "//input[@id='email']")

# Если тег не важен:
xpath_2 = (By.XPATH, "//*[@id='email']")


# HTML:
# <button id="login-button">Войти</button>

xpath_3 = (By.XPATH, "//button[@id='login-button']")


# ============================================================
# 5. XPATH ПО ЛЮБОМУ АТРИБУТУ
# ============================================================

# HTML:
# <input name="email">

(By.XPATH, "//input[@name='email']")

# HTML:
# <input type="email">

(By.XPATH, "//input[@type='email']")

# HTML:
# <button data-testid="login-button">

(By.XPATH, "//button[@data-testid='login-button']")


# ============================================================
# 6. НЕСКОЛЬКО УСЛОВИЙ В XPATH
# ============================================================

# HTML:
# <input id="email" name="email" type="text">

(By.XPATH, "//input[@id='email' and @name='email']")

(By.XPATH, "//input[@name='email' and @type='text']")

# Можно комбинировать несколько условий:
(By.XPATH, "//input[@id='email' and @type='email' and @name='email']")


# ============================================================
# 7. XPATH ПО ТЕКСТУ
# ============================================================

# HTML:
# <button>Войти</button>

(By.XPATH, "//button[text()='Войти']")

# Если внутри есть пробелы:
(By.XPATH, "//button[normalize-space()='Войти']")

# Если внутри есть другие HTML-элементы:
# <button><span>Войти</span></button>

(By.XPATH, "//button[contains(., 'Войти')]")


# ВАЖНО:
# text() работает с непосредственным текстовым узлом.
# contains(., '...') часто удобнее для кнопок/элементов
# с вложенными span/div.


# ============================================================
# 8. CONTAINS()
# ============================================================

# HTML:
# <div id="user-123456">

(By.XPATH, "//div[contains(@id, 'user-')]")

# HTML:
# <button class="btn btn-primary">

(By.XPATH, "//button[contains(@class, 'btn-primary')]")

# HTML:
# <input placeholder="Введите email">

(By.XPATH, "//input[contains(@placeholder, 'email')]")


# Используй contains(), когда известна только стабильная часть значения.


# ============================================================
# 9. STARTS-WITH()
# ============================================================

# HTML:
# <div id="user-123456">

(By.XPATH, "//div[starts-with(@id, 'user-')]")

# HTML:
# <input name="user_email">

(By.XPATH, "//input[starts-with(@name, 'user_')]")


# ============================================================
# 10. NOT()
# ============================================================

# Все input, кроме hidden:
(By.XPATH, "//input[not(@type='hidden')]")

# Элемент без disabled:
(By.XPATH, "//button[not(@disabled)]")


# ============================================================
# 11. AND / OR
# ============================================================

# AND:
(By.XPATH, "//input[@type='email' and @name='email']")

# OR:
(By.XPATH, "//input[@name='email' or @name='user_email']")


# ============================================================
# 12. ПОИСК ПО КЛАССУ
# ============================================================

# Не всегда безопасно:
(By.XPATH, "//button[@class='btn-primary']")

# Почему?
# У элемента может появиться еще один класс:
# class="btn-primary active"
#
# Тогда точное сравнение перестанет работать.

# Лучше:
(By.XPATH, "//button[contains(@class, 'btn-primary')]")


# Еще надежнее — если есть специальный test-id:
(By.XPATH, "//button[@data-testid='login-button']")


# ============================================================
# 13. ПОИСК ПО data-testid / data-test / data-qa
# ============================================================

(By.XPATH, "//*[@data-testid='login-button']")

(By.XPATH, "//*[@data-test='login-button']")

(By.XPATH, "//*[@data-qa='login-button']")

# Это часто очень хорошие локаторы для автотестов.


# ============================================================
# 14. ПОИСК ВНУТРИ ДРУГОГО ЭЛЕМЕНТА
# ============================================================

# HTML:
# <form id="login-form">
#     <input name="email">
# </form>

(By.XPATH, "//form[@id='login-form']//input[@name='email']")

# Кнопка submit внутри формы:
(By.XPATH, "//form[@id='login-form']//button[@type='submit']")


# ============================================================
# 15. / И // В XPATH
# ============================================================

# "/" — непосредственный дочерний элемент:
(By.XPATH, "//form[@id='login-form']/input")

# "//" — элемент на любом уровне внутри:
(By.XPATH, "//form[@id='login-form']//input")

# На практике // обычно удобнее и устойчивее.


# ============================================================
# 16. РОДИТЕЛЬСКИЙ ЭЛЕМЕНТ: ..
# ============================================================

# HTML:
# <div class="field">
#     <label>Email</label>
#     <input name="email">
# </div>

# Найти input, затем подняться к parent:
(By.XPATH, "//input[@name='email']/..")

# Найти конкретный родительский div:
(By.XPATH, "//input[@name='email']/parent::div")


# ============================================================
# 17. ANCESTOR — ПРЕДОК
# ============================================================

# Найти форму, внутри которой находится input:
(By.XPATH, "//input[@name='email']/ancestor::form")

# Найти form с определенным ID:
(By.XPATH, "//input[@name='email']/ancestor::form[@id='login-form']")


# ============================================================
# 18. FOLLOWING-SIBLING
# ============================================================

# HTML:
# <label>Email</label>
# <input name="email">

# Найти input после label:
(By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")

# Если между ними несколько элементов:
(By.XPATH, "//label[normalize-space()='Email']/following-sibling::input[1]")


# ============================================================
# 19. PRECEDING-SIBLING
# ============================================================

# HTML:
# <input name="email">
# <span class="error">Неверный email</span>

(By.XPATH, "//span[contains(@class, 'error')]/preceding-sibling::input")


# ============================================================
# 20. FOLLOWING
# ============================================================

# Более широкий поиск элементов после текущего элемента:
(By.XPATH, "//label[text()='Email']/following::input[1]")


# ВАЖНО:
# following:: может искать далеко за пределами текущего блока.
# Если возможно, предпочитай following-sibling или поиск внутри родителя.


# ============================================================
# 21. POSITION / ИНДЕКС ИСПОЛЬЗОВАТЬ В ПОСЛЕДНЮЮ ОЧЕРЕДЬ!
# ============================================================

# Третий button:
(By.XPATH, "(//button)[3]")

# Первый button:
(By.XPATH, "(//button)[1]")

# Второй input с name=email:
(By.XPATH, "(//input[@name='email'])[2]")


# Использовать позицию стоит осторожно.
# Если DOM изменится, локатор может начать указывать на другой элемент.


# ============================================================
# 22. ПЕРВЫЙ / ПОСЛЕДНИЙ
# ============================================================

(By.XPATH, "(//button)[1]")

(By.XPATH, "(//button)[last()]")

# Последний input:
(By.XPATH, "(//input)[last()]")


# ============================================================
# 23. ПРАВИЛЬНАЯ РАБОТА С КЛАССАМИ
# ============================================================

# Плохо:
(By.XPATH, "//div[@class='form-control']")

# Лучше:
(By.XPATH, "//div[contains(@class, 'form-control')]")

# Но contains(@class, ...) может дать ложные совпадения.
# Например:
# class="not-form-control"
#
# Более точная проверка класса:
(By.XPATH,
 "//div[contains(concat(' ', normalize-space(@class), ' '), ' form-control ')]"
)


# ============================================================
# 24. НОРМАЛИЗАЦИЯ ПРОБЕЛОВ
# ============================================================

# HTML:
# <button>   Войти   </button>

(By.XPATH, "//button[normalize-space()='Войти']")

# Для текста с пробелами это обычно лучше, чем text()='...'


# ============================================================
# 25. ДИНАМИЧЕСКИЙ ID
# ============================================================

# HTML:
# <input id="input-123456">

# Если меняется только конец:
(By.XPATH, "//input[starts-with(@id, 'input-')]")

# Или:
(By.XPATH, "//input[contains(@id, 'input-')]")


# Но сначала проверь, нет ли более стабильного атрибута:
# data-testid, name, aria-label и т.д.


# ============================================================
# 26. ARIA / ACCESSIBILITY АТРИБУТЫ
# ============================================================

# HTML:
# <button aria-label="Close">

(By.XPATH, "//button[@aria-label='Close']")

# HTML:
# <input aria-label="Email">

(By.XPATH, "//input[@aria-label='Email']")


# ============================================================
# 27. ROLE
# ============================================================

# HTML:
# <div role="button" aria-label="Войти">

(By.XPATH, "//*[@role='button' and @aria-label='Войти']")


# ============================================================
# 28. LINK / ССЫЛКИ
# ============================================================

# HTML:
# <a href="/login">Войти</a>

(By.XPATH, "//a[@href='/login']")

# По тексту:
(By.XPATH, "//a[normalize-space()='Войти']")

# Частичное совпадение href:
(By.XPATH, "//a[contains(@href, '/login')]")


# ============================================================
# 29. КНОПКА SUBMIT
# ============================================================

# HTML:
# <button type="submit">Войти</button>

(By.XPATH, "//button[@type='submit']")

# Если есть форма:
(By.XPATH, "//form[@id='login-form']//button[@type='submit']")


# ============================================================
# 30. CHECKBOX
# ============================================================

# HTML:
# <input type="checkbox" id="terms">

(By.ID, "terms")

# Или:
(By.XPATH, "//input[@type='checkbox' and @id='terms']")


# ============================================================
# 31. RADIO BUTTON
# ============================================================

# HTML:
# <input type="radio" name="gender" value="male">

(By.XPATH, "//input[@type='radio' and @value='male']")


# ============================================================
# 32. SELECT
# ============================================================

# HTML:
# <select id="country">
#     <option value="se">Sweden</option>
# </select>

(By.ID, "country")

# Для самого select:
# from selenium.webdriver.support.ui import Select
#
# select = Select(driver.find_element(By.ID, "country"))
# select.select_by_value("se")


# ============================================================
# 33. ЕСЛИ НУЖНО НАЙТИ ЭЛЕМЕНТ ПО LABEL
# ============================================================

# HTML:
# <label for="email">Email</label>
# <input id="email">

# Лучший вариант — использовать связь label -> for -> id:
(By.ID, "email")

# Если ID неизвестен:
(By.XPATH, "//label[@for='email']/following-sibling::input")


# Еще надежнее, если input находится внутри label:
# <label>
#     Email
#     <input>
# </label>

(By.XPATH, "//label[contains(., 'Email')]//input")


# ============================================================
# 34. ПОИСК ТЕКСТА В ЛЮБОМ ЭЛЕМЕНТЕ
# ============================================================

(By.XPATH, "//*[normalize-space()='Войти']")

# Лучше ограничивать тег, если это возможно:
(By.XPATH, "//button[normalize-space()='Войти']")


# ============================================================
# 35. ПОИСК ЭЛЕМЕНТА С ДВУМЯ СТАБИЛЬНЫМИ ПРИЗНАКАМИ
# ============================================================

# HTML:
# <input id="email" type="email" name="email">

(By.XPATH, "//input[@id='email' and @name='email']")

# Чем больше условий — не всегда лучше.
# Добавляй условия, если они действительно повышают уникальность
# и используют стабильные значения.


# ============================================================
# 36. XPATH AXES — КРАТКАЯ ШПАРГАЛКА
# ============================================================

# parent:
(By.XPATH, "//input[@id='email']/parent::*")

# ancestor:
(By.XPATH, "//input[@id='email']/ancestor::form")

# child:
(By.XPATH, "//form[@id='login']//child::input")

# following-sibling:
(By.XPATH, "//label[text()='Email']/following-sibling::input")

# preceding-sibling:
(By.XPATH, "//input[@id='email']/preceding-sibling::label")

# following:
(By.XPATH, "//label[text()='Email']/following::input[1]")

# preceding:
(By.XPATH, "//input[@id='email']/preceding::label[1]")


# ============================================================
# 37. XPATH: ИЗБЕГАЙ АБСОЛЮТНЫХ ПУТЕЙ
# ============================================================

# Плохо:
(By.XPATH, "/html/body/div[1]/div[2]/div[3]/form/div[2]/button")

# Лучше:
(By.XPATH, "//form[@id='login-form']//button[@type='submit']")

# Еще лучше, если есть test-id:
(By.XPATH, "//button[@data-testid='login-submit']")


# ============================================================
# 38. ID VS XPATH
# ============================================================

# Если есть стабильный ID:
(By.ID, "email")

# Если ID нет:
(By.XPATH, "//input[@name='email']")

# Если есть data-testid:
(By.XPATH, "//input[@data-testid='email']")

# Если нужен поиск по тексту:
(By.XPATH, "//button[normalize-space()='Войти']")

# Если нужна связь между элементами:
(By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")


# ============================================================
# 39. ОЖИДАНИЕ ЭЛЕМЕНТА
# ============================================================

# Локатор и ожидание — разные вещи.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_button = (By.ID, "login-button")

# Ожидание появления:
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(login_button)
# )

# Ожидание видимости:
# WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located(login_button)
# )

# Ожидание возможности клика:
# WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(login_button)
# )


# ============================================================
# 40. ПРАВИЛЬНЫЙ ПАТТЕРН ДЛЯ КЛИКА
# ============================================================

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# locator = (By.XPATH, "//button[@data-testid='login-button']")
#
# button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(locator)
# )
#
# button.click()


# ============================================================
# 41. ПРОВЕРКА CSS В DEVTOOLS
# ============================================================

# В Chrome Console:
#
# document.querySelector("#email")
#
# document.querySelectorAll("#email")
#
# document.querySelectorAll("[data-testid='login-button']")
#
# document.querySelectorAll("form input[name='email']")


# ============================================================
# 42. ПРОВЕРКА XPATH В DEVTOOLS
# ============================================================

# В Chrome Console:
#
# $x("//input[@id='email']")
#
# $x("//button[normalize-space()='Войти']")
#
# $x("//form[@id='login-form']//input[@name='email']")


# ============================================================
# 43. ПРОВЕРКА УНИКАЛЬНОСТИ
# ============================================================

# Для CSS:
#
# document.querySelectorAll("[data-testid='login-button']").length
#
# Результат 1 -> один элемент.
#
# Для XPath:
#
# $x("//button[@id='login-button']").length
#
# Результат 1 -> один элемент.


# ============================================================
# 44. ЧТО ВЫБИРАТЬ В ПЕРВУЮ ОЧЕРЕДЬ
# ============================================================

"""
Рекомендуемый порядок:

1. Стабильный ID
       ↓
2. data-testid / data-test / data-qa
       ↓
3. Стабильный name / aria-label / другой уникальный атрибут
       ↓
4. Короткий CSS
       ↓
5. XPath по атрибутам
       ↓
6. XPath по тексту
       ↓
7. XPath axes (parent, sibling, ancestor...)
       ↓
8. Позиционные XPath

Главное правило:

    Стабильность > краткость.

Не выбирай локатор только потому, что он короче.
"""


# ============================================================
# 45. АНТИПАТТЕРНЫ
# ============================================================

# Плохо:
(By.XPATH, "/html/body/div[2]/div[1]/div[3]/button")

# Плохо:
(By.XPATH, "(//button)[7]")

# Плохо:
(By.CSS_SELECTOR, "div:nth-child(4) > div:nth-child(2) > button")

# Потенциально плохо:
(By.CSS_SELECTOR, ".btn")

# Потенциально плохо:
(By.XPATH, "//div[contains(@class, 'button')]")

# Хорошо, если стабильно:
(By.ID, "login-button")

# Хорошо, если предусмотрено приложением:
(By.XPATH, "//button[@data-testid='login-button']")


# ============================================================
# 46. ПРИМЕР: РЕАЛЬНАЯ ФОРМА ЛОГИНА
# ============================================================

# HTML:
#
# <form id="login-form">
#     <input id="email" name="email" type="email">
#     <input id="password" name="password" type="password">
#     <button id="login-button" type="submit">
#         Войти
#     </button>
# </form>

email_locator = (By.ID, "email")
password_locator = (By.ID, "password")
login_locator = (By.ID, "login-button")

# Если ID нет:
email_xpath = (By.XPATH, "//form[@id='login-form']//input[@name='email']")
password_xpath = (By.XPATH, "//form[@id='login-form']//input[@name='password']")
login_xpath = (
    By.XPATH,
    "//form[@id='login-form']//button[@type='submit']"
)


# ============================================================
# 47. ПРИМЕР: КНОПКА ПО ТЕКСТУ
# ============================================================

# HTML:
# <button class="primary">
#     Сохранить
# </button>

save_button = (
    By.XPATH,
    "//button[normalize-space()='Сохранить']"
)


# ============================================================
# 48. ПРИМЕР: ТЕКСТ + АТРИБУТ
# ============================================================

# HTML:
# <button type="submit">Сохранить</button>

save_button = (
    By.XPATH,
    "//button[@type='submit' and normalize-space()='Сохранить']"
)


# ============================================================
# 49. ПРИМЕР: ЭЛЕМЕНТ В КАРТОЧКЕ
# ============================================================

# HTML:
#
# <div class="product-card">
#     <h2>iPhone</h2>
#     <button>Купить</button>
# </div>

# Кнопка купить внутри карточки iPhone:
buy_iphone = (
    By.XPATH,
    "//div[contains(@class, 'product-card')][.//h2[normalize-space()='iPhone']]"
    "//button[normalize-space()='Купить']"
)


# ============================================================
# 50. БЫСТРЫЙ ЧЕК-ЛИСТ
# ============================================================

CHECKLIST = """
Перед тем как оставить локатор в тесте:

[ ] Я проверил элемент через DevTools.
[ ] Локатор находит нужный элемент.
[ ] Локатор не зависит от позиции элемента.
[ ] Локатор не зависит от лишних div.
[ ] Значения атрибутов не генерируются случайно.
[ ] Локатор уникален или область поиска ограничена.
[ ] Если есть стабильный ID — я проверил его.
[ ] Если есть data-testid/data-test/data-qa — я проверил его.
[ ] Для текста я использовал normalize-space(), если это необходимо.
[ ] Для динамического значения я использовал стабильную часть.
[ ] Я не использовал длинный абсолютный XPath без необходимости.
[ ] Для динамической страницы я использую WebDriverWait (ожидания).
"""


# ============================================================
# 51. КОРОТКАЯ ШПАРГАЛКА
# ============================================================

LOCATOR_BY_ID = (By.ID, 'email')
XPATH_ID = (By.XPATH, "//input[@id='email']")
XPATH_ATTRIBUTE = (By.XPATH, "//input[@name='email']")
XPATH_AND = (By.XPATH, "//input[@name='email' and @type='text']")
XPATH_OR = (By.XPATH, "//input[@name='email' or @name='login']")
XPATH_TEXT = (By.XPATH, "//button[normalize-space()='Войти']")
XPATH_CONTAINS = (By.XPATH, "//div[contains(@id, 'user-')]")
XPATH_STARTS_WITH = (By.XPATH, "//div[starts-with(@id, 'user-')]")
XPATH_PARENT = (By.XPATH, "//input[@id='email']/parent::*")
XPATH_ANCESTOR = (By.XPATH, "//input[@id='email']/ancestor::form")
XPATH_SIBLING = (By.XPATH, "//label[text()='Email']/following-sibling::input")
XPATH_FIRST = (By.XPATH, "(//button)[1]")
XPATH_LAST = (By.XPATH, "(//button)[last()]")
XPATH_DATA_TESTID = (By.XPATH, "//*[@data-testid='login-button']")
