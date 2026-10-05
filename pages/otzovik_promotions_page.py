from selenium.webdriver.common.by import By

from locators.otzovik_promotions_page_locators import OtzovikPromotionsPageLocators
from pages.base_page import BasePage
from utils.logger import get_logger


class OtzovikPromotionsPage(BasePage):
    """Промоакции   https://otzovik.com/promo/"""

    def __init__(self, driver):
        self.logger = get_logger(__name__)
        super().__init__(driver)
        self.url = 'https://otzovik.com/promo/'

    def open(self):
        self.driver.get(self.url)
        return self

    def check_promo_ozon(self):
        self.assert_element_is_visible(OtzovikPromotionsPageLocators.ACTIVE_OZON_PROMO)
        return self

    def open_details_campaign(self):
        self.click(OtzovikPromotionsPageLocators.DETAILS_ABOUT_CAMPAIGN)
        return self

    def check_promo_active(self):
        self.assert_element_is_visible(OtzovikPromotionsPageLocators.STATUS_ACTIVE_ALERT)
        return self

    def check_have_all_text(self):
        self.assert_element_is_visible(OtzovikPromotionsPageLocators.OZON_BONUS_TEXT)
        element_text = self.wait_for_element(("//div[@class='promo-item-text']")).text
        self.asserts.assert_text_match("Срок акции: 01.10.2026 — 31.10.2026.", element_text)
        return self

    def check_promo_completed_number(self):
        self.assert_element_is_visible(OtzovikPromotionsPageLocators.COMPLETED_PROMO_NUMBER_BROKER)
        return self

    def check_have_massange(self):
        self.assert_element_is_visible(OtzovikPromotionsPageLocators.QUESTOIN_PROMO)
        return self
