from dataclasses import dataclass

import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def assert_account_header(self):
        with (allure.step("Проверка, что заголовок 'Моя учетная запись' отображается")):
            assert self.element_is_visible(AccountPageLocators.account_header), "Заголовок 'Моя учетная запись' отсутствует"

            return self


    def assert_exit_button(self):
        with allure.step("Проверка присутствия кнопки 'Выход' в личном кабинете"):
            assert self.wait_for_element(AccountPageLocators.exit_button), "Кнопка 'Выход' отсутствует"

            return self
