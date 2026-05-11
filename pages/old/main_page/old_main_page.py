from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.old.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class OldMainPage(BasePage):
    """Главная страница после входа"""
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    actual_username = (By.XPATH, "//*[@id='pt-userpage']/a/span")

    def open_main_page(self, url: str = "https://shop.finarty.ru"):
        self.driver.get(url)
        return self

    def open_user_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.USER_MENU)
        ).click()
        return self

    def get_logged_in_username(self):
        """Получаем имя авторизованного пользователя"""
        return BasePage.get_element_text(self, self.actual_username)

    def click_authorization(self):
        locator = MainPageLocators.AUTH_BUTTON
        self.click(locator)

        return LoginPage(self.driver)

    def accept_cookies(self):
        try:
            cookie_btn = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable(MainPageLocators.COOKIE_BUTTON)
            )
            cookie_btn.click()
        except Exception:
            pass
        return self