import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from src.utils.logger import get_logger

class OtzovikMainPage(BasePage):
    """Главная https://otzovik.com/"""

    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/'

    def open(self):
        self.driver.get(self.url)
        return self
