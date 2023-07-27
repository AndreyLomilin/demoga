from pages.textbox import TextBox

import time
def test_text_box(browser):
    name = 'family'
    address = 'city'
    textbox_page = TextBox(browser)
    textbox_page.visit()
    textbox_page.full_name.send_keys(name)
    textbox_page.current_address.send_keys(address)
    textbox_page.btn_submit.click()


    assert textbox_page.str_elem.check_count_elements(count=2)


