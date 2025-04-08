'''Scenario
Record 2 consecutive link clicks.
Execute the test and make sure that click count is increasing by 2.'''

import time
from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://www.uitestingplayground.com/mouseover")
    page.get_by_text("Click me").click()
    page.get_by_text("Click me").click()
    time.sleep(1)
    click_count_text = page.locator("#clickCount").text_content()
    assert click_count_text == "2"

    context.close()
    browser.close()

