import allure
from pages.base_page import BasePage

class MainPage(BasePage):
    """Главная shop.finarty.ru"""
    def __init__(self, driver):
        super().__init__(driver)
