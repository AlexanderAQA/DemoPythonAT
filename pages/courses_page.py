from pages.playwright_base_page import PlaywrightBasePage


class CoursesPage(PlaywrightBasePage):
    COURSES_PATH = "/kursy"

    def open_page(self):
        url = self.BASE_URL + self.COURSES_PATH
        self.logger.info(f"CoursesPage: Открываем страницу '{url}'")
        self.open(url)
        return self

