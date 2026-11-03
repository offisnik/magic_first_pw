from playwright.sync_api import Page, expect


class FilterTable:

    def __init__(self, driver: Page):
        self.driver = driver
        self.tooltip_btn = driver.locator('//button[@onclick="showHint(\'table2\')"]')
        self.tooltip_text = driver.locator('#hint-table2 h4')
        self.search_field = driver.get_by_placeholder('Поиск по имени...')
        self.count_row = driver.locator('//span[@id="visibleRows"]')
        self.dropdown_menu = driver.locator('#statusFilter')
        self.count_body = driver.locator('//tbody[@id="filterableTableBody"]/tr')
        self.visible_rows = driver.locator('#filterableTableBody tr:not([class*="hidden"])')


    def open_page(self):
        self.driver.goto("https://aqa-proka4.org/sandbox/web")

    def show_tooltip(self):
        expect(self.tooltip_text).not_to_be_visible()
        expect(self.tooltip_btn).to_have_text('Показать подсказку')
        self.tooltip_btn.click()
        expect(self.tooltip_text).to_be_visible()
        expect(self.tooltip_text).to_have_text('Подсказка для автоматизации:')
        self.tooltip_btn.click()
        expect(self.tooltip_text).not_to_be_visible()


    def change_status(self, value):
        self.dropdown_menu.select_option(label=value)
        expect(self.dropdown_menu).to_have_value(value)
        expect(self.visible_rows).to_have_count(int(self.count_row.inner_text()))

        self.dropdown_menu.select_option(label='Все статусы')
        expect(self.visible_rows).to_have_count(int(self.count_row.inner_text()))

    def input_status(self, value, name_value):
        self.search_field.fill(name_value)
        expect(self.visible_rows).to_have_count(int(self.count_row.inner_text()))

        self.dropdown_menu.select_option(label=value)
        expect(self.dropdown_menu).to_have_value(value)
        expect(self.visible_rows).to_have_count(int(self.count_row.inner_text()))

        self.search_field.clear()

        expect(self.visible_rows).to_have_count(int(self.count_row.inner_text()))










