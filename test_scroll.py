import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/scrollbars")

    # Wait until the element is visible and then scroll into view
    element = page.get_by_role("button", name="Hiding Button")
    element.wait_for(state="visible")
    element.scroll_into_view_if_needed()

    time.sleep(2)  # Adding delay before clicking
    element.click()
    time.sleep(2)  # Adding delay after clicking to observe the result

    # ---------------------
    context.close()
    browser.close()
