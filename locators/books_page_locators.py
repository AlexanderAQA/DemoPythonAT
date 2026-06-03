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

    # Локатор названия книги в карточке
    @staticmethod
    def get_book_cart_name(book_cart_name: str):
        locator = (By.XPATH, f"//h1[normalize-space()='{book_cart_name}']")

        return locator

    # Локатор цены книги в карточке
    @staticmethod
    def get_book_cart_price(book_price: str):
        locator = (By.XPATH, f"//span[@class='price-new' and normalize-space()='{book_price}']")

        return locator

    # Локатор артикула книги в карточке
    @staticmethod
    def get_book_article_code(article_code: str):
        locator = (By.XPATH, f"//li[contains(text(), 'Артикул')]/b[normalize-space()='{article_code}']")

        return locator

    # Локатор количества книг в карточке
    @staticmethod
    def get_book_quantity(quantity: int):
        locator = (By.XPATH, f"//input[@id='input-quantity' and @value='{quantity}']")

        return locator

    # Список локаторов для всех книг в описании
    @staticmethod
    def get_books_in_description():
        locators = [
            (By.XPATH, "//div[@id='tab-description']//strong[contains(text(), 'Клякса в небе и фифти-фифти')]"),
            (By.XPATH, "//div[@id='tab-description']//strong[contains(text(), '1000 лет одиночества')]"),
            (By.XPATH, "//div[@id='tab-description']//strong[contains(text(), 'Обратный отсчет')]")
        ]

        return locators

    # Локатор количества в закладках
    @staticmethod
    def get_count_of_bookmarks(count: int):
        locator = (By.XPATH, f"//span[contains(@class, 'd-lg-inline') and normalize-space()='Закладки ({count})']")

        return locator

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

    # Локатор названия книги "Клякса в небе и фифти-фифти" в описании карточки
    KLYAKSA_BOOK = (By.XPATH, "//div[@id='tab-description']//strong[contains(text(), 'Клякса в небе и фифти-фифти')]")

    # Локатор названия книги "1000 лет одиночества" в описании карточки
    THOUSAND_YEARS_BOOK = (By.XPATH, "//div[@id='tab-description']//strong[contains(text(), '1000 лет одиночества')]")

    # Локатор названия книги "Обратный отсчет" в описании карточки
    COUNTDOWN_BOOK = (By.XPATH, "//div[@id='tab-description']//strong[contains(text(), 'Обратный отсчет')]")

    # Локатор фразы "Книги поставляются с автографом автора" в описании карточки
    PHRASE_AUTOGRAPH = (By.XPATH, "//div[@id='tab-description']//span[contains(text(), 'автографом')]")