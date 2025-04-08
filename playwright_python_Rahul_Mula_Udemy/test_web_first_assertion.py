from playwright.sync_api import Page, expect
import pytest

DOCS_URL = "https://playwright.dev/python/docs/intro"


@pytest.fixture(autouse=True, scope="function")
def visit_playwright(page: Page):
    page.goto("https://playwright.dev/python")
    yield page
    page.close()
    print("\n[ Fixture ]: page closed!")


def test_page_assertion(page: Page):
    link = page.get_by_role("link", name="GET STARTED")
    link.click()
    # assert statement
    assert page.url == DOCS_URL
    # expect page url
    expect(page).to_have_url(DOCS_URL)
    # expect page title
    expect(page).to_have_title("Installation | Playwright Python")

def test_page_element_assertion(page: Page):
    link = page.get_by_role("link", name="GET STARTED")
    expect(link).to_be_visible()
    #expect(link).not_to_be_visible()

def test_text_assertion(page: Page):
    heading = page.locator("h1.hero__title")
    expect(heading).to_contain_text("testing")
    expect(heading).not_to_contain_text("playwright")
    expect(heading).to_have_text("Playwright enables reliable end-to-end testing for modern web apps.")

    dropdown = page.locator("ul.dropdown__menu")
    expect(dropdown).to_contain_text("Python")
    expect(dropdown).to_contain_text("Java")
    expect(dropdown).to_contain_text("Node.js")
    expect(dropdown).to_contain_text(".NET")

def test_input_field_asserrtion(page: Page):
    input = page.get_by_placeholder("Search docs")
    # input is hidden initially
    expect(input).to_be_hidden()
    # search button
    search_btn = page.get_by_role("button", name="Search")
    search_btn.press("Control+KeyK") 
    # input should be visible/editable
    expect(input).to_be_editable()
    # input should be empty initially
    expect(input).to_be_empty()\
    # type some query in the input
    query = "assertions"
    input.fill(query)
    # expect the input value as query
    expect(input).to_have_value(query)
