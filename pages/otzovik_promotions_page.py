from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import get_logger


class OtzovikPromotionsPage(BasePage):
    """Промоакции   https://otzovik.com/promo/"""

    ACTIVE_SBER_PROMO = (By.XPATH, "(//div[not(@class='section inactive')]//*[text()='Промоакция от СберСтрахования'])[1]")
    DETAILS_ABOUT_CAMPAIGN = (By.XPATH, "(//div[not(@class='section inactive')]//*[text()='Подробнее об акции'])[1]")
    CHECK_STATUS_ACTIVE = (By.XPATH, "//span[text()='Статус: промоакция активна']")
    TEXT_BONUS_SBER = (By.XPATH, "//p[text()='Получите бонусы СберСпасибо за отзыв']")
    DISCRIPTION_PROMO_TEXT_1 = (By.XPATH, "//p[text()='Поделитесь впечатлениями о продуктах и сервисе ']")
    DISCRIPTION_PROMO_TEXT_2 = (By.XPATH, "//p[text()='Для участия необходимо оставить отзыв ']")
    DISCRIPTION_PROMO_TEXT_3 = (By.XPATH, "//p[text()='Ваше мнение помогает нам становиться лучше и делать сервис ещё удобнее.']")
    DISCRIPTION_PROMO_TEXT_4 = (By.XPATH, "//p[text()='Подробные условия акции']")
    DISCRIPTION_PROMO_TEXT_5 = (By.XPATH, "//p[text()='Информацию об организаторе и полных правилах акции, сроках, количестве и порядке получения призов смотреть по ']")


    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/promo/'

    def open(self):
        self.driver.get(self.url)
        return self

    def check_promo_sber(self):
        self.assert_element_is_visible(self.ACTIVE_SBER_PROMO)
        return self

    def open_details_campaign(self):
        self.click(self.DETAILS_ABOUT_CAMPAIGN)
        return self

    def check_promo_active(self):
        self.assert_element_is_visible(self.CHECK_STATUS_ACTIVE)
        return self

    def check_have_all_text(self):
        self.assert_element_is_visible(self.TEXT_BONUS_SBER)
        self.assert_element_is_visible(self.DISCRIPTION_PROMO_TEXT_1)
        self.assert_element_is_visible(self.DISCRIPTION_PROMO_TEXT_2)
        self.assert_element_is_visible(self.DISCRIPTION_PROMO_TEXT_3)
        self.assert_element_is_visible(self.DISCRIPTION_PROMO_TEXT_4)
        self.assert_element_is_visible(self.DISCRIPTION_PROMO_TEXT_5)
        return self


