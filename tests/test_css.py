
from pages.elements_page import ElementsPage

def test_flex_menu(browser):
    elem_page = ElementsPage(browser)
    elem_page.visit()
    assert elem_page.left_menu.check_css('flex', '0 0 25%')
    assert elem_page.left_menu.check_css('max-width', '25%')

    browser.set_window_size(650, 1000)

    assert elem_page.left_menu.check_css('flex', '0 0 100%')
    assert elem_page.left_menu.check_css('max-width', '100%')

    browser.set_window_size(1000, 1000)





