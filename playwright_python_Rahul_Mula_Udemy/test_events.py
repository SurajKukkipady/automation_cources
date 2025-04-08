from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playright:
    browser = playright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto('https://testpages.eviltester.com/styled/alerts/alert-test.html')

    # Alert box
    alert_button = page.get_by_role('button', name='Show alert box')
    alert_button.click()
    time.sleep(1)

    # Confirm box
    page.on("dialog", lambda dialog: dialog.accept()) #or dialog.dismiss()
    alert_button_2 = page.get_by_role('button', name='Show confirm box')
    alert_button_2.click()
    time.sleep(1)

    # Prompt box
    page.on("dialog", lambda dialog: dialog.accept("Hello"))
    alert_button_3 = page.get_by_role('button', name='Show prompt box')
    alert_button_3.click()
    time.sleep(1)
