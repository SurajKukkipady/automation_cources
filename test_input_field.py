'''Scenario
Record setting text into the input field and pressing the button.
Then execute your test to make sure that the button name is changing.'''

from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://www.uitestingplayground.com/textinput")
    page.get_by_placeholder("MyButton").click()
    page.get_by_placeholder("MyButton").fill("Hello World")
    page.get_by_role("button", name="Button That Should Change it'").click()
    expect(page.get_by_role("button", name="Hello World")).to_be_visible()

    context.close()
    browser.close()


