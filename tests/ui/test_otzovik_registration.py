import allure
import pytest
from src.utils.test_data import negative_users


@pytest.mark.ui
@allure.title("Заполнение формы, проверки и нажатие Submit")
@pytest.mark.parametrize("user", negative_users)
def test_fields_validation(self, practice_page, user):
    (practice_page
     .open_practice_page()
     .close_google_popup()
     .fill_name_field(user.name)
     .fill_email_field(user.email)
     .fill_phone_field(user.phone)
     .fill_address_field(user.address)
     .assert_is_equal