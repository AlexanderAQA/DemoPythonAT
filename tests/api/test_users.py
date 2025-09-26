import pytest
from src.utils.api_client import *
from src.utils.assertions import assert_is_equal

@pytest.mark.positive
@pytest.mark.api
def test_get_user_returns_correct_user_data():
    user, status_code = get_user(1)

    assert_is_equal("Leanne Graham", user["name"])
    assert_is_equal(1, user["id"])
    assert_is_equal(200, status_code)

@pytest.mark.positive
@pytest.mark.api
def test_create_post_returns_new_post_data():
    title = "Hello World"
    body = "This is a test post."
    user_id = 1

    post, status_code = post_info(title = title, body = body, user_id = user_id)

    assert_is_equal(title, post["title"])
    assert_is_equal(body, post["body"])
    assert_is_equal(user_id, post["userId"])
    assert_is_equal(201, status_code)
