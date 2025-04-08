"""Scenario
Record button click and then duplicate the button click step in your test.
Execute the test to make sure that green button can not be hit twice."""

from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://www.uitestingplayground.com/hiddenlayers")

    green_button = page.locator("#greenButton")
    if green_button.is_visible():
        green_button.click()
    else:
        print("Green button is not visible or clickable")

    context.close()
    browser.close()
