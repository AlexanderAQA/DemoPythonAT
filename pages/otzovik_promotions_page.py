from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.logger import get_logger


class OtzovikPromotionsPage(BasePage):
    """Промоакции   https://otzovik.com/promo/"""

    ACTIVE_SBER_PROMO = (By.XPATH, "(//div[not(@class='section inactive')]//*[text()='Промоакция от СберСтрахования'])[1]")

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




