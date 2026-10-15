from selenium.webdriver.common.by import By

from locators.review_page_locators import  OtzovikReviewPageLocators
from pages.base_page import BasePage
from src.utils.logger import get_logger, allure_and_logger

class OtzovikReviewPage(BasePage):
    """Cтраница формы отзыва https://otzovik.com/postreview.php?pid=267733"""

    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/postreview.php?pid=267733'

    def open(self):
        allure_and_logger("Открыть страницу ревью")
        self.driver.get(self.url)
        return self

    def check_headline_info_your_review(self):
        allure_and_logger("Проверка заголовка информативность вашего отзыва")
        self.assert_element_is_visible(OtzovikReviewPageLocators.INFO_YOUR_REVIEW_HEADLINE)
        return self