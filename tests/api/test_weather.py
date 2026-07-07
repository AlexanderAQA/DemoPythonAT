import allure
import pytest


class TestWeather:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Получения страны из справочника")
    def test_get_weather(self, api_client_weather):
        api_client_weather.get_weather()