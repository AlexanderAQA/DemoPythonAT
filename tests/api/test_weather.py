import allure
import pytest
import re


class TestWeather:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Получения страны из справочника")
    def test_get_weather(self, api_client_weather, capsys):
        #  Шаг 1: Вызов метода
        api_client_weather.get_weather()

        # Шаг 2: Перехват вывода консоли
        captured = capsys.readouterr()
        output = captured.out

        # Шаг 3: Извлечение данных через regex
        temp_match = re.search(r'Температура:\s*([-\d.]+)', output)
        humidity_match = re.search(r'Влажность воздуха:\s*([\d.]+)', output)

        assert temp_match, f"Не найдена температура в выводе:\n{output}"
        assert humidity_match, f"Не найдена влажность в выводе:\n{output}"

        temperature = float(temp_match.group(1))
        humidity = float(humidity_match.group(1))

        # Чтобы было видно в консоли, что там есть какие-то данные
        print(f"\n Температура: {temperature}")
        print(f" Влажность воздуха: {humidity}")

        #  Шаг 4: Проверки
        (api_client_weather.assertions
         .assert_is_not_none(temperature)
         .assert_is_not_none(humidity))

        # Проверка диапазонов
        assert -50 <= temperature <= 60, f"Температура вне пределов: {temperature}°C"
        assert 0 <= humidity <= 100, f"Влажность вне пределов: {humidity}%"
