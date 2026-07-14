import allure
import pytest
from jsonschema import validate, ValidationError
from src.schemas.weather_schema import WEATHER_RESPONSE_SCHEMA


class TestWeather:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Получение погоды")
    def test_get_weather(self, api_client_weather):
        """Проверка, что ответ API соответствует JSON-схеме.
        Получение погоды"""

        # Получаем ответ
        body, status_code = api_client_weather.get_weather_requests()

        # Базовая проверка статуса
        api_client_weather.assertions.assert_is_equal(200, status_code)

        # Валидация структуры ответа по JSON-схеме
        validate(instance=body, schema=WEATHER_RESPONSE_SCHEMA)

        # Извлечение и проверка температуры и влажности
        temperature = body["current"]["temperature_2m"]
        humidity = body["current"]["relative_humidity_2m"]

        # Ассерты
        (api_client_weather.assertions
         .assert_is_not_empty(temperature)
         .assert_is_not_empty(humidity))

        # Проверка диапазонов
        assert -50 <= temperature <= 60, f"Температура вне пределов: {temperature}°C"
        assert 0 <= humidity <= 100, f"Влажность вне пределов: {humidity}%"
