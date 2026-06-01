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
