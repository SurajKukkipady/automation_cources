from playwright.sync_api import Page, expect
import pytest, time

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # This fixture runs before each test to navigate to the necessary page.
    # First, it navigates to the root page, then clicks to reach the "Smart Table" section.
    page.goto('http://localhost:4200/')

#def test_slider(page: Page):
    