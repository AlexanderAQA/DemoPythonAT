import os
import random
import string
from dataclasses import dataclass, field
from faker import Faker
from pages.sundry_page import SundryPage
import re
fake = Faker()


# Абсолютный путь к тестовым данным
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "test_data")  # adjust if needed

def get_valid_user():
    """
    Получить валидного юзера
    :return: Логин и пароль
    """
    with open(os.path.join(DATA_DIR, 'users.txt'), 'r') as f:
        line = f.readline().strip()
        return tuple(line.split(","))  # (username, password)

def get_invalid_user():
    """
    Получить невалидного юзера
    :return: Логин и пароль
    """
    with open(os.path.join(DATA_DIR, 'negative_users.txt'), 'r') as f:
        line = f.readline().strip()
        return tuple(line.split(","))

def get_login_list():
    """
    Получить список логинов
    :return: Список логинов
    """
    with open(os.path.join(DATA_DIR, 'logins.txt'), 'r') as f:
        return [line.strip() for line in f.readlines()]

def generate_random_string(str_length=7):
    rand_str = ''.join(random.choice(string.ascii_letters) for _ in range(str_length))
    return rand_str

def work_with_price(value, quantity=1, mode='calc'):
    """Универсальная функция для работы с ценами (рубли)"""
    if mode == 'clean':
        return int(re.sub(r'[^\d]', '', str(value)))
    num_value = int(value)

    if mode == 'format':
        total = num_value
    else:
        total = num_value * quantity

    return f"{total:,} ₽".replace(",", " ")

@dataclass
class TestUsers:
    login: str = ""
    password: str = ""
    name: str = ""
    email: str = ""
    phone: str = ""
    address: str = ""


USER_OLGA = TestUsers("helgaautotests@gmail.com", "Helgaautotests26", "Ольга")

USER_DATA = TestUsers(
    name="Helga",
    email="helga@gmail.com",
    phone="+79000001111",
    address="Тестовый адрес",
)

@dataclass
class TestBooks:
    name: str
    price: str
    article: str

BOOK_1 = TestBooks("Клякса в небе и фифти-фифти","860 ₽", "ФК0176")
BOOK_2 = TestBooks("1000 лет одиночества", "690 ₽","ФК0119")
BOOK_3 = TestBooks("Обратный отсчет","390 ₽", "ФК0192")

@dataclass
class Product:
    """Класс для описания товара на сайте"""
    name: str
    price: int
    article: str
    size: str = None
    sex: str = None

TSHIRT_ECONOMICS_BLACK = Product(
    name="Футболка «1001 секунда об экономике. От Я до А»-1 (черная)",
    price=2800,
    article="ФК0164",
    size= SundryPage.SIZE_OPTIONS["M"],
    sex= SundryPage.SEX_OPTIONS["male"]
)

TSHIRT_WALL_STREET_WHITE = Product(
    name="Футболка Wall Street (белая)",
    price=2800,
    article="ФК0137",
    size= SundryPage.SIZE_OPTIONS["L"],
    sex= SundryPage.SEX_OPTIONS["male"]
)

TSHIRT_VERTICAL_BLACK = Product(
    name="Футболка «1001 секунда об экономике» (вертикаль, черная)",
    price=3100,
    article="ФК0142",
    size= SundryPage.SIZE_OPTIONS["XL"],
    sex= SundryPage.SEX_OPTIONS["female"]
)

SUNDRY_PRODUCTS = [
    TSHIRT_ECONOMICS_BLACK,
    TSHIRT_WALL_STREET_WHITE,
    TSHIRT_VERTICAL_BLACK
]

COURSE_THREE_PILLARS_2_1 = Product(
    name="Три кита инвестиций» (2+1). Курс Алексея Бачерова в новом формате",
    price=19900,
    article="ФК0144",
)
COURSE_THREE_PILLARS_2_2 = Product(
    name="Три кита инвестиций» (2+2). Курс Алексея Бачерова в новом формате",
    price=28900,
    article="ФК0145",
)
COURSE_SYNTHETIC_BONDS = Product(
    name="Синтетические облигации. Авторский вебинар Алексея Хмелевского (Доступ к записи вебинара)",
    price=2400,
    article="ФК0111",
)
COURSES = [
COURSE_THREE_PILLARS_2_1,
COURSE_THREE_PILLARS_2_2,
COURSE_SYNTHETIC_BONDS
]

@dataclass
class WebElementPracticeUser:
    name: ""
    email: ""
    phone: ""
    address: ""

def generate_web_element_user() -> WebElementPracticeUser:
    """Генерирует случайного пользователя """
    return WebElementPracticeUser(
        name=fake.name()[:13],
        email=fake.email()[:25],
        phone=fake.phone_number()[:10],
        address=fake.address().replace('\n', ', ')[:30]
    )

countries = ["usa", "canada", "uk", "germany", "france", "australia", "japan", "china", "brazil", "india"]
days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
genders = ["male", "female"]
colors = ["red", "blue", "green", "yellow", "white"]
animals = ["cat", "cheetah", "deer", "dog", "elephant", "fox", "giraffe", "lion", "rabbit", "zebra"]

def get_random_days(days_list: list) -> list:
    """Возвращает случайный набор дней"""
    random_qty = random.randint(1, len(days_list))
    return random.sample(days_list, random_qty)

def get_random_colors(colors_list: list) -> list:
    """Возвращает случайный набор цветов"""
    random_qty = random.randint(1, min(3, len(colors_list)))
    return random.sample(colors_list, random_qty)

def get_random_animal(animals_list: list) -> str:
    """Возвращает случайное животное"""
    return random.choice(animals_list)

USER_1 = WebElementPracticeUser(54635, 84545, 789785, 545454545454545454)
USER_2 = WebElementPracticeUser("^%$%^%&$&", "*&(*(*&&(&)))", "(*(%::?:*?*", ")*№)(***)(")
USER_3 = WebElementPracticeUser("", "", "", "")
USER_4 = WebElementPracticeUser("4646(*:%:%","6898:%?(*?(", ":(*?*(*)789", "665478(*??*::%?")

negative_users = [USER_1, USER_2, USER_3, USER_4]

@dataclass
class OtzovikUser:
    login: str = ""
    password: str = ""
    email: str = ""

otzovik_negative_cases = [
    # Пустые поля
    (OtzovikUser(login="", email="test@mail.ru", password="StrongrtertPass123"), "Логин должен быть"),
    (OtzovikUser(login="fdjdghj", email="", password="StrongejgyPass123"), "Введите свой реальный email"),
    (OtzovikUser(login="kyuzsc", email="test@mail.ru", password=""),  "Пароль должен состоять минимум из 6"),

    # Некорректный email (без @ или без домена)
    (OtzovikUser(login="qwdfv", email="notanemail", password="Un1qdfgdguePassw0rd"), "Введите свой реальный email"),
    (OtzovikUser(login="lkoix", email="test@", password="Un1quejhhgjPassw0rd"), "Введите свой реальный email"),
    (OtzovikUser(login="uyiuy", email="@mail.ru", password="Passfghhh123"), "Введите свой реальный email"),
]
