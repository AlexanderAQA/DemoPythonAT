from dataclasses import dataclass

import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def assert_account_header(self):
        with (allure.step("Проверка, что заголовок 'Моя учетная запись' отображается")):
            assert self.wait_for_element(AccountPageLocators.account_header), \
                "Заголовок 'Моя учетная запись' отсутствует"
            return self


    def assert_exit_button(self):
        with allure.step("Проверка присутствия кнопки 'Выход' в личном кабинете"):
            assert self.wait_for_element(AccountPageLocators.exit_button), \
                "Кнопка 'Выход' отсутствует"

            return self

    def assert_username(self, expected_name: str = "Ольга"):
        with allure.step(f"Проверка актуального имени пользователя: '{expected_name}'"):
            actual_name = self.wait_for_element(AccountPageLocators.actual_username(expected_name)).text
            assert expected_name in actual_name, f"Ожидалось '{expected_name}', найдено '{actual_name}'"

            return self
