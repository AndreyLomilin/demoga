

from pages.textbox import TextBox

def test_placeholder(browser):
    form_page = TextBox(browser)
    form_page.visit()
    assert form_page.full_name.get_dom_attribute('placeholder') == 'Full Name'

