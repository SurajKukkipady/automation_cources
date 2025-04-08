from playwright.sync_api import Page, expect
import pytest, time

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # This fixture runs before each test to navigate to the necessary page.
    # First, it navigates to the root page, then clicks to reach the "Smart Table" section.
    page.goto('http://localhost:4200/')
    page.get_by_text('Tables & Data').click()  # Click on 'Tables & Data' menu item
    page.get_by_text('Smart Table').click()    # Click on 'Smart Table' to open the relevant page

def test_table(page: Page):
    page.get_by_role("row", name="twitter@outlook.com").locator('.nb-edit').click() #Access the row by email
    page.locator('input-editor').get_by_placeholder('Age').clear() #Clear the age field
    page.locator('input-editor').get_by_placeholder('Age').fill('30') #Update the age field
    page.locator('.nb-checkmark').click() #save

#Scenario 2, check table filter
def test_table2(page: Page):
    # List of ages to test with
    ages = ['20', '30']

    # Loop through each age in the list
    for age in ages:
        # Fill the age input field with the current age value
        page.locator('input-filter').get_by_placeholder('Age').fill(age)

        # Locate all table rows within the tbody tag
        agerow = page.locator('tbody tr')

        # Loop through each row in the table
        for i in range(agerow.count()):
            # Get the text content of the last cell (td) in the current row
            value = agerow.nth(i).locator('td').last.text_content()

            # Assert that the value in the last cell is equal to the current age being tested
            assert value == age



    