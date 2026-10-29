import time
import pytest
import allure
from pages.form_and_inputs.form_1_simple import SimpleForm
from pages.builder import username, email, password

@allure.epic('ЕПИК простая форма что-то типо страницы сайта')
@allure.suite('СЮТ простая форма что-то типо страницы сайта')
@allure.feature('ФИЧЕР Простая форма что-то типо модуля на странице (куска функционала)')
@allure.title('Заполнение формы и регистрация')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('country', ['ru', 'us', 'uk', 'de'])
def test_success_register_simple_form(driver, country):
    success_register = SimpleForm(driver)
    success_register.open_page()

    success_register.fill_user_form(username())
    success_register.fill_email_form(email())
    success_register.fill_password_form(password())
    success_register.fill_country_dropdown(country)
    success_register.fill_checkbox_terms()

    success_register.push_submit_btn()

    success_register.results()
