from playwright.sync_api import Page, expect

class DifficultForms:

    def __init__(self, driver: Page):
        self.driver = driver
        self.tooltip_btn = driver.locator('//button[@onclick="showHint(\'form3\')"]')
        self.tooltip_text = driver.locator('//div[@id="hint-form3"]')
        self.username_field = driver.locator('#dyn-name')
        self.email_add = driver.locator('#addEmailBtn')
        self.email_field = driver.locator('//input[@name="email[]"]')
        self.del_email_btn = driver.locator('//button[@onclick="removeEmailField(this)"]')
        self.phone_add = driver.locator('//button[@onclick="addPhoneField()"]')
        self.phone_field = driver.locator('//input[@name="phone[]"]')
        self.del_phone_btn = driver.locator('//button[@onclick="removePhoneField(this)"]')
        self.submit_btn = driver.locator('#dynSubmitBtn')
        self.submit_txt = driver.locator('(//div[@id="dynFormResult"]//p)[1]')

    """Открытие страницы"""
    def open_page(self):
        self.driver.goto('https://aqa-proka4.org/sandbox/web')

    """Отображение подсказки"""
    def show_tooltip(self):
        expect(self.tooltip_btn).to_be_visible()
        expect(self.tooltip_btn).to_have_text('Показать подсказку')
        expect(self.tooltip_text).not_to_be_visible()
        self.tooltip_btn.click()
        expect(self.tooltip_text).to_be_visible()
        expect(self.tooltip_text.locator('h4')).to_have_text('Подсказка для автоматизации:')
        self.tooltip_btn.click()
        expect(self.tooltip_text).not_to_be_visible()

    """Заполнение поля username"""
    def fill_username(self, username):
        self.username_field.type(username)
        expect(self.username_field).not_to_be_empty()

    def add_email(self, count=0):
        for i in range(count):
            self.email_add.click()
            expect(self.email_field.nth(i + 1)).to_be_visible()

    def fill_email(self, email, count=0):
        for i in range(count+1):
            self.email_field.nth(i).type(email)
            expect(self.email_field.nth(i)).not_to_be_empty()

    def add_phone(self, count=0):
        for i in range(count):
            self.phone_add.click()
            expect(self.phone_field.nth(i + 1)).to_be_visible()

    def fill_phone(self, phone, count=0):
        for i in range(count+1):
            self.phone_field.nth(i).type(phone)
            expect(self.phone_field.nth(i)).not_to_be_empty()


    def del_email(self, count=1):
        first = len(self.del_email_btn.all())
        self.del_email_btn.nth(count).click()
        second = len(self.del_email_btn.all())
        assert first > second, 'Элемент не удалился'

    def del_one_email(self):
        messages = []
        self.driver.once("dialog", lambda d: (messages.append(d.message), d.accept()))
        self.del_email_btn.click()
        assert ''.join(messages) == 'Должен остаться хотя бы один email!', f'Пришел текст {messages}'

    def del_phone(self, count=1):
        first = len(self.del_phone_btn.all())
        self.del_phone_btn.nth(count).click()
        second = len(self.del_phone_btn.all())
        assert first > second, 'Элемент не удалился'

    def del_one_phone(self):
        messages = []
        self.driver.once("dialog", lambda d: (messages.append(d.message), d.accept()))
        self.del_phone_btn.click()
        assert ''.join(messages) == 'Должен остаться хотя бы один телефон!', f'Пришел текст {messages}'

    def submit_form(self):
        self.submit_btn.click()
        expect(self.submit_txt).to_be_visible()
