from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/overlapped")
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Hello World")
    page.get_by_placeholder("Name").press("Enter")

    # ---------------------
    context.close()
    browser.close()
