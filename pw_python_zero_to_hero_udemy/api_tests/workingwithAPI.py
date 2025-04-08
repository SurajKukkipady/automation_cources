import pytest
from playwright.sync_api import sync_playwright

def handle_tags_route(route, request):
    # Fulfill the API request with a mock response
    # This replaces the actual API call with predefined tags
    route.fulfill(
        status=200,  # HTTP 200 OK status
        content_type="application/json",  # Specify JSON content type
        body='{"tags": ["Test", "Kukki"]}'  # Predefined mock tags
    )

def test_mock_tags_api():
    # Create Playwright instance
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Intercept and mock the tags API endpoint
        page.route("**/api/tags", handle_tags_route)
        page.goto("https://conduit.bondaracademy.com/")
        page.wait_for_timeout(10000)  # 10 seconds delay
        browser.close()