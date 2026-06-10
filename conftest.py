import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from config import settings
from pages import CartPage, InventoryPage, LoginPage
from utils import APIClient


def _create_chrome_service() -> ChromeService:
    driver_path = settings.CHROMEDRIVER_PATH or os.getenv("CHROMEDRIVER_PATH")
    if driver_path:
        return ChromeService(driver_path)
    return ChromeService(ChromeDriverManager().install())


@pytest.fixture(scope="function")
def driver():
    options = ChromeOptions()
    if settings.CHROME_BIN:
        options.binary_location = settings.CHROME_BIN
    if settings.HEADLESS:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = _create_chrome_service()
    browser = webdriver.Chrome(service=service, options=options)
    browser.implicitly_wait(settings.IMPLICIT_WAIT)

    yield browser

    browser.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def logged_in_user(login_page, inventory_page):
    login_page.open()
    login_page.login(settings.STANDARD_USER, settings.STANDARD_PASSWORD)
    assert inventory_page.get_products_count() > 0
    return inventory_page


@pytest.fixture(scope="session")
def api_client():
    return APIClient(settings.JSONPLACEHOLDER_BASE_URL)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            settings.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
            screenshot_path = settings.SCREENSHOTS_DIR / f"{item.name}.png"
            driver.save_screenshot(str(screenshot_path))
