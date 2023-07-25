import time
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
def test_size(browser):
    demoqa = DemoQa
    demoqa.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)

def test_visible_nav_bar(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    assert not element_page.nav_bar.visible()
    browser.set_window_size(767, 1000)
    assert element_page.nav_bar.visible()


