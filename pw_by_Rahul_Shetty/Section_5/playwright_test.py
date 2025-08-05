def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")

# chromium in headless by default
def test_playwright_shortcut(page):
    page.goto("https://google.com")