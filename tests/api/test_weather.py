import allure
import pytest
import re
from jsonschema import validate, ValidationError
from src.schemas.weather_schema import WEATHER_RESPONSE_SCHEMA


class TestWeather:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Получение погоды")
    def test_get_weather(self, api_client_weather):
        body, status_code = api_client_weather.get_weather_requests()

        temperature = body["current"]["temperature_2m"]
        humidity = body["current"]["relative_humidity_2m"]
        print(f"{temperature}°C, {humidity}%")

        (api_client_weather.assertions
         .assert_is_equal(200, status_code)
         .assert_is_not_none(temperature)
         .assert_is_not_none(humidity))

        assert isinstance(temperature, (int, float)), f"Температура должна быть числом"
        assert isinstance(humidity, (int, float)), f"Влажность должна быть числом"
        assert -50 <= temperature <= 60, f"Температура вне пределов: {temperature}°C"
        assert 0 <= humidity <= 100, f"Влажность вне пределов: {humidity}%"


    def test_get_weather_schema_validation(self, api_client_weather):
        """Проверка, что ответ API соответствует ожидаемой JSON-схеме"""
        body, status_code = api_client_weather.get_weather_requests()

        api_client_weather.assertions.assert_is_equal(200, status_code)

        try:
            validate(instance=body, schema=WEATHER_RESPONSE_SCHEMA)
        except ValidationError as e:
            pytest.fail(f"JSON не соответствует схеме: {e.message}\nПуть: {' -> '.join(map(str, e.path))}")

        temperature = body["current"]["temperature_2m"]
        humidity = body["current"]["relative_humidity_2m"]
        print(f"{temperature}°C, {humidity}%")

        assert -50 <= temperature <= 60, f"Температура вне пределов: {temperature}°C"
        assert 0 <= humidity <= 100, f"Влажность вне пределов: {humidity}%"

