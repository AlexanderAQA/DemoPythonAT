from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import get_logger


class OtzovikPromotionsPage(BasePage):
    """Промоакции   https://otzovik.com/promo/"""

    ACTIVE_SBER_PROMO = (By.XPATH, "(//div[not(@class='section inactive')]//*[text()='Промоакция от СберСтрахования'])[1]")
    DETAILS_ABOUT_CAMPAIGN = (By.XPATH, "//a[@href='/promo/2026-10-01_ozon/']/*[text()='Подробнее об акции']")
    STATUS_ACTIVE_ALERT = (By.XPATH, "//span[text()='Статус: промоакция активна']")
    SBER_BONUS_TEXT = (By.XPATH, "//p[text()='Получите бонусы СберСпасибо за отзыв']")


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
        self.assert_element_is_visible(self.STATUS_ACTIVE_ALERT)
        return self

    def check_have_all_text(self):
        self.assert_element_is_visible(self.SBER_BONUS_TEXT)
        element_text = self.wait_for_element(("//div[@class='promo-item-text']")).text
        self.asserts.assert_text_match("Срок акции: 01.10.2026 — 31.10.2026.", element_text)
        return self


