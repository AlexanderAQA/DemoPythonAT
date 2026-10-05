from selenium.webdriver.common.by import By
from locators.otzovik_main_page_locators import OtzovikMainPageLocators
from pages.base_page import BasePage
from src.utils.logger import get_logger, allure_and_logger


class OtzovikMainPage(BasePage):
    """Главная https://otzovik.com/"""

    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/'

    def open(self):
        allure_and_logger("Открывается главная страница")
        self.driver.get(self.url)
        return self


    def check_result(self, text):
        allure_and_logger("Проверка отображения результата поискового запроса")
        self.assert_element_is_visible((By.XPATH,f"//a[@class='product-name'][contains(.,'{text}')]"))
        return self

    def search_by_button(self, name):
        self.enter_text(OtzovikMainPageLocators.SEARCH_FIELD, name)
        self.driver.switch_to.default_content()
        self.click(OtzovikMainPageLocators.SEARCH_BUTTON)
        return self

    def open_card(self, item_name):
        self.click((By.XPATH,f"//a[text()='{item_name}']"))
        return self

    def check_review_tab(self):
        self.assert_element_is_visible(OtzovikMainPageLocators.REVIEW_TAB)
        return self

    def check_negative_tab(self):
        self.assert_element_is_visible(OtzovikMainPageLocators.NEGATIVE_TAB)
        return self

    def check_positive_tab(self):
        self.assert_element_is_visible(OtzovikMainPageLocators.POSITIVE_TAB)
        return self

    def check_headline_item(self, headline_name):
        self.assert_element_is_visible((By.XPATH,f"//span[text()='{headline_name}']"))
        return self

    def open_tab_promotions(self):
        self.click_by_script(OtzovikMainPageLocators.PROMOTION_TAB)
        return self

