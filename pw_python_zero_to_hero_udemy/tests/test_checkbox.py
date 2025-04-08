from playwright.sync_api import Page, expect
import pytest, time

@pytest.fixture(scope='function', autouse=True)
def setup(page: Page):
    # Navigate to the page before each test
    page.goto('http://localhost:4200/')
    page.get_by_text('Modal & Overlays').click()
    page.get_by_text('Toastr').click()

def test_check_box(page: Page):
    page.get_by_role('checkbox', name='Hide on click').uncheck(force=True)
    page.get_by_role('checkbox', name='Prevent arising of duplicate toast').check(force=True)

    all_boxes = page.get_by_role('checkbox')

        # Iterate over each checkbox and uncheck them (force if necessary)
    for box in all_boxes.all():
        box.uncheck(force=True)
        assert box.is_checked() is False
    