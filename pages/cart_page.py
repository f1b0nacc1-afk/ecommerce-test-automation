from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

    def get_items_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def proceed_to_checkout(self) -> None:
        self.click(self.CHECKOUT_BUTTON)

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self) -> None:
        self.click(self.FINISH_BUTTON)

    def get_completion_message(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_item_names(self) -> list[str]:
        return [el.text for el in self.driver.find_elements(*self.ITEM_NAMES)]
