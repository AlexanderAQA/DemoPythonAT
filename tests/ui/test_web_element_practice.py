import allure
import pytest
import random
from src.utils.test_data import (days, genders, countries, get_random_days, get_random_colors, get_random_animal,
                                 colors, animals, negative_users)
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
         .assert_form()
         .fill_name_field(test_user.name)
         .fill_email_field(test_user.email)
         .fill_phone_field(test_user.phone)
         .fill_address_field(test_user.address)
         .select_colors(random_colors)
         .select_animal(random_animal)

         .select_future_date_1(future_date_1)
         .select_future_date_2(future_date_2)
         .select_start_date(start_date)
         .select_end_date(end_date))

        (practice_page
         .select_gender(random_gender)
         .select_days(random_days)
         .select_country(random_country)

         .assert_test_user_name(test_user.name)
         .assert_test_user_email(test_user.email)
         .assert_test_user_phone(test_user.phone)
         .assert_test_address(test_user.address)

         .assert_check_gender(random_gender))

        for day in random_days:
            practice_page.assert_check_day(day)

        actual_country = practice_page.get_selected_country_value()
        (practice_page
            .asserts.assert_is_equal(random_country, actual_country))

        (practice_page
            .assert_colors_selected(random_colors)
            .assert_animal_selected(random_animal)
            .assert_check_date_1(formated_date_1)
            .assert_check_date_2(formated_date_2)
            .assert_check_start_date(formated_start_date)
            .assert_check_end_date(formated_end_date))

        (practice_page
            .click_submit()
            .check_text_result("You selected"))
