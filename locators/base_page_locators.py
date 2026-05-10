from selenium.webdriver.common.by import By

class BasePageLocators:
    """Локаторы базовой страницы ArtyShop"""

    #Поле поиска на базовой странице
    SEARCH_INPUT_FIELD = (By.XPATH, "//input[contains(@class, 'form-control-lg')]")