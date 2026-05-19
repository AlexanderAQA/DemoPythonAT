from pages.base_page import BasePage
import allure
from locators.books_page_locators import BooksPageLocators


class BooksPage(BasePage):
    """Страница Книги"""
    def __init__(self, driver):
        super().__init__(driver)

    def click_buy_button(self, book_name):
        with allure.step("Клик по кнопке 'Купить'"):
            # написать явное ожидание в base page например на 200 мс.
            self.wait_for()
            self.driver.switch_to.default_content()
            self.click(BooksPageLocators.get_buy_button(book_name))

        return self

    def click_product_in_cart_button(self):
        with allure.step("Клик по кнопке 'Товар в корзине'"):
            element = self.wait_for_element(BooksPageLocators.PRODUCT_IN_CART_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)
        return self

    def click_go_to_cart_button(self):
        with allure.step("Клик по кнопке 'Перейти в корзину'"):
            element = self.wait_for_element(BooksPageLocators.GO_TO_CART_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

        return self

    def assert_product_added_alert(self):
        with allure.step("Проверка: уведомление о добавлении товара"):
            assert self.element_is_visible(BooksPageLocators.PRODUCT_SUCCESS_ALERT)

            return self


    def scroll_to_book(self, book_name):
        with allure.step(f"Прокрутка к кнопке Купить в книге: {book_name}"):
            element = self.wait_for_element(BooksPageLocators.get_buy_button(book_name))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            return self