from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playright:
    browser = playright.chromium.launch(headless=False, args=["--disable-dev-shm-usage", "--disable-blink-features=AutomationControlled"])
    context = browser.new_context()

    page = context.new_page()
    page.goto('https://accounts.google.com')
    page.get_by_label("Email or Phone").fill('surajkukkipady8')
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Enter your password").fill('ABcd@1234')
    page.get_by_role("button", name="Next").click()
    page.pause()

    #save the auth state
    context.storage_state(path="playwright/.auth/storage_state.json")
    context.close()