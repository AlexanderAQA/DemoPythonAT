from selenium.webdriver.common.by import By

class BasePageLocators:
    """Локаторы базовой страницы ArtyShop"""

    #Поле поиска на базовой странице
    search_input_field = (By.XPATH, "//input[contains(@class, 'form-control-lg')]")