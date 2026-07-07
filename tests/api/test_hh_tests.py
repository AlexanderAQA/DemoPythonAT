import allure
import pytest



class TestHH:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("Получения страны из справочника")
    def test_get_country(self, api_client_hh):
        expected_response = [
                              {
                                "id": "113",
                                "name": "Россия",
                                "url": "https://api.hh.ru/areas/113"
                              },
                              {
                                "id": "6",
                                "name": "Австралия",
                                "url": "https://api.hh.ru/areas/6"
                              }
                            ]

        response, status_code = api_client_hh.get_country_hh_user()

        (api_client_hh.assertions
            .assert_is_equal(200, status_code)
            .assert_is_equal(expected_response, response))
