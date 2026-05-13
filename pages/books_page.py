from pages.base_page import BasePage
import allure
import time
from locators.books_page_locators import BooksPageLocators


class BooksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # def click_buy_button(self):
    #     with allure.step("Клик по кнопке 'Купить' три книги Яна Арта"):
    #         self.click(BooksPageLocators.BUY_BUTTON)
    #
    #     return self

    def click_product_in_cart_button(self):
        with allure.step("Клик по кнопке `Товаров`"):
            self.click(BooksPageLocators.PRODUCT_IN_CART_BUTTON)

        return self

    def click_go_to_cart_button(self):
        with allure.step("Клик по кнопке перехода в корзину"):
            self.click(BooksPageLocators.GO_TO_CART_BUTTON)

        return self

    def assert_product_added_alert(self):
        with allure.step("Проверка: уведомление о добавлении товара"):
            assert self.wait_for_element(BooksPageLocators.PRODUCT_SUCCESS_ALERT)

            return self

    def scroll_down(self, pixels: int = 250):
        with allure.step(f"Прокрутка страницы вниз на {pixels}px"):
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
            time.sleep(0.2)

        return self