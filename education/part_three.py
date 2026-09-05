"""
ЗАНЯТИЕ 3. ФУНКЦИИ И КОЛЛЕКЦИИ, РАБОТА С ФАЙЛАМИ

Темы:
1. Функции
2. list
3. tuple
4. dict
5. set
6. Работа с текстовыми файлами
7. CSV
8. JSON
9. Исключения
10. Практика
11. Домашнее задание
"""

import csv
import json


# ============================================================
# 1. ФУНКЦИИ
# это именованный блок кода, который выполняет определённую задачу и может принимать входные данные (аргументы) и возвращать результат.
# ============================================================
def say_hello(): # объявление функции с помощью ключевого слова def
    """Простая функция без параметров."""
    print("Привет, Python!")


say_hello() # вызов функции


def greet(name):
    """Функция с параметром."""
    print(f"Привет, {name}!")


greet("Анна")
greet("Иван")


def add_numbers(a, b):
    """Функция с return."""
    return a + b


result = add_numbers(10, 20)
print("Сумма:", result)


def calculate_discount(price, discount=10):
    """
    Функция с параметром по умолчанию.
    discount указывается в процентах.
    """
    return price - price * discount / 100


print("Цена со скидкой:", calculate_discount(1000))
print("Цена со скидкой 25%:", calculate_discount(1000, 25))


def get_student_info(name, age, city):
    """Функция возвращает несколько значений."""
    return name, age, city


student_name, student_age, student_city = get_student_info(
    "Алексей",
    30,
    "Стокгольм"
)

print(
    f"Студент: {student_name}, "
    f"возраст: {student_age}, "
    f"город: {student_city}"
)

"""
Коллекция в Python — это объект, который предназначен для хранения и организации нескольких элементов данных.

list — список, упорядоченная изменяемая коллекция: [1, 2, 3]
tuple — кортеж, упорядоченная неизменяемая коллекция: (1, 2, 3)
set — множество уникальных элементов: {1, 2, 3}
dict — словарь, коллекция пар «ключ–значение»: 
{
"name": "Alex",
"age": 20
 }
"""
# ============================================================
# 2. LIST — СПИСКИ
# ============================================================
numbers = [10, 20, 30, 40, 50]
print("Список:", numbers)

print("Первый элемент:", numbers[0])
print("Последний элемент:", numbers[-1])

numbers.append(60)
print("После append:", numbers)


numbers.insert(1, 15)
print("После insert:", numbers)

numbers.remove(30)
print("После remove:", numbers)

last_number = numbers.pop()
print("Удалённый элемент:", last_number)
print("Список после pop:", numbers)

print("\nПеребор списка:")
for number in numbers:
    print(number)

# ============================================================
# 3. TUPLE — КОРТЕЖИ
# ============================================================
coordinates = (59.3293, 18.0686)

print("Координаты:", coordinates)
print("Широта:", coordinates[0])
print("Долгота:", coordinates[1])


# Распаковка кортежа
latitude, longitude = coordinates

print("Latitude:", latitude)
print("Longitude:", longitude)


# Кортеж нельзя изменять
# coordinates[0] = 60.0
# Эта строка вызовет ошибку TypeError


student = ("Анна", 22, "Python")

name, age, course = student

print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Курс: {course}")


# ============================================================
# 4. DICT — СЛОВАРИ
# ============================================================

student = {
    "name": "Анна",
    "age": 22,
    "course": "Python",
    "city": "Стокгольм"
}

print("Студент:", student)

print("Имя:", student["name"])
print("Возраст:", student["age"])


# Добавление нового ключа
student["email"] = "anna@example.com"
print("После добавления email:", student)


# Изменение значения
student["age"] = 23
print("После изменения возраста:", student)


# Безопасное получение значения
phone = student.get("phone", "Телефон не указан")
print(phone)


print("\nКлючи словаря:")
for key in student:
    print(key)


print("\nЗначения словаря:")
for value in student.values():
    print(value)


print("\nКлюч и значение:")
for key, value in student.items():
    print(f"{key}: {value}")


# ============================================================
# 5. SET — МНОЖЕСТВА
# ============================================================
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]

unique_numbers = set(numbers)

print("Исходный список:", numbers)
print("Уникальные значения:", unique_numbers)


