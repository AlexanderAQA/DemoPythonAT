from selenium.webdriver.common.by import By


class OtzovikLocators:

    LOGIN_INPUT = (By.ID, "id_login")
    PASSWORD_INPUT = (By.ID, "id_pwd")
    EMAIL_INPUT = (By.ID, "id_mail")
    AGREEMENT_CHECKBOX = (By.XPATH, "//label[contains(., 'Я принимаю')]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.auth-error.not-empty")

