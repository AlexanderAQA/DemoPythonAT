"""
Урок: Принципы чистого кода в Python
====================================

Цель урока:
- понять, что такое "чистый код";
- увидеть практический смысл DRY, KISS, SRP и YAGNI;
- научиться замечать "запахи" кода;
- потренироваться улучшать существующий код.

Формат:
1. Сначала смотрим на проблемный пример.
2. Обсуждаем, что в нём неудобно.
3. Сравниваем с улучшенной версией.
4. Выполняем небольшие задания.
"""


# ============================================================
# 1. KISS — Keep It Simple, Stupid
# ============================================================
#
# Идея:
# Если задачу можно решить простым способом, не стоит усложнять её
# дополнительными абстракциями, классами и "магией".
#
# Плохой пример:

def is_adult_bad(age):
    if age >= 18:
        return True
    else:
        return False


# Хороший пример:

def is_adult(age):
    return age >= 18


# Почему лучше?
# Выражение `age >= 18` уже возвращает True или False.
# Дополнительный if/else ничего не добавляет.
#
# Правило:
# Сначала ищи самое простое решение, которое корректно решает задачу.


# ============================================================
# 2. DRY — Don't Repeat Yourself
# ============================================================
#
# Идея:
# Не дублируй одну и ту же логику в нескольких местах.
#
# Плохой пример:

def calculate_user_price_bad(price):
    price_with_tax = price * 1.2
    return price_with_tax


def calculate_admin_price_bad(price):
    price_with_tax = price * 1.2
    return price_with_tax


# Если ставка налога изменится с 20% на 21%, придётся искать
# все места с формулой `price * 1.2`.
#
# Улучшенный вариант:

# Налог НДС
TAX_RATE = 0.22


def add_tax(price):
    return price * (1 + TAX_RATE)


def calculate_user_price(price):
    return add_tax(price)


def calculate_admin_price(price):
    return add_tax(price)


# Важно:
# DRY — это не "вынеси абсолютно всё в функцию".
#
# Если два фрагмента похожи случайно, но представляют разные бизнес-правила,
# объединять их только ради DRY может быть плохой идеей.


# ============================================================
# 3. SRP — Single Responsibility Principle
# ============================================================
#
# Идея:
# У функции или класса должна быть одна понятная ответственность.
#
# Плохой пример:

def process_order_bad(order):
    # Проверяем заказ
    if not order["items"]:
        raise ValueError("Заказ пуст")

    # Считаем стоимость
    total = sum(item["price"] * item["quantity"] for item in order["items"])

    # Сохраняем заказ
    print(f"Сохраняем заказ на сумму {total}")

    # Отправляем email
    print(f"Отправляем email клиенту: {order['email']}")

    return total


# Здесь сразу несколько задач:
# 1. валидация;
# 2. расчёт;
# 3. сохранение;
# 4. уведомление.
#
# Разделим ответственность:

def validate_order(order):
    if not order["items"]:
        raise ValueError("Заказ пуст")


def calculate_order_total(order):
    return sum(
        item["price"] * item["quantity"]
        for item in order["items"]
    )


def save_order(order, total):
    print(f"Сохраняем заказ на сумму {total}")


def send_order_email(order):
    print(f"Отправляем email клиенту: {order['email']}")


def process_order(order):
    validate_order(order)
    total = calculate_order_total(order)
    save_order(order, total)
    send_order_email(order)
    return total


# Теперь каждую часть можно изменять и тестировать отдельно.


# ============================================================
# 4. YAGNI — You Aren't Gonna Need It
# ============================================================
#
# Идея:
# Не реализуй функциональность "на будущее", если она сейчас не нужна.
#
# Плохой подход:
#
# "Вдруг через год нам понадобится поддержка 17 форматов валют,
# распределённый кеш и плагинная архитектура — давайте сделаем это сейчас."
#
# Хороший подход:
# Реализовать текущую задачу минимально необходимым способом.
#
# Пример:

def format_price(price):
    return f"{price:.2f} ₽"


# Если бизнес пока работает только с рублями, необязательно сразу
# создавать CurrencyFactory, CurrencyStrategy и 15 классов.


# ============================================================
# 5. Хорошие имена
# ============================================================
#
# Код читается людьми чаще, чем пишется.
# Поэтому имена должны объяснять смысл.
#
# Плохо:

def calc(x, y):
    return x * y


# Лучше:

def calculate_total_price(price, quantity):
    return price * quantity


# Ещё пример.
#
# Плохо:

d = 86400


# Лучше:

SECONDS_IN_DAY = 86400


# Хорошее имя уменьшает необходимость в комментариях.


# ============================================================
# 6. Комментарии: объясняем "почему", а не "что"
# ============================================================
#
counter = 0
report_number = 0
# Плохо:

# Увеличиваем счётчик на единицу
counter += 1


# Такой комментарий бесполезен: код и так это показывает.
#
# Лучше:

# Первый элемент имеет индекс 1 в отчёте, потому что отчёт
# использует пользовательскую нумерацию, а не индексацию Python.
report_number += 1


# Комментарий должен объяснять причину, ограничение или контекст,
# который невозможно очевидно прочитать из самого кода.


# ============================================================
# 7. Маленькие функции
# ============================================================
#
# Если функция делает слишком много, её трудно читать и тестировать.
#
# Плохой пример:

