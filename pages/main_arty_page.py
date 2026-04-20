import allure
from pages.base_page import BasePage

class MainArtyPage(BasePage):
    """Главная shop.finarty.ru"""
    def __init__(self, driver):
        super().__init__(driver)
        self.main_url = 'https://shop.finarty.ru/'


    def open_main_page(self):
        url = self.main_url
        with allure.step(f"Открываем главную страницу finarty: {url}"):
            self.driver.get(url)

        return self
