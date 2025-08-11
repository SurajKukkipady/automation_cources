from playwright.sync_api import Page

def test_playwright_basics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")

# chromium in headless by default
def test_playwright_shortcut(page: Page):
    page.goto("https://google.com")

def test_core_locators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('combobox').select_option('teach')
    page.get_by_role("checkbox", name = "terms").click()
    page.get_by_role('button', name='Sign In').click()
    page.wait_for_timeout(5000)
