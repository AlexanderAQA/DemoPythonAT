import allure
import pytest
import requests
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

    @pytest.mark.negative
    @pytest.mark.api
    @allure.title("Неверные параметры широта/долгота")
    def test_get_weather_negative_lat_long(self, api_client_weather):
        # Получаем ответ
        body, status_code = api_client_weather.get_weather_by_params(56*8584, -56.8584,
                                                                     ["temperature_2m", "relative_humidity_2m"], "auto",
                                                                     api_client_weather.base_url)

        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(400, status_code)
         .assert_is_equal({'error': True, 'reason': 'Latitude must be in range of -90 to 90°. Given: 480704.0.'}, body))



    @pytest.mark.negative
    @pytest.mark.api
    @allure.title("Неверные ключи температуры и влажности")
    def test_get_weather_negative_current(self, api_client_weather):
        # Получаем ответ
        body, status_code = api_client_weather.get_weather_by_params(56.8584, 35.9006,
                                                                     ["temperature", 123], "auto",
                                                                     api_client_weather.base_url)

        expected_error = {'reason': "Data corrupted at path ''. Cannot initialize SurfacePressureAndHeightVariable"
                                     "<VariableAndPreviousDay, VariableOrSpread<ForecastPressureVariable>, "
                                     "ForecastHeightVariable> from invalid String value 123.", 'error': True}
        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(400, status_code)
         .assert_is_equal(expected_error, body))



    @pytest.mark.negative
    @pytest.mark.api
    @allure.title("Неверный URL")
    def test_get_weather_invalid_url(self, api_client_weather):

        invalid_url = f"{api_client_weather.base_url}/wrong-path"

        # Получаем ответ
        body, status_code = api_client_weather.get_weather_by_params(
            56.8584, 35.9006,
            ["temperature_2m", "relative_humidity_2m"],
            "auto",
            invalid_url
        )

        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(404, status_code)
         .assert_is_equal({'reason': 'Not Found', 'error': True}, body))



    @pytest.mark.negative
    @pytest.mark.api
    @allure.title("Неверный HTTP-метод (POST вместо GET)")
    def test_get_weather_invalid_method(self, api_client_weather):
        # Получаем ответ
        body, status_code = api_client_weather.get_weather_by_params(
            56.8584, 35.9006,
            ["temperature_2m", "relative_humidity_2m"],
            "auto",
            api_client_weather.base_url,
            method=requests.post
        )

        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(415, status_code)
         .assert_is_equal({'error': True, 'reason': "Can't decode data without a content type"}, body))
