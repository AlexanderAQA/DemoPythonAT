from locators.cart_page_locators import CartPageLocators
from pages.base_page import BasePage
from src.utils.logger import get_logger


class SundryPage(BasePage):
    """Страница Всякая всячина"""
    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)

    SEX_OPTIONS ={
        "select": " --- Выберите --- ",
        "male": 26,
        "female": 27
    }

    SIZE_OPTIONS ={
        "select": " --- Выберите --- ",
        "S": 18,
        "M": 23,
        "L": 24,
        "XL": 17,
        "2XL": 25,
        "3XL": 561
    }

    def click_sex_selector(self):
        self.logger.info(f"Клик по селектору")
        self.click(CartPageLocators.SEX_SELECTOR)

        return self

    def click_size_selector(self):
        self.logger.info(f"Клик по селектору")
        self.click(CartPageLocators.SIZE_SELECTOR)

        return self
