from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playright:
    browser = playright.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    page.goto('https://testpages.eviltester.com/styled/download/download-via-js.html')

    # Download file
    with page.expect_download() as download_info:
        download_button = page.get_by_text('Controlled Direct Download')
        download_button.click()
        time.sleep(1)
        download = download_info.value
        download.save_as("sample.txt")
    
