'''Scenario
Create a test that finds an element with Welcome... text.'''

import time
from playwright.sync_api import Playwright, sync_playwright

def test_welcome_user(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("http://www.uitestingplayground.com/verifytext")
    welcome_message = page.locator("div.bg-primary span.badge-secondary span").text_content().strip()
    print(f"Welcome message: Welcome {welcome_message}!")
    time.sleep(1)

    context.close()
    browser.close()
