from playwright.sync_api import Page, expect
import pytest, time

# Fixture to set up the browser and navigate to the required page before each test
@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # Go to the local development server (replace the URL with actual URL if needed)
    page.goto('http://localhost:4200/')
    
    # Navigate to the section containing 'Modal & Overlays'
    page.get_by_text('Modal & Overlays').click()

    # Click on 'Tooltip' to bring up the tooltip page
    page.get_by_text('Tooltip').click()

# Test to verify tooltip functionality
def test_tooltips(page: Page):
    # Hover over the button labeled 'Top' to trigger the tooltip
    page.get_by_role("button", name="Top").hover()

    # Locate the tooltip element (assuming the tooltip is represented by 'nb-tooltip' tag)
    tooltip = page.locator('nb-tooltip')

    # Get the text content of the tooltip
    tooltip_text = tooltip.text_content()

    # Assert that the tooltip text is as expected
    assert tooltip_text == "This is a tooltip"
