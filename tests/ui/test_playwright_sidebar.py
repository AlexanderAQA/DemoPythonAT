import allure
import pytest

from src.utils.test_data import generate_random_string


@pytest.mark.ui
class TestSidebarPage:

    @allure.title("Поиск невалидного значения в 'W'-поисковой строке")
    def test_searching_invalid_value(self, web_element_practice_page, sidebar_practice_page):
        invalid_query = "xYz_NonExistent_Word_12345"
        (web_element_practice_page
         .open_practice_page())

        (sidebar_practice_page
         .search_value(invalid_query))
        actual_text = sidebar_practice_page.get_results_text()

        (sidebar_practice_page.asserts
         .assert_text_match("No results found.", actual_text))

    @pytest.mark.ui
    @allure.title("Поиск валидного значения")
    def test_searching_valid_value(self, web_element_practice_page, sidebar_practice_page):
        valid_query = "Ленин"
        (web_element_practice_page
         .open_practice_page())

        (sidebar_practice_page
         .search_value(valid_query))
        actual_text = sidebar_practice_page.get_results_text()

        (sidebar_practice_page.asserts
         .assert_text_match("Ленин", actual_text))

    @pytest.mark.ui
    @allure.title("Переход по ссылке валидного результата поиска")
    def test_click_valid_result_link(self, web_element_practice_page, sidebar_practice_page):
        valid_query = "Ленин"
        expected_path = "en.wikipedia.org/wiki/Vladimir_Lenin"

        (web_element_practice_page
         .open_practice_page())

        (sidebar_practice_page
         .search_value(valid_query)
         .click_search_result("Ленин")
         .should_have_partial_url(expected_path))

    @pytest.mark.ui
    @allure.title("Нажатие кнопки Start и Simple Alert")
    def test_start_and_simple_alert(self, web_element_practice_page, sidebar_practice_page):
        (web_element_practice_page
         .open_practice_page())

        (sidebar_practice_page
         .click_start_button())

        start_text = sidebar_practice_page.get_start_button_text()

        (sidebar_practice_page.asserts
         .assert_is_equal("STOP", start_text))

        alert_text = sidebar_practice_page.handle_simple_alert()

        (sidebar_practice_page.asserts
         .assert_text_match("I am an alert box!", alert_text))

    @pytest.mark.ui
    @allure.title("Работа с confirmation alert - нажатие ОК")
    def test_confirmation_alert_ok(self, web_element_practice_page, sidebar_practice_page):
        (web_element_practice_page
         .open_practice_page())

        alert_text = sidebar_practice_page.click_confirmation_alert_and_accept()

        (sidebar_practice_page
         .asserts.assert_text_match("Press a button!", alert_text))

        result_text = sidebar_practice_page.get_confirmation_result_text()

        (sidebar_practice_page
         .asserts.assert_text_match("You pressed OK!", result_text))

    @pytest.mark.ui
    @allure.title("Работа с confirmation alert - нажатие Отмена")
    def test_confirmation_alert_cancel(self, web_element_practice_page, sidebar_practice_page):
        (web_element_practice_page
         .open_practice_page())

        alert_text = sidebar_practice_page.click_confirmation_and_dismiss()

        (sidebar_practice_page
         .asserts.assert_text_match("Press a button!", alert_text))

        result_text = sidebar_practice_page.get_confirmation_result_text()

        (sidebar_practice_page
         .asserts.assert_text_match("You pressed Cancel!", result_text))

    @pytest.mark.ui
    @allure.title("Проверка открытия новой вкладки при клике на New Tab")
    def test_new_tab(self, web_element_practice_page, sidebar_practice_page):
        expected_path = "pavantestingtools.com"
        expected_text = "Online Training"

        (web_element_practice_page
         .open_practice_page())
        (sidebar_practice_page
         .click_new_tab()
         .should_have_partial_url(expected_path))

        actual_text = sidebar_practice_page.get_text_from_new_tab()

        (web_element_practice_page.
         asserts.assert_is_equal(expected_text, actual_text))

    @pytest.mark.ui
    @allure.title("Проверка открытия Playwright сайта через кнопку Popup Windows")
    def test_popup_windows(self, web_element_practice_page, sidebar_practice_page):
        expected_path = "playwright.dev"
        expected_text = "Get started"

        (web_element_practice_page
         .open_practice_page())
        (sidebar_practice_page
         .open_multi_popup("https://playwright.dev/")
         .should_have_partial_url(expected_path))

        actual_text = sidebar_practice_page.get_playwright_get_started_text()

        (web_element_practice_page
         .asserts.assert_is_equal(expected_text, actual_text))

    @pytest.mark.ui
    @allure.title("Проверка появления 2 ссылок при наведении на Point Me")
    def test_point_me_hover(self, web_element_practice_page, sidebar_practice_page):
        (web_element_practice_page
         .open_practice_page())
        (sidebar_practice_page
         .hover_point_me()
         .assert_mobiles_link_visible()
         .assert_laptops_link_visible())

    @pytest.mark.ui
    @allure.title("Проверка двойного клика")
    def test_double_click(self, web_element_practice_page, sidebar_practice_page):
        (web_element_practice_page
         .open_practice_page())

        expected_text = sidebar_practice_page.get_text_field_1()

        (sidebar_practice_page
         .copy_text_double_click()
         .assert_field_2_text(expected_text))

    @pytest.mark.ui
    @allure.title("Проверка Drag and Drop")
    def test_drag_and_drop(self, web_element_practice_page, sidebar_practice_page):
        (web_element_practice_page
         .open_practice_page())
        (sidebar_practice_page
         .drag_and_drop_object()
         .assert_object_dropped())

    @pytest.mark.ui
    @allure.title("Проверка Slider")
    def test_slider(self, web_element_practice_page, sidebar_practice_page):
        target_price_range = (30, 400)
        (web_element_practice_page
         .open_practice_page())
        (sidebar_practice_page
         .set_price_range(target_price_range)
         .assert_price_range(target_price_range))

    @pytest.mark.ui
    @allure.title("Выставление диапазона цен в слайдере")
    def test_set_price_range(self, web_element_practice_page, sidebar_practice_page):
        expected_price = (120, 125)

        (web_element_practice_page
         .open_practice_page())

        (sidebar_practice_page
         .set_price_range(expected_price)
         .assert_price_range(expected_price))

    @pytest.mark.ui
    @allure.title("Кастомный дабл клик")
    def test_custom_double_click(self, web_element_practice_page, sidebar_practice_page):
        random_word = generate_random_string(10)

        (web_element_practice_page
         .open_practice_page())

        (sidebar_practice_page
         .clear_field_1()
         .assert_field_1_is_empty()
         .fill_field_1(random_word)
         .copy_text_double_click()
         .assert_field_2_text(random_word))

    @pytest.mark.ui
    @allure.title("Перетаскивание ссылки Posts (Atom) в текстовое поле")
    def test_drag_and_drop_link(self, web_element_practice_page, sidebar_practice_page):
        expected_url = "https://testautomationpractice.blogspot.com/feeds/posts/default"
        (web_element_practice_page
         .open_practice_page())

        (sidebar_practice_page
         .drag_atom_link_to_field2()
         .assert_field2_url(expected_url))
