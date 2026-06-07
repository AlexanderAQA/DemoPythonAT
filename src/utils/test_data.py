import os
import random
import string
from dataclasses import dataclass

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

@dataclass
class TestUsers:
    login: str
    password: str
    name: str

USER_OLGA = TestUsers("helgaautotests@gmail.com", "Helgaautotests26", "Ольга")

@dataclass
class TestBooks:
    name: str
    price: str
    article: str

BOOK_1 = TestBooks("Клякса в небе и фифти-фифти","860 ₽", "ФК0176")
BOOK_2 = TestBooks("1000 лет одиночества", "690 ₽","ФК0119")
BOOK_3 = TestBooks("Обратный отсчет","390 ₽", "ФК0192")
