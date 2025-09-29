import allure
import pytest
from src.utils.api_client import ApiClient

@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("Sign")
@allure.story("Sign Feature Functionality")
@allure.severity(allure.severity_level.BLOCKER)
class TestUsersApi:

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("GET-запрос по ID пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://testit.example.com/tc-221", name="ТК 221")
    def test_get_user_returns_correct_user_data(self):
        client = ApiClient()
        user, status_code = client.get_user(1)

        (client.assertions
         .assert_is_equal("Leanne Graham", user["name"])
         .assert_is_equal(1, user["id"])
         .assert_is_equal(200, status_code))

    @pytest.mark.positive
    @pytest.mark.api
    @allure.title("POST-запрос для создание сообщения")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.link("https://testit.example.com/tc-1000", name="ТК 1000")
    def test_create_post_returns_new_post_data(self):
        client = ApiClient()

        title = "Hello World"
        body = "This is a test post."
        user_id = 1

        post, status_code = client.post_info(title = title, body = body, user_id = user_id)

        (client.assertions
         .assert_is_equal(title, post["title"])
         .assert_is_equal(body, post["body"])
         .assert_is_equal(user_id, post["userId"])
         .assert_is_equal(201, status_code))
