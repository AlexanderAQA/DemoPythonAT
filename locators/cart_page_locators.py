from selenium.webdriver.common.by import By

class CartPageLocators:
    """Локаторы страницы "Корзина" ArtyShop"""

    # Локатор книги "три книги Яна Арта" в корзине
    # TODO: локатор конкретной книги удалить, потому что ниже есть метод, через который нужно работать
    BOOK_LINK = (By.XPATH, "//td[contains(@class, 'text-start') and contains(@class, 'text-wrap')]//a[contains(., '3 в 1: три книги Яна Арта')]")

    # Локатор для поля количества книг корзине
    # TODO: локатор конкретного количества удалить, потому что ниже есть метод, через который нужно работать
    QUANTITY_INPUT = (By.XPATH, "//input[@data-cart-id='466']")

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
    def get_quantity_input(number: int, book_name: str):
        locator = (By.XPATH, f"//input[@data-cart-id='{number}' and contains='{book_name}']")

        return locator