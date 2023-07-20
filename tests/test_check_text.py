from pages.elements_page import ElementsPage


def test_page_elements(browser):
    elem = ElementsPage(browser)
    elem.visit()

    assert elem.text_element.get_text == 'Elements'


    assert elem.icon.exist()
    assert elem.btn_sidebar_first.exist()
    assert elem.btn_sidebar_first_textbox.exist()
