from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playright:
    browser = playright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://bootswatch.com/default/')


    #Get by role selectors
    #Role selectors (button)
    button = page.get_by_role('button', name='Default button')
    button.scroll_into_view_if_needed()
    button.highlight()
    time.sleep(2)

    #Role selectors (heading)
    heading = page.get_by_role('heading', name='Heading 2')
    heading.scroll_into_view_if_needed()
    heading.highlight()
    time.sleep(2)

    #Role selectors (radio button)
    radio_button = page.get_by_role("radio", name="Option one is this and that—be sure to include why it's great")
    radio_button.scroll_into_view_if_needed()
    radio_button.highlight()
    time.sleep(2)

    #Role selectors (checkbox)
    checkbox = page.get_by_role('checkbox', name='Default checkbox')
    checkbox.scroll_into_view_if_needed()
    checkbox.highlight()
    time.sleep(2)

    #Get by label selectors
    email_field = page.get_by_label('Email address').nth(0)
    email_field.scroll_into_view_if_needed()
    email_field.highlight()
    time.sleep(2)

    #Get by placeholder selectors
    placeholder = page.get_by_placeholder('Enter email')
    placeholder.scroll_into_view_if_needed()
    placeholder.highlight()
    time.sleep(2)

    #Get by text selectors
    text = page.get_by_text('Middle')
    text.scroll_into_view_if_needed()
    text.highlight()
    time.sleep(2)

    #Get by title selectors
    title = page.get_by_title('attribute')
    title.scroll_into_view_if_needed()
    title.highlight()
    time.sleep(2)

    #Get by css selectors
    css = page.locator('button.btn-success').nth(0)
    css.scroll_into_view_if_needed()
    css.highlight()
    time.sleep(2)

    #Get by id selectors
    id = page.locator('#btnGroupDrop2')
    id.scroll_into_view_if_needed()
    id.highlight()
    time.sleep(2)

    #Get by xpath selectors
    xpath = page.locator('xpath=//h1[@id="navbars"]')
    xpath.scroll_into_view_if_needed()
    xpath.highlight()
    time.sleep(2)

    #Get by nth selectors
    nth = page.locator('button').nth(10)
    nth.scroll_into_view_if_needed()
    nth.highlight()
    time.sleep(2)












    