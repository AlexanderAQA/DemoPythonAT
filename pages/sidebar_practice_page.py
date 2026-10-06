from pages.playwright_base_page import PlaywrightBasePage
from playwright.sync_api import expect
from src.utils.logger import allure_and_logger

class SideBarPracticePage(PlaywrightBasePage):

    SEARCH_INPUT_W = "#Wikipedia1_wikipedia-search-input"
    SEARCH_BUTTON = "input.wikipedia-search-button"
    SEARCH_RESULTS_HEADER = "#Wikipedia1_wikipedia-search-results-header"
    SEARCH_RESULTS_CONTAINER = "#Wikipedia1_wikipedia-search-results"
    START_BUTTON = "button.start"
    SIMPLE_ALERT_BUTTON = "#alertBtn"
    CONFIRMATION_ALERT_BUTTON = "button:has-text('Confirmation Alert')"
    CONFIRMATION_RESULT = "#demo"
    SEARCH_RESULTS_LINK = "#wikipedia-search-result-link"
    NEW_TAB_BUTTON = "button:has-text('New Tab')"
    POPUP_WINDOWS_BUTTON = "#PopUp"
    POINT_ME_BUTTON = "button.dropbtn"
    ONLINE_TRAINING_LINK_TEXT = "a:has-text('Online Training')"
    PLAYWRIGHT_GET_STARTED_LINK = "a.getStarted_Sjon[href='/docs/intro']"
    DROPDOWN_MENU_LINKS = ".dropdown-content a"
    MOBILES_LINK = "a:has-text('Mobiles')"
    LAPTOPS_LINK = "a:has-text('Laptops')"
    FIELD_1 = "#field1"
    FIELD_2 = "#field2"
    SOURCE_OBJECT = "#draggable"
    TARGET_FIELD = "#droppable"
    PRICE_AMOUNT = "#amount"
    SLIDER_RANGE = "#slider-range"
    SLIDER_HANDLES = ".ui-slider-handle"
    COPY_TEXT_BUTTON = "button:has-text('Copy Text')"
    POSTS_ATOM_LINK = "a.feed-link"


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
        allure_and_logger("Нажатие кнопки Simple Alert")
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

    def open_multi_popup(self, expected_url: str):
        allure_and_logger("Открывает Popup среди множество новых страниц")

        context = self.page.context

        button = self.page.get_by_role("button", name="Popup Windows", exact=True)

        # Ждём первую новую страницу
        with context.expect_page() as page_info:
            button.click()

        page_1 = page_info.value
        page_1.wait_for_load_state()

        allure_and_logger(f"Страниц (окон): {len(context.pages)}")

        for i, page in enumerate(context.pages):
            allure_and_logger(f"PAGE {i}: url={page.url}, title={page.title()}")

        # Ждём вторую страницу, если она создаётся сайтом
        try:
            with context.expect_page(timeout=5000) as page_info_2:
                page_1.wait_for_timeout(1000)

            page_2 = page_info_2.value
            page_2.wait_for_load_state()

        except Exception:
            page_2 = None

        for i, page in enumerate(context.pages):
            allure_and_logger(f"PAGE {i}: url={page.url}, title={page.title()}")

        # Ищем именно нужную страницу
        target_page = next(
            (
                page
                for page in context.pages
                if expected_url in page.url
            ),
            None
        )

        if target_page is None:
            raise AssertionError(f"Не нашли нужную страницу с URL '{expected_url}'")

        self.page = target_page
        allure_and_logger(
            f"Переключились на нужную страницу: {self.page.url}"
        )

        return self


    def click_new_tab(self):
        allure_and_logger("Кликает на кнопку New Tab и переключается на новую вкладку")
        with self.page.context.expect_page() as new_page_info:
            self.page.locator(self.NEW_TAB_BUTTON).click()

        self.page = new_page_info.value
        return self


    def get_text_from_new_tab(self):
        allure_and_logger("Получаем текст проверочной ссылки на новой вкладке `pavantestingtools`")
        return self.page.locator(self.ONLINE_TRAINING_LINK_TEXT).text_content().strip()


    def get_playwright_get_started_text(self):
        allure_and_logger("Получает текст ссылки Get started на странице Playwright")
        return self.page.locator(self.PLAYWRIGHT_GET_STARTED_LINK).text_content().strip()


    def hover_point_me(self):
        allure_and_logger("Наводит курсор на кнопку Point Me")
        self.page.locator(self.POINT_ME_BUTTON).hover()
        return self


    def assert_mobiles_link_visible(self):
        allure_and_logger("Проверяет видимость ссылки Mobiles")
        expect(self.page.locator(self.MOBILES_LINK)).to_be_visible()
        return self


    def assert_laptops_link_visible(self):
        allure_and_logger("Проверяет видимость ссылки Laptops")
        expect(self.page.locator(self.LAPTOPS_LINK)).to_be_visible()
        return self

    def get_text_field_1(self):
        allure_and_logger("Получает текст из поля 1")
        return self.get_field_value(self.FIELD_1)

    def copy_text_double_click(self):
        button = self.page.get_by_role("button", name="Copy Text", exact=True)
        button.dblclick()
        return self

    def get_text_field_2(self):
        allure_and_logger("Получает текст из поля 2")
        return self.get_field_value(self.FIELD_2)

    def assert_field_2_text(self, expected_text):
        allure_and_logger("Проверяет что текст в поле 1 и 2 совпадает")
        self.asserts.assert_is_equal(expected_text, self.get_text_field_2())
        return self

    def drag_and_drop_object(self):
        allure_and_logger("Перенос объекта в контейнер")
        self.page.locator(self.SOURCE_OBJECT).drag_to(self.page.locator(self.TARGET_FIELD))
        return self

    def assert_object_dropped(self):
        allure_and_logger("Проверка что объект перенесен в контейнер")
        target_text = self.page.locator(self.TARGET_FIELD).inner_text()
        self.asserts.assert_is_equal("Dropped!", target_text)
        return self

    def slide_price(self):
        allure_and_logger("Передвигает слайдер цены")
        slider_range = self.page.locator("#slider-range")
        slider_handles = slider_range.locator(".ui-slider-handle")

        left = slider_handles.nth(0)
        right = slider_handles.nth(1)

        left.focus()

        for _ in range(10):
            left.press("ArrowLeft")

        right.focus()

        for _ in range(10):
            right.press("ArrowRight")

        return self

    def assert_price_amount(self):
        allure_and_logger("Проверяет цену")
        self.asserts.assert_is_equal("$65 - $310", self.get_field_value(self.PRICE_AMOUNT))
        return self

    def set_price_range(self, min_val: int, max_val: int):
        allure_and_logger(f"Выставляет диапазон цен: от {min_val} до {max_val}")

        slider = self.page.locator(self.SLIDER_RANGE)
        handles = slider.locator(self.SLIDER_HANDLES)
        left = handles.nth(0)
        right = handles.nth(1)

        left.focus()
        left.press("Home")
        for _ in range(min_val):
            left.press("ArrowRight")

        right.focus()
        right.press("Home")

        steps = max_val - min_val
        for _ in range(steps):
            right.press("ArrowRight")

        return self

    def assert_price_range(self, expected_text: str):
        allure_and_logger(f"Проверяет, что цена соответствует: '{expected_text}'")
        actual_text = self.get_field_value(self.PRICE_AMOUNT)
        self.asserts.assert_is_equal(expected_text, actual_text)
        return self

    def clear_field_1(self):
        allure_and_logger("Очищает поле Field1 через Ctrl+A и Delete")
        field = self.page.locator(self.FIELD_1)
        field.click()
        field.press("Control+a")
        field.press("Delete")
        return self

    def fill_field_1(self, text: str):
        allure_and_logger(f"Вводит текст в Field1: '{text}'")
        self.page.locator(self.FIELD_1).fill(text)
        return self

    def assert_field_1_is_empty(self):
        allure_and_logger("Проверяет, что поле Field1 пустое")
        actual_text = self.get_text_field_1()
        self.asserts.assert_is_empty(actual_text)
        return self

    def drag_atom_link_to_field2(self):
        allure_and_logger("Перетаскивает ссылку Posts (Atom) в поле Field2")
        source = self.page.locator(self.POSTS_ATOM_LINK)
        target = self.page.locator(self.FIELD_2)
        source.drag_to(target)
        return self

    def assert_field2_url(self):
        allure_and_logger("Проверка URL в поле Field2")
        expected_url = "https://testautomationpractice.blogspot.com/feeds/posts/default"
        actual_url = self.get_field_value(self.FIELD_2)
        self.asserts.assert_is_equal(expected_url, actual_url)
        return self
