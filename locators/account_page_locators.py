from selenium.webdriver.common.by import By

class AccountPageLocators:
    """Локаторы страницы учетной записи ArtyShop"""

    # Заголовок "Моя учетная запись" после входа
    ACCOUNT_HEADER = (By.XPATH, "//div[@id='content']//h1[normalize-space()='Моя учетная запись']")

    # Кнопка "Выход" в ЛК после авторизации
    EXIT_BUTTON = (By.XPATH, "//div[contains(@class,'list-group')]//a[normalize-space()='Выход']")

    # Имя пользователя в хедере после авторизации
    @staticmethod
    def get_actual_username(text: str):
        locator = (By.XPATH, f"//span[normalize-space()='{text}']")

        return locator