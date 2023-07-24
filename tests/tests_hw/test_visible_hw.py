import time
from pages.accordion import Accordion
from selenium.common.exceptions import NoSuchElementException

def test_visible_accordion(browser):
    element_page = Accordion(browser)
    element_page.visit()
    assert element_page.btn_widgets_accordian.visible()
    element_page.section1Heading.click()
    time.sleep(2)
    assert not element_page.btn_widgets_accordian.visible()

def test_visible_accordion_default(browser):
    element_page = Accordion(browser)
    element_page.visit()
    assert not element_page.elem1.visible()
    assert not element_page.elem2.visible()
    assert not element_page.elem3.visible()