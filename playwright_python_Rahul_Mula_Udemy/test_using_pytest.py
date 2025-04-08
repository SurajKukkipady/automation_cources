from playwright.sync_api import Page

DOCS_URL = "https://playwright.dev/python/docs/intro"


def test_page_has_get_started_link(page: Page):
    page.goto("https://playwright.dev/python")

    link = page.get_by_role("link", name="GET STARTED")
    link.click()

    assert page.url == DOCS_URL

#To run use pytest test_using_pytest.py
#To run in headed mode use pytest test_using_pytest.py --headed
#To run in a different browser use pytest test_using_pytest.py --browser=firefox