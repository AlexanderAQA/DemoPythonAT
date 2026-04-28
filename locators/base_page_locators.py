from selenium.webdriver.common.by import By

class BasePageLocators():
    """Локаторы главной страницы ArtyShop"""

    search_input_field = (By.XPATH, "//input[@id='searchInput']")

    # Кнопка "Войти"
    login_button = (By.XPATH, f"//button[@type='submit' and normalize-space(text())='Войти']")

    # Поле ввода E-Mail на странице авторизации
    login_field = (By.XPATH, f"//input[@id='input-email']")

    # Поле ввода пароля на странице авторизации
    password_field = (By.XPATH, f"//input[@id='input-password']")

