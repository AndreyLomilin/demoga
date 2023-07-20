
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    elements_page = ElementsPage(browser)
    demo_qa_page.btn_element.click()

    # assert demo_qa_page.equal_url()
    assert elements_page.equal_url()

