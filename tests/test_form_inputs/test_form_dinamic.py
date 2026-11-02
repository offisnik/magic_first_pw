import pytest
from pages.builder import username, email, phone, rand_int
from pages.form_and_inputs.form_3_dinamic import DifficultForms


"""Позитивные проверки"""

"""Проверка Тултипа подсказки"""
def test_tooltip_btn(driver):
    tooltip_form = DifficultForms(driver)
    tooltip_form.open_page()
    tooltip_form.show_tooltip()

"""Проверка успешной отправки формы с 1м полем"""
def test_success_register_many_form(driver):
    success_form = DifficultForms(driver)
    success_form.open_page()

    success_form.fill_username(username())
    success_form.fill_email(email())
    success_form.fill_phone(phone())

    success_form.submit_form()

"""Проверка успешной отправки формы где много полей"""
def test_success_register_many_fields(driver):
    random_int = rand_int()
    success_form = DifficultForms(driver)
    success_form.open_page()

    success_form.fill_username(username())

    success_form.add_email(random_int)
    success_form.fill_email(email(), random_int)

    success_form.add_phone(random_int)
    success_form.fill_phone(phone(), random_int)

    success_form.submit_form()

"""Проверка успешной отправки формы после удаления одного из полей"""
def test_success_register_with_del_fields(driver):
    random_int = rand_int(2)
    success_form_del_field = DifficultForms(driver)
    success_form_del_field.open_page()

    success_form_del_field.fill_username(username())

    success_form_del_field.add_email(random_int)
    success_form_del_field.fill_email(email(), random_int)

    success_form_del_field.add_phone(random_int)
    success_form_del_field.fill_phone(phone(), random_int)

    success_form_del_field.del_email(random_int)
    success_form_del_field.del_phone(random_int)

    success_form_del_field.submit_form()



"""Негативные проверки"""
"""Проверка удаления последнего элемента email и phone"""
def test_del_last_element(driver):
    del_last_element = DifficultForms(driver)
    del_last_element.open_page()

    del_last_element.del_one_email()
    del_last_element.del_one_phone()




