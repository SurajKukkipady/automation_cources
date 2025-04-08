from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playright:
    browser = playright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://bootswatch.com/default/')

    #Click action
    button = page.get_by_role('button', name='Block button').first
    button.scroll_into_view_if_needed()
    button.click()
    time.sleep(1)

    #Double click action
    button.dblclick(delay=1000)
    time.sleep(1)

    #Right click action
    button.click(button='right')
    time.sleep(1)

    #Shift click action
    button.click(modifiers=['Shift'])
    time.sleep(1)

    #Hover action
    button.hover()
    time.sleep(1)

    #Fill action
    input = page.get_by_placeholder('Enter email')
    input.scroll_into_view_if_needed()
    input.fill('test@test.com')
    time.sleep(1)
    input.clear()

    #Type action
    input.type('test@test.com', delay=100)
    time.sleep(1)

    #input value action (show the value of the input)
    print(input.input_value())

    #Check radio button
    radio = page.get_by_label('Option two can be something else and selecting it will deselect option one')
    radio.scroll_into_view_if_needed()
    radio.check()
    time.sleep(1)

    #Check checkbox
    checkbox = page.get_by_label('Default checkbox')
    checkbox.scroll_into_view_if_needed()
    checkbox.check()
    time.sleep(1)
    checkbox.uncheck()
    time.sleep(1)
    checkbox.set_checked(True)
    time.sleep(1)
    checkbox.set_checked(False)
    time.sleep(1)
    checkbox.click()
    time.sleep(1)

    #Switch action
    switch = page.get_by_label('Default switch checkbox input')
    switch.scroll_into_view_if_needed()
    switch.click()
    time.sleep(1)
    switch.uncheck()

    #Dropdown action
    button = page.locator('#btnGroupDrop1')
    button.scroll_into_view_if_needed()
    button.click()
    time.sleep(1)
    page.get_by_role('link', name='Dropdown link').first.click()

    #File upload action
    input = page.get_by_label('Default file input example')
    input.scroll_into_view_if_needed()
    input.set_input_files('test_selectors.py')
    time.sleep(1)

    #Keyboard action
    text_area = page.get_by_label('Example textarea')
    text_area.scroll_into_view_if_needed()
    text_area.press('KeyA')
    time.sleep(1)
    text_area.press('Shift+KeyB')
    time.sleep(1)







