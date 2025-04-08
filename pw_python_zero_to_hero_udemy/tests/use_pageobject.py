from playwright.sync_api import Page, expect
import pytest, time
from page_object.navigation_page import NavigationPage

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    page.goto('http://localhost:4200/')

def test_navigate_to_form_layouts(page: Page):
    navigation = NavigationPage(page)
    navigation.form_layouts_page()