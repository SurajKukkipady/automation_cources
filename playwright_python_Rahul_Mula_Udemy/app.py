from playwright.sync_api import sync_playwright

with sync_playwright() as playright:
    browser = playright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://playwright.dev/python/docs/api-testing')
    docs_button = page.get_by_role('link', name='Docs')
    docs_button.click()
    print(page.url)
    browser.close() 

    # In REPL
    # from playwright.sync_api import sync_playwright