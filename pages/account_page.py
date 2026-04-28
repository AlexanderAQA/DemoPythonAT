from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def assert_account_header(self):
        self.wait_for_element(AccountPageLocators.account_header)

        return self

    def assert_exit_button(self):
        self.wait_for_element(AccountPageLocators.exit_button)

        return self

    def assert_username(self):
        self.wait_for_element(AccountPageLocators.actual_username)

        return self