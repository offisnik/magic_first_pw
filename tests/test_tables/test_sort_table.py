from pages.tables.sort_table import SortTable


def test_show_tooltip(driver):
    tooltip = SortTable(driver)
    tooltip.open_page()
    tooltip.show_tooltip()


def test_check_head_el(driver):
    check_head = SortTable(driver)
    check_head.open_page()

    check_head.check_head_el()


def test_sort_id(driver):
    sort_id = SortTable(driver)
    sort_id.open_page()

    sort_id.check_sort_id()

def test_sort_name(driver):
    sort_name = SortTable(driver)
    sort_name.open_page()

    sort_name.check_sort_name()


def test_sort_age(driver):
    sort_age = SortTable(driver)
    sort_age.open_page()

    sort_age.check_sort_age()


def test_sort_sum(driver):
    sort_sum = SortTable(driver)
    sort_sum.open_page()

    sort_sum.check_sort_salary()