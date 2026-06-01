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

    # Локатор кнопки "Изменить информацию"
    CHANGE_INFORMATION_BUTTON =  (By.XPATH, "//a[normalize-space()='Изменить информацию']")

    # Локатор заголовка Ваша учетная запись
    YOUR_ACCOUNT =  (By.XPATH, "//legend[normalize-space()='Ваша учетная запись']")

    # Локатор названия поля "Имя, Отчество"
    NAME_PATRONYMIC =  (By.XPATH, "//label[@for='input-firstname']")

    # Локатор названия поля "Фамилия"
    SURNAME =  (By.XPATH, "//label[@for='input-lastname']")

    # Локатор названия поля "E-Mail"
    EMAIL =  (By.XPATH, "//label[@for='input-email']")

    # Локатор названия поля "Телефон"
    TELEPHONE =  (By.XPATH, "//label[@for='input-telephone']")

    # Локатор текста в поле "Имя"
    @staticmethod
    def get_text_in_name_field(name: str):
            locator = (By.XPATH, f"//input[@id='input-firstname' and @value='{name}']")

            return locator

    # Локатор текста в поле "Фамилия"
    @staticmethod
    def get_text_in_surname_field(surname: str):
            locator = (By.XPATH, f"//input[@id='input-lastname' and contains(@value, '{surname}')]")

            return locator

    # Локатор текста в поле "E-mail"
    @staticmethod
    def get_text_in_email_field(email: str):
            locator = (By.XPATH, f"//input[@id='input-email' and @value='{email}']")

            return locator

    # Локатор текста в поле "Телефон"
    @staticmethod
    def get_text_in_telephone_field(tel: str):
            locator = (By.XPATH, f"//input[@id='input-telephone' and @value='{tel}']")

            return locator

    # Локатор кнопки "Назад"
    BACK_BUTTON =  (By.XPATH, "//a[normalize-space()='Назад']")

    # Локатор кнопки "Продолжить"
    CONTINUE_BUTTON =  (By.XPATH, "//button[normalize-space()='Продолжить']")

    # Локатор кнопки "Личный кабинет"
    PERS_ACCOUNT =  (By.XPATH, "//ul[@class='breadcrumb']//a[normalize-space()='Личный Кабинет']")

    # Локатор кнопки "Домой"
    HOME =  (By.XPATH, "//li[@class='breadcrumb-item']/a[i[@class='fas fa-home']]")