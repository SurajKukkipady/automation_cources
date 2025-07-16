#pages/inventory_page.py
from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.item_names = page.locator(".inventory_item_name")
        self.item_prices = page.locator(".inventory_item_price")

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def get_item_names(self):
        return self.item_names.all_inner_texts()

    def get_item_prices(self):
        prices = self.item_prices.all_inner_texts()
        return [float(p.replace("$", "")) for p in prices]
    
    def get_product_count(self):
        return self.page.locator(".inventory_item").count()
    
    def add_first_item_to_cart(self):
        self.page.locator('[data-test^="add-to-cart-"]').first.click()

    def get_first_item_button_text(self):
        return self.page.locator('[data-test^="remove-"]').first.inner_text()

    def get_cart_badge_count(self):
        return self.page.locator(".shopping_cart_badge").inner_text()
    
    def add_multiple_items_to_cart(self, count: int):
        buttons = self.page.locator('[data-test^="add-to-cart-"]')
        total_buttons = buttons.count()
        assert count <= total_buttons, f"Requested {count} items but only {total_buttons} available"

        for i in range(count):
            buttons.nth(i).click()

    def logout(self):
        self.page.locator("#react-burger-menu-btn").click()
        self.page.locator("#logout_sidebar_link").click()

