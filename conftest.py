import pytest
from playwright.sync_api import sync_playwright


# #Запуск для ОТЛАДКИ визуала
# @pytest.fixture
# def driver():
#     with sync_playwright() as pw:
#         browser = pw.chromium.launch(headless=False, args=["--start-maximized"])
#         context = browser.new_context(no_viewport=True)
#         page = context.new_page()
#         yield page
#         page.close()


#Запуск БЕЗ визуала для ОТЧЁТА
@pytest.fixture
def driver():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        # Явно указываем viewport 1920x1080
        context = browser.new_context(
            viewport={'width': 1920, 'height': 1080}
        )
        page = context.new_page()
        yield page
        page.close()