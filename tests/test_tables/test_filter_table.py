import pytest
from pages.tables.filter_table import FilterTable



def test_check_tooltip(driver):
    tooltip = FilterTable(driver)
    tooltip.open_page()

    tooltip.show_tooltip()


@pytest.mark.parametrize('values', ['Active', 'Inactive', 'Pending'])
def test_change_status(driver, values):
    status = FilterTable(driver)
    status.open_page()

    status.change_status(values)

@pytest.mark.parametrize('name', ['m', 'alice', 'dfggv'])
@pytest.mark.parametrize('values', ['Active', 'Inactive', 'Pending'])
def test_input_count(driver, values, name):
    input_count = FilterTable(driver)
    input_count.open_page()

    input_count.input_status(values, name)