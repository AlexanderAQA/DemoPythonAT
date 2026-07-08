import logging
import os
import sys
import allure
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.account_page import AccountPage
from pages.books_page import BooksPage
from pages.cart_page import CartPage
from src.utils.api_client_hh import ApiHH
from src.utils.api_client_weather import ApiWeather

# Сделано для локального запуска, иначе сохраняет allure-отчет не в том месте
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.utils.api_client import ApiClient
from src.screenshots import Screenshots
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from src.utils.test_data import generate_random_string

logger = logging.getLogger(__name__)

def pytest_addoption(parser):
    parser.addoption("--debug-mode")

@pytest.fixture(autouse=True)
def driver(request):
    logger.debug(f"driver: request\n{request}")
    global driver
    # Инициализация хром драйвера
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    # chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    driver.implicitly_wait(4)
    request.node._driver = driver
    logger.debug("yield driver")
    yield driver
    logger.debug(f"Закрываем вебдрайвер: {driver.current_url}")
    driver.quit()

@pytest.fixture()
def clear_cookies(driver):
    yield
    logger.debug("Удаляем cookie браузера")
    driver.delete_all_cookies()


@pytest.fixture(autouse=True, scope="session")
def set_logger(request):
    global logger
    debug_value = str(request.config.getoption("--debug-mode")).lower()
    debug_enabled = debug_value in ("true", "yes")
    logger = logging.getLogger()

    if debug_enabled:
        print("Debug ON")
        log_level = logging.DEBUG
    else:
        print("Debug OFF")
        log_level = logging.INFO

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ])
    logger = logging.getLogger()

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    console_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(console_handler)

    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("selenium").setLevel(logging.WARNING)


@pytest.fixture()
def generate_string():
    with allure.step("Генерируем случайную строку"):
        return generate_random_string(7)


def pytest_exception_interact(node, report):
    if report.failed:
        driver = getattr(node, "_driver", None)
        if driver:
            # Сохраняем скриншот
            screenshot_path = os.path.join(Screenshots.dirname, f"{datetime.now().strftime("%H-%M-%S-%d-%m-%Y")}_{node.name}.png")
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

@pytest.fixture(scope="function", autouse=True)
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

@pytest.fixture(scope="function", autouse=True)
def api_client_hh():
    return ApiHH()

@pytest.fixture(scope="function")
def api_client_weather():
    return ApiWeather()
