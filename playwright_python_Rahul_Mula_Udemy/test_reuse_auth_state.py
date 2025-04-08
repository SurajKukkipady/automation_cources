from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playright:
    browser = playright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="playwright/.auth/storage_state.json")

    page = context.new_page()
    page.goto('https://accounts.google.com')
    page.pause()