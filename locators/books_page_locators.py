from selenium.webdriver.common.by import By

class BooksPageLocators:
    """Локаторы страницы "Книги" ArtyShop"""

    # Всплывающее уведомление о добавлении товара в корзину на странице "Книги"
    PRODUCT_SUCCESS_ALERT = (By.XPATH, "//div[contains(@class, 'alert-success') "
                                       "and contains(., 'добавлен в корзину покупок')]")

    # Кнопка "Товаров в корзине" на странице "Книги"
    PRODUCT_IN_CART_BUTTON = (By.XPATH, "//button[@data-bs-toggle='dropdown' and ."
                                        "//i[contains(@class, 'fa-cart-shopping')]]")

    # Кнопка "Перейти в корзину" после нажатия на "Товаров в корзине" на странице "Книги"
    GO_TO_CART_BUTTON = (By.XPATH, "//a[normalize-space()='Перейти в корзину']")

    # Кнопка "Купить" в карточке книги
    @staticmethod
    def get_buy_button(book_name: str):
        locator = (By.XPATH, f"//div[contains(@class, 'product-thumb')][.//a[contains(text(),'{book_name}')]]"
                             f"//button[@class='cart-add-button']")

        return locator

    # Локатор названия книги
    @staticmethod
    def get_book_name(book_name: str):
        locator = (By.XPATH, f"//div[@id='content']//a[normalize-space()='{book_name}']")

        return locator

    # Локатор цены книги
    @staticmethod
    def get_book_price(book_name: str):
        locator = (By.XPATH, f"//h4[normalize-space()='{book_name}']/..//span[@class='price-new']")

        return locator
