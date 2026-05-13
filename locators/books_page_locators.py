from selenium.webdriver.common.by import By

class BooksPageLocators:
    """Локаторы страницы "Книги" ArtyShop"""

    # Кнопка "Купить" книга три книги Яна Арта "Книги"
    BUY_BUTTON = (By.XPATH, "//div[@id='content']//a[normalize-space()='3 в 1: три книги Яна Арта из серии «Библиотека Finversia»']")

    # Всплывающее уведомление о добавлении товара в корзину на странице "Книги"
    PRODUCT_SUCCESS_ALERT = (By.XPATH, "//div[contains(@class, 'alert-success') and contains(., 'добавлен') and contains(., 'в корзину покупок')]")

    # Кнопка "Товаров в корзине" на странице "Книги"
    PRODUCT_IN_CART_BUTTON = (By.XPATH, "//button[@data-bs-toggle='dropdown' and .//i[contains(@class, 'fa-cart-shopping')]]")

    # Кнопка "Перейти в корзину" после нажатия на "Товаров в корзине" на странице "Книги"
    GO_TO_CART_BUTTON = (By.XPATH, "//a[normalize-space()='Перейти в корзину']")