from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/clientdelay")
    page.get_by_role("button", name="Button Triggering Client Side").click()
    page.wait_for_selector("text=Data calculated on the client", state="visible")
    expect(page.get_by_text("Data calculated on the client")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()

