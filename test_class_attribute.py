import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/classattr")
    time.sleep(2)
    page.once("dialog", lambda dialog: dialog.dismiss())
    button_locator = page.locator("//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    button_locator.click()
    time.sleep(2)

    # time.sleep(2)
    # page.get_by_role("button", name="Button").nth(1).click()
    # time.sleep(2)
    # page.once("dialog", lambda dialog: dialog.dismiss())
    # time.sleep(2)
    # page.get_by_role("button", name="Button").nth(2).click()
    # time.sleep(2)

    # ---------------------
    context.close()
    browser.close()
