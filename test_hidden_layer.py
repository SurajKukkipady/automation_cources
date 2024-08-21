from playwright.sync_api import Playwright, sync_playwright, expect

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.uitestingplayground.com/hiddenlayers")

    # Click the green button if visible
    green_button = page.locator("#greenButton")
    if green_button.is_visible():
        green_button.click()
    else:
        print("Green button is not visible or clickable")

    # Click the blue button if visible
    blue_button = page.locator("#blueButton")
    if blue_button.is_visible():
        blue_button.click()
    else:
        print("Blue button is not visible or clickable")

    # Optional: Add explicit wait for buttons to be visible
    
    #page.wait_for_selector("#blueButton", state="visible")

    # ---------------------
    context.close()
    browser.close()
