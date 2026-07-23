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

    # Локатор фразы "Книги поставляются с автографом автора" в описании карточки
    PHRASE_AUTOGRAPH = (By.XPATH, "//div[@id='tab-description']"
                                  "//span[contains(text(), 'Книга поставляется с автографом автора')]")

    # Локатор количества книг в карточке
    QUANTITY_BOOKS = (By.XPATH, f"//input[@id='input-quantity']")

    # Локатор лейбла "Артикул" книги в карточке
    ARTICLE_LABEL = (By.XPATH, "//li[contains(text(), 'Артикул')]")

    # Локатор кнопки + в карточке
    PLUS_BUTTON = (By.XPATH, "//span[@class='bt_plus']")

    # Локатор кнопки - в карточке
    MINUS_BUTTON = (By.XPATH, "//span[@class='bt_minus']")

    # Локатор кнопки "Добавить в избранное" в карточке
    ADD_TO_FAVORITES_BUTTON = (By.XPATH, "//button[@title='Добавить в закладки']")

    # Локатор кнопки "Удалить из закладок" в карточке
    DELETE_FROM_FAVORITES_BUTTON = (By.XPATH, "//button[@title='Удалить из закладок']")

    # Локатор количества в закладках
    GET_COUNT_OF_BOOKMARKS = (By.XPATH, "//span[contains(@class, 'd-lg-inline') and contains(text(), 'Закладки')]")

    # Локатор цены книги в карточке
    GET_BOOK_CART_PRICE = (By.XPATH, "//span[@class='price-new']")

    # Локатор селектора сортировки
    SORT_SELECTOR = (By.ID, "input-sort")

    # Локатор селектора от А до Я
    NAME_A_Z = (By.XPATH, "//option[@value='https://shop.finarty.ru?sort=pd.name&order=ASC']")

    # Все названия книг на странице (универсальный)
    COMMON_BOOK_NAMES = (By.CSS_SELECTOR, "#product-list h4 a")

    # Кнопка "Купить" в карточке книги
    @staticmethod
    def get_buy_button(book_name: str):
        locator = (By.XPATH, f"//div[contains(@class, 'product-thumb')][.//a[contains(text(),'{book_name}')]]"
                             f"//button[@class='cart-add-button']")

        return locator

    # Локатор названия книги на странице "Книги"
    @staticmethod
    def get_book_name(book_name: str):
        locator = (By.XPATH, f"//a[contains(normalize-space(), '{book_name}')]")

        return locator

    # Локатор цены книги
    @staticmethod
    def get_book_price(book_name: str):
        locator = (By.XPATH, f"//h4[normalize-space()='{book_name}']/..//span[@class='price-new']")

        return locator

    # Локатор названия книги в карточке
    @staticmethod
    def get_book_cart_by_name(book_cart_name: str):
        locator = (By.XPATH, f"//h1[normalize-space()='{book_cart_name}']")

        return locator

    # Локатор артикула книги в карточке
    @staticmethod
    def get_book_by_article(article_code: str):
        locator = (By.XPATH, f"//li[contains(text(), 'Артикул')]/b[normalize-space()='{article_code}']")

        return locator

    #Локатор названия книг в описании карточки товара
    @staticmethod
    def get_name_book_in_description(name_in_description: str):
        locator = (By.XPATH, f"//div[@id='tab-description']//strong[contains(text(), '{name_in_description}')]")

        return locator
