import allure
import pytest
from jsonschema import validate, ValidationError
from src.schemas.hh_areas_schema import HH_AREAS_SCHEMA

class TestHH:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Получения страны из справочника")
    def test_get_country_schema(self, api_client_hh):
        """Проверка, что ответ API соответствует ожидаемой JSON-схеме"""

        # Получаем ответ
        response, status_code = api_client_hh.get_country_hh_user()

        # 🔹Проверяем статус
        (api_client_hh.assertions
         .assert_is_equal(200, status_code)
         .assert_is_not_empty(response))

        # Валидация по JSON-схеме
        try:
            validate(instance=response, schema=HH_AREAS_SCHEMA)
        except ValidationError as e:
            pytest.fail(f"JSON не соответствует схеме: {e.message}\nПуть: {' -> '.join(map(str, e.path))}")

        # Проверки полей, что реально есть в ответе - первые 5 элементов. Названия должны быть строками,
        # координаты должны быть числами, идентификаторы должны быть строками.
        for item in response[:5]:
            assert isinstance(item.get("id"), str), f"id должен быть строкой: {item}"
            assert isinstance(item.get("name"), str), f"name должен быть строкой: {item}"
            if "lat" in item:
                assert isinstance(item["lat"], (int, float)), f"lat должен быть числом"
            if "lng" in item:
                assert isinstance(item["lng"], (int, float)), f"lng должен быть числом"
