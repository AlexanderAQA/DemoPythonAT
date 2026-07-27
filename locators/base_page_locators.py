from selenium.webdriver.common.by import By

class BasePageLocators:
    """Локаторы базовой страницы ArtyShop"""

    # Поле поиска на базовой странице
    SEARCH_INPUT_FIELD = (By.XPATH, "//input[contains(@class, 'form-control-lg')]")

    # Локатор разделов
    @staticmethod
    def get_tab_link(tab_name: str):
        locator = (By.XPATH, f"//a[@class='dropdown-item' and contains (.,'{tab_name}')]")

        return locator

    # Кнопка "Купить" в карточке книги
    @staticmethod
    def get_buy_button(book_name: str):
        locator = (By.XPATH, f"//div[contains(@class, 'product-thumb')][.//a[contains(text(),'{book_name}')]]"
                             f"//button[@class='cart-add-button']")

        return locator