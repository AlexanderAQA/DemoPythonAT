import allure
import pytest
import random
from locators.web_element_practice_locators import WebElementPracticeLocators as Practice
from src.utils.test_data import (days, genders, countries, get_random_days, get_random_colors, get_random_animal,
                                 colors, animals)
from datetime import datetime, timedelta


class TestWebElementPractice:

    @pytest.mark.ui
    @allure.title("Заполнение формы, проверки и нажатие Submit")
    def test_full_fill_form_and_submit(self, web_element_practice_page, generate_user):
        practice_page = web_element_practice_page
        test_user = generate_user

        random_days = get_random_days(days)
        random_gender = random.choice(genders)
        random_country = random.choice(countries)
        random_colors = get_random_colors(colors)
        random_animal = get_random_animal(animals)

        future_date_1 = datetime.now() + timedelta(days=random.randint(10, 60))
        future_date_2 = datetime.now() + timedelta(days=random.randint(10, 60))
        start_date = datetime.now() + timedelta(days=random.randint(5, 20))
        end_date = start_date + timedelta(days=random.randint(10, 30))
        formated_date_1 = future_date_1.strftime("%m/%d/%Y")
        formated_date_2 = future_date_2.strftime("%d/%m/%Y")
        formated_start_date = start_date.strftime("%Y-%m-%d")
        formated_end_date = end_date.strftime("%Y-%m-%d")

        (practice_page
         .open_practice_page()
         .close_google_popup()
         .assert_is_visible(Practice.NAME_FIELD)
         .assert_is_visible(Practice.EMAIL_FIELD)
         .assert_is_visible(Practice.PHONE_FIELD)
         .assert_is_visible(Practice.ADDRESS_FIELD)
         .assert_is_visible(Practice.COUNTRY_DROPDOWN)
         .assert_is_visible(Practice.COLORS_LISTBOX)
         .assert_is_visible(Practice.ANIMALS_LISTBOX))

        (practice_page
         .fill_name_field(test_user["name"])
         .fill_email_field(test_user["email"])
         .fill_phone_field(test_user["phone"])
         .fill_address_field(test_user["address"])
         .select_colors(random_colors)
         .select_animal(random_animal)
         .select_date_from_calendar(Practice.DATE_PICKER_1, future_date_1)
         .select_date_from_calendar(Practice.DATE_PICKER_2, future_date_2)
         .fill_native_date(Practice.DATE_PICKER_3_START, start_date)
         .fill_native_date(Practice.DATE_PICKER_3_END, end_date))

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
            .assert_colors_selected(random_colors)
            .assert_animal_selected(random_animal)
            .asserts.assert_is_equal(formated_date_1, practice_page.get_field_value(Practice.DATE_PICKER_1))
            .assert_is_equal(formated_date_2, practice_page.get_field_value(Practice.DATE_PICKER_2))
            .assert_is_equal(formated_start_date, practice_page.get_field_value(Practice.DATE_PICKER_3_START))
            .assert_is_equal(formated_end_date, practice_page.get_field_value(Practice.DATE_PICKER_3_END)))

        (practice_page
            .click_submit()
            .check_text_result("You selected"))
