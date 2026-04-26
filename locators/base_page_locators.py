from selenium.webdriver.common.by import By
class BaseArtyPageLocators():
    """Локаторы главной страницы ArtyShop"""

    #Кнопка "Войти"
    login_button = (By.XPATH, f"//button[@type='submit' and normalize-space(text())='Войти']")

    #Поле ввода E-Mail на странице авторизации
    login_field = (By.XPATH, f"//input[@id='input-email' and @placeholder='E-Mail']")

    # Поле ввода пароля на странице авторизации
    password_field = (By.XPATH, f"//input[@placeholder='Пароль' and @type='password']")

