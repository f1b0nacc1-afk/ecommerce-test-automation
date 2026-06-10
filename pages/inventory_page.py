from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_ITEM = (By.CSS_SELECTOR, ".inventory_item")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    SORT_DROPDOWN = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "[id^='add-to-cart']")

    def get_products_count(self) -> int:
        return len(self.driver.find_elements(*self.INVENTORY_ITEM))

    def add_product_to_cart_by_index(self, index: int = 0) -> None:
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        buttons[index].click()

    def get_cart_items_count(self) -> int:
        if not self.is_visible(self.CART_BADGE):
            return 0
        return int(self.get_text(self.CART_BADGE))

    def open_cart(self) -> None:
        self.click(self.CART_LINK)

    def sort_by(self, option_value: str) -> None:
        dropdown = self.find(self.SORT_DROPDOWN)
        for option in dropdown.find_elements(By.TAG_NAME, "option"):
            if option.get_attribute("value") == option_value:
                option.click()
                break

    def get_product_names(self) -> list[str]:
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        names = []
        for item in items:
            name = item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
            names.append(name)
        return names

    def get_product_prices(self) -> list[float]:
        items = self.driver.find_elements(*self.INVENTORY_ITEM)
        prices = []
        for item in items:
            price_text = item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
            prices.append(float(price_text.replace("$", "")))
        return prices
