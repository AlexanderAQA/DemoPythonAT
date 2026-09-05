### Переменные и типы данных

rating = 0.0 # float
grade = 5 # int
name = "Иван" # str
graduated = True # bool
contact = {"name": "Ivan", "phone": "89091234567"} # dict
products = ["Яблоко", "Молоко", "Хлеб", "Кефир"] # list
apple_item = {"name": "Яблоко", "price": 100, "quantity": 1} # dict
bread_item = {"name": "Хлеб", "price": 70, "quantity": 1} # dict
items = [apple_item, bread_item] # list
new_contact = ("Иван", "+79091234567", "рабочий") # tuple

"""
Задача 1. Информация о человеке

Создай три переменные:

name — имя человека (str)
age — возраст (int)
height — рост в метрах (float)

Присвой им свои значения и выведи их на экран. Можешь использовать print, f-string.

Пример результата:
Имя: Анна
Возраст: 20
Рост: 1.68
"""
# Решение писать сюда

name = "Анна"
age = 20
height = 1.68
print(f"Имя: {name}\nВозраст: {age}\nРост: {height}")

"""
Задача 2. Товар в магазине

Создай переменные:

product — название товара (str)
price — цена товара (float)
quantity — количество товара (int)
is_available — есть ли товар в наличии (bool)

Выведи всю информацию на экран. Можешь использовать print, f-string.

Пример результата:
Товар: Клавиатура
Цена: 49.99
Количество: 3
В наличии: True
"""
# Решение писать сюда

product = "Молоко"
price = 500.50
quantity = 5
is_available = True

print(f"Товар: {product}\nЦена: {price}\nКоличество: {quantity}\nНаличие: {is_available}")


### Операции
"""
int / float
 ├── +  -  *  /  //  %  **
 └── сравнения

str
 ├── +  * 
 ├── индексы и срезы
 └── методы строк
 """
hello_text = "Привет!"
""" У каждого символа в строке есть свой индекс
 П  р  и  в  е  т  !
 0  1  2  3  4  5  6
 
 Можно выбрать конкретный символ из строки, например:
 print(text[0])
 Результат: "П"
 
 
 Срез строка[start:stop]
"""
print(hello_text[0:3]) # получим "При" (первые три символа)
# Можно не указывать начало
print(hello_text[:3]) # получим "При" (первые три символа)
"""
Взять последние символы
print(text[-1]) # получим "!" (последний символ)

Взять 4 последних символа
print(text[-4:])


Методы строк. 
s - переменная со строкой
s.upper()        # в верхний регистр
s.lower()        # в нижний регистр
s.capitalize()   # первая буква заглавная
s.title()        # Первые Буквы Всех Слов Заглавные

len(name) — функция, которая возвращает количество символов в строке (длину имени)


s.strip()       # убрать пробелы с обоих концов
s.lstrip()      # убрать слева
s.rstrip()      # убрать справа

s.removeprefix("http://")  # убрать префикс
s.removesuffix(".txt")     # убрать суффикс
"""
nam = nam.replace(" ", "")  # Удаление
new_offer = offer.replace(" ", "-") # замена символа
print(new_offer)
"""
Задача 3.
Из переменной которая хранит цену товара убрать лишние символы, оставить только число. 
Вывести новое значение на печать

"""

price_str = "1050 Р"
print(price_str[:4])

"""
Задача 4.
Есть переменная, которая хранит адрес электронной почты. Нужны привести его в нижний регистр
"""

user_email = "MyEmail@Ya.ru"
print(user_email.lower())

"""
Задача 5.
Есть переменная, которая хранит цену товара на сайте. Нужно убрать все пробелы и лишние символы кроме числа.
Вывести на печать получившуюся цену в формате int
"""
new_price = " 1 850 ₽! "
nam = new_price.strip()
nam = nam.replace(" ", "")
print(nam[:-2])



"""
list
 ├── индексы и срезы
 ├── изменение элементов
 ├── append / remove (del) / pop
 └── + и *

tuple
 └── индексы и срезы, но без изменения

dict
 ├── получение по ключу
 ├── добавление / изменение
 └── удаление

bool
 ├── and
 ├── or
 └── not
"""

### Управляющие конструкции
# if/elif/else; циклы; range; break/continue
""" КРАТКО: 
if -> если 
elif -> иначе если 
else -> иначе 
for -> повторяет действие заданное количество раз 
while -> повторяет действие, пока условие True 
range() -> создаёт последовательность чисел 
break -> полностью остановить цикл 
continue -> пропустить текущую итерацию 
"""

### Функции, list, tuple, dict, set. Файлы, CSV, JSON, исключения

# ФУНКЦИИ
def add(a, b):
    return a + b

# LIST — изменяемый список
a = [1, 2, 3]
a.append(4)
a[0]          # 1

# TUPLE — неизменяемый
a = (1, 2, 3)

# DICT — ключ: значение
user = {"name": "Alex", "age": 20}
user["name"]          # Alex
user["age"] = 21

# SET — только уникальные элементы
a = {1, 2, 2, 3}      # {1, 2, 3}
a.add(4)

# ФАЙЛЫ
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("Hello")

# CSV
import csv

with open("data.csv", encoding="utf-8") as f:
    rows = list(csv.reader(f))

# JSON
import json

data = {"name": "Alex"}
text = json.dumps(data)    # Python → JSON
data = json.loads(text)    # JSON → Python

# ИСКЛЮЧЕНИЯ
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Ошибка")
finally:
    print("Завершено")