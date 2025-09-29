from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    """Главная страница после входа"""
    def __init__(self, driver):
        super().__init__(driver)

    # Локаторы
    actual_username = (By.XPATH, "//*[@id='pt-userpage']/a/span")

    def get_logged_in_username(self):
        """Получаем имя авторизованного пользователя"""
        return BasePage.get_element_text(self, self.actual_username)