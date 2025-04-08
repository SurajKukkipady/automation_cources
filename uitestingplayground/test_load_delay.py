'''Scenario
Navigate to Home page and record Load Delays link click and button click on this page.
Then play the test. It should wait until page is loaded'''

from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://www.uitestingplayground.com/loaddelay")
    page.get_by_role("button", name="Button Appearing After Delay").click()

    context.close()
    browser.close()

