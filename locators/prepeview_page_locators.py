from selenium.webdriver.common.by import By


class OtzovikPrereviewPageLocators:
    """Локаторы промежуточной страницы формы отзыва"""

    #Текст с отображением о правилах добавления отзыва
    RULES_ADD_REVIEW_TEXT = (By.XPATH, "//div[@class='postnote']")

    #Поле ввода текста
    FIELD_ENTRY_TEXT = (By.ID, "tproduct")