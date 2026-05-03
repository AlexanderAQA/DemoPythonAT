import allure

from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def assert_account_header(self):
        with allure.step(f"Проверка заголовка элемента `Моя учетная запись`"):
         self.wait_for_element(AccountPageLocators.account_header)

        return self

    def assert_exit_button(self):
        with allure.step(f"Проверка кнопки `Выход` в ЛК после авторизации"):
         self.wait_for_element(AccountPageLocators.exit_button)

        return self


    def assert_username(self, expected_name: str = "Ольга"):
        with allure.step(f"Проверка актуального имени пользователя: '{expected_name}'"):
         actual_text = self.wait_for_element(AccountPageLocators.actual_username(expected_name)).text
         assert expected_name in actual_text, f"Ожидалось '{expected_name}', найдено '{actual_text}'"

        return self