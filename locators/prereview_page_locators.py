from selenium.webdriver.common.by import By


class OtzovikPrereviewPageLocators:
    """Локаторы промежуточной страницы формы отзыва"""

    #Текст с отображением о правилах добавления отзыва
    RULES_ADD_REVIEW_TEXT = (By.XPATH, "//div[@class='postnote']")

    #Поле ввода текста
    FIELD_ENTRY_TEXT = (By.ID, "tproduct")

    #Apple iPhone 17 Pro Max в результате поиска
    IPHONE_17_PRO_MAX_RESULT = (By.XPATH, "//a[contains(.,'Смартфон Apple iPhone ') and "
                                          "contains(.,'17') and contains(.,' Pro Max')]")

    #Заговок Apple iPhone 17 Pro Max
    IPHONE_17_PRO_MAX_RESULT_HEADLINE = (By.XPATH, "//h2[text()='Смартфон Apple iPhone 17 "
                                                   "Pro Max']")

    #Поле заголовка отзыва
    REVIEW_TITLE_FIELD = (By.ID, 'content_title')

    #Поле текста отзыва
    REVIEW_TEXT_FIELD = (By.XPATH, "//div[@class='editor-content ta2023']")

    #Фильм подарок с характером в результате поиска
    MOVIE_GIFT_WITH_CHARACTER = (By.XPATH, "//a[contains(., 'Подарок') and contains(., 'характером')]")

    #Заголовок отзыва универсальный
    HEADLINE_REVIEW_UNIVERSAL = (By.XPATH, "//h2[@class='product-name']")
