import openmeteo_requests
import requests_cache
from retry_requests import retry

from src.utils.assertions import CommonAssertions


class ApiWeather:
	def __init__(self):
		self.assertions = CommonAssertions(self)
		self.base_url = "https://api.open-meteo.com/v1/forecast"

		self.cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
		self.retry_session = retry(self.cache_session, retries=5, backoff_factor=0.2)
		self.openmeteo = openmeteo_requests.Client(session=self.retry_session)

		# Шапка для браузера
		self.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
			"Accept": "application/json, text/javascript, */*; q=0.01",
			"Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
			"Connection": "keep-alive",
		}

	def get_weather(self):
		params = {
			"latitude": 56.8584,
			"longitude": 35.9006,
			"current": [
					"temperature_2m",
					"relative_humidity_2m"
					],
			"timezone": "auto",
		}
		responses = self.openmeteo.weather_api(self.base_url, params = params)

		# Process first location. Add a for-loop for multiple locations or weather models
		response = responses[0]
		print(f"\nКоординаты: {response.Latitude()}°N {response.Longitude()}°E")
		print(f"Elevation: {response.Elevation()} m asl")
		print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
		# print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")
		current = response.Current()
		current_temperature_2m = current.Variables(0).Value()
		current_relative_humidity_2m = current.Variables(1).Value()
		print(f"Температура: {current_temperature_2m}")
		print(f"Влажность воздуха: {current_relative_humidity_2m}")
