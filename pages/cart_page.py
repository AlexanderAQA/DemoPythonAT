from pages.base_page import BasePage
import allure
from locators.cart_page_locators import CartPageLocators

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def assert_quantity(self, expected: int = 1):
        with allure.step(f"Проверка количества книг в корзине = {expected}"):
            actual = int(self.wait_for_element(CartPageLocators.QUANTITY_INPUT).get_attribute('value'))
            assert actual == expected, f"Ожидаемо {expected}, фактически {actual}"

        return self

    def clear_cart(self):
        with allure.step("Клик по кнопке очистки корзины"):
            self.click(CartPageLocators. CLEAR_CART_BUTTON)

            return self
