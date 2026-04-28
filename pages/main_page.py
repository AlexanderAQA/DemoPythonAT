import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    """Главная shop.finarty.ru"""
    def __init__(self, driver):
        super().__init__(driver)
        self.main_url = 'https://shop.finarty.ru/'


    def open_main_page(self):
        url = self.main_url
        with allure.step(f"Открываем главную страницу finarty: {url}"):
            self.driver.get(url)

        return self

    def open_user_menu(self):
        self.click(MainPageLocators.user_menu)

        return self

    def get_logged_in_username(self):
        """Получаем имя авторизованного пользователя"""
        return BasePage.get_element_text(self, MainPageLocators.actual_username)

    def click_authorization(self):
        self.click(MainPageLocators.auth_button)

        return self


    def accept_cookies(self):
        self.click(MainPageLocators.cookie_button)

        return self