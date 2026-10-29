from playwright.sync_api import expect, Page
import allure


class SimpleForm:

    def __init__(self, driver: Page):
        self.driver = driver
        self.form = driver.locator('#registrationForm')
        self.user_field = driver.locator('#username')
        self.email_field = driver.locator('#email')
        self.password_field = driver.locator('#password')
        self.country_dropdown = driver.get_by_label('country')
        self.checkbox_terms = driver.locator('#terms')
        self.submit_btn = driver.locator('#submitBtn')
        self.accept_text = driver.locator('#formResult')


    @allure.step('Открыть URL сайта')
    def open_page(self):
        self.driver.goto('https://aqa-proka4.org/sandbox/web')

    @allure.step('Заполнить поле USER')
    def fill_user_form(self, user):
        self.user_field.click()
        self.user_field.type(user)
        expect(self.user_field).not_to_be_empty()

    @allure.step('Заполнить поле Email')
    def fill_email_form(self, email):
        self.email_field.click()
        self.email_field.type(email)
        expect(self.email_field).not_to_be_empty()

    @allure.step('Заполнить поле Password')
    def fill_password_form(self, password):
        self.password_field.click()
        self.password_field.type(password)
        expect(self.password_field).not_to_be_empty()

    @allure.step('Выбрать страну из Дропдауна')
    def fill_country_dropdown(self, county):
        self.country_dropdown.select_option(county)
        expect(self.country_dropdown).to_have_value(county)

    @allure.step('Кликнуть на Чекбокс согласия')
    def fill_checkbox_terms(self):
        self.checkbox_terms.check()
        expect(self.checkbox_terms).to_be_checked()

    @allure.step('Нажать кнопку Register')
    def push_submit_btn(self):
        self.submit_btn.click()

    def results(self):
        with allure.step("Форма успешно отправлена"):
            # 1. Получаем скриншот в виде байтов (не сохраняя на диск)
            screenshot_bytes = self.driver.screenshot()

            # 2. Прикрепляем его к текущему шагу
            allure.attach(
                screenshot_bytes,
                name="Скриншот результата",
                attachment_type=allure.attachment_type.PNG
            )
        expect(self.accept_text).to_have_text('Форма успешно отправлена!')