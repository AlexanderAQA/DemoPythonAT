from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.assertions import assert_is_empty

class BasePage:
    """Страница с базововыми методами"""
    # Сколько ждать секунд
    waitSec = 5

    def __init__(self, driver):
        self.driver = driver

    # Общие локаторы
    search_input_field = (By.XPATH, "//input[@id='searchInput']")

    def wait_for_element(self, locator, timeout = waitSec):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        try:
            self.wait_for_element(locator).click()
        except NoSuchElementException:
            print(f"Элемент не найден. Локатор: '{locator}'")

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        print(f"Очищаем поле")
        element.clear()
        print(f"Вводим текст: '{text}'")
        element.send_keys(text)

    def get_element_text(self, locator):
        return self.wait_for_element(locator).text

    def refresh(self):
        print(f"Обновляем страницу")
        WebDriver.refresh(self.driver)

    def double_click(self, element):
        if not isinstance(self.driver, WebDriver):
            raise ValueError("Invalid WebDriver instance passed to ActionChains.")

        print(f"Двойной клик на элемент: '{element}'")
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def right_click(self, element):
        print(f"Нажатие правой кнопки мыши на элемент: '{element}'")
        action = ActionChains(self.driver)
        action.context_click(element).perform()

    def assert_value_is_empty(self, element):
        """Проверяем, что значение веб элемента пустое"""
        print("Проверяем, что значение веб элемента пустое")
        value = self.get_element_text(element)
        assert_is_empty(value)
