from selenium.webdriver.common.by import By


class SundryPageLocators:
    """Локаторы страницы 'Всякая всячина' / Карточка товара"""

    # Селектор пола
    SEX_SELECTOR = (By.XPATH, "//select[contains(.,'Мужской')]")

    #Селектор размера
    SIZE_SELECTOR = (By.XPATH, "//select[contains(.,'2XL')]")

    # Кнопка "Купить" в карточке товара Всякой всячины
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")

    # Всплывающее уведомление об успешном добавлении
    PRODUCT_SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success, .alert.alert-dismissible")

    # Ссылка "Корзина" внутри уведомления (чтобы перейти в корзину)
    CART_LINK_IN_ALERT = (By.XPATH, "//div[contains(@class, 'alert-success')]//a[contains(@href, '/cart')]")
