from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/shadowdom")
    page.locator("#buttonGenerate").click()
    page.locator("#buttonCopy").click()
    page.wait_for_timeout(1000)
    clipboard_content = page.evaluate("navigator.clipboard.readText()")
    print(clipboard_content)

    # ---------------------
    context.close()
    browser.close()

