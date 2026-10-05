from selenium.webdriver.common.by import By

class OtzovikPromotionsPageLocators:
    """Промоакции   https://otzovik.com/promo/"""

    ACTIVE_OZON_PROMO = (By.XPATH, "(//div[not(@class='section inactive')]//*[text()='Промоакция от Ozon'])[1]")
    DETAILS_ABOUT_CAMPAIGN_BUTTON = (By.XPATH, "//a[@href='/promo/2026-10-01_ozon/']/*[text()='Подробнее об акции']")
    STATUS_ACTIVE_ALERT = (By.XPATH, "//span[text()='Статус: промоакция активна']")
    OZON_BONUS_TEXT = (By.XPATH, "//div[@class='promo-item-text']")
    COMPLETED_PROMO_NUMBER_TITLE = (By.XPATH, "//div[@class='section inactive']//*[text()='Промоакция от Цифра Брокер']")
    QUESTOIN_PROMO = (By.XPATH, "//p[text()='По вопросам организации промоакций, конкурсов, розыгрышей и тестирования продукции обращаться в ']")
