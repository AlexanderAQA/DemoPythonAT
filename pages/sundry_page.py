import allure
from selenium.webdriver.common.by import By

from locators.sundry_page_locators import SundryPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from src.utils.logger import get_logger
import random


class SundryPage(BasePage):
    """Страница Всякая всячина"""
    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)

    SEX_OPTIONS ={
        "male": "26",
        "female": "27"
    }

    SIZE_OPTIONS ={
        "S": "18",
        "M": "23",
        "L": "24",
        "XL": "17",
        "2XL": "25",
        "3XL": "561"
    }

    def click_sex_selector(self):
        self.logger.info(f"Клик по селектору")
        self.click(SundryPageLocators.SEX_SELECTOR)

        return self

    def click_size_selector(self):
        self.logger.info(f"Клик по селектору")
        self.click(SundryPageLocators.SIZE_SELECTOR)

        return self

    def select_sex(self, sex_key):
        self.logger.info(f"Выбор пола: {sex_key}")
        if sex_key not in self.SEX_OPTIONS:
            raise ValueError(f"Неизвестный пол: {sex_key}. Актуально: {list(self.SEX_OPTIONS.keys())}")

        element = self.wait_for_element(SundryPageLocators.SEX_SELECTOR)
        Select(element).select_by_value(self.SEX_OPTIONS[sex_key])

        return self

    def select_size(self, size_key):
        self.logger.info(f"Выбор размера: {size_key}")
        if size_key not in self.SIZE_OPTIONS:
            raise ValueError(f"Неизвестный размер: {size_key}. Актуально: {list(self.SIZE_OPTIONS.keys())}")

        element = self.wait_for_element(SundryPageLocators.SIZE_SELECTOR)
        Select(element).select_by_value(self.SIZE_OPTIONS[size_key])

        return self

    def select_random_sex(self):
        """Случайный выбор пола"""
        return self.select_sex(random.choice(list(self.SEX_OPTIONS.keys())))

    def select_random_size(self):
        """Случайный выбор размера"""
        return self.select_size(random.choice(list(self.SIZE_OPTIONS.keys())))

    def set_quantity(self, quantity: int):
        self.logger.info(f"Установка количества: {quantity}")
        # Локатор поля количества (универсальный для OpenCart)
        quantity_locator = (By.NAME, "quantity")
        element = self.wait_for_element(quantity_locator)
        element.clear()
        element.send_keys(str(quantity))

        return self

    def click_add_to_cart(self):
        self.logger.info("Клик по кнопке 'Купить' и переход в корзину из уведомления о добавлении")
        self.click(SundryPageLocators.ADD_TO_CART_BUTTON)
        self.wait_for_element(SundryPageLocators.PRODUCT_SUCCESS_ALERT)
        self.click(SundryPageLocators.CART_LINK_IN_ALERT)
        self.wait_for_element((By.ID, "checkout-total"))

        return self
