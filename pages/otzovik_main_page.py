import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from src.utils.logger import get_logger

class OtzovikMainPage(BasePage):
    """Главная https://otzovik.com/"""

    SEARCH_FIELD = (By.ID, "header-search-input")
    SEARCH_BUTTON = (By.XPATH, "input[@class='header-search-btn']")
    REVIEW_TAB = (By.XPATH, "//a[text()='Отзывы ']")
    NEGATIVE_TAB = (By.XPATH, "//a[text()='Негатив']")
    POSITIVE_TAB = (By.XPATH, "//a[text()='Позитив']")


    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/'

    def open(self):
        self.driver.get(self.url)
        return self


    def check_film(self, text):
        self.assert_element_is_visible((By.XPATH,f"//a[@class='product-name'][contains(.,'{text}')]"))
        return self

    def search_by_button(self, name):
        self.enter_text(self.SEARCH_FIELD, name)
        self.click(OtzovikMainPage.SEARCH_BUTTON)
        return self

    def open_card(self, item_name):
        self.click((By.XPATH,f"//a[text()='{item_name}')]"))
        return self

    def check_review_tab(self):
        self.assert_element_is_visible(self.REVIEW_TAB)
        return self

    def check_negative_tab(self):
        self.assert_element_is_visible(self.NEGATIVE_TAB)
        return self

    def check_positive_tab(self):
        self.assert_element_is_visible(self.POSITIVE_TAB)
        return self

    def check_headline(self, headline_name):
        self.assert_element_is_visible((By.XPATH,f"//a[text()='{headline_name}')]"))
        return self

