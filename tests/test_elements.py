from pages.elements_page import ElementsPage
from pages.checkbox import CheckBox


def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btns_first_menu.check_count_elements(count=9)


def test_count_checkbox(browser):
    elem_checkbox = CheckBox(browser)
    elem_checkbox.visit()
    assert elem_checkbox.element_checkbox.check_count_elements(count=1)
    elem_checkbox.btn_plus.click()
    assert elem_checkbox.element_checkbox.check_count_elements(count=17)
    browser.refresh()
    assert elem_checkbox.element_checkbox.check_count_elements(count=1)