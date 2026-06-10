import allure
import pytest

from config import settings
from data.test_data import INVALID_LOGIN_CASES, VALID_USERS


@allure.feature("Authentication")
@allure.story("Login")
@pytest.mark.ui
class TestLogin:
    @allure.title("Successful login with valid credentials")
    @pytest.mark.smoke
    @pytest.mark.parametrize("user", VALID_USERS, ids=lambda u: u["username"])
    def test_successful_login(self, login_page, inventory_page, user):
        login_page.open()
        login_page.login(user["username"], user["password"])

        assert inventory_page.get_products_count() == 6
        assert inventory_page.get_cart_items_count() == 0

    @allure.title("Login fails with invalid credentials")
    @pytest.mark.parametrize("case", INVALID_LOGIN_CASES, ids=lambda c: c["username"] or "empty_username")
    def test_failed_login(self, login_page, case):
        login_page.open()
        login_page.login(case["username"], case["password"])

        assert case["error"] in login_page.get_error_message()
        assert not login_page.is_inventory_visible()

    @allure.title("Locked out user cannot login")
    @pytest.mark.smoke
    def test_locked_out_user(self, login_page):
        login_page.open()
        login_page.login(settings.LOCKED_USER, settings.STANDARD_PASSWORD)

        assert "locked out" in login_page.get_error_message().lower()
