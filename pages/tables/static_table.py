from playwright.sync_api import Page, expect


class SimpleTable:

    def __init__(self, driver: Page):
        self.driver = driver
        self.head_table = driver.locator('#usersTable thead tr th')
        self.body_table = driver.locator("//table[@id='usersTable']//tbody/tr")
        self.edit_btn = driver.locator('//i[@class="fas fa-edit"]')
        self.trash_btn = driver.locator('//tbody//i[@class="fas fa-trash"]')

    """Открытие страницы"""

    def open_page(self):
        self.driver.goto('https://aqa-proka4.org/sandbox/web')

    def check_header(self):
        head = self.head_table
        check = ['ID', 'Name', 'Email', 'Status', 'Actions']
        for i in range(len(head.all())):
            expect(head.nth(i)).to_have_text(check[i])

    def check_body(self):
        expect(self.body_table.nth(0)).to_have_text("1\tJohn Doe\tjohn@example.com\tActive")
        expect(self.body_table.nth(1)).to_have_text("2\tJane Smith\tjane@example.com\tPending")
        expect(self.body_table.nth(2)).to_have_text("3\tBob Johnson\tbob@example.com\tInactive")

        expect(self.edit_btn).to_have_count(4)
        expect(self.trash_btn).to_have_count(3)

        for i in range(len(self.edit_btn.all())):
            expect(self.edit_btn.nth(i)).to_be_visible()
            expect(self.trash_btn.nth(i)).to_be_visible()
