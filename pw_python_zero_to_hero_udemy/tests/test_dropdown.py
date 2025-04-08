from playwright.sync_api import Page, expect
import pytest, time

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # Navigate to the page before each test
    page.goto('http://localhost:4200/')

def test_drop_down(page: Page):
    page.locator('ngx-header nb-select').click()

    #To do later
    
    