def create_invoice_bad(customer, items):
    if not customer["name"]:
        raise ValueError("Нет имени клиента")

    total = 0

    for item in items:
        if item["quantity"] <= 0:
            raise ValueError("Количество должно быть положительным")

        total += item["price"] * item["quantity"]

    invoice = {
        "customer": customer["name"],
        "total": total,
    }

    print("Счёт создан")
    return invoice


# Можно выделить отдельные действия:

def validate_customer(customer):
    if not customer["name"]:
        raise ValueError("Нет имени клиента")


def validate_item(item):
    if item["quantity"] <= 0:
        raise ValueError("Количество должно быть положительным")


def calculate_items_total(items):
    total = 0

    for item in items:
        validate_item(item)
        total += item["price"] * item["quantity"]

    return total


def create_invoice(customer, items):
    validate_customer(customer)

    total = calculate_items_total(items)

    invoice = {
        "customer": customer["name"],
        "total": total,
    }

    print("Счёт создан")
    return invoice


# ============================================================
# 8. Избегаем глубокой вложенности
# ============================================================
#
# Плохо:

def can_buy_bad(user, product):
    if user["active"]:
        if product["available"]:
            if user["balance"] >= product["price"]:
                return True

    return False


# Можно сделать условия плоскими:

def can_buy(user, product):
    if not user["active"]:
        return False

    if not product["available"]:
        return False

    return user["balance"] >= product["price"]


# Такой стиль часто называют guard clauses.
# Мы быстро отбрасываем неподходящие случаи и оставляем основной сценарий
# максимально читаемым.


# ============================================================
# 9. Магические числа и строки
# ============================================================
#
# Плохо:

def is_valid_password(password):
    return len(password) >= 8


# Лучше:

MIN_PASSWORD_LENGTH = 12


def is_valid_password(password):
    return len(password) >= MIN_PASSWORD_LENGTH


# Теперь правило имеет имя и его проще изменить.


# ============================================================
# 10. Чистый код ≠ максимально короткий код
# ============================================================
#
# Это важная мысль урока.
#
# Иногда чрезмерное сокращение делает код менее понятным.
#
# Например:

def calculate_total(items):
    return sum(x["price"] * x["quantity"] for x in items)


# Такой вариант вполне хорош.
#
# Но если расчёт станет сложнее, явный цикл может быть понятнее:

def calculate_total_explicit(items):
    total = 0

    for item in items:
        item_total = item["price"] * item["quantity"]
        total += item_total

    return total


# Чистый код — это не конкурс на минимальное количество строк.
# Главный критерий: насколько легко другому разработчику понять,
# проверить и изменить код.


# ============================================================
# 11. Практическое упражнение
# ============================================================
#
# Найдите проблемы в функции ниже:
#
# - плохие имена;
# - дублирование;
# - лишняя сложность;
# - слишком много ответственности;
# - магические значения;
# - нарушение KISS/DRY/SRP.


def make_report_bad(users):
    result = []

    for u in users:
        if u["active"] == True:
            if u["age"] >= 18:
                if u["country"] == "SE":
                    result.append({
                        "name": u["name"],
                        "isAdult": "adult",
                        "country": "Sweden",
                    })

    print("Report created:", len(result))
    return result

# использование более компактного вида

def make_report(users):
    result = [
        {
            "name": u["name"],
            "isAdult": "adult",
            "country": "Sweden",
        }
        for u in users
        if u["active"] and u["age"] >= 18 and u["country"] == "SE"
    ]
    print("Report created:", len(result))
    return result

# Один из возможных вариантов:

ADULT_AGE = 18
TARGET_COUNTRY = "SE"
COUNTRY_NAME = "Sweden"


def is_active_adult_from_target_country(user):
    return (
        user["active"]
        and user["age"] >= ADULT_AGE
        and user["country"] == TARGET_COUNTRY
    )


def make_report(users):
    report = []

    for user in users:
        if not is_active_adult_from_target_country(user):
            continue

        report.append({
            "name": user["name"],
            "status": "adult",
            "country": COUNTRY_NAME,
        })

    print("Report created:", len(report))
    return report


# ============================================================
# 12. Итоговая памятка
# ============================================================
#
# KISS
#   Keep It Simple, Stupid
#   -> не усложняй без причины.
#
# DRY
#   Don't Repeat Yourself
#   -> не дублируй одну и ту же логику.
#
# SRP
#   Single Responsibility Principle
#   -> одна функция/класс — одна понятная ответственность.
#
# YAGNI
#   You Aren't Gonna Need It
#   -> не делай функциональность заранее без реальной необходимости.
#
# Хорошие имена
#   -> код должен объяснять себя сам.
#
# Маленькие функции
#   -> одна функция должна решать одну понятную задачу.
#
# Guard clauses
#   -> избегай глубокой вложенности.
#
# Комментарии
#   -> объясняй "почему", если это не очевидно из кода.
#
# Главное правило:
#
#     "Код пишется один раз, а читается много раз."
#
# Поэтому при рефакторинге спрашивай себя:
#
# 1. Понятно ли, что делает этот код?
# 2. Легко ли изменить его?
# 3. Есть ли здесь дублирование?
# 4. Не слишком ли он сложный?
# 5. Есть ли у функций и переменных понятные обязанности и имена?
