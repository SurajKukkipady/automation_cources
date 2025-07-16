from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator('[data-test="firstName"]')
        self.last_name_input = page.locator('[data-test="lastName"]')
        self.postal_code_input = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.confirmation_message = page.locator(".complete-header")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def complete_checkout(self):
        self.finish_button.click()

    def get_confirmation_message(self):
        expect(self.confirmation_message).to_be_visible()
        return self.confirmation_message.inner_text()
    
    def get_item_prices(self):
        prices = self.page.locator(".inventory_item_price").all_inner_texts()
        return [float(price.replace("$", "")) for price in prices]

    def get_subtotal(self):
        subtotal_text = self.page.locator(".summary_subtotal_label").inner_text()
        return float(subtotal_text.replace("Item total: $", ""))

    def get_tax(self):
        tax_text = self.page.locator(".summary_tax_label").inner_text()
        return float(tax_text.replace("Tax: $", ""))

    def get_total(self):
        total_text = self.page.locator(".summary_total_label").inner_text()
        return float(total_text.replace("Total: $", ""))
    
    def click_continue_without_info(self):
        self.continue_button.click()

    def get_error_message(self):
        error = self.page.locator('[data-test="error"]')
        return error.inner_text() if error.is_visible() else None
