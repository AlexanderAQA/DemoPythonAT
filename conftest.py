import logging
import os
import sys
from pathlib import Path

import allure
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Сделано для локального запуска, иначе сохраняет allure-отчет не в том месте
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.utils.api_client_hh import ApiHH
from src.utils.api_client_weather import ApiWeather
from src.utils.api_client import ApiClient
from src.screenshots import Screenshots
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.books_page import BooksPage
from pages.cart_page import CartPage
from src.utils.test_data import generate_random_string

logger = logging.getLogger(__name__)

@pytest.fixture(autouse=True)
def driver(request):
    if request.node.get_closest_marker("api"):
        logger.info("Для API теста не запускаем вебдрайвер")
        yield None
        return
    else:
        logger.info(f"driver: request\n{request}")
        global driver
        # Инициализация хром драйвера
        chrome_options = Options()


        if os.getenv("CI"):
            chrome_options.add_argument("--headless=new")
        else:
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        driver.implicitly_wait(4)
        request.node._driver = driver
        logger.info("yield driver")
        yield driver
        logger.info(f"Закрываем вебдрайвер: {driver.current_url}")
        driver.quit()

@pytest.fixture()
def clear_cookies(driver):
    yield
    logger.info("Удаляем cookie браузера")
    driver.delete_all_cookies()


def configure_logging():
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    logger = logging.getLogger()

    if logger.handlers:
        return

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    file_handler = logging.FileHandler(logs_dir / "test.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    configure_logging()


@pytest.fixture(autouse=True)
def log_test_start_end(request):
    log = logging.getLogger("pytest")

    log.info("=" * 80)
    log.info(f"START TEST: {request.node.nodeid}")

    yield

    log.info(f"END TEST: {request.node.nodeid}")


@pytest.fixture()
def generate_string():
    with allure.step("Генерируем случайную строку"):
        return generate_random_string(7)


def pytest_exception_interact(node, report):
    if report.failed:
        driver = getattr(node, "_driver", None)
        if driver:
            # Сохраняем скриншот
            screenshot_path = os.path.join(Screenshots.dirname, f"{datetime.now().strftime('%H-%M-%S-%d-%m-%Y')}_"
                                                                f"{node.name}.png")
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            driver.save_screenshot(screenshot_path)
            print(f"Скриншот сохранён: {screenshot_path}")

def pytest_configure(config):
    allure_dir = os.path.join(project_root, "allure-results")
    config.option.allure_report_dir = allure_dir

@pytest.fixture(scope="function", autouse=True)
def base_page(driver):
    return BasePage(driver)

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    yield page

@pytest.fixture(scope="function", autouse=False)
def main_page(driver):
    page = MainPage(driver)
    yield page

@pytest.fixture(scope="function")
def api_client():
    return ApiClient()

@pytest.fixture(scope="function", autouse=False)
def account_page(driver):
    page = AccountPage(driver)
    yield page

@pytest.fixture(scope="function", autouse=False)
def books_page(driver):
    page = BooksPage(driver)
    yield page

@pytest.fixture(scope="function", autouse=False)
def cart_page(driver):
    page = CartPage(driver)
    yield page

@pytest.fixture(scope="function")
def api_client_hh():
    return ApiHH()

@pytest.fixture(scope="function")
def api_client_weather():
    return ApiWeather()
