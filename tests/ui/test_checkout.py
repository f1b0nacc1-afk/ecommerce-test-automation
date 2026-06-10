import allure
import pytest

from data.test_data import CHECKOUT_DATA


@allure.feature("Checkout")
@allure.story("Order flow")
@pytest.mark.ui
class TestCheckout:
    @allure.title("Complete checkout flow")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_complete_checkout(self, logged_in_user, cart_page):
        inventory = logged_in_user
        inventory.add_product_to_cart_by_index(0)
        inventory.add_product_to_cart_by_index(1)
        inventory.open_cart()

        cart_page.proceed_to_checkout()
        cart_page.fill_checkout_info(
            CHECKOUT_DATA["first_name"],
            CHECKOUT_DATA["last_name"],
            CHECKOUT_DATA["postal_code"],
        )
        cart_page.finish_order()

        assert cart_page.get_completion_message() == "Thank you for your order!"

    @allure.title("Sort products by price low to high")
    def test_sort_products_by_price(self, logged_in_user):
        inventory = logged_in_user
        inventory.sort_by("lohi")
        prices = inventory.get_product_prices()

        assert prices == sorted(prices)
