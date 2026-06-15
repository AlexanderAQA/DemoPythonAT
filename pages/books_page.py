from pages.base_page import BasePage
import allure
from locators.books_page_locators import BooksPageLocators


class BooksPage(BasePage):
    """Страница Книги"""
    def __init__(self, driver):
        super().__init__(driver)

    def click_buy_button(self, book_name):
        with allure.step("Клик по кнопке 'Купить'"):
            self.wait_for()
            self.driver.switch_to.default_content()
            self.click(BooksPageLocators.get_buy_button(book_name))

        return self

    def click_product_in_cart_button(self):
        with allure.step(f"Клик по кнопке 'Товар в корзине'"):
            element = self.wait_for_element(BooksPageLocators.PRODUCT_IN_CART_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

        return self

    def click_go_to_cart_button(self):
        with allure.step(f"Клик по кнопке 'Перейти в корзину'"):
            element = self.wait_for_element(BooksPageLocators.GO_TO_CART_BUTTON)
            self.driver.execute_script("arguments[0].click();", element)

        return self

    def assert_product_added_alert(self):
        with allure.step(f"Проверка: уведомление о добавлении товара"):
            self.assert_element_is_visible(BooksPageLocators.PRODUCT_SUCCESS_ALERT)

            return self


    def scroll_to_book(self, book_name):
        with allure.step(f"Прокрутка к кнопке Купить в книге: {book_name}"):
            element = self.wait_for_element(BooksPageLocators.get_buy_button(book_name))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

            return self

    def get_price_from_book(self, book_name: str):
        with allure.step(f"Сохранение цены книги"):
            book_price = self.wait_for_element(BooksPageLocators.get_book_price(book_name)).text

        return book_price

    def click_book_by_name(self, book_name: str):
        with allure.step(f"Клик по карточке книги '{book_name}'"):
            element = self.wait_for_element(BooksPageLocators.get_book_name(book_name))
            self.driver.execute_script("arguments[0].click();", element)

        return self

    def assert_book_cart_name_displayed(self, book_cart_name):
        with allure.step(f"Проверка отображения названия книги"):
            self.assert_element_is_visible(BooksPageLocators.get_book_cart_by_name(book_cart_name))

        return self

    def assert_book_cart_price_displayed(self, book_price):
        with allure.step(f"Проверка отображения цены"):
            self.assert_element_is_visible(BooksPageLocators.GET_BOOK_CART_PRICE)
            actual_text = self.wait_for_element(BooksPageLocators.GET_BOOK_CART_PRICE).text
            actual_clean = ''.join([c for c in actual_text if c.isdigit()])
            expected_clean = ''.join([c for c in str(book_price) if c.isdigit()])
            self.asserts.assert_is_equal(expected_clean, actual_clean)

        return self

    def assert_article_code_displayed(self, article_code):
        with allure.step(f"Проверка отображения названия, цены и артикула"):
            self.assert_element_is_visible(BooksPageLocators.get_book_by_article(article_code))

        return self

    def assert_article_label_displayed(self):
        with allure.step(f"Проверка отображения названия, цены и артикула"):
            self.assert_element_is_visible(BooksPageLocators.ARTICLE_LABEL)

        return self

    def get_quantity_books(self):
        with allure.step(f"Получить текущее количество книг"):
            value = self.wait_for_element(BooksPageLocators.QUANTITY_BOOKS).get_attribute('value')
            quantity_books = int(value)

            return quantity_books

    def click_plus_button(self):
        with allure.step(f"Кликнуть плюс"):
            self.click(BooksPageLocators.PLUS_BUTTON)

            return self

    def assert_plus(self, expected_count):
        with allure.step(f"Проверить, что после плюса стало {expected_count}"):
            actual_plus = int(self.wait_for_element(BooksPageLocators.QUANTITY_BOOKS).get_attribute('value'))
            self.asserts.assert_is_equal(expected_count, actual_plus)

        return self

    def click_minus_button(self):
        with allure.step(f"Кликнуть минус"):
            self.click(BooksPageLocators.MINUS_BUTTON)

            return self

    def assert_minus(self, expected_count):
        with allure.step(f"Проверить, что после минуса вернулось {expected_count}"):
            actual_minus = int(self.wait_for_element(BooksPageLocators.QUANTITY_BOOKS).get_attribute('value'))
            self.asserts.assert_is_equal(expected_count, actual_minus)

        return self

    def assert_description_content(self, expected_book_name: str):
        with allure.step(f"Проверка наличия названий книги и фразы про автограф в описании"):
            self.assert_element_is_visible(BooksPageLocators.get_name_book_in_description(expected_book_name))
            self.assert_element_is_visible(BooksPageLocators.PHRASE_AUTOGRAPH)

        return self

    def get_wishlist_count(self):
        with allure.step(f"Получить текущее количество избранного"):
            text = self.wait_for_element(BooksPageLocators.GET_COUNT_OF_BOOKMARKS).text
            wishlist_count = int(text.split('(')[1].split(')')[0])

            return wishlist_count

    def click_add_to_wishlist(self):
        with allure.step(f"Кликнуть на добавить в избранное"):
            self.click(BooksPageLocators.ADD_TO_FAVORITES_BUTTON)

            return self

    def assert_wishlist_count_add(self, expected_count):
        with allure.step(f"Проверить количество закладок после добавления +1"):
            text = self.wait_for_element(BooksPageLocators.GET_COUNT_OF_BOOKMARKS).text
            actual_list = int(text.split('(')[1].split(')')[0])
            self.asserts.assert_is_equal(expected_count, actual_list)

        return self

    def click_delete_from_wishlist(self):
        with allure.step(f"Кликнуть на удалить из избранного"):
            self.click(BooksPageLocators.DELETE_FROM_FAVORITES_BUTTON)

            return self

    def assert_wishlist_count_delete(self, expected_count):
        with allure.step(f"Проверить количество закладок после удаления -1"):
            text = self.wait_for_element(BooksPageLocators.GET_COUNT_OF_BOOKMARKS).text
            actual_list = int(text.split('(')[1].split(')')[0])
            self.asserts.assert_is_equal(expected_count, actual_list)

        return self
