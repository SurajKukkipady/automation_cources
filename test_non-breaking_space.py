import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/nbsp")

    #//button[text()='My Button']
    #In XPath, non-breaking spaces are represented as &#160; or \u00A0.

    page.locator("//button[text()='My\u00A0Button']").click()
    
    # ---------------------
    context.close()
    browser.close()

