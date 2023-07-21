import time
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demoqa_page = DemoQa(browser)
    element_page = ElementsPage(browser)
    demoqa_page.visit()
    demoqa_page.btn_element.click()
    time.sleep(3)
    demoqa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    element_page.equal_url()



