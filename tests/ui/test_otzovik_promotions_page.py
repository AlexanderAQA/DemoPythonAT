import allure
import pytest

@allure.epic("Cтраница промоакции")
# @allure.story("")
class TestOtzovikPromotionsPage:

    @pytest.mark.ui
    @allure.title("Проверка отображения активной промоакции")
    @allure.link("https://testit.example.com/tc-1")
    def test_active_promotion(self, otzivik_promotion_page, otzivik_main_page):
        (otzivik_main_page
         .open()
         .open_tab_promotions())

        (otzivik_promotion_page
         .check_promo_ozon())

    @pytest.mark.ui
    @allure.title("Проверка перехода в активную промоакцию")
    @allure.link("https://testit.example.com/tc-1")
    def test_transition_active_promotion(self, otzivik_promotion_page):
        (otzivik_promotion_page
         .open()
         .open_details_campaign()
         .check_promo_active()
         .check_have_promo_ozon_text())

    @pytest.mark.ui
    @allure.title("Проверка завершенной промоакции")
    @allure.link("https://testit.example.com/tc-1")
    def test_completed_promotion(self, otzivik_promotion_page):
        (otzivik_promotion_page
         .open()
         .check_promo_completed_zufra())

    @pytest.mark.ui
    @allure.title("Проверка наличия информационного сообщения")
    @allure.link("https://testit.example.com/tc-1")
    def test_have_info_message(self, otzivik_promotion_page):
        (otzivik_promotion_page
         .open()
         .check_info_message())