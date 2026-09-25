import allure
import pytest

from conftest import web_element_practice_page


@pytest.mark.ui
class TestPlaywrightPractice:

    @allure.title("Поиск невалидного значения в 'W'-поисковой строке")
    def test_searching_invalid_value(self, web_element_practice_page, playwright_practice_page):
        invalid_query = "xYz_NonExistent_Word_12345"
        (web_element_practice_page
         .open_practice_page())

        (playwright_practice_page
         .search_value(invalid_query))
        actual_text = playwright_practice_page.get_results_text()

        (playwright_practice_page.asserts
         .assert_text_match("No results found.", actual_text))

    @pytest.mark.ui
    @allure.title("Поиск валидного значения")
    def test_searching_valid_value(self, web_element_practice_page, playwright_practice_page):
        valid_query = "Ленин"
        (web_element_practice_page
         .open_practice_page())

        (playwright_practice_page
         .search_value(valid_query))
        actual_text = playwright_practice_page.get_results_text()

        (playwright_practice_page.asserts
         .assert_text_match("Ленин", actual_text))

    @pytest.mark.ui
    @allure.title("Переход по ссылке валидного результата поиска")
    def test_click_valid_result_link(self, web_element_practice_page, playwright_practice_page):
        valid_query = "Ленин"
        expected_path = "en.wikipedia.org/wiki/Vladimir_Lenin"

        (web_element_practice_page
         .open_practice_page())

        (playwright_practice_page
         .search_value(valid_query)
         .click_search_result("Ленин")
         .should_have_partial_url(expected_path))

    @pytest.mark.ui
    @allure.title("Нажатие кнопки Start и Simple Alert")
    def test_start_and_simple_alert(self, web_element_practice_page, playwright_practice_page):
        (web_element_practice_page
         .open_practice_page())

        (playwright_practice_page
         .click_start_button())

        start_text = playwright_practice_page.get_start_button_text()

        (playwright_practice_page.asserts
         .assert_is_equal("STOP", start_text))

        alert_text = playwright_practice_page.handle_simple_alert()

        (playwright_practice_page.asserts
         .assert_text_match("I am an alert box!", alert_text))

    @pytest.mark.ui
    @allure.title("Работа с confirmation alert - нажатие ОК")
    def test_confirmation_alert_ok(self, web_element_practice_page, playwright_practice_page):
        (web_element_practice_page
         .open_practice_page())

        alert_text = playwright_practice_page.click_confirmation_alert_and_accept()

        (playwright_practice_page
         .asserts.assert_text_match("Press a button!", alert_text))

        result_text = playwright_practice_page.get_confirmation_result_text()

        (playwright_practice_page
         .asserts.assert_text_match("You pressed OK!", result_text))

    @pytest.mark.ui
    @allure.title("Работа с confirmation alert - нажатие Отмена")
    def test_confirmation_alert_cancel(self, web_element_practice_page, playwright_practice_page):
        (web_element_practice_page
         .open_practice_page())

        alert_text = playwright_practice_page.click_confirmation_and_dismiss()

        (playwright_practice_page
         .asserts.assert_text_match("Press a button!", alert_text))

        result_text = playwright_practice_page.get_confirmation_result_text()

        (playwright_practice_page
         .asserts.assert_text_match("You pressed Cancel!", result_text))

    @pytest.mark.ui
    @allure.title("Работа с PopUp")
    def test_open_popup(self, web_element_practice_page):
        (web_element_practice_page
         .open_practice_page()
         .open_popup()
         .time.sleep())