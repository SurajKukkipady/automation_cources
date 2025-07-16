#tests/test_checkout.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page

def test_products_displayed(page: Page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    product_count = inventory.get_product_count()

    assert product_count > 0, f"Expected at least one product, but found {product_count}."

def test_add_to_cart_one_item(page: Page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_first_item_to_cart()

    # ✅ Assert the button changes to "Remove"
    button_text = inventory.get_first_item_button_text()
    assert button_text == "Remove", f"Expected button to say 'Remove', but got '{button_text}'"

    #Assert cart badge shows 1
    cart_count = inventory.get_cart_badge_count()
    assert cart_count == "1", f"Expected cart badge to show '1', but got '{cart_count}'"

def test_add_multiple_items_to_cart(page: Page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)

    number_of_items_to_add = 3
    inventory.add_multiple_items_to_cart(number_of_items_to_add)

    cart_count = inventory.get_cart_badge_count()
    assert int(cart_count) == number_of_items_to_add, f"Expected cart count to be {number_of_items_to_add}, but got {cart_count}"

