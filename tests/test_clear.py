import time
from pages.textbox import TextBox

def test_clear(browser):
    testbox_page = TextBox(browser)
    testbox_page.visit()
    testbox_page.full_name.send_keys('Family')
    time.sleep(3)
    testbox_page.full_name.clear()
    time.sleep(3)
    assert  testbox_page.full_name.get_text() == ''



