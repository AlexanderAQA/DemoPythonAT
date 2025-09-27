from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.assertions import CommonAssertions


class BasePage:
    """Страница с базововыми методами"""
    # Сколько ждать секунд
    waitSec = 5

    def __init__(self, driver):
        self.driver = driver
        self.asserts = CommonAssertions(driver, self)

    # Общие локаторы
    search_input_field = (By.XPATH, "//input[@id='searchInput']")

    def wait_for_element(self, locator, timeout = waitSec):
        """Ожидание веб элемента"""
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Клик по элементу"""
        try:
            self.wait_for_element(locator).click()
        except NoSuchElementException:
            print(f"Элемент не найден. Локатор: '{locator}'")
        return self

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        print(f"Очищаем поле")
        element.clear()
        print(f"Вводим текст: '{text}'")
        element.send_keys(text)
        return self

    def get_element_text(self, locator):
        return self.wait_for_element(locator).get_attribute("value")

    def refresh(self):
        print(f"Обновляем страницу")
        self.driver.refresh()
        return self

    def double_click(self, element):
        if not isinstance(self.driver, WebDriver):
            raise ValueError("Invalid WebDriver instance passed to ActionChains.")

        print(f"Двойной клик на элемент: '{element}'")
        action = ActionChains(self.driver)
        action.double_click(element).perform()
        return self

    def right_click(self, element):
        print(f"Нажатие правой кнопки мыши на элемент: '{element}'")
        action = ActionChains(self.driver)
        action.context_click(element).perform()
        return self

    def to_assertions(self):
        """Переходим к проверкам"""
        return CommonAssertions(self.driver)
