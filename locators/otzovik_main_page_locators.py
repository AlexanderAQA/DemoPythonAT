from selenium.webdriver.common.by import By


class OtzovikMainPageLocators:
    """Локаторы главной страницы Otzovik"""

    SEARCH_FIELD = (By.ID, "header-search-input")
    SEARCH_BUTTON = (By.XPATH, "//input[@class='header-search-btn button2023 button-blue']")
    REVIEW_TAB = (By.XPATH, "//a[text()='Отзывы ']")
    NEGATIVE_TAB = (By.XPATH, "//a[text()='Негатив']")
    POSITIVE_TAB = (By.XPATH, "//a[text()='Позитив']")
    PROMOTION_TAB = (By.XPATH, "//a[@href='/promo/']")
