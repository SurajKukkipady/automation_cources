from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_successful_checkout(page: Page):
    # Login
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Add to cart
    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()

    # Go to cart
    cart = CartPage(page)
    cart.go_to_cart()
    cart.click_checkout()


    # Fill checkout info and complete
    checkout = CheckoutPage(page)
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.complete_checkout()

    # Verify order confirmation
    confirmation = checkout.get_confirmation_message()
    assert confirmation == "Thank you for your order!", \
        f"Expected 'Thank you for your order!', but got '{confirmation}'"
    

def test_verify_price_and_tax(page: Page):
    # Login and add product
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_multiple_items_to_cart(3)

    cart = CartPage(page)
    cart.go_to_cart()
    cart.click_checkout()

    checkout = CheckoutPage(page)
    checkout.fill_customer_info("John", "Doe", "12345")

    # Get pricing details
    item_prices = checkout.get_item_prices()
    subtotal = checkout.get_subtotal()
    tax = checkout.get_tax()
    total = checkout.get_total()

    calculated_subtotal = round(sum(item_prices), 2)
    calculated_total = round(calculated_subtotal + tax, 2)

    assert subtotal == calculated_subtotal, f"Expected subtotal {calculated_subtotal}, but got {subtotal}"
    assert total == calculated_total, f"Expected total {calculated_total}, but got {total}"

def test_checkout_with_empty_info_shows_error(page: Page):
    # Login and add product
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()

    cart = CartPage(page)
    cart.go_to_cart()
    cart.click_checkout()

    checkout = CheckoutPage(page)

    # Try to continue without filling info
    checkout.click_continue_without_info()

    error_msg = checkout.get_error_message()
    assert error_msg is not None, "Expected an error message, but none was shown."
    assert "First Name is required" in error_msg, f"Unexpected error message: {error_msg}"


