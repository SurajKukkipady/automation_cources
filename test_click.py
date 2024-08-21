#test_click.py

import time
from playwright.sync_api import Playwright, sync_playwright, expect
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def test_run(playwright: Playwright) -> None:
    logger.info('Starting test_run function.')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    logger.info('Navigating to the URL.')
    page.goto("http://www.uitestingplayground.com/click")
    page.get_by_role("button", name="Button That Ignores DOM Click").click()
    time.sleep(2)
    logger.info('Close')

    # ---------------------
    context.close()
    browser.close()

