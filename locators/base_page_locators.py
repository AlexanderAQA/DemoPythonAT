from selenium.webdriver.common.by import By

class BaseArtyPageLocators():
    """Локаторы главной страницы ArtyShop"""

    user_menu = (By.XPATH, f"//a[@class='dropdown-toggle']")
