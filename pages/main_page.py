from pages.base_page import BasePage
from src.utils.logger import get_logger

class MainPage(BasePage):
    """Главная shop.finarty.ru"""
    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)

