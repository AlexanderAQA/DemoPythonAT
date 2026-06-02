from selenium.webdriver.common.by import By

class AccountPageLocators:
    """Локаторы страницы учетной записи ArtyShop"""

    # Заголовок "Моя учетная запись" после входа
    ACCOUNT_HEADER = (By.XPATH, "//div[@id='content']//h1[normalize-space()='Моя учетная запись']")

    # Кнопка "Выход" в ЛК после авторизации
    EXIT_BUTTON = (By.XPATH, "//div[contains(@class,'list-group')]//a[normalize-space()='Выход']")

    # Локатор кнопки "Изменить информацию"
    CHANGE_INFO_BUTTON = (By.XPATH, "//a[normalize-space()='Изменить информацию']")

    # Локатор заголовка Ваша учетная запись
    HEAD_YOUR_ACCOUNT = (By.XPATH, "//legend[normalize-space()='Ваша учетная запись']")

    # Локатор названия поля "Имя, Отчество"
    FIRSTNAME_FIELD_LABEL = (By.XPATH, "//label[@for='input-firstname']")

    # Локатор названия поля "Фамилия"
    SURNAME_FIELD_LABEL = (By.XPATH, "//label[@for='input-lastname']")

    # Локатор названия поля "E-Mail"
    EMAIL_FIELD_LABEL = (By.XPATH, "//label[@for='input-email']")

    # Локатор названия поля "Телефон"
    TELEPHONE_FIELD_LABEL =  (By.XPATH, "//label[@for='input-telephone']")

    # Локатор текста в поле "Имя"
    TEXT_IN_NAME_FIELD = (By.XPATH, f"//input[@id='input-firstname']")

    # Локатор текста в поле "Фамилия"
    TEXT_IN_SURNAME_FIELD = (By.XPATH, f"//input[@id='input-lastname']")

    # Локатор текста в поле "E-mail"
    TEXT_IN_EMAIL_FIELD = (By.XPATH, f"//input[@id='input-email']")

    # Локатор текста в поле "Телефон"
    TEXT_IN_TELEPHONE_FIELD = (By.XPATH, f"//input[@id='input-telephone']")

    # Локатор кнопки "Назад"
    BACK_BUTTON = (By.XPATH, "//a[normalize-space()='Назад']")

    # Локатор кнопки "Продолжить"
    CONTINUE_BUTTON = (By.XPATH, "//button[normalize-space()='Продолжить']")

    # Локатор кнопки "Личный кабинет"
    PERS_ACCOUNT_BUTTON = (By.XPATH, "//ul[@class='breadcrumb']//a[normalize-space()='Личный Кабинет']")

    # Локатор кнопки "Домой"
    HOME_BUTTON_IN_ACCOUNT = (By.XPATH, "//i[@class='fas fa-home']")

    # Имя пользователя в хедере после авторизации
    @staticmethod
    def get_actual_username(text: str):
        locator = (By.XPATH, f"//span[normalize-space()='{text}']")

        return locator