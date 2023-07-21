
from pages.elements_page import ElementsPage
import time

def test_visible_btn_sidebar(browser):
    # sidebar = ElementsPage(browser)
    # sidebar.visit()
    # # sidebar.btn_sidebar_first.click()
    # # time.sleep(5)
    # # assert sidebar.btn_sidebar_first_textbox.exist()
    # sidebar.btn_sidebar_first_textbox.visible()
    element_page = ElementsPage(browser)
    element_page.visit()
    assert element_page.btn_sidebar_first_checkbox.visible()
    element_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not element_page.btn_sidebar_first_checkbox.visible()



