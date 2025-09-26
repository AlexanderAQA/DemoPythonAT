from pages.base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver

class MainPage(BasePage):
    """Главная страница после логина"""
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы
    actual_username = (By.XPATH, "//*[@id='pt-userpage']/a/span")

    def get_logged_in_username(self):
        """Получаем имя авторизованного пользователя в нижнем регистре"""
        element = self.driver.find_element(*self.actual_username)
        return element.text.lower()