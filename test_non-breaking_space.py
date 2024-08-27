'''Scenario
Use the following xpath to find the button in your test:
//button[text()='My Button']
Notice that the XPath does not work. Change the space between 'My' and 'Button' 
to a non-breaking space. This time the XPath should be valid.'''

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

