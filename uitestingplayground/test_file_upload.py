import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/upload")
    # Locate the file input element by its ID and upload the specified file
    page.locator("#file-upload").set_input_files("aaaaa.png")
    # Locate and click the "Upload" button
    page.get_by_role("button", name="Upload").click()
    #Validate
    page.get_by_role("heading", name="File Uploaded!").click()

    context.close()
    browser.close()

