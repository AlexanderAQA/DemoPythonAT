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
            self.click(AccountPageLocators.CHANGE_INFORMATION_BUTTON)

        return self

    def assert_field_headers(self):
        with allure.step("Проверка наличия всех основных заголовков полей на странице"):
            self.wait_for_element(AccountPageLocators.YOUR_ACCOUNT)
            self.wait_for_element(AccountPageLocators.NAME_PATRONYMIC)
            self.wait_for_element(AccountPageLocators.SURNAME)
            self.wait_for_element(AccountPageLocators.EMAIL)
            self.wait_for_element(AccountPageLocators.TELEPHONE)

        return self

    def assert_profile_field_values(self):
        with allure.step("Проверка значений во всех полях профиля"):
            self.wait_for_element(AccountPageLocators.get_text_in_name_field("Ольга"))
            self.wait_for_element(AccountPageLocators.get_text_in_surname_field("Тверская"))
            self.wait_for_element(AccountPageLocators.get_text_in_email_field("helgaautotests@gmail.com"))
            self.wait_for_element(AccountPageLocators.get_text_in_telephone_field("+7 (900) 000-00-00"))

        return self

    def assert_back_continue_buttons(self):
        with allure.step("Проверка наличия кнопок 'Назад' и 'Продолжить'"):
            self.wait_for_element(AccountPageLocators.BACK_BUTTON)
            self.wait_for_element(AccountPageLocators.CONTINUE_BUTTON)

        return self

    def assert_pers_account_and_home_buttons(self):
        with allure.step("Проверка наличия кнопок `Домой` и `Личный кабинет`"):
            self.wait_for_element(AccountPageLocators.HOME)
            self.wait_for_element(AccountPageLocators.PERS_ACCOUNT)

        return self
