from playwright.sync_api import Page, expect
import pytest

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # Navigate to the page before each test
    page.goto('http://localhost:4200/')
    page.get_by_text('Forms').click()
    page.get_by_text('Form Layouts').click()

def test_radio_buttons(page: Page):
    # Locate the form section that has the text "Using the Grid"
    using_the_grid_form = page.locator('nb-card', has_text='Using the Grid')

    # Check the radio button labeled "Option 1", forcing the action even if it's not visible
    using_the_grid_form.get_by_role('radio', name='Option 1').check(force=True) #force=True

    # Verify that the "Option 1" radio button is checked
    radio_status = using_the_grid_form.get_by_role('radio', name='Option 1').is_checked()
    assert radio_status == True  # Assert that the radio button is indeed checked

    # Another way to assert that "Option 1" is checked using Playwright's built-in expect function
    expect(using_the_grid_form.get_by_role('radio', name='Option 1')).to_be_checked()

    # Check the radio button labeled "Option 2"
    using_the_grid_form.get_by_role('radio', name='Option 2').check(force=True)

    # Verify that "Option 1" is no longer checked
    assert using_the_grid_form.get_by_role('radio', name='Option 1').is_checked() == False

    # Verify that "Option 2" is now checked
    assert using_the_grid_form.get_by_role('radio', name='Option 2').is_checked() == True


