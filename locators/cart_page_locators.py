from selenium.webdriver.common.by import By

class CartPageLocators:
    """Локаторы страницы "Книги" ArtyShop"""

    # Локатор книги "три книги Яна Арта" в корзине
    BOOK_LINK = (By.XPATH, "//td[contains(@class, 'text-start') and contains(@class, 'text-wrap')]//a[contains(., '3 в 1: три книги Яна Арта')]")

    # Локатор для поля количества книг корзине
    QUANTITY_INPUT = (By.XPATH, "//input[@data-cart-id='466']")

    # Локатор кнопки "Удалить" содержимое корзины
    CLEAR_CART_BUTTON = (By.XPATH, "//a[@title='Удалить']")

    # Локатор кнопки "Корзина" в хедере
    CART_LINK = (By.XPATH, "//a[@title='Корзина']")