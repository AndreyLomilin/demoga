import pytest

from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

from conftest import @pytest.fixture()


def footer_text(browser):
    footer = DemoQa(browser)
    field = ElementsPage(browser)
    footer.visit()
    footer.btn_element.click()



    assert footer.footer_text.get_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    assert field.text_element.get_text == 'Please select an item from left to start practice.'

