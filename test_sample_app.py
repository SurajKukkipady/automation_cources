from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/sampleapp")
    page.get_by_placeholder("User Name").click()
    page.get_by_placeholder("User Name").fill("test")
    page.get_by_placeholder("User Name").press("Tab")
    page.get_by_placeholder("********").fill("pwd")
    page.get_by_role("button", name="Log In").click()
    expect(page.get_by_text("Welcome, test!")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()

