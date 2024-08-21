import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/upload")
    #page.locator("#file-upload").click()
    page.locator("#file-upload").set_input_files("aaaaa.png")
    page.get_by_role("button", name="Upload").click()
    page.get_by_role("heading", name="File Uploaded!").click()
    #time.sleep(1000)

    # ---------------------
    context.close()
    browser.close()

