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
         .open_tab_promotions()
         .check_promo_sber())

    @pytest.mark.ui
    @allure.title("Проверка отображения активной промоакции")
    @allure.link("https://testit.example.com/tc-1")
    def test_active_promotion(self, otzivik_promotion_page):
        (otzivik_promotion_page
         .open()
         )




