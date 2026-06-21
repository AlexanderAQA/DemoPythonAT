import requests
from src.utils.assertions import CommonAssertions


class ApiClient:
    def __init__(self):
        self.assertions = CommonAssertions(self)
        # Базовый URL магазина
        self.base_url = "https://shop.finarty.ru/"

        # Сохраняет куки между запросами
        self.session = requests.Session()

        # Шапка для браузера
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
        }

    def add_product_to_cart(self, product_id, quantity=1):
        """Добавление товара в корзину через API"""
        url = f"{self.base_url}?route=checkout/cart.add"

        payload = {
            "product_id": str(product_id),
            "quantity": str(quantity)
        }

        response = self.session.post(url, headers=self.headers, data=payload)

        try:
            return response.json(), response.status_code
        except ValueError:
            return {"html": response.text}, response.status_code
