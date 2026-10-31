from playwright.sync_api import Page, expect
import allure

class UsualFormPositive:

    def __init__(self, driver: Page):
        self.driver = driver
        self.tooltip_btn = driver.locator('//button[@onclick="showHint(\'form2\')"]')
        self.tooltip_text = driver.locator('//div[@id="hint-form2"]')
        self.username = driver.locator('#val-username')
        self.email = driver.locator('#val-email')
        self.password = driver.locator('#val-password')
        self.conf_password = driver.locator('#val-confirm-password')
        self.submit_btn = driver.locator('#valSubmitBtn')
        self.success_message = driver.locator('#valFormResult p[class*="green"]')

    """Открытие страницы"""
    @allure.step('Открыть URL сайта')
    def open_page(self):
        self.driver.goto('https://aqa-proka4.org/sandbox/web')

    """Отображение подсказки"""
    @allure.step('Подсказка Тултип отображается')
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
    @allure.step('Поля username заполнено корректно')
    def fill_username(self, username):
        self.username.type(username)
        expect(self.username).not_to_be_empty()

    """Заполнение поля email"""
    @allure.step('Поля email заполнено корректно')
    def fill_email(self, email):
        self.email.type(email)
        expect(self.email).not_to_be_empty()

    """Заполнение полей пароля"""
    @allure.step('Поля password заполнены корректно')
    def fill_all_password(self, password):
        the_same_password = password
        self.password.type(the_same_password)
        self.conf_password.type(the_same_password)
        expect(self.password).not_to_be_empty()
        expect(self.conf_password).not_to_be_empty()

    """Отправка формы"""
    @allure.step('Форма успешно отправлена')
    def submit_form(self):
        self.submit_btn.click()
        expect(self.success_message).to_have_text('Все проверки пройдены! Форма валидна.')




class UsualFormNegative(UsualFormPositive):

    def __init__(self, driver: Page):
        super().__init__(driver)
        self.username_error = driver.locator('#username-error')
        self.email_error = driver.locator('#email-error')
        self.password_error = driver.locator('p#password-error').get_by_text('Password должен содержать минимум 8 символов, включая буквы и цифры')
        self.conf_password_error = driver.locator('#confirm-password-error')
        self.unsuccess_message = driver.locator('#valFormResult p[class*="red"]')


    """Проверка валидации пустых полей при отправке формы"""
    @allure.step('Проверка сообщений подсказок при пустых полях')
    def check_validation_empty_fields(self):
        self.submit_btn.click()
        expect(self.unsuccess_message).to_be_visible()
        expect(self.unsuccess_message).to_have_text('Форма содержит ошибки. Исправьте их и попробуйте снова.')
        expect(self.username_error).to_be_visible()
        expect(self.username_error).to_have_text('Username должен содержать минимум 5 символов')
        expect(self.email_error).to_be_visible()
        expect(self.email_error).to_have_text('Email должен содержать символ @')
        expect(self.password_error).to_be_visible()
        expect(self.password_error).to_have_text('Password должен содержать минимум 8 символов, включая буквы и цифры')
        expect(self.conf_password_error).not_to_be_visible()

    """Проверка что пароли не совпадают"""
    @allure.step('Проверка сообщения что пароли не совпадают')
    def check_different_passwords(self, password=None):
        self.password.type(password)
        self.conf_password.type(password[::-1])
        self.submit_btn.click()
        expect(self.conf_password_error).to_be_visible()
        expect(self.conf_password_error).to_have_text('Пароли не совпадают')

    """Проверка что пароли не соответвтует паттерну"""
    @allure.step('Проверка паттерна ввода паролей негативная')
    def check_wrong_format_password(self, password=None):
        self.password.type(password)
        self.submit_btn.click()
        expect(self.password_error).to_be_visible()
        expect(self.password_error).to_have_text('Password должен содержать минимум 8 символов, включая буквы и цифры')

    """Проверка что username не соответствует минимальное длине"""
    @allure.step('Проверка длины ввода паролей негативная')
    def check_wrong_name(self, name=None):
        self.username.type(name)
        self.submit_btn.click()
        expect(self.username_error).to_be_visible()
        expect(self.username_error).to_have_text('Username должен содержать минимум 5 символов')

    """Проверка что в почте нет символа @"""
    @allure.step('Проверка паттерна почты')
    def check_wrong_email(self, email=None):
        email = email.replace('@', '')
        self.email.type(email)
        self.submit_btn.click()
        expect(self.email_error).to_be_visible()
        expect(self.email_error).to_have_text('Email должен содержать символ @')





