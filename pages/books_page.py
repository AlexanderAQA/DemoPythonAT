from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
import allure
from locators.books_page_locators import BooksPageLocators


class BooksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_buy_button(self, book_name):
        with allure.step("Клик по кнопке 'Купить'"):
            self.click(BooksPageLocators.get_buy_button(book_name))

        return self

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
            assert self.element_is_visible(BooksPageLocators.PRODUCT_SUCCESS_ALERT)

            return self

    def click_books_link(self):
        with allure.step(f"Клик по разделу 'Книги' в верхнем меню"):
            self.click(BasePageLocators.BOOKS_LINK)

            return self
