

from pages.modal_dialogs import ModalDialogs

def test_modal_elements(browser):
    element_page = ModalDialogs(browser)
    element_page.visit()
    assert element_page.modal.check_count_elements(count=5)
