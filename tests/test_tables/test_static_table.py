from pages.tables.static_table import SimpleTable


def test_check_head_table(driver):
    simple_table = SimpleTable(driver)
    simple_table.open_page()

    simple_table.check_header()
    simple_table.check_body()
