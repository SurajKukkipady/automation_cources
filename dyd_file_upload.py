from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://dyp2-qa02.dev.hhstechgroup.com/landing")
    page.get_by_role("button", name="Sign In / Register").click()
    page.get_by_label("Username *").click()
    page.get_by_label("Username *").fill("dyp.provider+13aug24_02@gmail.com")
    page.get_by_label("Password *").click()
    page.get_by_label("Password *").fill("Aa123321!")
    page.get_by_role("button", name="Log in").click()
    page.get_by_role("button", name="AGREE", exact=True).click()
    page.get_by_label("Close").click()
    page.get_by_label("Continue").click()

    page.get_by_text("Upload Documents").click()
    file_input = page.locator('input[type="file"]')
    file_input.set_input_files("aaaaa.png")
    page.locator(".sc-dnqmqq > svg").nth(0).click()
    page.get_by_role("button", name="Next").click()

    # ---------------------
    context.close()
    browser.close()

