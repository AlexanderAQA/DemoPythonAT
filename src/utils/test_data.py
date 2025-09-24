import os

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
