import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from src.utils.logger import get_logger

class OtzovikMainPage(BasePage):
    """Главная https://otzovik.com/"""

    SEARCH_FIELD = (By.ID, "header-search-input")
    SEARCH_BUTTON = (By.XPATH, "input[@class='header-search-btn']")

    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/'

    def open(self):
        self.driver.get(self.url)
        return self

    def search(self,name):
        self.enter_text(self.SEARCH_FIELD, name)
        self.enter_text(self.SEARCH_FIELD,Keys.ENTER)
        return self

    def check_film(self):
        self.assert_element_is_visible((By.XPATH,"//a[contains(.,'Сериал \"Кремниевая долина\" ')]"))
        return self

    def search_by_button(self):
        self.enter_text(self.SEARCH_FIELD, name)
        self.click(OtzovikMainPage.SEARCH_BUTTON)


