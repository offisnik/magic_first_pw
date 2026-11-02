from playwright.sync_api import Page, expect


class SortTable:

    def __init__(self, driver: Page):
        self.driver = driver
        self.tooltip_btn = driver.locator('//button[@onclick="showHint(\'table1\')"]')
        self.tooltip_text = driver.locator('#hint-table1')
        self.header_table = driver.locator('#sortableTable thead tr th')
        self.head_id = driver.locator('#sortableTable thead tr th:nth-child(1)')
        self.name_id = driver.locator('#sortableTable thead tr th:nth-child(2)')
        self.age_id = driver.locator('#sortableTable thead tr th:nth-child(3)')
        self.sum_id = driver.locator('#sortableTable thead tr th:nth-child(4)')
        self.first_colum_id = driver.locator('#sortableTableBody tr:nth-child(1) td:nth-child(1)')
        self.first_colum_name = driver.locator('#sortableTableBody tr:nth-child(1) td:nth-child(2)')
        self.first_colum_age = driver.locator('#sortableTableBody tr:nth-child(1) td:nth-child(3)')
        self.first_colum_sum = driver.locator('#sortableTableBody tr:nth-child(1) td:nth-child(4)')


    """Открытие страницы"""

    def open_page(self):
        self.driver.goto('https://aqa-proka4.org/sandbox/web')

    def show_tooltip(self):
        expect(self.tooltip_btn).to_be_visible()
        expect(self.tooltip_btn).to_have_text('Показать подсказку')
        expect(self.tooltip_text).not_to_be_visible()
        self.tooltip_btn.click()
        expect(self.tooltip_text).to_be_visible()
        expect(self.tooltip_text.locator('h4')).to_have_text('Подсказка для автоматизации:')
        self.tooltip_btn.click()
        expect(self.tooltip_text).not_to_be_visible()

    def check_head_el(self):
        headers = ["ID", "Name", "Age",	"Salary"]
        for i in range(len(self.header_table.all())):
            expect(self.header_table.nth(i)).to_be_visible()
            expect(self.header_table.nth(i)).to_have_text(headers[i])

    def check_sort_id(self):
        self.head_id.click()
        expect(self.first_colum_id).to_have_text('1')
        self.head_id.click()
        expect(self.first_colum_id).to_have_text('5')

    def check_sort_name(self):
        self.name_id.click()
        expect(self.first_colum_name).to_have_text('Alice Johnson')
        self.name_id.click()
        expect(self.first_colum_name).to_have_text('Evan Davis')

    def check_sort_age(self):
        self.age_id.click()
        expect(self.first_colum_age).to_have_text('25')
        self.age_id.click()
        expect(self.first_colum_age).to_have_text('42')

    def check_sort_salary(self):
        self.sum_id.click()
        expect(self.first_colum_sum).to_have_text('$65,000')
        self.sum_id.click()
        expect(self.first_colum_sum).to_have_text('$105,000')







