import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user(user_id: int):
    """Получаем пользователя по id через API"""
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    response.raise_for_status()
    return response.json(), response.status_code

def post_info(title: str, body: str, user_id: int):
    """Создаем пост через API"""
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    headers = {
        "Content-type": 'application/json; charset=UTF-8'}
    response = requests.post(f"{BASE_URL}/posts", json=payload, headers=headers)
    response.raise_for_status()
    return response.json(), response.status_code
