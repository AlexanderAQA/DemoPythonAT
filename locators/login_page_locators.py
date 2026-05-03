from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Локаторы страницы ввода логина и пароля ArtyShop"""

 # Кнопка "Войти"
    login_button = (By.XPATH, f"//button[normalize-space()='Войти']")

 # Поле ввода E-Mail на странице авторизации
    login_field = (By.XPATH, f"//input[@id='input-email']")

 # Поле ввода пароля на странице авторизации
    password_field = (By.XPATH, f"//input[@id='input-password']")