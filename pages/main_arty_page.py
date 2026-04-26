import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.old.login_page import LoginPage
from locators.main_page_locators import MainArtyPageLocators
from pages.base_page import BasePage

class MainArtyPage(BasePage):
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
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainArtyPageLocators.user_menu)
        ).click()
        return self

    def get_logged_in_username(self):
        """Получаем имя авторизованного пользователя"""
        return BasePage.get_element_text(self, self.actual_username)

    def click_authorization(self):
        locator = MainArtyPageLocators.authorization
        self.click(locator)

        return LoginPage(self.driver)


    def accept_cookies(self):
        try:
            self.click(self.MainArtyPageLocators.cookie_button, timeout=2)
        except:
            pass
        return self