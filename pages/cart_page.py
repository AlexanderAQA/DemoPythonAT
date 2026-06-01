import time
from locators.books_page_locators import BooksPageLocators
from pages.base_page import BasePage
import allure
from locators.cart_page_locators import CartPageLocators

class CartPage(BasePage):
    """Страница Корзина"""
    def __init__(self, driver):
        super().__init__(driver)

    def assert_quantity(self, expected: int):
        with allure.step(f"Проверка количества книг в корзине = {expected}"):
            actual = int(self.wait_for_element(CartPageLocators.get_quantity_input(expected)).get_attribute('value'))
            self.asserts.assert_is_equal(expected, actual)

        return self

    def clear_cart_button(self):
        with allure.step("Клик по кнопке очистки корзины"):
            self.click(CartPageLocators.CLEAR_CART_BUTTON)

            return self

    def clear_cart(self):
        with allure.step("Очистка корзины"):
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
        with allure.step(f"Сверка цены товара и стоимости в корзине"):
            self.assert_element_is_visible(CartPageLocators.get_cart_total_price(price))

        return self
