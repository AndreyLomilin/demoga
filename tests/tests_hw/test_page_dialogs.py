
from pages.demoqa import DemoQa
from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    element_page = ModalDialogs(browser)
    element_page.visit()
    assert element_page.modal.check_count_elements(count=5)


def test_navigation_modal(browser):
    element_page = ModalDialogs(browser)
    demoqa = DemoQa(browser)
    element_page.visit()
    browser.refresh()
    element_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert demoqa.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
