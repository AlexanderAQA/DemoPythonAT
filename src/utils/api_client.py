import requests
from src.utils.assertions import CommonAssertions
import re
from urllib.parse import quote, urlparse, parse_qs


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
            raise ValueError("Невалидный JSON")

    def get_account_page(self, customer_token: str):
        """GET запрос к личному кабинету с токеном"""
        url = f"{self.base_url}account"

        params = {"customer_token": customer_token}

        response = self.session.get(url, headers=self.headers, params=params)

        return response.text, response.status_code

    def login(self, email: str, password: str):
        """Авторизация с извлечением токена из redirect URL"""

        # GET страница логина для того чтобы сайт пустил пользователя
        form_url = f"{self.base_url}?route=account/login"
        form_resp = self.session.get(form_url, headers=self.headers)

        # Поиск login_token
        token_match = re.search(r'login_token=([a-zA-Z0-9]+)', form_resp.text)
        if not token_match:
            return False, form_resp.status_code

        login_token = token_match.group(1)

        # POST-запрос
        login_url = f"{self.base_url}?route=account/login.login&login_token={login_token}"

        encoded_email = quote(email, safe='')
        payload = f"email={encoded_email}&password={quote(password, safe='')}&redirect={quote(self.base_url + 'account', safe='')}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Referer": f"{self.base_url}login"
        }

        response = self.session.post(login_url, headers=headers, data=payload)

        # 4. Писк customer_token в ответе из redirect URL
        customer_token = None

        # Парсим JSON ответ
        data = response.json()
        redirect_url = data.get("redirect", "")

        # Ищем customer_token в URL редиректа
        token_match = re.search(r'customer_token=([a-zA-Z0-9]+)', redirect_url)
        if token_match:
            customer_token = token_match.group(1)

        # Если не найден в redirect, ищем в cookie
        if not customer_token:
            customer_token = self.session.cookies.get("customer_token")

        return customer_token, response.status_code
