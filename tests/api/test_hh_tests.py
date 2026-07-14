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

        # Проверяем статус
        (api_client_hh.assertions
         .assert_is_equal(200, status_code)
         .assert_is_not_empty(response))

        # Валидация по JSON-схеме
        validate(instance=response, schema=HH_AREAS_SCHEMA)
