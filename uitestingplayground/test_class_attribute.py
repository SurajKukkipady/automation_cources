'''Scenario
Record primary (blue) button click and press ok in alert popup.
Then execute your test to make sure that it can identify the button using btn-primary class.'''

import time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://www.uitestingplayground.com/classattr")
    time.sleep(2)
    # Set up a listener for any dialog (e.g., alert, confirm)
    page.once("dialog", lambda dialog: dialog.dismiss())
    # Locate the button with the class attribute
    button_locator = page.locator("//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    button_locator.click()
    time.sleep(2)

    context.close()
    browser.close()
