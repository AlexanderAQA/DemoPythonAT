import requests
from src.utils.assertions import CommonAssertions

class ApiWeather:
    def __init__(self):
        self.assertions = CommonAssertions(self)
        self.base_url = "https://api.open-meteo.com/v1/forecast"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
        }

    def get_weather_requests(self):
        """Получение погоды , возвращает (body, status_code)"""
        params = {
            "latitude": 56.8584,
            "longitude": 35.9006,
            "current": ["temperature_2m", "relative_humidity_2m"],
            "timezone": "auto",
        }

        response = requests.get(self.base_url, params=params)
        body = response.json()

        return body, response.status_code

    def get_weather_by_params(self, latitude, longitude, current, timezone, url, method=requests.get):
        """Получение погоды. Возвращает (body, status_code)"""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": current,
            "timezone": timezone
        }

        response = method(url=url, params=params)
        body = response.json()

        return body, response.status_code
