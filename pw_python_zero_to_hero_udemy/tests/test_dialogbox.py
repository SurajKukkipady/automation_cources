from playwright.sync_api import Page, expect
import pytest, time

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # This fixture runs before each test to navigate to the necessary page.
    # First, it navigates to the root page, then clicks to reach the "Smart Table" section.
    page.goto('http://localhost:4200/')
    page.get_by_text('Tables & Data').click()  # Click on 'Tables & Data' menu item
    page.get_by_text('Smart Table').click()    # Click on 'Smart Table' to open the relevant page

def test_dialog_box(page: Page):
    # Listen for a browser dialog (like an alert or confirm dialog) and accept it (click "Yes"/"OK").
    page.once("dialog", lambda dialog: dialog.accept())

    # Find the table row with the name "Mark Otto @mdo" and click the second link (nth(1) refers to the second link, first link is edit btn).
    page.get_by_role("row", name="  1 Mark Otto @mdo mdo@").get_by_role("link").nth(1).click()
