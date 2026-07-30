import time
from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators
from src.utils.logger import get_logger

class CartPage(BasePage):
    """Страница Корзина"""
    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)

    def assert_quantity(self, expected: int):
        self.logger.info(f"Проверка количества книг в корзине = {expected}")
        actual = int(self.wait_for_element(CartPageLocators.get_quantity_input(expected)).get_attribute('value'))
        self.asserts.assert_is_equal(expected, actual)

        return self

    def clear_cart_button(self):
        self.logger.info(f"Клик по кнопке очистки корзины")
        self.click(CartPageLocators.CLEAR_CART_BUTTON)

        return self

    def clear_cart(self):
        self.logger.info(f"Очистка корзины")
        self.driver.get("https://shop.finarty.ru/cart")
        while self.driver.find_elements(*CartPageLocators.CLEAR_CART_BUTTON):
            self.clear_cart_button()
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except:
                pass
            time.sleep(0.3)

        return self

    def check_price(self, price: str):
        self.logger.info(f"Сверка цены товара и стоимости в корзине")
        self.assert_element_is_visible(CartPageLocators.get_cart_total_price(price))

        return self

    def check_size(self, size: str):
        self.logger.info(f"Сверка размера товара в корзине")
        self.assert_element_is_visible(CartPageLocators.get_cart_size(size))

        return self

    def check_sex(self, sex: str):
        self.logger.info(f"Сверка пола товара в корзине")
        self.assert_element_is_visible(CartPageLocators.get_cart_sex(sex))

        return self
