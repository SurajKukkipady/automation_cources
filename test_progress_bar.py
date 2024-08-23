from playwright.sync_api import Playwright, sync_playwright, expect
import time

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("http://www.uitestingplayground.com/progressbar")
    page.get_by_role("button", name="Start").click()

    while True:
        progress = int(page.locator("#progressBar").get_attribute("aria-valuenow"))
        if progress >= 75:
            page.get_by_role("button", name="Stop").click()
            break
        time.sleep(0.1)  # Adding a short delay to avoid excessive CPU usage
    
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()

