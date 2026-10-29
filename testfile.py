import time

from playwright.sync_api import Page


def test_open_page(page: Page):
    page.goto('https://aqa-proka4.org/sandbox/web')
    page.get_by_role('button', name='Register').click()
    time.sleep(5)

