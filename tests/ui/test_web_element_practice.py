import allure
import pytest
import random
from locators.web_element_practice_locators import WebElementPracticeLocators as Practice
from src.utils.test_data import days, genders, countries, get_random_days


class TestWebElementPractice:

    @pytest.mark.ui
    @allure.title("Заполнение формы, проверки и нажатие Submit")
    def test_full_fill_form_and_submit(self, web_element_practice_page, generate_user):
        practice_page = web_element_practice_page
        test_user = generate_user

        random_days = get_random_days(days)
        random_gender = random.choice(genders)
        random_country = random.choice(countries)

        (practice_page
         .open_practice_page()
         .close_google_popup()
         .assert_is_visible(Practice.NAME_FIELD)
         .assert_is_visible(Practice.EMAIL_FIELD)
         .assert_is_visible(Practice.PHONE_FIELD)
         .assert_is_visible(Practice.ADDRESS_FIELD)
         .assert_is_visible(Practice.COUNTRY_DROPDOWN))

        (practice_page
         .fill_name_field(test_user["name"])
         .fill_email_field(test_user["email"])
         .fill_phone_field(test_user["phone"])
         .fill_address_field(test_user["address"]))

        (practice_page
         .select_gender(random_gender)
         .select_days(random_days)
         .select_country(random_country)
         .asserts.assert_is_equal(test_user["name"], practice_page.get_field_value(Practice.NAME_FIELD))
         .assert_is_equal(test_user["email"], practice_page.get_field_value(Practice.EMAIL_FIELD))
         .assert_is_equal(test_user["phone"], practice_page.get_field_value(Practice.PHONE_FIELD))
         .assert_is_equal(test_user["address"], practice_page.get_field_value(Practice.ADDRESS_FIELD)))
        practice_page.assert_is_checked(Practice.get_gender_button(random_gender))

        for day in random_days:
            practice_page.assert_is_checked(Practice.get_day_button(day))

        actual_country = practice_page.get_selected_country_value()
        (practice_page
            .asserts.assert_is_equal(random_country, actual_country))

        (practice_page
          .click_submit()
          .check_text_result("You selected"))
