from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_link = page.locator(".shopping_cart_link")
        self.checkout_button = page.locator('[data-test="checkout"]')

    def go_to_cart(self):
        self.cart_link.click()

    def click_checkout(self):
        self.checkout_button.click()
