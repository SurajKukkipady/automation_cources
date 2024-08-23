import time
from playwright.sync_api import Playwright, sync_playwright

def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    page.goto("http://www.uitestingplayground.com/dynamictable")
    # Find the index of the "CPU" column
    cpu_column_index = page.locator("div[role='rowgroup'] div[role='row'] span[role='columnheader']").all_text_contents().index("CPU")
    # Find the row where the first cell contains "Chrome"
    chrome_row = page.locator(f"div[role='row']:has(span[role='cell']:has-text('Chrome'))")
    # Use the index to get the corresponding cell in the "Chrome" row for the CPU value
    chrome_cpu_value = chrome_row.locator("span[role='cell']").nth(cpu_column_index).text_content()
    
    print(f"Chrome CPU Usage: {chrome_cpu_value}")

    expected_cpu_value = page.locator("p.bg-warning").text_content().split(":")[1].strip()
    assert chrome_cpu_value == expected_cpu_value
    print("Test Passed: Chrome CPU value matches the expected value.")

    time.sleep(10)

    # ---------------------
    context.close()
    browser.close()

