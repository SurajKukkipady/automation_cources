from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playright:
    browser = playright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="playwright/.auth/storage_state.json")

    page = context.new_page()
    page.goto('https://gmail.com')
    table = page.locator("div.UI table")
    emails = table.locator("tr")
    first_email = emails.first
    first_email.locator("li[data-tooltip='Mark as read']").highlight()
    new_email=[]
    for email in emails.all():
        is_new_email = email.locator("li[data-tooltip='Mark as read']").count()==1
        if is_new_email:
            sender = email.locator("td span[email]:visible").inner_text()

            title = email.locator("td span[data-thread-id]:visible").inner_text()
            new_email.append([sender, title])
    
    if len(new_email)==0:
        print("No new emails")
    else:
        print(f'{len(new_email)} new emails')
        for email in new_email:
            print(f'Sender: {email[0]}')
            print(f'Title: {email[1]}')
            print('-'*20)

    context.close()
    