from selenium.webdriver.common.by import By

from locators.prereview_page_locators import OtzovikPrereviewPageLocators
from pages.base_page import BasePage
from src.utils.logger import get_logger, allure_and_logger

class OtzovikPrereviwPage(BasePage):
    """Промежуточная страница формы отзыва https://otzovik.com/postreview.php"""

    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/postreview.php'

    def check_have_text_prereview(self, expected_text):
        allure_and_logger("Проверка отображения текста о правилах добавления отзыва")
        text = self.wait_for_element (OtzovikPrereviewPageLocators.RULES_ADD_REVIEW_TEXT).text
        self.asserts.assert_text_match(expected_text, text)
        return self

    def entre_reveiw_name(self, name):
        allure_and_logger("Ввод текста в поисковую строку названия субъекта отзыва")
        self.enter_text(OtzovikPrereviewPageLocators.FIELD_ENTRY_TEXT, name)
        return self

    def select_iphone_17_pro_max(self):
        allure_and_logger("Выбор iphone_17_pro_max в поисковой строке")
        self.click (OtzovikPrereviewPageLocators.IPHONE_17_PRO_MAX_RESULT)
        return self

    def check_review_headline_iphone_17_pro_max(self):
        allure_and_logger("Проверка заголовка iphone_17_pro_max ")
        self.assert_element_is_visible(OtzovikPrereviewPageLocators.IPHONE_17_PRO_MAX_RESULT_HEADLINE)
        return self

    def check_label(self, name):
        allure_and_logger(f"Проверка заголовка '{name}'")
        label = (By.XPATH, f"//div[@class='field-caption'][text()='{name}:']")
        self.assert_element_is_visible(label)
        return self

    def check_field(self):
        allure_and_logger("Проверка поля заголовка отзыва и поля текста отзыва")
        self.assert_element_is_visible(OtzovikPrereviewPageLocators.REVIEW_TITLE_FIELD)
        self.assert_element_is_visible(OtzovikPrereviewPageLocators.REVIEW_TEXT_FIELD)
        return self

    def open(self):
        allure_and_logger("Открыть страницу преревью")
        self.driver.get(self.url)
        return self

    def check_entry_text(self, expected_text):
        allure_and_logger("Проверить что текст (или value) в поле соответствует ранее введенному тексту")
        text = self.wait_for_element(OtzovikPrereviewPageLocators.FIELD_ENTRY_TEXT).text
        self.asserts.assert_text_match(expected_text, text)
        return self

    def select_movies_gift_with_character(self):
        allure_and_logger("Выбор фильма подарос с характером")
        self.click(OtzovikPrereviewPageLocators.MOVIE_GIFT_WITH_CHARACTER)
        return self

    def check_review_headline(self, review_name):
        allure_and_logger(f"Проверка заголовка объекта отзыва: {review_name}")
        self.assert_element_is_visible(OtzovikPrereviewPageLocators.HEADLINE_REVIEW_UNIVERSAL)
        return self




