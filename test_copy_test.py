import time
from playwright.sync_api import Playwright, sync_playwright

def test_welcome_user(playwright: Playwright) -> None:
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Navigate to the page where the element is located
    page.goto("http://www.uitestingplayground.com/verifytext")  # Replace with the actual URL containing the element

    # Locate the text "Welcome UserName!" inside the div
    welcome_message = page.locator("div.bg-primary span.badge-secondary span").text_content().strip()
    
    # Print the welcome message
    print(f"Welcome message: Welcome {welcome_message}!")
    
    # Adding delay to observe the execution
    time.sleep(5)

    # ---------------------
    context.close()
    browser.close()