languages_1 = {"Python", "Java", "C++"}
languages_2 = {"Python", "JavaScript", "Java"}

print("Множество 1:", languages_1)
print("Множество 2:", languages_2)

# Объединение
print("Объединение:", languages_1 | languages_2)

# Пересечение
print("Пересечение:", languages_1 & languages_2)

# Разность
print("Разность:", languages_1 - languages_2)


languages_1.add("Go")
print("После добавления Go:", languages_1)


# ============================================================
# 6. ПРАКТИКА: ФУНКЦИЯ И КОЛЛЕКЦИИ
# ============================================================
def calculate_average(numbers):
    """Возвращает среднее значение списка."""
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


grades = [5, 4, 5, 3, 5, 4, 5]

average_grade = calculate_average(grades)

print("Оценки:", grades)
print("Средняя оценка:", average_grade)


def get_unique_words(text):
    """Возвращает множество уникальных слов."""
    words = text.lower().split()
    return set(words)


text = "Python Python Java Python Java C++"

unique_words = get_unique_words(text)

print("Текст:", text)
print("Уникальные слова:", unique_words)


def count_words(text):
    """Подсчитывает количество упоминаний каждого слова."""
    result = {}

    words = text.lower().split()

    for word in words:
        result[word] = result.get(word, 0) + 1

    return result


word_statistics = count_words(
    "python java python c++ python java"
)

print("Статистика слов:", word_statistics)


# ============================================================
# 7. РАБОТА С ТЕКСТОВЫМИ ФАЙЛАМИ
# ============================================================

# Создание и запись в файл
with open("lesson_notes.txt", "w", encoding="utf-8") as file:
    file.write("Занятие 3\n")
    file.write("Тема: Функции и коллекции\n")
    file.write("Работа с файлами\n")

print("Файл lesson_notes.txt создан.")


