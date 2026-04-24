from selenium.webdriver.common.by import By

class BaseArtyPageLocators():
    """Локаторы главной страницы ArtyShop"""

    user_menu = (By.XPATH, f"//a[@class='dropdown-toggle']")

    authorization = (By.XPATH, f"//a[normalize-space(text())='Авторизация']")

    login_field = (By.XPATH, f"//input[@id='input-email' and @placeholder='E-Mail']")

    password_field = (By.XPATH, f"//input[@placeholder='Пароль' and @type='password']")

    login_button = (By.XPATH, f"//button[@type='submit' and normalize-space(text())='Войти']")

    account_header = (By.XPATH, "//div[@id='content']//h1[normalize-space()='Моя учетная запись']")

    exit_button = (By.XPATH, "//div[contains(@class,'list-group')]//a[normalize-space()='Выход']")
