from pages.base_page import BasePage
from selenium.webdriver.common.by import By
class MainArtyPageLocators(BasePage):
    """Локаторы главной страницы ArtyShop"""

    #Заголовок "Личный кабинет"
    user_menu = (By.XPATH, f"//a[@class='dropdown-toggle']")

    #Заголовок "Моя учетная запись" после входа
    account_header = (By.XPATH, "//div[@id='content']//h1[normalize-space()='Моя учетная запись']")

    #Кнопка "Авторизация" в выпадающем меню
    authorization = (By.XPATH, f"//a[normalize-space(text())='Авторизация']")

    #Кнопка "ОК" принять cookies
    cookie_button = (By.XPATH, "//button[contains(@class, 'bg-primary') and normalize-space()='ОК']")
