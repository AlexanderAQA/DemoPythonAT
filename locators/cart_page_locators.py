from selenium.webdriver.common.by import By

class CartPageLocators:
    """Локаторы страницы "Корзина" ArtyShop"""

    # Локатор кнопки "Удалить" содержимое корзины
    CLEAR_CART_BUTTON = (By.XPATH, "//a[@title='Удалить']")

    # Локатор кнопки "Корзина" в хедере
    CART_LINK = (By.XPATH, "//a[@title='Корзина']")

    # Локатор книги для добавления в корзину
    @staticmethod
    def get_book_link(book_name: str):
        locator = (By.XPATH, f"//td[contains(@class, 'text-start') and contains(@class, 'text-wrap')]//a[contains='{book_name}']")

        return locator

    # Локатор для поля количества книг корзине
    @staticmethod
    def get_quantity_input(value: int):
        locator = (By.XPATH, f"//input[@name='quantity' and @type='number']")

        return locator
