"""Scenario
Record the following steps. Press the button below and wait for data to appear (15 seconds), click on text of the loaded label.
Then execute your test to make sure it waits for label text to appear."""

import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("http://www.uitestingplayground.com/ajax")
    #clicking on the button
    page.get_by_role("button", name="Button Triggering AJAX Request").click()
    #waiting for the element to be visible after the delay
    page.wait_for_selector("text=Data loaded with AJAX get", state="visible")
    #validation
    expect(page.get_by_text("Data loaded with AJAX get")).to_be_visible()

    context.close()
    browser.close()

