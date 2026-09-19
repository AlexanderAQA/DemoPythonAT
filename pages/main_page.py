from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from src.utils.logger import get_logger

class MainPage(BasePage):
    """Главная shop.finarty.ru"""
    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)

    def check_banner(self):
        self.assert_element_is_visible(MainPageLocators.PROMOTION_BANNER)
        return self


