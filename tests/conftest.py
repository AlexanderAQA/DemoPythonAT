import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from src.screenshots import Screenshots
from pages.base_page import BasePage
from pages.login_page.login_page import LoginPage

@pytest.fixture(scope="function")
def driver(request):
    # Инициализация хром драйвера
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    # chrome_options.add_argument("--headless=new")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    driver.implicitly_wait(4)
    request.node._driver = driver
    yield driver
    driver.quit()

def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = getattr(node, "_driver", None)
        if driver:
            # Сохраняем скриншот
            screenshot_path = os.path.join(Screenshots.dirname, f"{datetime.now().strftime("%H-%M-%S-%d-%m-%Y")}_{node.name}.png")
            # os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            driver.save_screenshot(screenshot_path)
            print(f"Скриншот сохранён: {screenshot_path}")

@pytest.fixture
def base_page(driver):
    return BasePage(driver)

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)
