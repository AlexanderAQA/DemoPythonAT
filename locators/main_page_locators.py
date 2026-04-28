from selenium.webdriver.common.by import By


class MainPageLocators():
    """Локаторы главной страницы ArtyShop"""

    # Заголовок "Личный кабинет"
    user_menu = (By.XPATH, "//a[@class='dropdown-toggle']")

    # Кнопка "Авторизация" в выпадающем меню
    auth_button = (By.XPATH, f"//a[normalize-space(text())='Авторизация']")

    # Кнопка "ОК" принять cookies
    cookie_button = (By.XPATH, "//button[contains(@class, 'bg-primary') and normalize-space()='ОК']")
