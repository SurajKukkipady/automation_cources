# tests/test_login.py
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

def test_login_success(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    #Assertion: User should be redirected to inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    logo = page.locator(".app_logo")
    expect(logo).to_have_text("Swag Labs")

def test_login_failure_locked_out_user(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")
    #Assertion: Error message should be displayed
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Epic sadface: Sorry, this user has been locked out.")

def test_login_performance_glitch_user(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("performance_glitch_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    logo = page.locator(".app_logo")
    expect(logo).to_have_text("Swag Labs")

def test_login_failure_invalid_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("invalid_user", "invalid_password")
    
    #Assertion: Error message should be displayed
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")

def test_login_failure_empty_credentials(page: Page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("", "")

    #Assertion: Error message should be displayed
    error_message = page.locator('[data-test="error"]')
    expect(error_message).to_be_visible()
    expect(error_message).to_have_text("Epic sadface: Username is required")

def test_logout(page: Page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.logout()

    #Assert we're back at the login page
    assert page.url == "https://www.saucedemo.com/", f"Expected to be on login page, but was on {page.url}"

    #Check that username field is visible
    assert page.locator('[data-test="username"]').is_visible(), "Username field is not visible after logout"



