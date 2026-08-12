import allure
import pytest
from locators.web_element_practice_locators import WebElementPracticeLocators as Practice


class TestWebElementPractice:

    @pytest.mark.ui
    @allure.title("Заполнение формы данными")
    def test_fill_form_with_test_users(self, web_element_practice_page, common_assertions, test_user_data):
        practice_page = web_element_practice_page
        assertions = common_assertions
        test_user = test_user_data

        (practice_page
         .open_practice_page()
         .close_google_popup()
         .assert_is_visible(Practice.NAME_FIELD)
         .assert_is_visible(Practice.EMAIL_FIELD)
         .assert_is_visible(Practice.COUNTRY_DROPDOWN)
         .fill_name_field(test_user["name"])
         .fill_email_field(test_user["email"])
         .fill_phone_field(test_user["phone"])
         .select_random_days())

        selected_gender, gender_locator = practice_page.select_gender("random")
        expected_country = practice_page.select_random_country()

        assertions.assert_is_equal(test_user["name"], practice_page.get_field_value(Practice.NAME_FIELD))
        assertions.assert_is_equal(test_user["email"], practice_page.get_field_value(Practice.EMAIL_FIELD))

        practice_page.assert_is_checked(gender_locator, f"Радиокнопка {selected_gender.capitalize()}")
        practice_page.assert_element_exists("день недели")

        actual_country = practice_page.get_selected_country_value()
        assertions.assert_is_not_empty(actual_country)
        assertions.assert_is_equal(expected_country, actual_country)
