from selenium.webdriver.common.by import By

class AccountPageLocators():

    # Заголовок "Моя учетная запись" после входа
    account_header = (By.XPATH, "//div[@id='content']//h1[normalize-space()='Моя учетная запись']")

    # Кнопка "Выход" в ЛК после авторизации
    exit_button = (By.XPATH, "//div[contains(@class,'list-group')]//a[normalize-space()='Выход']")

    # Актуальное имя пользователя в заголовке после авторизации
    actual_username = (By.XPATH, "//span[normalize-space()='{text}']")