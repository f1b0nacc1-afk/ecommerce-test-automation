import allure
import pytest


@allure.feature("Shopping Cart")
@allure.story("Cart management")
@pytest.mark.ui
class TestCart:
    @allure.title("Add single product to cart")
    @pytest.mark.smoke
    def test_add_product_to_cart(self, logged_in_user):
        inventory = logged_in_user
        inventory.add_product_to_cart_by_index(0)

        assert inventory.get_cart_items_count() == 1

    @allure.title("Add multiple products to cart")
    def test_add_multiple_products(self, logged_in_user):
        inventory = logged_in_user
        inventory.add_product_to_cart_by_index(0)
        inventory.add_product_to_cart_by_index(1)
        inventory.add_product_to_cart_by_index(2)

        assert inventory.get_cart_items_count() == 3

    @allure.title("Cart displays added products")
    def test_cart_contains_added_products(self, logged_in_user, cart_page):
        inventory = logged_in_user
        product_name = inventory.get_product_names()[0]

        inventory.add_product_to_cart_by_index(0)
        inventory.open_cart()

        assert cart_page.get_items_count() == 1
        assert product_name in cart_page.get_item_names()
