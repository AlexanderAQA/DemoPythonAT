import allure
import pytest
from pages.playwright_practice_page import PlaywrightPracticePage


@pytest.mark.ui
class TestPlaywrightPractice:

    @allure.title("Поиск невалидного значения в 'W'-поисковой строке")
    def test_searching_invalid_value(self, playwright_practice_page: PlaywrightPracticePage):
        invalid_query = "xYz_NonExistent_Word_12345"
        (playwright_practice_page
         .open_playwright_practice_page()
         .search_value(invalid_query))
        actual_text = playwright_practice_page.get_results_text()
        (playwright_practice_page.asserts
         .assert_text_match("No results found.", actual_text))

    @pytest.mark.ui
    @allure.title("Поиск валидного значения")
    def test_searching_valid_value(self, playwright_practice_page: PlaywrightPracticePage):
        valid_query = "Ленин"
        (playwright_practice_page
         .open_playwright_practice_page()
         .search_value(valid_query))
        actual_text = playwright_practice_page.get_results_text()
        (playwright_practice_page.asserts
         .assert_text_match("Ленин", actual_text))

    @pytest.mark.ui
    @allure.title("Переход по ссылке валидного результата поиска")
    def test_click_valid_result_link(self, playwright_practice_page: PlaywrightPracticePage):
        valid_query = "Ленин"
        expected_path = "en.wikipedia.org/wiki/Vladimir_Lenin"

        (playwright_practice_page
         .open_playwright_practice_page()
         .search_value(valid_query)
         .click_first_result_link()
         .should_have_partial_url(expected_path))

    @pytest.mark.ui
    @allure.title("Нажатие кнопки Start и Simple Alert")
    def test_start_and_simple_alert(self, playwright_practice_page: PlaywrightPracticePage):
        (playwright_practice_page
         .open_playwright_practice_page()
         .click_start_button())

        start_text = playwright_practice_page.get_start_button_text()
        (playwright_practice_page.asserts
         .assert_is_equal("STOP", start_text))

        alert_text = playwright_practice_page.handle_simple_alert()
        (playwright_practice_page.asserts
         .assert_text_match("I am an alert box!", alert_text))

    @pytest.mark.ui
    @allure.title("Работа с confirmation alert - нажатие ОК")
    def test_confirmation_alert_ok(self, playwright_practice_page: PlaywrightPracticePage):
        (playwright_practice_page
         .open_playwright_practice_page())
        alert_text = playwright_practice_page.click_confirmation_alert_and_accept()
        (playwright_practice_page
         .asserts.assert_text_match("Press a button!", alert_text))
        result_text = playwright_practice_page.get_confirmation_result_text()
        (playwright_practice_page
         .asserts.assert_text_match("You pressed OK!", result_text))

    @pytest.mark.ui
    @allure.title("Работа с confirmation alert - нажатие Отмена")
    def test_confirmation_alert_cancel(self, playwright_practice_page: PlaywrightPracticePage):
        playwright_practice_page.open_playwright_practice_page()
        alert_text = playwright_practice_page.click_confirmation_and_dismiss()
        (playwright_practice_page
         .asserts.assert_text_match("Press a button!", alert_text))
        result_text = playwright_practice_page.get_confirmation_result_text()
        (playwright_practice_page
         .asserts.assert_text_match("You pressed Cancel!", result_text))
