from pages.base_page import BasePage
import allure
from locators.account_page_locators import AccountPageLocators
from src.utils.test_data import TestUsers


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def assert_account_header(self):
        with allure.step("Проверка, что заголовок 'Моя учетная запись' отображается"):
            self.assert_element_is_visible(AccountPageLocators.ACCOUNT_HEADER)

            return self

    def assert_exit_button(self):
        with allure.step("Проверка присутствия кнопки 'Выход' в личном кабинете"):
            assert self.wait_for_element(AccountPageLocators.EXIT_BUTTON)

            return self

    def assert_username(self, user: TestUsers):
        with allure.step(f"Проверка актуального имени пользователя: '{user.name}'"):
            actual_name = self.wait_for_element(AccountPageLocators.get_actual_username(user.name)).text
            self.asserts.assert_is_equal(user.name, actual_name)

            return self

    def click_change_information(self):
        with allure.step("Клик по кнопке 'Изменить информацию'"):
            self.click(AccountPageLocators.CHANGE_INFO_BUTTON)

        return self

    def assert_field_headers(self):
        with allure.step("Проверка наличия всех основных заголовков полей на странице"):
            self.assert_element_is_visible(AccountPageLocators.HEAD_YOUR_ACCOUNT)
            self.assert_element_is_visible(AccountPageLocators.FIRSTNAME_FIELD_LABEL)
            self.assert_element_is_visible(AccountPageLocators.SURNAME_FIELD_LABEL)
            self.assert_element_is_visible(AccountPageLocators.EMAIL_FIELD_LABEL)
            self.assert_element_is_visible(AccountPageLocators.TELEPHONE_FIELD_LABEL)

        return self

    def assert_profile_field_values(self, expected: list):
        with allure.step("Проверка значений во всех полях профиля"):
            actual_name = self.wait_for_element(AccountPageLocators.TEXT_IN_NAME_FIELD).get_attribute('value'),
            actual_sur = self.wait_for_element(AccountPageLocators.TEXT_IN_SURNAME_FIELD).get_attribute('value'),
            actual_email = self.wait_for_element(AccountPageLocators.TEXT_IN_EMAIL_FIELD).get_attribute('value'),
            actual_phone = self.wait_for_element(AccountPageLocators.TEXT_IN_TELEPHONE_FIELD).get_attribute('value')
            actual_fields = [*actual_name, *actual_sur, *actual_email, actual_phone]

            self.asserts.assert_is_equal(expected, actual_fields)
        return self

    def assert_back_continue_buttons(self):
        with allure.step("Проверка наличия кнопок 'Назад' и 'Продолжить'"):
            self.assert_element_is_visible(AccountPageLocators.BACK_BUTTON)
            self.assert_element_is_visible(AccountPageLocators.CONTINUE_BUTTON)

        return self

    def assert_pers_account_and_home_buttons(self):
        with allure.step("Проверка наличия кнопок `Домой` и `Личный кабинет`"):
            self.assert_element_is_visible(AccountPageLocators.HOME_BUTTON_IN_ACCOUNT)
            self.assert_element_is_visible(AccountPageLocators.PERS_ACCOUNT_BUTTON)

        return self
