from playwright.sync_api import Page, expect
import pytest, time

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # This fixture runs before each test to navigate to the necessary page.
    # First, it navigates to the root page, then clicks to reach the "Smart Table" section.
    page.goto('http://localhost:4200/')
    page.get_by_text('Forms').click()  # Click on 'Tables & Data' menu item
    page.get_by_text('Datepicker').click()    # Click on 'Smart Table' to open the relevant page

def datepicker(page: Page):
    date_picker = page.get_by_placeholder("Form Picker")
    date_picker.click()
    # Locate a day element with the text "1" and click it (this selects October 1st)
    page.locator('[class="day-cell ng-star-inserted"]').get_by_text("1", exact=True).click()
    
    expect(date_picker).to_have_value('Oct 1, 2024')

from datetime import datetime

def test_datepicker2(page: Page):
    # Get the current date
    current_date = datetime.now()
    
    # Find and click on the date picker field using placeholder text
    date_picker = page.get_by_placeholder("Form Picker")
    date_picker.click()
    
    # Extract the current day and remove leading zero if present
    current_day = current_date.strftime("%d").lstrip('0')
    print(type(current_day), 'that was current day')
    
    # Locate the current day element and click it
    page.locator('[class="today day-cell ng-star-inserted"]').click()
    
    # Format the current date to match the expected value format (e.g., 'Oct 5, 2024')
    expected_value = current_date.strftime('%b ') + str(int(current_date.strftime('%d'))) + current_date.strftime(', %Y')
    # Assert that the selected date matches the expected value
    expect(date_picker).to_have_value(expected_value)









