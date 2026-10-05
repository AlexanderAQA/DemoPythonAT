from pages.playwright_base_page import PlaywrightBasePage
from src.utils.logger import allure_and_logger


class PlaywrightPracticePage(PlaywrightBasePage):

    SEARCH_INPUT_W = "#Wikipedia1_wikipedia-search-input"
    SEARCH_BUTTON = "input.wikipedia-search-button"
    SEARCH_RESULTS_HEADER = "#Wikipedia1_wikipedia-search-results-header"
    SEARCH_RESULTS_CONTAINER = "#Wikipedia1_wikipedia-search-results"
    START_BUTTON = "button.start"
    SIMPLE_ALERT_BUTTON = "#alertBtn"
    CONFIRMATION_ALERT_BUTTON = "button:has-text('Confirmation Alert')"
    CONFIRMATION_RESULT = "#demo"
    SEARCH_RESULTS_LINK = "#wikipedia-search-result-link"

    def search_value(self, value: str):
        """Вводит значение и нажимает кнопку поиска"""
        self.logger.info(f"Поиск значения: '{value}'")
        self.page.locator(self.SEARCH_INPUT_W).fill(value)
        self.page.locator(self.SEARCH_BUTTON).click()
        self.page.wait_for_load_state("networkidle")
        return self

    def get_results_text(self) -> str:
        """Возвращает текст из блока результатов"""
        allure_and_logger("Получение текста из блока результатов")
        locator = self.page.locator(self.SEARCH_RESULTS_CONTAINER)
        locator.wait_for(state="visible")
        return locator.inner_text()

    def click_search_result(self,text):
        """Кликает по результату поиска"""
        allure_and_logger("Кликает по результату поиска")
        with self.page.expect_popup() as page_info:
            link = self.page.locator(self.SEARCH_RESULTS_CONTAINER).get_by_text(text, exact=True)
            link.wait_for(state="visible")
            link.click()
        new_page = page_info.value
        self.page = new_page
        new_page.wait_for_load_state("networkidle")
        return self

    def click_start_button(self):
        """Нажимает кнопку START"""
        allure_and_logger("Нажатие кнопки START")
        self.page.locator("button:has-text('START')").click()
        return self

    def get_start_button_text(self) -> str:
        """Возвращает текущий текст кнопки (STOP)"""
        allure_and_logger("Получение текста кнопки (проверка на STOP)")
        return self.page.locator("button:has-text('STOP')").inner_text()

    def handle_simple_alert(self) -> str:
        """Нажимает Simple Alert и возвращает текст"""
        self.logger.info("Нажатие кнопки Simple Alert")
        alert_text = ""
        def handle_dialog(dialog):
            nonlocal alert_text
            alert_text = dialog.message
            dialog.accept()
        self.page.on("dialog", handle_dialog)
        self.page.locator(self.SIMPLE_ALERT_BUTTON).click()
        return alert_text

    def click_confirmation_alert_and_accept(self) -> str:
        """Нажимает Confirmation Alert и выбирает ОК. Возвращает текст."""
        allure_and_logger("Нажатие кнопки Confirmation Alert и выбор ОК")
        alert_text = ""
        def handle_dialog(dialog):
            nonlocal alert_text
            alert_text = dialog.message
            dialog.accept()
        self.page.on("dialog", handle_dialog)
        self.page.locator(self.CONFIRMATION_ALERT_BUTTON).click()
        return alert_text

    def get_confirmation_result_text(self) -> str:
        """Возвращает текст результата"""
        allure_and_logger("Получение текста результата confirmation alert")
        return self.page.locator(self.CONFIRMATION_RESULT).inner_text()

    def click_confirmation_and_dismiss(self) -> str:
        """Нажимает Confirmation Alert и выбирает Отмена. Возвращает текст."""
        allure_and_logger("Нажатие кнопки Confirmation Alert и выбор Отмена")
        alert_text = ""
        dialog_handled = False
        def handle_dialog(dialog):
            nonlocal alert_text, dialog_handled
            if not dialog_handled:
                alert_text = dialog.message
                dialog.dismiss()
                dialog_handled = True
        self.page.on("dialog", handle_dialog)
        self.page.locator(self.CONFIRMATION_ALERT_BUTTON).click()
        return alert_text
