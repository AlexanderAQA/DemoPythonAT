import requests
from src.utils.assertions import CommonAssertions

class ApiHH:
    def __init__(self):
        self.assertions = CommonAssertions(self)
        # Базовый URL магазина
        self.base_url = "https://api.hh.ru"

        # Сохраняет куки между запросами
        self.session = requests.Session()

        # Шапка для браузера
        self.headers = {
            "HH-User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            # "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
        }

    def get_country_hh_user(self):
        url = f"{self.base_url.rstrip('/')}/areas"
        response = self.session.get(url, headers=self.headers)

        if "application/json" not in response.headers.get("content-type", ""):
            raise ValueError(f"Server returned non-JSON: {response.status_code}")

        return response.json(), response.status_code
