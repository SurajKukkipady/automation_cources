from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/dynamicid")
    page.get_by_role("button", name="Button with Dynamic ID").click()
    page.get_by_role("button", name="Button with Dynamic ID").click()

    # ---------------------
    context.close()
    browser.close()
