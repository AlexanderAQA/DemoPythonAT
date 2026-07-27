from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from src.utils.test_data import TestUsers
from src.utils.logger import get_logger


class AccountPage(BasePage):
    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)


    def assert_account_header(self):
        self.logger.info(f"Проверка, что заголовок 'Моя учетная запись' отображается")
        self.assert_element_is_visible(AccountPageLocators.ACCOUNT_HEADER)

        return self

    def assert_exit_button(self):
        self.logger.info(f"Проверка присутствия кнопки 'Выход' в личном кабинете")
        assert self.wait_for_element(AccountPageLocators.EXIT_BUTTON)

        return self

    def assert_username(self, user: TestUsers):
        self.logger.info(f"Проверка актуального имени пользователя: '{user.name}'")
        actual_name = self.wait_for_element(AccountPageLocators.get_actual_username(user.name)).text
        self.asserts.assert_is_equal(user.name, actual_name)

        return self

    def click_change_information(self):
        self.logger.info(f"Клик по кнопке 'Изменить информацию'")
        self.click(AccountPageLocators.CHANGE_INFO_BUTTON)

        return self

    def assert_field_headers(self):
        self.logger.info(f"Проверка наличия всех основных заголовков полей на странице")
        self.assert_element_is_visible(AccountPageLocators.HEAD_YOUR_ACCOUNT)
        self.assert_element_is_visible(AccountPageLocators.FIRSTNAME_FIELD_LABEL)
        self.assert_element_is_visible(AccountPageLocators.SURNAME_FIELD_LABEL)
        self.assert_element_is_visible(AccountPageLocators.EMAIL_FIELD_LABEL)
        self.assert_element_is_visible(AccountPageLocators.TELEPHONE_FIELD_LABEL)

        return self

    def assert_profile_field_values(self, expected: list):
        self.logger.info(f"Проверка значений во всех полях профиля")
        actual_name = self.wait_for_element(AccountPageLocators.TEXT_IN_NAME_FIELD).get_attribute('value'),
        actual_sur = self.wait_for_element(AccountPageLocators.TEXT_IN_SURNAME_FIELD).get_attribute('value'),
        actual_email = self.wait_for_element(AccountPageLocators.TEXT_IN_EMAIL_FIELD).get_attribute('value'),
        actual_phone = self.wait_for_element(AccountPageLocators.TEXT_IN_TELEPHONE_FIELD).get_attribute('value')
        actual_fields = [*actual_name, *actual_sur, *actual_email, actual_phone]

        self.asserts.assert_is_equal(expected, actual_fields)
        return self

    def assert_back_continue_buttons(self):
        self.logger.info(f"Проверка наличия кнопок 'Назад' и 'Продолжить'")
        self.assert_element_is_visible(AccountPageLocators.BACK_BUTTON)
        self.assert_element_is_visible(AccountPageLocators.CONTINUE_BUTTON)

        return self

    def assert_pers_account_and_home_buttons(self):
        self.logger.info(f"Проверка наличия кнопок `Домой` и `Личный кабинет`")
        self.assert_element_is_visible(AccountPageLocators.HOME_BUTTON_IN_ACCOUNT)
        self.assert_element_is_visible(AccountPageLocators.PERS_ACCOUNT_BUTTON)

        return self