# Чтение всего файла
with open("lesson_notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("\nСодержимое файла:")
print(content)


# Добавление данных в файл
with open("lesson_notes.txt", "a", encoding="utf-8") as file:
    file.write("Следующая тема: ООП\n")


# Чтение файла построчно
print("Построчное чтение:")

with open("lesson_notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# ============================================================
# 8. CSV
# ============================================================
students = [
    ["name", "age", "course"],
    ["Анна", 22, "Python"],
    ["Иван", 25, "Java"],
    ["Мария", 21, "Python"]
]


# Запись CSV
with open(
    "students.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)
    writer.writerows(students)

print("Файл students.csv создан.")


# Чтение CSV
print("\nДанные из CSV:")

with open(
    "students.csv",
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)


# CSV с использованием словарей
students_data = [
    {
        "name": "Анна",
        "age": 22,
        "course": "Python"
    },
    {
        "name": "Иван",
        "age": 25,
        "course": "Java"
    },
    {
        "name": "Мария",
        "age": 21,
        "course": "Python"
    }
]


fieldnames = ["name", "age", "course"]

with open(
    "students_dict.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(students_data)

print("Файл students_dict.csv создан.")


# ============================================================
# 9. JSON
# ============================================================
user = {
    "name": "Алексей",
    "age": 30,
    "city": "Стокгольм",
    "skills": [
        "Python",
        "SQL",
        "Git"
    ],
    "is_student": True
}


# Запись JSON
with open(
    "user.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        user,
        file,
        ensure_ascii=False,
        indent=4
    )

print("Файл user.json создан.")


# Чтение JSON
with open(
    "user.json",
    "r",
    encoding="utf-8"
) as file:

    loaded_user = json.load(file)

print("Данные из JSON:")
print(loaded_user)

print("Имя пользователя:", loaded_user["name"])
print("Навыки:", loaded_user["skills"])


# ============================================================
# 10. ИСКЛЮЧЕНИЯ
# ============================================================
try:
    number = int("abc")
except ValueError:
    print("Ошибка: невозможно преобразовать 'abc' в число.")
print("Выполнение программы")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Ошибка: нельзя делить на ноль.")


try:
    with open(
        "unknown_file.txt",
        "r",
        encoding="utf-8"
    ) as file:
        print(file.read())

except FileNotFoundError:
    print("Ошибка: файл не найден.")


# Несколько типов ошибок
try:
    value = int("100")
    result = 10 / value
    print("Результат:", result)

except ValueError:
    print("Ошибка преобразования значения.")

except ZeroDivisionError:
    print("Ошибка деления на ноль.")

except Exception as error:
    print("Неизвестная ошибка:", error)

else:
    print("Операция выполнена успешно.")

finally:
    print("Блок finally выполняется всегда.")


# ============================================================
# 11. ПРАКТИЧЕСКАЯ ЗАДАЧА
# МИНИ-СИСТЕМА УЧЁТА СТУДЕНТОВ
# ============================================================
students = []


def add_student(name, age, course):
    """Добавляет студента в список."""

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)


def show_students():
    """Выводит список студентов."""

    if not students:
        print("Список студентов пуст.")
        return

    for index, student in enumerate(students, start=1):
        print(
            f"{index}. "
            
            
            f"{student['name']}, "
            f"{student['age']} лет, "
            f"курс: {student['course']}"
        )


def save_students_to_json(filename):
    """Сохраняет студентов в JSON."""

    try:
        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                students,
                file,
                ensure_ascii=False,
                indent=4
            )

        print(f"Данные сохранены в файл {filename}.")

    except OSError as error:
        print("Ошибка при сохранении файла:", error)


def load_students_from_json(filename):
    """Загружает студентов из JSON."""

    try:
        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        print(f"Данные загружены из файла {filename}.")
        return data

    except FileNotFoundError:
        print("Файл не найден.")
        return []

    except json.JSONDecodeError:
        print("Ошибка: файл содержит некорректный JSON.")
        return []

    except OSError as error:
        print("Ошибка при работе с файлом:", error)
        return []


# Добавляем тестовых студентов
add_student("Анна", 22, "Python")
add_student("Иван", 25, "Java")
add_student("Мария", 21, "Python")

print("\nСписок студентов:")
show_students()


# Сохраняем
save_students_to_json("students.json")


# Загружаем
loaded_students = load_students_from_json(
    "students.json"
)

print("\nЗагруженные студенты:")

for student in loaded_students:
    print(student)


# ============================================================
# 12. ЗАДАНИЯ ДЛЯ САМОСТОЯТЕЛЬНОЙ ПРАКТИКИ
# ============================================================

"""
ЗАДАНИЕ 1
----------
Напишите функцию multiply_numbers(a, b),
которая возвращает произведение двух чисел.

Пример:
multiply_numbers(5, 10)
Результат: 50
"""
# Писать задание сюда

def multiply_numbers(a, b):
    return a * b
print("Результат:",multiply_numbers(5, 10))

"""
ЗАДАНИЕ 2
----------
Дан список:

numbers = [10, 5, 20, 10, 30, 5, 40]

1. Нужно вывести на печать все уникальные значения списка
2. Найдите сумму всех уникальных значений.
"""
# Писать задание сюда
numbers = [10, 5, 20, 10, 30, 5, 40]
unique_numbers = list(set(numbers))
print(unique_numbers)

numbers = [10, 5, 20, 10, 30, 5, 40]
sum_unique = sum(set(numbers))
print(sum_unique)

"""
ЗАДАНИЕ 3
----------
Создайте словарь:

student = {
    "name": "Ваше имя",
    "age": 20,
    "skills": ["Python", "Git"]
}

Добавьте:
1. Город.
2. Email.
3. Ещё один навык.

Выведите все пары ключ: значение.
"""
# Писать задание сюда
student = {
    "name": "Ваше имя",
    "age": 20,
    "skills": ["Python", "Git"]
}

student ["Город"] = "Москва"
student ["Email"] = "Gyry@mail.ru"
student ["Пол"] = "Муж"

print(student)


"""
ЗАДАНИЕ 4
----------
Создайте текстовый файл tasks.txt.

Запишите в него минимум 5 задач.

Затем:
1. Прочитайте файл.
2. Выведите каждую задачу с номером.
3. Добавьте ещё одну задачу.
"""
# Писать задание сюда

with open("tasks.txt.", "w", encoding="utf-8") as file:
    file.write("Выучить функции\n")
    file.write("Выучить коллекции\n")
    file.write("Выучить списки\n")
    file.write("Выучить кортежи\n")
    file.write("Выучить файлы\n")
with open("tasks.txt.", "r", encoding="utf-8") as file:
    content = file.read()
print("\nСодержимое файла:")
print(content)
with open("tasks.txt.", "a", encoding="utf-8") as file:
    file.write("Выучить след тему\n")
print("\nСодержимое файла:")
print(content)

"""
ЗАДАНИЕ 5
----------
Создайте CSV-файл products.csv со столбцами:

name, price, quantity

Добавьте минимум 3 товара.

Затем прочитайте CSV и выведите данные.
"""
# Писать задание сюда


"""
ЗАДАНИЕ 6
----------
Создайте JSON-файл profile.json со структурой:

{
    "name": "Ваше имя",
    "age": 25,
    "city": "Ваш город",
    "skills": ["Python", "SQL"],
    "experience": {
        "years": 1,
        "level": "Junior"
    }
}

Сохраните данные в файл, затем прочитайте их обратно.
"""
# Писать задание сюда

"""
ЗАДАНИЕ 7
----------
Напишите функцию divide(a, b).

Она должна:
1. Выполнять деление.
2. Обрабатывать ZeroDivisionError.
3. Обрабатывать ValueError при неверном вводе.
"""
# Писать задание сюда



# ============================================================
# 13. ДОМАШНЕЕ ЗАДАНИЕ
# ============================================================

"""
# Домашнее задание: «Менеджер задач»

Создайте отдельный Python-файл:

education/task_manager.py

Программа должна быть простым менеджером задач.

## Что нужно сделать

Создайте список для хранения задач:

tasks = []

Каждая задача должна быть словарём:

{
    "title": "Изучить функции",
    "completed": False
}

## Создайте функции

### 1. `add_task()`

Функция должна:

* попросить пользователя ввести название задачи;
* создать новую задачу;
* добавить её в список `tasks`.



### 2. `show_tasks()`

Функция должна вывести все задачи.

Пример:

```text
1. Изучить функции — Не выполнено
2. Сделать домашнее задание — Выполнено
```

Если задач нет:

```text
Список задач пуст.
```

### 3. `complete_task()`

Функция должна:

* попросить пользователя ввести номер задачи;
* отметить выбранную задачу как выполненную;
* использовать `try/except`, чтобы программа не завершилась с ошибкой, если пользователь введёт не число.

### 4. `delete_task()`

Функция должна:

* попросить пользователя ввести номер задачи;
* удалить выбранную задачу;
* обработать ошибку, если номер задачи неправильный.

### 5. `save_tasks()`

Сохраните список `tasks` в файл:

```text
tasks.json
```

Используйте модуль:

```python
import json
```

### 6. `load_tasks()`

При запуске программы попробуйте загрузить задачи из `tasks.json`.

Если файла ещё нет, программа не должна завершаться с ошибкой. Просто создайте пустой список задач:

```python
tasks = []
```

Используйте:

```python
try:
    ...
except FileNotFoundError:
    ...
```

## Меню программы

Программа должна работать в цикле:

```text
1. Добавить задачу
2. Показать задачи
3. Выполнить задачу
4. Удалить задачу
5. Сохранить задачи
6. Выход
```

После выбора пункта меню должна вызываться соответствующая функция.

При выходе из программы обязательно сохраните задачи.

## Пример работы

```text
1. Добавить задачу
2. Показать задачи
3. Выполнить задачу
4. Удалить задачу
5. Сохранить задачи
6. Выход

Выберите действие: 1

Введите задачу: Изучить JSON
Задача добавлена!

Выберите действие: 2

1. Изучить JSON — Не выполнено

Выберите действие: 3

Введите номер задачи: 1
Задача выполнена!

Выберите действие: 2

1. Изучить JSON — Выполнено
```

## Минимальные требования

* [ ] Использовать список `tasks`
* [ ] Использовать словари для задач
* [ ] Создать 6 функций
* [ ] Использовать `json`
* [ ] Сохранять задачи в `tasks.json`
* [ ] Загружать задачи из `tasks.json`
* [ ] Использовать `try/except` хотя бы для неверного ввода и отсутствующего файла
* [ ] Создать меню с `while True`

"""
