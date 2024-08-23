import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/mouseover")
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()

