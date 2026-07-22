from src.utils.logger import get_logger


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
        # Получаем ответ
        body, status_code = api_client_weather.get_weather_requests()

        # Валидация структуры ответа по JSON-схеме
        validate(instance=body, schema=WEATHER_RESPONSE_SCHEMA)

        # Извлечение и проверка температуры и влажности
        temperature = body["current"]["temperature_2m"]
        humidity = body["current"]["relative_humidity_2m"]

        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(200, status_code)
         .assert_is_not_empty(temperature)
         .assert_is_not_empty(humidity)
         .assert_in_range(-50, temperature, 60)
         .assert_in_range(0, humidity, 100))


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

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Почасовые данные погоды")
    def test_get_weather_hourly(self, api_client_weather):
        # Получаем ответ
        body, status_code = api_client_weather.get_weather_by_hourly()

        # Извлекаем первые значения за час прогноза
        hourly = body["hourly"]
        temperature = hourly["temperature_2m"][0]
        precipitation = hourly["precipitation"][0]
        wind_speed = hourly["wind_speed_10m"][0]

        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(200, status_code)
         .assert_is_not_empty(temperature)
         .assert_is_not_empty(precipitation)
         .assert_is_not_empty(wind_speed)
         .assert_in_range(-50, temperature, 60)
         .assert_in_range(0, precipitation, 500)
         .assert_in_range(0, wind_speed, 300))


    @pytest.mark.negative
    @pytest.mark.api
    @allure.title("Неверные параметры широта/долгота (hourly)")
    def test_get_weather_hourly_negative_lat_long(self, api_client_weather):
        # Ответ
        body, status_code = api_client_weather.get_weather_by_params(
            56 * 8584, -56.8584,
            ["temperature_2m", "precipitation", "wind_speed_10m"], "auto",
            api_client_weather.base_url
        )
        expected_error = {'reason': 'Latitude must be in range of -90 to 90°. Given: 480704.0.', 'error': True}

        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(400, status_code)
         .assert_is_equal(expected_error, body))




    @pytest.mark.negative
    @pytest.mark.api
    @allure.title("Неверные ключи hourly параметров")
    def test_get_weather_hourly_negative_keys(self, api_client_weather):
        # Ответ
        body, status_code = api_client_weather.get_weather_by_params(
            56.8584, 35.9006,
            ["invalid_temp", "fake_precipitation", 123], "auto",
            api_client_weather.base_url
        )
        expected_error = {'error': True, 'reason': "Data corrupted at path ''. Cannot initialize "
                                                   "SurfacePressureAndHeightVariable<VariableAndPreviousDay, "
                                                   "VariableOrSpread<ForecastPressureVariable>, "
                                                   "ForecastHeightVariable> from invalid String value invalid_temp."}

        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(400, status_code)
         .assert_is_equal(expected_error, body))



    @pytest.mark.negative
    @pytest.mark.api
    @allure.title("Неверный URL (hourly)")
    def test_get_weather_hourly_invalid_url(self, api_client_weather):
        invalid_url = f"{api_client_weather.base_url}/wrong-hourly-path"

        # Ответ
        body, status_code = api_client_weather.get_weather_by_params(
            56.8584, 35.9006,
            ["temperature_2m", "precipitation", "wind_speed_10m"],
            "auto",
            invalid_url
        )
        expected_error = {'error': True, 'reason': 'Not Found'}

        # Ассерты
        (api_client_weather.assertions
         .assert_is_equal(404, status_code)
         .assert_is_equal(expected_error, body))


    @pytest.mark.negative
    @pytest.mark.api
    @allure.title("Неверный HTTP-метод (POST вместо GET) hourly")
    def test_get_weather_hourly_invalid_method(self, api_client_weather):
        # Ответ
        body, status_code = api_client_weather.get_weather_by_params(
            56.8584, 35.9006,
            ["temperature_2m", "precipitation", "wind_speed_10m"],
            "auto",
            api_client_weather.base_url,
            method=requests.post
        )
        expected_error = {'error': True, 'reason': "Can't decode data without a content type"}

        # Проверка кода ошибки
        (api_client_weather.assertions
         .assert_is_equal(415, status_code)
         .assert_is_equal(expected_error, body))
