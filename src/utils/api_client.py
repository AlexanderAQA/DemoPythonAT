import requests
from src.utils.assertions import CommonAssertions

class ApiClient:
    def __init__(self):
        self.assertions = CommonAssertions(self)

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_user(self, user_id: int):
        """Получаем пользователя по id через API"""
        response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        response.raise_for_status()
        return response.json(), response.status_code

    def post_info(self, title: str, body: str, user_id: int):
        """Создаем пост через API"""
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        headers = {
            "Content-type": 'application/json; charset=UTF-8'}
        response = requests.post(f"{self.BASE_URL}/posts", json=payload, headers=headers)
        response.raise_for_status()
        return response.json(), response.status_code
