import os
import sys
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

from src.utils.api_client import ApiClient
from src.screenshots import Screenshots
from pages.base_page import BasePage
from pages.login_page.login_page import LoginPage
from pages.main_page.main_page import MainPage

@pytest.fixture(autouse=True)
def driver(request):
    global driver
    # Инициализация хром драйвера
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    driver.implicitly_wait(4)
    request.node._driver = driver
    yield driver
    driver.quit()

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
    return LoginPage(driver)

@pytest.fixture(scope="function", autouse=True)
def main_page(driver):
    return MainPage(driver)

@pytest.fixture(scope="function", autouse=True)
def api_client():
    return ApiClient()
