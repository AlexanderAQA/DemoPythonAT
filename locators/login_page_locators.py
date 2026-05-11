from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Локаторы страницы ввода логина и пароля ArtyShop"""

    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, f"//button[normalize-space()='Войти']")

    # Поле ввода E-Mail на странице авторизации
    LOGIN_FIELD = (By.XPATH, f"//input[@id='input-email']")

    # Поле ввода пароля на странице авторизации
    PASSWORD_FIELD = (By.XPATH, f"//input[@id='input-password']")