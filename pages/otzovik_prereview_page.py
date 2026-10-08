from selenium.webdriver.common.by import By

from locators.prepeview_page_locators import OtzovikPrereviewPageLocators
from pages.base_page import BasePage
from src.utils.logger import get_logger, allure_and_logger

class OtzovikPrereviwPage(BasePage):
    """Промежуточная страница формы отзыва https://otzovik.com/postreview.php"""

    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/postreview.php'

    def check_have_text_prereview(self):
        allure_and_logger("Проверка отображения текста о правилах добавления отзыва")
        self.assert_element_is_visible(OtzovikPrereviewPageLocators.RULES_ADD_REVIEW_TEXT)
        return self

    def check_entre_text(self, name):
        allure_and_logger("Ввод текста в поисковую строку")
        self.enter_text(OtzovikPrereviewPageLocators.FIELD_ENTRY_TEXT, name)
        return self

