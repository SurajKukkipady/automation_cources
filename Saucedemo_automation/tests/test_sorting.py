#tests/test_sorting.py
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import Page

def test_sort_name_z_to_a(page: Page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.sort_by("za")

    item_names = inventory.get_item_names()
    sorted_names = sorted(item_names, reverse=True)
    assert item_names == sorted_names, f"Expected {sorted_names}, but got {item_names}"


def test_sort_name_a_to_z(page: Page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.sort_by("az")

    item_names = inventory.get_item_names()
    sorted_names = sorted(item_names, reverse=False)
    assert item_names == sorted_names, f"Expected {sorted_names}, but got {item_names}"
    

def test_sort_price_high_to_low(page: Page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.sort_by("hilo")

    prices = inventory.get_item_prices()
    sorted_prices = sorted(prices, reverse=True)
    assert prices == sorted_prices, f"Expected {sorted_prices}, but got {prices}"

def test_sort_price_low_to_high(page: Page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.sort_by("lohi")

    prices = inventory.get_item_prices()
    sorted_prices = sorted(prices, reverse=False)
    assert prices == sorted_prices, f"Expected {sorted_prices}, but got {prices}"
    