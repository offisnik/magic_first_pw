import pytest
from pages.builder import username, email, password
from pages.form_and_inputs.form_2_validate import UsualFormPositive, UsualFormNegative
import allure


"""
Позитивные проверки
"""

"""Проверка успешной отправки формы"""
@allure.epic('ЕПИК простая форма что-то типо страницы сайта')
@allure.suite('СЮТ 2я форма простая форма что-то типо страницы сайта')
@allure.feature('ФИЧЕР 2я форма Простая форма что-то типо модуля на странице (куска функционала)')
@allure.title('Заполнение формы и регистрация')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('length, digits, upper_case, lower_case', [
    (8, True, True, None),
    (15, True, None, True),
    (8, True, None, True),
    (15, True, True, None),
    (20, True, False, True),
    (10, True, True, False)
])
def test_success_register_usual_form(driver, faker, length, digits, upper_case, lower_case):
    passw = faker.password(
        length=length,
        digits=digits,
        upper_case=upper_case,
        lower_case=lower_case
    )

    success_register = UsualFormPositive(driver)
    success_register.open_page()

    success_register.show_tooltip()

    success_register.fill_username(username())
    success_register.fill_email(email())
    success_register.fill_all_password(passw)

    success_register.submit_form()


"""
Негативные проверки
"""

"""Проверка сообщения ошибок при пустых полях и что форма не отправляется"""
@allure.feature('Негативный ФИЧЕР 2я форма Простая форма что-то типо модуля на странице (куска функционала)')
@allure.title('Валидация сообщений ошибок на форме при пустых полях')
@allure.severity(allure.severity_level.CRITICAL)
def test_validation_empty_fields(driver):
    empty_fields = UsualFormNegative(driver)
    empty_fields.open_page()

    empty_fields.check_validation_empty_fields()

"""Проверка что пароли не совпадают"""
@allure.title('Разные пароли в полях')
def test_different_passwords(driver):
    diff_pass = UsualFormNegative(driver)
    diff_pass.open_page()

    diff_pass.check_different_passwords(password())

"""Проверка что пароль не соответствует Паттерну"""
@allure.title('Не верный паттерн ввода пароля')
@pytest.mark.parametrize('length, digits, upper_case, lower_case', [
    (1, None, None, None),
    (7, None, None, None),
    (10, False, None, None),
    (15, True, False, False)
])
def test_wrong_format_passwords(driver, faker, length, digits, upper_case, lower_case):
    # Генерируем пароль прямо в тесте
    passw = faker.password(
        length=length,
        digits=digits,
        upper_case=upper_case,
        lower_case=lower_case
    )

    diff_pass = UsualFormNegative(driver)
    diff_pass.open_page()

    diff_pass.check_wrong_format_password(passw)

"""Проверка что в поле email нет символа @"""
@allure.title('Проверка валидности email')
def test_wrong_email(driver):
    wrong_email = UsualFormNegative(driver)
    wrong_email.open_page()

    wrong_email.check_wrong_email(email())

"""Проверка что username менее 5 символов """
@allure.title('Проверка валидности username')
def test_wrong_username(driver):
    wrong_username = UsualFormNegative(driver)
    wrong_username.open_page()

    wrong_username.check_wrong_name(username()[:4])
