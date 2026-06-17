import requests

class ApiClient:
    def __init__(self):
        # Базовый URL магазина
        self.base_url = "https://shop.finarty.ru/"

        # Сохраняет куки между запросами
        self.session = requests.Session()

        # Шапка для браузера
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Connection": "keep-alive",
        }

    def get_response_json(self, url, params=None):
        """Гет запрос"""
        response = self.session.get(url, headers=self.headers, params=params)
        return response.json(), response.status_code

    def add_product_to_cart(self, product_id, quantity=1):
        """Добавление товара в корзину через API"""
        url = f"{self.base_url}?route=checkout/cart.add"

        payload = {
            "product_id": str(product_id),
            "quantity": str(quantity)
        }

        response = self.session.post(url, headers=self.headers, data=payload)

        try:
            if response.headers.get('content-type') == 'application/json':
                return response.json(), response.status_code
            result_html = response.text
            return {"html": result_html}, response.status_code
        except ValueError:
            return {"error": "Невалидный JSON"}, response.status_code