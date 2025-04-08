from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # Navigate to the page before each test
    page.goto('http://localhost:4200/')
    page.get_by_text('Forms').click()
    page.get_by_text('Form Layouts').click()

def test_input_fields(page: Page):
    using_the_grid_email_input = page.locator('nb-card', has_text='Using the Grid').get_by_role('textbox', name='Email')

    # Fill the email input using fill
    using_the_grid_email_input.fill('test@test.com')

    #  To clear the input field
    using_the_grid_email_input.clear()

    # For typing the email with a delay between each character
    using_the_grid_email_input.type("test2@test.com", delay=500)

    # Generic assertion to check input value
    input_value = using_the_grid_email_input.input_value()
    assert input_value == 'test2@test.com'

    # Locator assertion to ensure the input field has the correct value
    expect(using_the_grid_email_input).to_have_value('test2@test.com')

