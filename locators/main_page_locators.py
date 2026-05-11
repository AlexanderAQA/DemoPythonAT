from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы ArtyShop"""

    # Заголовок "Личный кабинет"
    USER_MENU = (By.XPATH, "//a[@class='dropdown-toggle']")

    # Кнопка "Авторизация" в выпадающем меню
    AUTH_BUTTON = (By.XPATH, f"//a[normalize-space(text())='Авторизация']")

    # Кнопка "ОК" принять cookies
    COOKIE_BUTTON = (By.XPATH, "//button[contains(@value,'cookie.confirm&agree')]")
